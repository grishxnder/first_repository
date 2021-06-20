class rooms_innop():
    a = []
    def __init__(self, name, number, level):
        self.name = name
        self.number = number
        self.level = level
        rooms_innop.a.append(self)
    def __str__(self):
        return f'{self.name} {self.number}'
    def entry_room(self, person_innop):
        print(f'{person_innop.type} {person_innop.name} {person_innop.surname} пытается войти в {self.name} {self.number} {self.level <= person_innop.level_access}')


class person_innop():

    @classmethod
    def __init__(self, name, surname, feature):
        pass

    @classmethod
    def get_level(self):
        pass



class parent(person_innop):
    a = []
    def __str__(self):
        return
    def __init__(self, name, surname, feature):
        self.name = name
        self.surname = surname
        self.feature = feature
        self.level_access = 0
        self.type = 'Родитель'
        parent.a.append(self)

    def get_level(self):
        return self.level_access()


    def __str__(self):
        return (f'{self.name} {self.surname} {self.feature}')


class student(person_innop):
    a = []
    def __init__(self, name, surname, feature):
        self.name = name
        self.surname = surname
        self.feature = feature
        self.level_access = 1
        self.type = 'Ученик'
        student.a.append(self)

    def get_level(self):
        return self.level_access()

    def __str__(self):
        return (f'{self.name} {self.surname} {self.feature}')


class teacher(person_innop):
    a = []
    def __init__(self, name, surname, feature):
        self.name = name
        self.surname = surname
        self.feature = feature
        self.level_access = 2
        self.type = 'Учитель'
        teacher.a.append(self)

    def get_level(self):
        return self.level_access()

    def __str__(self):
        return (f'{self.name} {self.surname} {self.feature}')


class director(person_innop):
    a = []
    def __init__(self, name, surname, feature):
        self.name = name
        self.surname = surname
        self.feature = feature
        self.level_access = 3
        self.type = 'Директор'
        director.a.append(self)

    def get_level(self):
        return self.level_access()

    def __str__(self):
        return (f'{self.name} {self.surname} {self.feature}')


act_hall = rooms_innop('Актовый зал', 1,  0)
class_room = rooms_innop('Класс', 2,  1)
teacher_room = rooms_innop('Учительская комната', 3, 2)
direct_room = rooms_innop('Кабинет Директора', 4, 3)
student_1 = student('Ivan', 'Ivanov', '10E')
parent_1 = parent('Ivan', 'Neivanov', '10 детей')
teacher_1 = teacher('Anna', 'Prokhorova', 'Шутка смешная.')
director_1 = director('Grigoriy', 'Prokhorov', '10 наград')
print('Учителя: ', end='')
print(*teacher.a)
print('Родители: ', end='')
print(*parent.a)
print('Ученики: ', end='')
print(*student_1.a)
print('Директора: ', end='')
print(*director.a)
print(*rooms_innop.a)
act_hall.entry_room(student_1)
class_room.entry_room(parent_1)
direct_room.entry_room(student_1)
teacher_room.entry_room(parent_1)
