class Rectangle:
    def __init__(self , length , width):
        self.__length = length
        self.__width = width
        pass

    def area(self):
        return  self.__length * self.__width
        pass

    def perimeter(self):
        return (self.__length + self.__width)*2
        pass