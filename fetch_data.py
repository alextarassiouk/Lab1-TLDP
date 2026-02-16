import requests
import json

def fetch_meals_by_area(area, output_file="meals_by_area.json"):
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?a={area}"

    try:
        response = requests.get(url, timeout=10) #sends the request to the URL and waits for a response.
        response.raise_for_status() #prevents silent failures.

        data = response.json() #API sends response in JSON format.

        #checks if meals exist in this area
        if data["meals"] is None:
            print("No meals found for that area.")
            return

        print(json.dumps(data, indent=4)) #converts to python dictionary

        #saves file and overwrites if it already exists
        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)

        print(f"\nSaved response to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    area = input("Enter area (e.g., Mexican, Italian, Canadian): ") #user input for area
    fetch_meals_by_area(area)
