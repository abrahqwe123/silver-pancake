
class Purse:
    def __init__(self, currency: str, name: str):
        if currency not in ('USD', 'EUR', 'RUB'):
            return ValueError('Ошибка создания кошелька')
        12e4123er123r
        self.__money = 0.00
        self.currency = currency
        self.name = name
        self.__start()

    def __start(self):
        print(f"Аккаунт {self.name} успешно создан c валютой {self.currency}")

    def topUpBalance(self, *, money: float):
        self.__money += money
        print(f"Пополнение баланса на: {self.__money} {self.currency}")

    def topDownBalance(self, money: float):
        if (self.__money - money) > 0:
            self.__money -= money
            print(f"Снятие с баланса: {self.__money} {self.currency}")
        else:
            print(f"Не достаточно средств, текущий баланс: {self.__money} {self.currency}")

    def transferMoney(self, user: 'Purse', amount: int):
        if self.currency != user.currency:
            print(f"Ошибка! Нельзя перевести деньги между кошельками с разными валютами")
            return
        
        if (self.__money - amount) < 0:
            print(f"Ошибка! Недостаточно средств на кошельке {self.name}")
            return
        else:
            self.__money -= amount
            user.__money += amount
            print(f"[{self.name}] Успешный перевод пользователю {user.name} суммы: {amount} {user.currency}")


    def balance(self):
        print(f"[{self.name}] Текущий баланс: {self.__money} {self.currency}")

    
user1 = Purse('RUB', 'Vadim')
user1.topUpBalance(money=700)

user2 = Purse('RUB', 'Ivan')
user1.transferMoney(user2, 200) 

user1.balance()
user2.balance()