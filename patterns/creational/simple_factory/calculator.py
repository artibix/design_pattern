class Operation:
    num1 = 0
    num2 = 0

    def result(self):
        pass


class Add(Operation):
    def result(self):
        return self.num1 + self.num2


class Sub(Operation):
    def result(self):
        return self.num1 - self.num2


class Mul(Operation):
    def result(self):
        return self.num2 * self.num1


class Div(Operation):
    def result(self):
        if self.num2 == 0:
            raise ValueError('除数不能为0')
        return self.num1 / self.num2


class OperationFactory:
    @staticmethod
    def create_operate(operate):
        match operate:
            case '+':
                return Add()
            case '-':
                return Sub()
            case '*':
                return Mul()
            case '/':
                return Div()


if __name__ == '__main__':
    op = OperationFactory.create_operate('-')
    op.num1 = 100
    op.num2 = 321
    print(op.result())
