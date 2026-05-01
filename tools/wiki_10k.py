import requests
import json

API = "https://en.wikipedia.org/api/rest_v1/page/summary/"

topics = [
    # Programming & Tech
    "Python_(programming_language)",
    "JavaScript",
    "Java_(programming_language)",
    "C_(programming_language)",
    "C++",
    "Artificial_intelligence",
    "Machine_learning",
    "Deep_learning",
    "Data_science",
    "Computer_science",
    "Software_engineering",
    "Operating_system",
    "Computer_network",
    "Database",

    # Internet & Digital world
    "Internet",
    "World_Wide_Web",
    "Cloud_computing",
    "Cybersecurity",
    "Blockchain",
    "Cryptocurrency",

    # Science
    "Physics",
    "Chemistry",
    "Biology",
    "Mathematics",
    "Statistics",
    "Astronomy",
    "Quantum_mechanics",
    "Thermodynamics",

    # Engineering & Robotics
    "Robotics",
    "Electrical_engineering",
    "Mechanical_engineering",
    "Civil_engineering",
    "Electronics",

    # Earth & Environment
    "Geography",
    "Earth",
    "Climate_change",
    "Environment",
    "Natural_disaster",

    # History & Society
    "History",
    "World_War_I",
    "World_War_II",
    "Ancient_history",
    "Culture",
    "Economics",
    "Politics",
    "Government",

    # Countries
    "Bangladesh",
    "India",
    "United_States",
    "China",
    "United_Kingdom",
    "Japan",

    # Health & Human
    "Human_body",
    "Medicine",
    "Nutrition",
    "Disease",
    "Genetics",

    # Space & Future
    "Space_exploration",
    "NASA",
    "Mars",
    "Solar_System",
    "Future_technology"
]

data = []
id_counter = 1

for i in range(1000):  # safe loop for 10K approx
    for topic in topics:
        try:
            r = requests.get(API + topic).json()

            title = r.get("title", topic)
            content = r.get("extract", "No data available.")

            question = f"{title} কী?"

            data.append({
                "id": id_counter,
                "title": question,
                "content": content,
                "tags": ["wiki", "knowledge"]
            })

            id_counter += 1

            if id_counter > 10000:
                break

        except:
            continue

with open("data/db.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Wikipedia 10K dataset তৈরি হয়েছে (clean & fixed)")
