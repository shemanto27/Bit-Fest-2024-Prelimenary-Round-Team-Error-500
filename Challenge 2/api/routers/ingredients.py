from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api.db import SessionLocal
from api.models import Ingredient

router = APIRouter()

# DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Schema for Ingredient model
class IngredientRequest(BaseModel):
    name: str
    quantity: float
    unit: str

class UpdateIngredientRequest(BaseModel):
    name: str
    quantity: float
    unit: str

# POST method to add an ingredient
@router.post("/ingredients/")
def add_ingredient(ingredient: IngredientRequest, db: Session = Depends(get_db)):
    # Check if ingredient already exists
    existing_ingredient = db.query(Ingredient).filter(Ingredient.name == ingredient.name).first()
    if existing_ingredient:
        raise HTTPException(status_code=400, detail="Ingredient already exists")

    # Add new ingredient to the database
    new_ingredient = Ingredient(
        name=ingredient.name,
        quantity=ingredient.quantity,
        unit=ingredient.unit,
    )
    db.add(new_ingredient)
    db.commit()
    db.refresh(new_ingredient)
    return new_ingredient

# GET method to get all ingredients
@router.get("/ingredients/")
def all_ingredients(db: Session = Depends(get_db)):
    return db.query(Ingredient).all()

# PUT method to update an ingredient by id
@router.put("/ingredients/{id}")
def update_ingredient(id: int, ingredient: UpdateIngredientRequest, db: Session = Depends(get_db)):
    # Fetch the existing ingredient by ID
    existing_ingredient = db.query(Ingredient).filter(Ingredient.id == id).first()
    if not existing_ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    
    
    existing_ingredient.name = ingredient.name
    existing_ingredient.quantity = ingredient.quantity
    existing_ingredient.unit = ingredient.unit
    db.commit()
    db.refresh(existing_ingredient)
    return existing_ingredient
