

content = {
    "employees": [
        {
            "name": "John Doe",
            "age": 30,
            "department": "Engineering",
            "skills": ["Python", "C++", "Java"],
            "projects": [
                {"name": "Project A", "duration": 12, "completed": True},
                {"name": "Project B", "duration": 6, "completed": False}
            ],
            "contact": {
                "email": "john.doe@example.com",
                "phone": {"home": "123-456-7890", "work": "987-654-3210"}
            }
        },
        {
            "name": "Jane Smith",
            "age": 25,
            "department": "Marketing",
            "skills": ["SEO", "Content Writing", "Social Media"],
            "projects": [
                {"name": "Project X", "duration": 3, "completed": True},
                {"name": "Project Y", "duration": 4, "completed": True}
            ],
            "contact": {
                "email": "jane.smith@example.com",
                "phone": {"home": "555-123-4567", "work": "555-765-4321"}
            }
        }
    ],
    "departments": {
        "Engineering": {"head": "Alice Brown", "budget": 500000},
        "Marketing": {"head": "Bob White", "budget": 200000}
    },
    "company_info": {
        "name": "Tech Solutions",
        "location": ("123 Tech Avenue", "Tech City", "Techland"),
        "established": 2010
    }
}
# 5
print(content["company_info"]["location"])

# 4
print(content['employees'][0]['skills'])

# 3
print(content["departments"]["Marketing"]["head"])

# 2
print(content['employees'][0]['projects'][0]['duration'])

# 1
print(content['employees'][1]["contact"]["email"])
