"""Write a function that accepts a grade and returns the corresponding letter grade based on
Ashesi’s grading system"""

print("Welcome to the Grading system check.")
def grading_system():
    while True:
        print("press 'Q' to exit")
        grade = (input("Enter your grade'\n'"))
        if grade == 'Q':
            break
        try:
            grade = int(grade)
            if grade >= 80 and grade <= 100:
                print("You had 'A+'")
            elif grade >= 70 and grade <= 89:
               print("You had 'A'")
            elif grade >= 65 and grade <= 69:
               print("You had 'B+'")
            elif grade >= 60 and grade <= 64:
               print("You had 'B'")
            elif grade >= 55 and grade <= 59:
               print("You had 'C+'")
            elif grade >= 50 and grade <= 54:
               print("You had 'C'")
            elif grade >= 45 and grade <= 49:
               print("You had 'D+'")
            elif grade >= 40 and grade <= 44:
               print("You had 'D'")
            elif grade >= 0 and grade <= 39:
                print("You had 'F'")
            else:
               print("Your Score should be less than 100")
        except ValueError:
            print("please Enter Your score in Numerals!")
grading_system()
        
            