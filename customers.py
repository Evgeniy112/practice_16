from cats import Customers

costomer_1 = Customers('Иван','Петров','Москва',50)
costomer_2 = Customers('Владимир','Зайцев','Кострома',50)
costomer_3 = Customers('Олеся','Янина','Новосибирск',50)

guest_list = [costomer_1, costomer_2, costomer_3]

for guest in guest_list:
    print(guest.get_guests())