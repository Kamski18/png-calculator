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
    
}

weight = {
    "A" : 4.0,
    "A-" : 3.67,
    "B+" : 3.33,
    "B" : 3.0,
    "B-" : 2.67,
    "C+" : 2.33,
    "C" : 2.0,
    "C-" : 1.67,
    "D+" : 1.33,
    "D" : 1.0,
    "D-" : 0.67,
    "E" : 0.0,
    "F" : 0.0
    
}

def calculate():
    marks = input("Enter your grade in order from up to down (space separated): ").split(" ")

    while len(marks) != len(credithour):
        print("Error: Number of subjects entered is not equal to the number of subjects in the list")
        marks = input("Enter your grade in order from up to down (space separated): ").split(" ")

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
    print(f"Your GPA is: {gpa:.3f}")
calculate()
