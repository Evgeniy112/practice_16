from cats import Cat, Customers

c1 = Cat('Барон', 'Кот', 2)
c2 = Cat('Муся', 'Кошка', 5)
pet_list = [c1,c2]
for pet in pet_list:
    print(pet.get_pet())

costomer_1 = Customers('Иван','Петров','Москва',50)
costomer_2 = Customers('Владимир','Зайцев','Кострома',50)
costomer_3 = Customers('Олеся','Янина','Новосибирск',50)

guest_list = [costomer_1, costomer_2, costomer_3]

for guest in guest_list:
    print(guest.get_guests())