import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = [1] * self.sides_count
        self.__color = list(color)
        self.filled = False

        if self.__is_valid_sides(*sides):
            self.set_sides(*sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color, circumference)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def get_radius(self):
        return self.__radius

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            super().set_sides(*new_sides)
            self.__radius = new_sides[0] / (2 * math.pi)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = self.__len() / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, edge):
        super().__init__(color, edge)
        self.__sides = [edge] * self.sides_count

    def get_volume(self):
        edge = self.get_sides()[0]
        return edge ** 3



circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)


circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())


cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())


print(len(circle1))


print(cube1.get_volume())  