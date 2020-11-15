import sqlite3
from sql_context_manager import DataBaseManager


NOT_EXIST = "Студент с таким ID не найден!"


class User:

    @classmethod
    def show_all_students(cls):
        students = ''
        request_sql = "SELECT students.name, students.surname, faculty.faculty_name, students.group_id "\
                      "FROM students INNER JOIN faculty on students.faculty_id=faculty.faculty_id"
        with DataBaseManager("students.db") as db:
            db.execute(request_sql)
            for student in db:
                students += f"{student}\n"
            return students

    @classmethod
    def show_all_excellent_students(cls):
        students = ''
        request_sql = "SELECT students.name, students.surname FROM students INNER JOIN grades "\
                      "ON students.id = grades.student_id WHERE grades.marks >= 9"
        with DataBaseManager("students.db") as db:
            db.execute(request_sql)
            for student in db:
                students += f"{student}\n"
            return students

    @classmethod
    def student_by_id(cls, student_id):
        students = ''
        request_sql = "SELECT students.name, students.surname, faculty.faculty_name, students.group_id "\
                      "FROM students INNER JOIN faculty on students.faculty_id=faculty.faculty_id "\
                      "WHERE id = ?"
        with DataBaseManager("students.db") as db:
            result = db.execute(request_sql, [student_id])
            if result:
                for student in db:
                    students += f"{student}\n"
                return students
            else:
                return False

    @classmethod
    def show_full_student_info(cls, student_id):
        students = ''
        request_sql = "SELECT students.id, students.name,students.surname, faculty.faculty_name, "\
                      "subjects.subject_name, grades.marks "\
                      "FROM students INNER JOIN faculty on students.faculty_id=faculty.faculty_id "\
                      "INNER JOIN grades on students.id = grades.student_id "\
                      "INNER JOIN subjects on grades.subject_id = subjects.subject_id WHERE students.id = ?"
        with DataBaseManager("students.db") as db:
            db.execute(request_sql, [student_id])
            for student in db:
                students += f"{student}\n"
            return students


class Admin:

    @classmethod
    def add_student(cls, name, surname, faculty_id, group_id):
        request_sql = "INSERT INTO students ('name', 'surname', 'faculty_id', 'group_id') VALUES (?,?,?,?)"
        with DataBaseManager("students.db") as db:
            db.executemany(request_sql, [(name, surname, faculty_id, group_id)])

    @classmethod
    def modify_existing_student(cls, student_id, name, surname, faculty_id, group_id):
        request_sql = "UPDATE students SET name = ?, surname = ?, faculty_id = ?, group_id = ? WHERE id = ?;"
        with DataBaseManager("students.db") as db:
            db.executemany(request_sql, [(name, surname, faculty_id, group_id, student_id)])
            return db.fetchall()


if __name__ == "__main__":
    user = User()
    print("\nСписок студентов:\n" + "=" * 25)
    print(user.show_all_students())
    print("Список отличников,:\n" + "=" * 25)
    print(user.show_all_excellent_students())
    print("\nСтудент:\n" + "=" * 25)
    print(user.student_by_id(1))
    print("\nПолная информация о студенте:\n" + "=" * 25)
    print(user.show_full_student_info(2))
    admin = Admin()
    admin.add_student("Петер", "Петров", 2, 3)

