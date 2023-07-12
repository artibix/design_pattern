# 本文件由 ChatGPT 生成

class Person:
    def __init__(self, name: str):
        self._name = name

    def show(self):
        print(f'{self._name}的装扮')


def hat(cls):
    class Decorator(cls):
        def show(self):
            print('帽子')
            super().show()

    return Decorator


def coat(cls):
    class Decorator(cls):
        def show(self):
            print('外套')
            super().show()

    return Decorator


def pants(cls):
    class Decorator(cls):
        def show(self):
            print('裤子')
            super().show()

    return Decorator


@hat
@coat
@pants
class Finery(Person):
    def __init__(self, component: Person):
        self._component = component

    def show(self):
        if self._component:
            self._component.show()


if __name__ == '__main__':
    p = Person('小明')

    print('Finery 1: \n')

    finery = Finery(p)
    finery.show()
