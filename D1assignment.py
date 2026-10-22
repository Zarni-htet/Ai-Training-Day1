students = []

Grade_Categories = ("Excellent", "Good", "Pass", "Fail")

def classify_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 80:
        return Grade_Categories[0]
    elif score >= 60:
        return Grade_Categories[1]
    elif score >= 40:
        return Grade_Categories[2]
    else:
        return Grade_Categories[3]


for i in range(1, 6):
    print(f"Student{i}")
    name = input("Enter name:")
    age = int(input("Enter age:"))
    study_hours = float(input("Enter study hours:"))
    score = float(input("Enter Python score(0-100):")) 

    students_record = {
        "name": name,
        "age" : age,
        "study_hours" : study_hours,
        "score" : score,
        "grade" : classify_grade(score)
    }
    students.append(students_record)


score = float(input("Enter score(0-100):"))
while score < 0 or score > 100:
    print("Invalid marks! Score must be between 0 and 100.")
    score = float(input("Enter Python score(0-100):"))

print("\n===STUDENT PERFORMANCE REPORT===")
for student in students:
    print(f"\nName:{student['name']}")
    print(f"Age:{student['age']}")
    print(f"Study Hours:{student['study_hours']}")
    print(f"Score:{student['score']}")
    print(f"Grade:{student['grade']}")

def calculate_average(score):
    if len(score) == 0:
        return 0
    return sum(score) / len(score)

def count_passed(students):
    passed_count = 0
    for student in students:
        if student["score"] >= 40:
            passed_count += 1
    return passed_count

score = [s["score"] for s in students]
total_student = len(students)
avg_score = calculate_average(score)
highest_score = max(score)
lowest_score = min(score)
passed_students = count_passed(students)
failed_students = total_student - passed_students

top_student = students[0]
for student in students:
    if student["score"] > top_student["score"]:
        top_student = student

print("\n====SUMMARY====")
print(f"\nTotal Students: {total_student}")
print(f"Average score: {avg_score}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Passed Students: {passed_students}")
print(f"Failed Student: {failed_students}")

if top_student:
    print(f"Top Student:{top_student['name']} ({top_student['score']})")
