from pathlib import Path
path = Path("tasks_from_course")
for file in path.glob("*.py"):
    print(file)
print("This is a list of tasks I have done! Stay Hard!")