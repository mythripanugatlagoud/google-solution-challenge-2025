# Smart Meal Planner for Hostellers

## Project Structure

```
📂 smart-meal-planner
 ┣ 📂 frontend  # React-based UI
 ┣ 📂 backend   # Python (Flask/Django) API
 ┣ 📂 database  # SQL/Firebase for meal storage
 ┣ 📂 ai_model  # AI-based meal suggestion
 ┣ 📜 README.md # Project details
 ┗ 📜 requirements.txt # Dependencies
```

## Backend (Python + Flask) - Initial Setup

from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample meal database (this will later be connected to SQL/Firebase)
meals = [
    {"id": 1, "name": "Grilled Chicken with Rice", "category": "high protein", "calories": 500},
    {"id": 2, "name": "Paneer Salad", "category": "vegetarian", "calories": 300},
    {"id": 3, "name": "Egg Sandwich", "category": "PCOS-friendly", "calories": 350},
]

@app.route("/meals", methods=["GET"])
def get_meals():
    category = request.args.get("category")
    if category:
        filtered_meals = [meal for meal in meals if meal["category"] == category]
        return jsonify(filtered_meals)
    return jsonify(meals)

if __name__ == "__main__":
    app.run(debug=True)

```
🔹 This is a simple **Flask API** that returns meal suggestions based on category.
🔹 Next, we will **connect it to a database & integrate AI recommendations**.
