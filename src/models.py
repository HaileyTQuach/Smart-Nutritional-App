from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class Recipe(BaseModel):
    title: str = Field(..., description="Recipe title")
    ingredients: List[str] = Field(..., description="List of ingredients required for the recipe")
    instructions: str = Field(..., description="Step-by-step cooking instructions")
    calorie_estimate: int = Field(..., description="Estimated calories per serving")

class RecipeSuggestionOutput(BaseModel):
    recipes: List[Recipe] = Field(..., description="List of suggested recipes")

class VitaminInfo(BaseModel):
    name: str = Field(..., description="Name of the vitamin")
    percentage_dv: str = Field(..., description="Percentage of the Daily Value")

class MineralInfo(BaseModel):
    name: str = Field(..., description="Name of the mineral")
    amount: str = Field(..., description="Amount and unit of the mineral")

class NutrientBreakdown(BaseModel):
    protein: Optional[str] = Field(None, description="Protein content")
    carbohydrates: Optional[str] = Field(None, description="Carbohydrates content")
    fats: Optional[str] = Field(None, description="Fats content")
    vitamins: List[VitaminInfo] = Field(default_factory=list, description="List of vitamins and their %DV")
    minerals: List[MineralInfo] = Field(default_factory=list, description="List of minerals and their amounts")

class NutrientAnalysisOutput(BaseModel):
    dish: Optional[str] = Field(None, description="Identified dish")
    portion_size: Optional[str] = Field(None, description="Portion size description")
    estimated_calories: Optional[int] = Field(None, description="Estimated calories per portion")
    nutrients: NutrientBreakdown = Field(default_factory=NutrientBreakdown, description="Detailed nutrient breakdown")
    health_evaluation: Optional[str] = Field(None, description="Health evaluation summary")

