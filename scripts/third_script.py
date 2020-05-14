# INPUT three values then print a message

#

names = input("Enter name: ").title().split(",")
assignments = input("Enter assignment count: ").split(",")
grades = input("Enter current grades: ").split(",")

message = "\nHi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. \nYou're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))