# manual_sort.py
# ------------------------------
# Manually written by: Nolly Masai
# Purpose: Sort a list of dictionaries by a given key (e.g., score)
# ------------------------------

students = [
    {"name": "Nolly", "score": 85},
    {"name": "Kyle", "score": 92},
    {"name": "Aisha", "score": 78},
    {"name": "Faith", "score": 89}
]

# Manual sort using lambda function
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)

print("Sorted list (manual implementation):")
for student in sorted_students:
    print(f"{student['name']}: {student['score']}")

