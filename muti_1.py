class Shape:
    def area(self):
        raise NotImplementedError(&quot;Subclasses must Implement area()&quot;)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def area(self):
        print(f&quot;The Area of Rectangle is {self.length*self.width}&quot;)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        print(f&quot;The Area of Rectangle is {self.length ** 2}&quot;)


# Creating Objects of class
Rect = Rectangle(3, 4)
my_sqre = Square(4)

Rect.area()
my_sqre.area()