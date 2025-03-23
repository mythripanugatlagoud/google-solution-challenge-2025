from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Sample meal data
meals = [
    {"id": 1, "name": "Chicken Biryani", "calories": 600, "protein": 35},
    {"id": 2, "name": "Paneer Butter Masala", "calories": 500, "protein": 25},
    {"id": 3, "name": "Egg Fried Rice", "calories": 450, "protein": 20}
]

# Home Route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Smart Meal Planner API!"})

# Get all meals
@app.route('/meals', methods=['GET'])
def get_meals():
    return jsonify(meals)

# Get meal by ID
@app.route('/meals/<int:meal_id>', methods=['GET'])
def get_meal(meal_id):
    meal = next((m for m in meals if m["id"] == meal_id), None)
    if meal:
        return jsonify(meal)
    return jsonify({"error": "Meal not found"}), 404

# Add a new meal
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

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
