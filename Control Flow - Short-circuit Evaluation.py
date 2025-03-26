# Short-circuit Evaluation
# Eg : A person can be eligible if they have either high income or good credit and it should not be a student

high_income = False
good_credit = True
student = True

if (high_income or good_credit) and not student:
    print("Eligible")

# (high_income or good_credit) and not student: the evaluation stops as soon as the one of these arguments (high_income) evaluates to false
# the same happens with or operators - (high_income or good_credit) or not student, the evaluation stops as soon as the one of these arguments evaluates to true
# In python, logical operators are short-circuit
