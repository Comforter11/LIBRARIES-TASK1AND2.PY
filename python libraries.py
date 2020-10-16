# TASK 2.

student_name = input("Enter the student's name and surname:")
test1 = int(input("Please enter test 1 mark:"))
test2 = int(input("Please enter test 2 mark:"))
test3 = int(input("Please enter test 3 mark:"))
average = test1 + test2 + test3
average = average / 3
print("The average of the test is", round(average, 3))

if average >= 50:
    print("You have passed!")
if average < 50:
    print("You have failed!")

print("Your mark is" + str(average) + "%")


# Print 10 dates, two weeks apart.
from datetime import datetime, timedelta

today = datetime.today()

# Print 10 dates, two weeks apart.
for d in range(10):
    now_date = today + timedelta(days=14)
    today = now_date
    print(now_date.strftime("%Y %m %d"))



