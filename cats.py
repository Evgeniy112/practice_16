class Cat:
    def __init__(self, name='', gender='', age='0'):
        self.name = name
        self.gender = gender
        self.age = age
    def get_pet(self):
        return f'{self.name} {self.age} {self.gender}'


class Customers:
    def __init__(self,first_name,second_name,city,baiance):
        self.first_name = first_name
        self.second_name = second_name
        self.balance = baiance
        self.city = city
    def __str__(self):
        return f'''"{self.first_name} {self.second_name}".{self.city}. Баланс: {self.balance} руб.'''
    def get_guests(self):
        return f'{self.first_name} {self.second_name} {self.city}'
