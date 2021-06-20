class Person:
    def __init__(self, fullname, age):
        self.fullname = fullname
        self.age = age

    def __str__(self):
        return f"Имя человека - {self.fullname}, его возраст {self.age}"


class Driver(Person):
    def __init__(self, fullname, age, experience):
        super().__init__(fullname, age)
        self.experience = experience

    def __str__(self):
        return f"Имя водителя - {self.fullname}, его возраст {self.age}, стаж {self.experience}"


class Engine:
    def __init__(self, force, name_company):
        self.force = force
        self.name_company = name_company

    def __str__(self):
        return f"Мощность двигателя - {self.force}, производитель - {self.name_company}"


class Car:
    def __init__(self, car_name, driver_name, driver_age, driver_experience, engine_force, engine_name_company):
        self.car_name = car_name
        self.driver = Driver(driver_name, driver_age, driver_experience)
        self.engine = Engine(engine_force, engine_name_company)

    def start(self):
        print('Car has been moved forward.')

    @staticmethod
    def stop():
        print('Car has stopped.')

    @staticmethod
    def turn_right():
        print('Car has turned right.')

    @staticmethod
    def turn_left():
        print('Car has turned left.')

    def __str__(self):
        return f"Марка машины - {self.car_name}, имя водителя {self.driver.fullname}, стаж водителя {self.driver.experience}," \
               f" его возраст {self.driver.age}, мощность двигателя {self.engine.force}, производитель {self.engine.name_company}"

class Lorry(Car):
    def __init__(self, car_name, driver_name, driver_age, driver_experience, engine_force, engine_name_company, *data_of_full):
        super().__init__(car_name, driver_name, driver_age, driver_experience, engine_force, engine_name_company)
        if data_of_full == ():
            self.is_full = 'Не загружен'
        else:
            self.is_full = data_of_full[0]

    def __str__(self):
        return f"Марка машины - {self.car_name}, имя водителя {self.driver.fullname}, стаж водителя {self.driver.experience}," \
               f" его возраст {self.driver.age}, мощность двигателя {self.engine.force}, производитель {self.engine.name_company}" \
               f" заполненность - {self.is_full}"


class SportCar(Car):
    def __init__(self, car_name, driver_name, driver_age, driver_experience, engine_force, engine_name_company, *data_of_speed):
        super().__init__(car_name, driver_name, driver_age, driver_experience, engine_force, engine_name_company)
        if data_of_speed == ():
            self.speed = 0
        else:
            self.speed = data_of_speed[0]

    def start(self):
        self.speed = 100
        print('Разгоняюсь до 100 км/ч.')

    def stop(self):
        self.speed = 0
        print('Сбавляю скорость до 0.')

    def turn_right(self):
        print('SportCar has turned right.')

    def turn_left(self):
        print('SportCar has turned left.')

    def __str__(self):
        return f"Марка машины - {self.car_name}, имя водителя {self.driver.fullname}, стаж водителя {self.driver.experience}," \
               f" его возраст {self.driver.age}, мощность двигателя {self.engine.force}, производитель {self.engine.name_company}" \
               f" скорость машины - {self.speed}"


print('-------------TASK1-------------')
new_person = Person('name_main', 100)
print(new_person)
new_driver1 = Driver('name1', 15, 15)
new_driver2 = Driver('name2', 27, 17)
print(new_driver1)
new_lorry = Lorry('Mercedez', 'Grisha', 15, 2, 660, 'GeneralMotors')
print(new_lorry)
new_sportcar = SportCar('Ferrari', 'Grisha', 15, 10, 800, 'GeneralMotors', 100)
print(new_sportcar)
print('-------------------------------')
new_sportcar.start()
new_sportcar.stop()
print('-------------TASK2-------------')
new_sportcar.turn_left()
new_lorry.turn_right()
