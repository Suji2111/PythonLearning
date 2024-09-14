#Grade calculator using simplified chaining format

score = int(input("Enter your score\n"))
# score >=90 and score <=100 -> "A"
# score >=80 and score <=89 -> "B"

if 90 <= score <= 100:  # Simplified Chaining Format -> 90 <= score <= 100
    print("You grade is ", "A")
elif 80 <= score <= 89:
    print("You grade is ", "B")
elif 70 <= score <= 79:
    print("You grade is ", "C")
elif 60 <= score <= 69:
    print("You grade is ", "D")
elif score >= 100:
    print("You are  Superman!!")
else:
    print("You grade is ", "F")