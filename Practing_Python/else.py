print("The letter grade system")

def my_letter_offer():
    print("Enter the year you started to study:")
    year = int(input("Year: "))
    print("Enter the semester you want:")
    semester = int(input("Semester: "))
    return year, semester

def my_letter_grade():
    max_grade = 4.0
    min_grade = 0.0
    return max_grade, min_grade

def student(max_grade, min_grade):
    print("Prediction maximum grade:")
    max_grade = float(input("Enter predicted max grade: "))
    print("Prediction minimum grade:")
    min_grade = float(input("Enter predicted min grade: "))

    if max_grade > min_grade:
        print("The system was right")
    elif max_grade == min_grade:
        print("The system was wrong")
    else:
        print("Student failed!")
    
    return max_grade, min_grade

def main():
    # Get year and semester
    year, semester = my_letter_offer()
    print(f"You started in year {year} and chose semester {semester}.")

    # Get letter grades
    max_grade, min_grade = my_letter_grade()
    print(f"Default grades: Max={max_grade}, Min={min_grade}")

    # Predict student grades
    max_grade, min_grade = student(max_grade, min_grade)

# Run the program
if __name__ == "__main__":
    main()


