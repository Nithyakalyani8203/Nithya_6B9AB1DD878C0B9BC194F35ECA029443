def sort _ students (student _list ):
# sort the student list based on CGPA in descending order
Sorted_ students= sorted (student _list, key= lambdax: x.cgpa, reverse = True )
Return sorted_students # Define tge student class
Class students:
def_ _init_ _(self, name, roll_number, cgpa):
self.name =name
Self. roll_number
Self. cgpa=cgpa
# Test the function with a list od student objects
Student= [
Student ("Alice", "A101", 3.8),
Student("Bob", "B102", 3.6),
Student("Charlie", "C103", 3.9),
Student("David", "D104", 3.5), ]
Sorted_students=sort_students (students)
#print tge sorted list od students
for students in sorted_students:
Print(f"Name: { student. name}, Roll Number : {students. roll_number }, CGPA :{student. cgpa}")

