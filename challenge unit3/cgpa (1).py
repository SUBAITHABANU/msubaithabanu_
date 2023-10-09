class student:

  def __init__(self, name, roll__number, cgpa):
    self.name = name
    self.roll_number =  roll__number
    self.cgpa = cgpa


def sort_students(student_list):
  # sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students
# Example usage:
students = [
    student("seetha", "C230", 8.8),
    student("subai", "C231", 8.9),
    student("sameem", "C232", 9.2),
    student("nabila", "C233", 9.3),
  ]

sorted_students = sort_students(students)

# print the sorted list of students
for student in sorted_students:
  print( "Name: {}, Roll Number: {}. CGPA: {}".format(student.name, student.roll_number, student.cgpa))


  
  
  