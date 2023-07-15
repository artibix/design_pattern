# 原型模式 with Python
import copy
# 用copy包实现深拷贝(copy.deepcopy())和浅拷贝(copy.copy())
from abc import abstractmethod, ABCMeta


# 创建接口
class Shape(metaclass=ABCMeta):
    _id: str
    _type: str

    @abstractmethod
    def draw(self):
        pass

    def get_type(self):
        return self._type

    def get_id(self):
        return self._id

    def set_id(self, _id):
        self._id = _id

    def clone(self):
        # 深拷贝
        clone = copy.deepcopy(self)
        return clone


# 创建实体类
class Rectangle(Shape):
    def __init__(self):
        self._type = "Rectangle"

    def draw(self):
        print("Inside Rectangle.draw() method.")


class Square(Shape):
    def __init__(self):
        self._type = "Square"

    def draw(self):
        print("Inside Square.draw() method.")


class Circle(Shape):
    def __init__(self):
        self._type = "Circle"

    def draw(self):
        print("Inside Circle.draw() method.")


# 获取数据实体类
class ShapeCache:
    # Python 无静态变量，用开放类变量
    shapeMap = {}

    def get_shape(self, shape_id):
        cached_shape = self.shapeMap[shape_id]
        return cached_shape.clone()

    # 静态方法
    @staticmethod
    def load_cache():
        circle1 = Circle()
        circle1.set_id("1")
        ShapeCache.shapeMap[circle1.get_id()] = circle1

        square1 = Square()
        square1.set_id("2")
        ShapeCache.shapeMap[square1.get_id()] = square1

        rectangle1 = Rectangle()
        rectangle1.set_id("3")
        ShapeCache.shapeMap[rectangle1.get_id()] = rectangle1


# 调用输出
if __name__ == '__main__':
    ShapeCache.load_cache()
    myShape = ShapeCache()

    cloneShape1 = myShape.get_shape("1")
    print("Shape : %s" % cloneShape1.get_type())
    cloneShape1.draw()

    cloneShape2 = myShape.get_shape("2")
    print("Shape : %s" % cloneShape2.get_type())
    cloneShape2.draw()

    cloneShape3 = myShape.get_shape("3")
    print("Shape : %s" % cloneShape3.get_type())
    cloneShape3.draw()
