def greet():
    print("Welcome to Python for AI!")

greet()

def greet_student(name):
    print(f"Hello, {name}!")

greet_student("Aung Aung")
greet_student("Su Su")

def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)
marks = [70,80,90]
result = calculate_average(marks)

print("Average:", result)


def classify_score(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"

print(classify_score(90))
print(classify_score(55))
print(classify_score(25))

def count_passed(scores):
    passed_count=0
    for score in scores:
        if score >= 50:
            passed_count+=1
        return passed_count

scores=[70, 40, 90, 30, 50]
count=count_passed(scores)
print(count)