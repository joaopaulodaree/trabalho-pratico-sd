from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class ActivityLevel(str, Enum):
    SEDENTARY = "sedentary"
    LIGHT = "light"
    MODERATE = "moderate"
    VERY_ACTIVE = "very_active"
    ATHLETE = "athlete"

class FitnessGoal(str, Enum):
    WEIGHT_LOSS = "weight_loss"
    MUSCLE_GAIN = "muscle_gain"
    MAINTENANCE = "maintenance"
    ENDURANCE = "endurance"
    STRENGTH = "strength"

class FitnessProfile(BaseModel):
    age: int
    weight: float
    height: float
    gender: str
    activity_level: ActivityLevel
    fitness_goal: FitnessGoal
    dietary_restrictions: List[str] = []
    injuries: List[str] = []
    preferred_workout_time: str
    available_equipment: List[str] = []
    workout_days_per_week: int
    


class Exercise(BaseModel):
    name: str = Field(..., description="Name of the exercise. Give a specific name, not just 'squat' or 'bench press', but something like 'Barbell Squat' or 'Incline Dumbbell Bench Press'")
    muscle_group: str = Field(..., description="Primary muscle group targeted by the exercise")
    sets: int
    reps: int
    rest_time: int = Field(..., description="Rest time in seconds")

class Meal(BaseModel):
    name: str = Field(..., description="Name of the meal. Use a different name, not only breakfast or lunch, but something like 'Protein-Packed Breakfast' or 'Bananas with Honey and Peanut Butter'")
    ingredients: List[str] = Field(..., description="List of ingredients for the meal")
    portions: List[str] = Field(..., description="Portion sizes for each ingredient")
    timing: str = Field(..., description="breakfast, lunch, dinner, snack")
    

class FitnessReportResult(BaseModel):
    workout_plan: List[Exercise] = Field(description="Customized workout routine. Make a detailed workout plan for each exercise, with specific, sets, reps, machines and rest times. Remember that a workout plan should be full of different exercises, not just one or two. Include at least 15 different exercises for each muscle group (legs, chest, arms, etc).")
    meal_plan: List[Meal] = Field(description="Daily meal plan. Make a detailed meal plan for each meal, with specific foods, portion sizes, ingredients, and preparation methods.")
    daily_calories: int = Field(description="Recommended daily caloric intake")
    macros: dict = Field(description="Recommended macro split (protein, carbs, fats)")
    tips: List[str] = Field(description="Personalized fitness and nutrition tips")
    weekly_schedule: dict = Field(description="Weekly workout schedule. The keys (days of the week) should be in lowercase, e.g., 'monday', 'tuesday', etc.")
    motivational_quote: str = Field(description="Motivational quote")