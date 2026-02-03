import requests
import json

API_URL = "https://official-joke-api.appspot.com/random_joke"

try:
    response = requests.get(API_URL, timeout=10)

    if response.status_code == 200:
        data = response.json()

        print("😂 Random Joke")
        print("-" * 30)
        print(f"Setup : {data['setup']}")
        print(f"Punch : {data['punchline']}")

        with open("api_response.json", "w") as f:
            json.dump(data, f, indent=4)

        print("\n✅ Data saved to api_response.json")

    else:
        print("❌ Failed with status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("⚠️ API request failed")
    print("Error:", e)
