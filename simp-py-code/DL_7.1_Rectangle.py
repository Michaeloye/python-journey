class Rectangle:
    def __init__(self, width = 1, height = 2):
        self.__width = width
        self.__height = height
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    def getArea(self):
        return self.__width * self.__height
    def getPerimeter(self):
        return (2 * self.__width) + (2 * self.__height)

rectangle1 = Rectangle(4, 40)
rectangle2 = Rectangle(3.5, 35.7)
print("Width is ", rectangle1.getWidth(), "\tHeight is ", rectangle1.getHeight(), "Area is ", rectangle1.getArea(), "Perimeter is ", rectangle1.getPerimeter())
print("Width is ", rectangle2.getWidth(), "\tHeight is ", rectangle2.getHeight(), "Area is ", rectangle2.getArea(), "Perimeter is ", rectangle2.getPerimeter())