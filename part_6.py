for i in range(5):
    print(i)

scores = [70, 85, 60, 90, 45]
for score in scores:
    print("Score:", score)

count = 1
while count <= 5:
    print(count)
    count += 1


scores = [45, 70, 85, 30, 90, 55]
total = 0
for i in scores:
    total += i

average = total / len(scores)
print("Total:", total)
print("Average:", average)


pas_c = 0
fai_c = 0
for i in scores:
    if  i > 40:
     pas_c += 1

    elif i < 40:
        fai_c += 1

print(f"Fail student{fai_c}")
print(f"Pass student{pas_c}")

