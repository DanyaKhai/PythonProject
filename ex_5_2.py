class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius
cricle1 = Circle(5)
print(cricle1.get_radius())
cricle1.set_radius(10)
print(cricle1.get_radius())