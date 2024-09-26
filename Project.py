class Student:
    student_dictionary = {}
    school_name = "Nandha"
    
    def __init__(self):
        self.roll_no = input("\n\tEnter the Student Roll Number: ")
        self.name = input("\n\tEnter the Student Name: ")
        self.address = input("\n\tEnter the Student Address: ")
        self.phone_number = input("\n\tEnter the Student Phone Number: ")
        self.student_class = input("\n\tEnter the Student class [Ex: 1 2 3 4 5 6 7 8 9 10]: ")
        
        if self.student_class in StudentClass.classes:
            StudentClass.classes[self.student_class].studentList.append(self)
        else:
            new_class = StudentClass(self.student_class)
            new_class.studentList.append(self)
            StudentClass.classes[self.student_class] = new_class
        
        print("\nStudent Added Successfully")
        self.getStudent()
        
    def getStudent(self):
        print('\n--- STUDENT DETAILS ---\n')
        print(f'\tRoll Number : {self.roll_no}')
        print(f'\tName : {self.name}')
        print(f'\tPhone Number : {self.phone_number}')
        print(f'\tAddress : {self.address}')
        print(f'\tClass : {self.student_class}')
        print(f'\tSchool Name : {Student.school_name}')
    
    def updateStudent(self):
        print('\t\tSelect option to update student details:')
        print('\t\t1) Change Student Name')
        print('\t\t2) Change Student Phone Number')
        print('\t\t3) Change Student Address')
        print('\t\t4) Change Student Class')
        
        option = input('\t\tEnter any above-given option: ')
        
        if option == "1":
            self.name = input('\t\tEnter the Student New Name: ')
            print('\n\t\tStudent Name changed successfully\n')
        elif option == "2":
            self.phone_number = input('\t\tEnter the Student New Phone Number: ')
            print('\n\t\tStudent Phone Number changed successfully')
        elif option == "3":
            self.address = input('\t\tEnter the Student New Address: ')
            print('\n\t\tStudent Address changed successfully')
        elif option == "4":
            new_class = input('\t\tEnter the Student New Class: ')
            self.student_class.studentList.remove(self)
            if new_class in StudentClass.classes:
                self.student_class = StudentClass.classes[new_class]
            else:
                new_class_obj = StudentClass(new_class)
                StudentClass.classes[new_class] = new_class_obj
                self.student_class = new_class_obj
            self.student_class.studentList.append(self)
            print('\n\t\tStudent Class changed successfully')
        else:
            print('\n\t\tYou have chosen a wrong option')
        
        self.getStudent()

    @classmethod
    def updateSchoolName(cls, new_school_name):
        cls.school_name = new_school_name

    @classmethod
    def getTotalStudentsCount(cls):
        return len(cls.student_dictionary)


class StudentClass:
    classes = {}

    def __init__(self, name):
        self.name = name
        self.studentList = []


def main():
    print(f"---- Welcome to {Student.school_name} ----\n")
    print("\t1) Get Student Details")
    print("\t2) Add New Student")
    print("\t3) Remove Student")
    print("\t4) Update Student Details")
    print("\t5) Update School Name")
    print("\t6) Get Number of Students in School")
    print("\t7) Get All Student Details")
    print("\t8) Get Class Student Details")
    
    option = input("Enter any given option: ")
    
    if option == "1":
        roll_no = input('\tEnter Student Roll Number: ')
        student = Student.student_dictionary.get(roll_no)
        if student:
            student.getStudent()
        else:
            print("\t\tStudent not found")
    
    elif option == "2":
        new_student = Student()
        Student.student_dictionary[new_student.roll_no] = new_student
    
    elif option == "3":
        roll_no = input('\tEnter Student Roll Number: ')
        student = Student.student_dictionary.pop(roll_no, None)
        if student:
            student.student_class.studentList.remove(student)
            print(f'\t\tStudent {roll_no} deleted successfully')
        else:
            print('\t\tNo student found to delete')
    
    elif option == "4":
        roll_no = input('\tEnter Student Roll Number: ')
        student = Student.student_dictionary.get(roll_no)
        if student:
            student.updateStudent()
        else:
            print("\n\t\tStudent not found")
    
    elif option == "5":
        new_school_name = input("\tEnter the New School Name: ")
        Student.updateSchoolName(new_school_name)
        print('School Name changed successfully')
    
    elif option == "6":
        print(f"Total Number of Students in School: {Student.getTotalStudentsCount()}")
    
    elif option == "7":
        if Student.student_dictionary:
            print(f"Total Number of Students: {Student.getTotalStudentsCount()}")
            for student in Student.student_dictionary.values():
                student.getStudent()
        else:
            print('\tNo students available')
    
    elif option == "8":
        class_name = input('\tEnter the Class Name: ')
        student_class = StudentClass.classes.get(class_name)
        if student_class:
            print(f'\nStudents in Class {class_name}:')
            for student in student_class.studentList:
                student.getStudent()
        else:
            print("\t\tNo such class found")


if __name__ == '__main__':
    option = "y"
    while option.lower() == "y":
        main()
        option = input('\nDo you want to continue [y/n]: ')
