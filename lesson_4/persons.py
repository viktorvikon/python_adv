from abc import abstractmethod, ABC
from datetime import date


class Person(ABC):

    def __init__(self, name, birthday, faculty):
        self.name = name
        self.birthday = birthday
        self.faculty = faculty

    @abstractmethod
    def person_age(self):
        today = date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age

    @abstractmethod
    def __str__(self):
        return f"Фамилия: {self.name}\nДата рождения: {self.birthday}\nФакультет: {self.faculty}"


class Enrolment(Person):

    def person_age(self):
        age = super().person_age()
        return age

    def __str__(self):
        main_str = super().__str__()
        return main_str


class Student(Person):

    def __init__(self, name, birthday, faculty, course):
        super().__init__(name, birthday, faculty)
        self.course = course

    def person_age(self):
        age = super().person_age()
        age_str = "Возраст: " + str(age)
        age_str.__str__()
        return age

    def __str__(self):
        main_str = super().__str__()
        return f"{main_str}\nКурс: {self.course}"


class Teacher(Person):

    def __init__(self, name, birthday, faculty, position, experience):
        super().__init__(name, birthday, faculty)
        self.position = position
        self.experience = experience

    def person_age(self):
        age = super().person_age()
        age_str = "Возраст: " + str(age)
        age_str.__str__()
        return age

    def __str__(self):
        main_str = super().__str__()
        return f"{main_str}\nДолжность: {self.position}\nСтаж: {self.experience}"


petrov = Enrolment("Петров", date(2001, 11, 23), "Математический")
serezhin = Enrolment("Сережин", date(2002, 10, 11), "Кибернетики")
sidorov = Student("Сидоров", date(1998, 10, 20), "Математический", 3)
gorelov = Student("Горелов", date(1997, 10, 20), "Кибернетики", 4)
pavlov = Teacher("Павлов", date(1981, 5, 6), "Математический", "Старший преподаватель", 12)
korkin = Teacher("Коркин", date(1979, 5, 6), "Кибернетики", "Ассистент", 14)

list_of_person = [petrov, serezhin, sidorov, gorelov, pavlov, korkin]

for i in range(len(list_of_person)):
    print("-" * 45)
    print(list_of_person[i])

print("\n" + "*" * 45 + "\n")


for i in range(len(list_of_person)):
    if list_of_person[i].person_age() <= 18:
        print("-" * 45)
        print(list_of_person[i])
