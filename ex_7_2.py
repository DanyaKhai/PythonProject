class Employee:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    def get_info(self):
        return f'Базавая информация о сотруднике: Имя: {self.name}, Уникальный номер: {self.id_number}.'



class Manager(Employee):
    def __init__(self, name, id_number, deportment):
        super().__init__(name, id_number)
        self.deportment = deportment
    def manage_project(self):
        return f'Сотрудник в должности менеджера, отвечающий за: {self.deportment}. '


class Technician(Employee):
    def __init__(self, name, id_number, specialization):
        super().__init__(name, id_number)
        self.specialization = specialization
    def perform_maintenance(self):
        return f'Выполняет техническое обслуживание: {self.specialization}. '


class TechManager(Manager, Technician):
    def __init__(self, name, id_number,deportment, specialization):
        Employee.__init__(self, name, id_number)
        self.deportment = deportment
        self.specialization = specialization
        self.list = []
    def add_employee(self, man):
        self.list.append(man)
    def get_tean_info(self):
        return f'Список всех сотрудников: {self.list}. '


emp1 = Employee('Сергей', 1)
emp2 = Manager('Валентин', 2, 'Котиков')
emp3 = Technician('Вова', 3, 'Микровалновки')
emp4 = TechManager('Никита', 4, 'Собачки', 'ЧайникиСобачки')

print(emp1.get_info())
print(emp2.manage_project())
print(emp3.perform_maintenance())

emp4.add_employee(emp1)
emp4.add_employee(emp2)
emp4.add_employee(emp3)

print(emp4.get_tean_info())