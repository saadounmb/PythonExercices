class StudentRecordManager:
    def __init__(self):
        self.students = []
    
    def add_student(self, student_id, name, age, course):
        student = {
            'id': student_id,
            'name': name,
            'age': age,
            'course': course
        }
        self.students.append(student)
        print(f"Student added successfully with ID: {student_id}")
    
    def display_all_students(self):
        print("List of all students:")
        for student in self.students:
            print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")
    
    def search_student(self, student_id):
        for student in self.students:
            if student['id'] == student_id:
                print(f"Student found with ID: {student_id}")
                print(f"Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")
                return
        print(f"Student with ID {student_id} not found.")
    
    def delete_student(self, student_id):
        for student in self.students:
            if student['id'] == student_id:
                self.students.remove(student)
                print(f"Student with ID {student_id} deleted successfully.")
                return
        print(f"Student with ID {student_id} not found.")
    
    def run(self):
        while True:
            print("\nStudent Record Management System")
            print("1. Add Student")
            print("2. Display All Students")
            print("3. Search Student")
            print("4. Delete Student")
            print("5. Quit")
            choice = input("Enter your choice (1-5): ")
            
            if choice == '1':
                student_id = input("Enter student ID: ")
                name = input("Enter student name: ")
                age = input("Enter student age: ")
                course = input("Enter student course: ")
                self.add_student(student_id, name, age, course)
            
            elif choice == '2':
                self.display_all_students()
            
            elif choice == '3':
                student_id = input("Enter student ID to search: ")
                self.search_student(student_id)
            
            elif choice == '4':
                student_id = input("Enter student ID to delete: ")
                self.delete_student(student_id)
            
            elif choice == '5':
                print("Exiting program...")
                break
            
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

# Create an instance of StudentRecordManager and run the program
if __name__ == "__main__":
    record_manager = StudentRecordManager()
    record_manager.run()
