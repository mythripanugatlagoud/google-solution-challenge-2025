from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Sample meal data (temporary storage)
meals = [
    {"id": 1, "name": "Chicken Biryani", "calories": 600, "protein": 35},
    {"id": 2, "name": "Paneer Butter Masala", "calories": 500, "protein": 25},
    {"id": 3, "name": "Egg Fried Rice", "calories": 450, "protein": 20}
]

meal_plans = []  # Stores user meal plans

# ✅ Route: Home
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Smart Meal Planner API!"})

# ✅ Route: Get All Meals
@app.route('/meals', methods=['GET'])
def get_meals():
    return jsonify(meals)

# ✅ Route: Get a Specific Meal by ID
@app.route('/meals/<int:meal_id>', methods=['GET'])
def get_meal(meal_id):
    meal = next((m for m in meals if m["id"] == meal_id), None)
    if meal:
        return jsonify(meal)
    return jsonify({"error": "Meal not found"}), 404

# ✅ Route: Add a New Meal
@app.route('/meals', methods=['POST'])
def add_meal():
    data = request.json
    new_meal = {
        "id": len(meals) + 1,
        "name": data["name"],
        "calories": data["calories"],
        "protein": data["protein"]
    }
    meals.append(new_meal)
    return jsonify(new_meal), 201

# ✅ Route: Create a Meal Plan
@app.route('/meal-plans', methods=['POST'])
def create_meal_plan():
    data = request.json
    new_plan = {
        "id": len(meal_plans) + 1,
        "user": data["user"],
        "meals": data["meals"],  # List of meal IDs
        "date": data["date"]
    }
    meal_plans.append(new_plan)
    return jsonify(new_plan), 201

# ✅ Route: Get All Meal Plans
@app.route('/meal-plans', methods=['GET'])
def get_meal_plans():
    return jsonify(meal_plans)

# ✅ Route: Get Meal Plan by ID
@app.route('/meal-plans/<int:plan_id>', methods=['GET'])
def get_meal_plan(plan_id):
    plan = next((p for p in meal_plans if p["id"] == plan_id), None)
    if plan:
        return jsonify(plan)
    return jsonify({"error": "Meal plan not found"}), 404

# ✅ Route: Delete a Meal Plan
@app.route('/meal-plans/<int:plan_id>', methods=['DELETE'])
def delete_meal_plan(plan_id):
    global meal_plans
    meal_plans = [p for p in meal_plans if p["id"] != plan_id]
    return jsonify({"message": "Meal plan deleted successfully"}), 200

# ✅ Route: Update a Meal Plan
@app.route('/meal-plans/<int:plan_id>', methods=['PUT'])
def update_meal_plan(plan_id):
    data = request.json
    for plan in meal_plans:
        if plan["id"] == plan_id:
            plan["meals"] = data.get("meals", plan["meals"])
            plan["date"] = data.get("date", plan["date"])
            return jsonify(plan), 200
    return jsonify({"error": "Meal plan not found"}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
