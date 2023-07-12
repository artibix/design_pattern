# component
class Person:
    def __init__(self, name: str = None):
        self.__name = name

    def show(self):
        print(f'{self.__name}的装扮')


# decorate
class Finery(Person):
    def __init__(self, component: Person):
        self._component = component

    def show(self):
        if self._component:
            self._component.show()


class Hat(Finery):
    def show(self):
        print('帽子')
        super().show()


class Coat(Finery):
    def show(self):
        print('外套')
        super().show()


class Pants(Finery):
    def show(self):
        print('裤子')
        super().show()


if __name__ == '__main__':
    p = Person('小明')

    print('Finery 1: \n')

    hat = Hat(p)
    coat = Coat(hat)
    pants = Pants(coat)

    pants.show()
