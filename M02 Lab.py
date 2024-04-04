# Nathan Sepe
# Deans_List_vs_Honor_Roll.py
# This app accepts student names and GPAs, then checks if they qualify for the Dean's List or the Honor Roll.

while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    if last_name == 'ZZZ':
        break

    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")


