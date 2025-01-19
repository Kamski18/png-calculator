credithour = {
    "BM" : 6,
    "BI" : 6,
    "SEJ" : 4,
    "MAT" : 6,
    "ADDMATH" : 6,
    "BIO" : 6,
    "PHY" : 6,
    "CHEM" : 6,
    "PAI" : 5,
    "PJK" : 3,
    "SENI" : 2,
    "SK" : 2,
}

weight = {
    "A" : 4.0,
    "A-" : 3.75,
    "B+" : 3.50,
    "B" : 3.25,
    "B-" : 3.00,
    "C+" : 2.75,
    "C" : 2.50,
    "C-" : 2.25,
    "D" : 2.00,
    "E" : 1.00,
    "F" : 0.00,
}

def calculate():
    marks = input("Enter your marks in order from up to down (space separated): ").split(" ")

    while len(marks) != len(credithour):
        print("Error: Number of subjects entered is not equal to the number of subjects in the list")
        marks = input("Enter your marks in order from up to down (space separated): ").split(" ")

    totalcredits = 0
    total = 0

    for i, (subject, credit) in enumerate(credithour.items()):
        grade = marks[i].capitalize()
        if grade in weight:
            total += weight[grade] * credit
            totalcredits += credit
        else:
            print(f"Error: Invalid grade '{grade}' for subject '{subject}'")
            return

    gpa = total / totalcredits
    print(f"Your GPA is: {gpa:.2f}")
calculate()
