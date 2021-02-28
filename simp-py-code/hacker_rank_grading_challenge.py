"""HackerLand University has the following grading policy:

Every student receives a grade in the inclusive range 0 from to 100 .
Any grade less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:

  If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
  If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
Examples

 grade = 84 round to  (85 - 84 is less than 3)
 grade = 29 do not round (result is less than 40)
 grade = 57 do not round (60 - 57 is 3 or higher)
Given the initial value of grade for each of Sam's n students, write code to automate the rounding process

Input Format

The first line contains a single integer, n, the number of students.
Each line i of the n subsequent lines contains a single integer, grades[i].
"""
def gradingStudents(grades):
    i = 0
    for grade in grades:
        if ((grade + 1) % 5 == 0  and (i < len(grades) and (grade > 37))):
            grades[i] = grades[i] + 1
        if ((grade + 2) % 5 == 0  and (i < len(grades) and (grade > 37))):
            grades[i] = grades[i] + 2            
        i += 1
    return grades       
if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)