import math


class CashSuper:
    def accept_cash(self, money: float):
        pass


class CashNormal(CashSuper):
    def accept_cash(self, money: float):
        return money


# 打折
class CashRebate(CashSuper):
    money_rebate: float = 1

    def __init__(self, money_rebate: float):
        self.money_rebate = money_rebate

    def accept_cash(self, money: float):
        return self.money_rebate * money


# 满 condition 反 return
class CashReturn(CashSuper):
    money_condition: float = 0
    money_return: float = 0

    def __init__(self, money_condition, money_return):
        self.money_condition = money_condition
        self.money_return = money_return

    def accept_cash(self, money: float):
        if money > self.money_condition:
            return money - math.floor(money / self.money_condition) * self.money_return


class CashContext:
    def __init__(self, cash_type: str):
        match cash_type:
            case '正常收费':
                self.c = CashNormal()
            case '满300反100':
                self.c = CashReturn(300, 100)
            case '打5折':
                self.c = CashRebate(0.5)

    def result(self, money: float):
        return self.c.accept_cash(money)


if __name__ == '__main__':
    cash_demo = CashContext('打5折')
    total_price: float = 1000.23
    print(cash_demo.result(total_price))
