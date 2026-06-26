import json

def main():
    data = {
        "message": "Scholarship data updated successfully",
        "total_scholarships": 1
    }

    with open("scholarships.json", "w") as f:
        json.dump(data, f, indent=4)

    print("scholarships.json created successfully!")

if __name__ == "__main__":
    main()
