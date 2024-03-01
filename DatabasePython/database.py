class Student:
    def __init__(self, id, name, birthDate):
        self.id = id
        self.name = name
        self.birthDate = birthDate

class Database:
    def __init__(self):
        self.table = {}

    def insertStudent(self, student):
        self.table[student.id] = student

    def getStudentById(self, id):
        return self.table.get(id)


def main():
    database = Database()
    for i in range (1,11):
        student = Student(i, f"Aluno({i})", "19/04/2001")
        database.insertStudent(student)
        
    id = 4
    studentOnDatabase = database.getStudentById(id)

    if studentOnDatabase is not None:
        print(f"\nDados sobre o aluno com o ID {id}")
        print(f"Id: {studentOnDatabase.id}")
        print(f"Nome: {studentOnDatabase.name}")
        print(f"Data de Nascimento: {studentOnDatabase.birthDate}\n")
    
    else:
        print(F"Aluno com o  Id {id} não encontrado!")



if __name__ == "__main__":
    main()





