subjects = {
    "Python": 3,
    "DBMS": 5,
    "AI": 4,
    "Java": 2
}

print("Priority List:")

for subject, difficulty in sorted(
        subjects.items(), key=lambda x: x[1], reverse=True):

    print(subject, "→ Difficulty:", difficulty)
