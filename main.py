from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic import BaseModel

# SQLite database URL
DATABASE_URL = "sqlite:///./test.db"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI app instance
app = FastAPI()

# SQLAlchemy model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Pydantic schema
class UserSchema(BaseModel):
    name: str
    email: str

# Routes
@app.get("/")
async def hello():
    return {"message": "Hello, DINESH"}

@app.post("/users")
async def create_user(user: UserSchema):
    db = SessionLocal()
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return {"message": "User created successfully", "user": user}
