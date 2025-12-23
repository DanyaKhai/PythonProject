class Employee:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    def get_info(self):
        return f'Имя: {self.name}. Id:  {self.id_number}.'

class Manager(Employee):
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department
    def manager_project(self):
        return f'{super().get_info()}  Менеджер: {self.department}.'

class Technician(Employee):
    def __init__(self, name, id_number, specialization):
        super().__init__(name, id_number)
        self.specialization = specialization
    def perform_maintenance(self):
        return f'{super().get_info()} Техник отвечающий за: {self.specialization}.'

class TeachManager(Manager, Technician):
    def __init__(self, name, id_number, department, specialization):
        super().__init__(name,id_number,department)
        self.specialization = specialization
        self.team = []
    def add_employee(self, man):
        self.team.append(man)
    def get_team_info(self):
        print(f'Команда: {self.team}.')







