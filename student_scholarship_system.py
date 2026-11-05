'''Task 1: Student Scholarship Eligibility System.

Topic: Conditional Statements (if, elif, else)
Develop a Python application that evaluates students' eligibility for university scholarships based on their academic marks, attendance percentage, and monthly family income.

Your application must:
1. Collect the student's name, academic marks, attendance percentage, and monthly family income.
2. Validate the entered information.
3. Apply the following eligibility criteria:
- Academic marks must be at least 80%.
- Attendance must be at least 85%.
- Monthly family income must be Rs. 50,000 or less.
4. If all eligibility conditions are satisfied:
- Marks of 90% or above: Full Scholarship.
- Marks between 80% and 89%: Partial Scholarship.
5. If the student does not meet the criteria, display the appropriate reason for ineligibility.
6. Display a complete scholarship evaluation report.'''


print("===============Evaluation for scholorship===============")

candidate_name = input("Enter the student name ")
academic_marks = float(input("enter student marks in percentage"))
attand_percentage = float(input("enter your attandance percentage"))
income =         float(input("enter family income"))

if academic_marks < 0 or academic_marks > 100:
    print("it is not correct marks ")

elif attand_percentage < 0 or academic_marks > 100:
    print("incorrect attandance ")
elif income < 0 or income > 50000:
    print("incorrect income info")

else:
    marks = academic_marks >= 80
    attand = attand_percentage >= 85
    income_info = income <= 50000

    if marks and attand and income_info:
        if academic_marks >= 90:
            scholorship = "fully scholorship "

        elif academic_marks >= 80 or academic_marks < 90:
            scholorship = " partially scholorship"

        else:
            scholorship ="Not elegible"
    else:
        scholorship = "Not elegible"


print("\n========== SCHOLARSHIP REPORT ==========")
print(f"Student Name: {candidate_name}")
print(f"Academic Marks: {academic_marks:.2f}%")
print(f"Attendance: {attand_percentage:.2f}%")
print(f"Monthly Family Income: Rs. {income:.2f}")

print("Eligibility Evaluation:")

if not academic_marks:
    print("- Marks below required 80%.")

if not attand_percentage:
    print("- Attendance below required 85%.")

if not income:
    print("- Family income exceeds Rs. 50,000.")

print(f"nScholarship Result: {scholorship}")
