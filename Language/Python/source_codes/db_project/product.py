from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel
import redis
import json

# Step 1: Setting up the FastAPI app
app = FastAPI()

# Step 2: Database connection configuration for Product Service
DATABASE_URL = "postgresql://postgres:password@localhost/product_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Step 3: Product Database Model
class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)

# Step 4: Pydantic Schema for Product Service
class ProductCreate(BaseModel):
    name: str
    price: int

class ProductOut(BaseModel):
    id: int
    name: str
    price: int

# Step 5: Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Step 6: Setting up Redis connection
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# Step 7: Fetch product details with caching
@app.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    # Step 7.1: Check if product exists in Redis cache
    cached_product = redis_client.get(f"product:{product_id}")
    
    if cached_product:
        # Step 7.2: Return the product data from the cache
        return json.loads(cached_product)
    
    # Step 7.3: If not in cache, fetch from the database
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Step 7.4: Cache the product data in Redis for future requests
    redis_client.set(f"product:{product_id}", json.dumps({
        "id": db_product.id,
        "name": db_product.name,
        "price": db_product.price
    }))
    
    # Step 7.5: Return the product data from the database
    return db_product

# Step 8: Create a new product (No caching involved)
@app.post("/products/", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Step 9: Create database and run the Product Service
if __name__ == "__main__":
    import uvicorn
    Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host="127.0.0.1", port=8003)
