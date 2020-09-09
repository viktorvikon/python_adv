class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Point(new_x, new_y, new_z)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        return Point(new_x, new_y, new_z)
    
    def __mul__(self, other):
        new_x = self.x * other.x
        new_y = self.y * other.y
        new_z = self.z * other.z
        return Point(new_x, new_y, new_z)

    def __truediv__(self, other):
        try:
            new_x = self.x // other.x
            new_y = self.y // other.y
            new_z = self.z // other.z
        except ZeroDivisionError:
            print("You can't divide by zero")
        else:
            return Point(new_x, new_y, new_z)

    def __neg__(self):
        return Point(-self.x, -self.y, -self.z)

    def __str__(self):
        return f"{self.x} {self.y} {self.z}"


point_1 = Point(1, 2, 3)
point_2 = Point(1, 2, 3)
result = point_1 * point_2
print("-" * 45)
print(result)
print("-" * 45)
