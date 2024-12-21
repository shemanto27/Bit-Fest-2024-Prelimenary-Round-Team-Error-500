from fastapi import FastAPI
from .routers import ingredients
from .db import engine, Base


app = FastAPI()
Base.metadata.create_all(bind=engine)


app.include_router(ingredients.router, prefix="/api", tags=["Ingredients"])
# app.include_router(recipes.router, prefix="/api/v1", tags=["Recipes"])
# app.include_router(chatbot.router, prefix="/api/v1", tags=["Chatbot"])
