import mongoengine as me


me.connect('students')


class Group(me.Document):
    group_name = me.StringField(max_length=64)


class Marks(me.Document):
    marks = me.IntField(min_value=0, max_value=10)


class Curator(me.Document):
    curator_name = me.StringField(max_length=64)


class Faculty(me.Document):
    faculty_name = me.StringField(max_length=64)


class Student(me.Document):
    name = me.StringField(max_length=64)
    group_name = me.ReferenceField(Group)
    marks = me.ListField(me.ReferenceField(Marks))
    curator_name = me.ReferenceField(Curator)
    faculty_name = me.ReferenceField(Faculty)

    @classmethod
    def get_bests_students(cls, faculty=None):
        if faculty:
            star_student = {}
            for student in cls.objects(faculty_name=faculty):
                star_student[student.id] = student.average_score()
            return dict(sorted(star_student.items(), key=lambda item: item[1], reverse=True)[:3])
        else:
            star_student = {}
            for student in cls.objects():
                star_student[student.id] = student.average_score()
            return dict(sorted(star_student.items(), key=lambda item: item[1], reverse=True)[:3])

    @classmethod
    def get_students_by_curator(cls, curator=None):
        if curator is None:
            return cls.objects
        return cls.objects(curator_name=curator)

    def average_score(self):
        return sum(self.marks) / len(self.marks)
