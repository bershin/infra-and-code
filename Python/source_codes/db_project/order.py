from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel

# Step 1: Setting up the FastAPI app for Order Service
app = FastAPI()

# Step 2: Database connection configuration for Order Service
ORDER_DATABASE_URL = "postgresql://postgres:password@localhost/order_db"

# SQLAlchemy setup for Order Service
order_engine = create_engine(ORDER_DATABASE_URL)
SessionLocalOrder = sessionmaker(autocommit=False, autoflush=False, bind=order_engine)
BaseOrder = declarative_base()

# Step 3: Order Database Model
class Order(BaseOrder):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    item_name = Column(String, index=True)

# Step 4: Pydantic Schema for Order Service
class OrderCreate(BaseModel):
    user_id: int
    item_name: str

# Step 5: Dependency to get the Order Service DB session
def get_order_db():
    db = SessionLocalOrder()
    try:
        yield db
    finally:
        db.close()

# Step 6: Create an order
@app.post("/orders/", response_model=OrderCreate)
def create_order(order: OrderCreate, db: Session = Depends(get_order_db)):
    db_order = Order(user_id=order.user_id, item_name=order.item_name)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# Step 7: Get order by ID
@app.get("/orders/{order_id}", response_model=OrderCreate)
def get_order(order_id: int, db: Session = Depends(get_order_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

# Step 8: Create database and run the Order Service
if __name__ == "__main__":
    import uvicorn
    BaseOrder.metadata.create_all(bind=order_engine)
    uvicorn.run(app, host="127.0.0.1", port=8002)
