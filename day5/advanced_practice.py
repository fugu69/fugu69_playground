"""
Nested Dictionary Manipulation

Challenge: Modify this to allow empty "skills" lists without errors
"""

employees = {
    "Alice": {"age": 30, "skills": ["Python", "SQL"], "city": "New York"},
    "Bob": {"age": 25, "skills": ["Java", "C++"], "city": "London"},
    "Charlie": {"age": 35, "skills": ["Go", "Rust"], "city": "Berlin"},
    "August": {"age": 19, "skills": [], "city": "Arcansas"}
}

# Unpack dict to  key name (str) and value details (dict)
for name, details in employees.items():    
    skills = ", ".join(details['skills']) if details['skills'] else "Nothing yet"
    print(f"{name}: {details['age']} years old, skilled in {skills}, from {details['city']}")
