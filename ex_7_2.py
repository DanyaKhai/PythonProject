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
        return f'Сотрудник в должности менеджера, отвечающий за '
