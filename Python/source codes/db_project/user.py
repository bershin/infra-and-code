from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy.exc import NoResultFound
from pydantic import BaseModel

# Step 1: Setting up the FastAPI app
app = FastAPI()

# Step 2: Database Connection Configuration
DATABASE_URL = "postgresql://postgres:password@localhost/user_db"

# SQLAlchemy setup: Creating the engine to connect to the PostgreSQL database
engine = create_engine(DATABASE_URL)

# Step 3: Create a Session class to handle database transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Step 4: Base class to define database models
Base = declarative_base()

# Step 5: Define a database model (table)
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Step 6: Pydantic schema for input validation
class UserCreate(BaseModel):
    name: str
    email: str

# Step 7: Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Step 8: Route to create a new user
@app.post("/users/", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Step 9: Route to get user by ID
@app.get("/users/{user_id}", response_model=UserCreate)
def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        db_user = db.query(User).filter(User.id == user_id).one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Step 10: Run FastAPI
if __name__ == "__main__":
    import uvicorn
    Base.metadata.create_all(bind=engine)  # This creates tables in the database
    uvicorn.run(app, host="127.0.0.1", port=8000)
