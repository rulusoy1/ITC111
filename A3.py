def main():
    studentFile = "students.txt"
    studentList = setupList(studentFile)
    choice = menu()
    while choice != 'Q':
        if choice == 'A':
            print("Processing option A")
            addStudent(studentFile, studentList)
        elif choice == 'S':
            print("Processing option S")
            searchStudent(studentList)
        else:
            print("Invalid input - select A, S or Q!")
        choice = menu()
    print("Ending program!")

def menu():
    print("\n\nWelcome to the AGoS System of IUA\n")
    print("Please select an option from the following.")
    print("<A>dd details of a student.")
    print("<S>earch student details for a student.")
    print"<Q>uit.")
    option = input("Enter option (A,S, or Q): ")
    return option

def setupList(f):
    infile = open(f, 'r')
    studentList = []
    for line in infile:
        lineList = (line.strip()).split()
        studentList.append(lineList)
    infile.close()
    return studentList

def searchStudent(studentList):
    search = 'Y'
    while search == 'Y':
        id = input("Enter student id: ")
        displayStudent(studentList, id)
        search = input("Do you want to search another student (Y/N): ")
        while (search != 'Y' or search != 'N'):
            search = input("Do you want to search another student (Y/N): ")
    
'''
def displayStudent(studentList, id):


def addStudent(studentFile, studentList):
    sFile = open(studentFile, 'a')
    id, name, assignment1, assignment2, exam = getStudentDetails()
    weightedTotal, weightedTotalWithBonus = calculateWeightedMarks(assignment1, assignment2, exam)
    writeToFile(id, name, assignment1, assignment2, exam, weightedTotal, weightedTotalWithBonus, sFile)
    sFile.close()
    writeToList(id, name, assignment1, assignment2, exam, weightedTotal, weightedTotalWithBonus, studentList)
'''
    
main()
