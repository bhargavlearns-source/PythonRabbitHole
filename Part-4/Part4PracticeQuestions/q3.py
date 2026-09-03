def student_info(name, age, **kwargs):
    print(f"Name:{name}\nAge: {age}")
    for i,j in kwargs.items():
        print(f"{i}: {j}")

student_info(
    "Bhargav",
    19,
    city="Gurdaspur",
    course="CSE",
    hobby="Programming"
)
