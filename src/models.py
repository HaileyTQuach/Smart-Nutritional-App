from pydantic import BaseModel, Field
from typing import List

class Recipe(BaseModel):
    title: str = Field(..., description="Recipe title")
    ingredients: List[str] = Field(..., description="List of ingredients required for the recipe")
    instructions: str = Field(..., description="Step-by-step cooking instructions")
    calorie_estimate: int = Field(..., description="Estimated calories per serving")

class RecipeSuggestionOutput(BaseModel):
    recipes: List[Recipe] = Field(..., description="List of suggested recipes")

class NutrientAnalysisOutput(BaseModel):
    calories: int = Field(..., description="Total calorie count of the meal")
    nutrients: Dict[str, str] = Field(
        ..., description="Mapping of nutrient names to their amounts (with units if applicable)"
    )
    health_evaluation: Optional[str] = Field(
        None, description="Summary of health evaluation based on the nutrient analysis"
    )
