# MealDB API Project

## i. API Used

This project uses **TheMealDB API**  
Website: https://www.themealdb.com/  

TheMealDB is a free REST API that provides meal and recipe data in JSON format.  

---

## ii. Data Retrieved

This script retrieves meal data filtered by **area (cuisine type)**.

Example areas include:
- Mexican
- Italian
- Canadian
- American
- Indian
- Japanese

When filtering by area, the API returns:

- `idMeal` – Unique meal ID
- `strMeal` – Name of the meal
- `strMealThumb` – URL to meal thumbnail image

The response data is:
- Printed to the console
- Saved locally as a `.json` file

---

## iii. How to Run the Code

1. This project requires python
2. This project works with the requests library
    pip install requests
3. Run the script and enter an Area
