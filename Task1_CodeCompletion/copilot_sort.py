# copilot_sort.py
# ------------------------------
# Suggested by: GitHub Copilot
# Purpose: Sort a list of dictionaries by key with flexibility and error handling
# ------------------------------

def sort_by_key(data_list, key_name, reverse=True):
    """
    Sort a list of dictionaries by a specific key.
    If key is missing, use 0 as default.
    """
    return sorted(data_list, key=lambda x: x.get(key_name, 0), reverse=reverse)

# Example dataset
students = [
    {"name": "Nolly", "score": 85},
    {"name": "Kyle", "score": 92},
    {"name": "Aisha", "score": 78},
    {"name": "Faith", "score": 89}
]

sorted_students = sort_by_key(students, "score")

print("Sorted list (AI-generated version):")
for student in sorted_students:
    print(f"{student['name']}: {student['score']}")

