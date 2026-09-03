students = [
    ("Bhargav", 85),
    ("Paru", 92),
    ("Rahul", 78),
    ("Aman", 88)
]


students = [
    ("Bhargav", 85),
    ("Paru", 92),
    ("Rahul", 78),
    ("Aman", 88)
]

result = sorted(students, key=lambda student: student[1], reverse=True)

print(result)