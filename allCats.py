from cats import Cat, Customers

c1 = Cat('Барон', 'Кот', 2)
print(c1.name, c1.age, c1.gender)
c2 = Cat('Муся', 'Кошка', 5)
print(c2.name, c2.age, c2.gender)

customer_1 = Customers('Иван','Петров','Москва',50)
print(customer_1)