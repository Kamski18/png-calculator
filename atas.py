import sys
# pylint: disable=unused-variable,missing-function-docstring

CREDIT_HOUR: dict[str, int] = {
    "BM": 6,
    "BI": 6,
    "SEJ": 4,
    "MATH": 6,
    "ADDMATH": 6,
    "BIO": 6,
    "PHYS": 6,
    "CHEM": 6,
    "PAI": 5,
    "PJK": 3,
}

GRADE_WEIGHTAGES: dict[str, float] = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.67,
    "B+": 3.33,
    "B": 3.0,
    "B-": 2.67,
    "C+": 2.33,
    "C": 2.0,
    "C-": 1.67,
    "D+": 1.33,
    "D": 1.0,
    "D-": 0.67,
    "E": 0.0,
    "F": 0.0,
}

weightages: dict[str, float] = {
    "BM": 0,
    "BI": 0,
    "SEJ": 0,
    "MATH": 0,
    "ADDMATH": 0,
    "BIO": 0,
    "PHYS": 0,
    "CHEM": 0,
    "PAI": 0,
    "PJK": 0,
}


def calculate_png() -> float:
    grades: list[str] = []
    for subject in weightages:
        user_input: str = input(f"Enter grade for {subject}: ").upper()
        if user_input not in GRADE_WEIGHTAGES:
            print("Invalid grade!")
            sys.exit(1)

        weightages[subject] = GRADE_WEIGHTAGES[user_input.upper()]

    product_of_credhour_weightages: float = 0
    total_credit_hours: int = sum(CREDIT_HOUR.values())

    for subject, credit_hour in CREDIT_HOUR.items():
        product_of_credhour_weightages += credit_hour * weightages[subject]

    return product_of_credhour_weightages / total_credit_hours


print(f"{calculate_png():.3f}")
