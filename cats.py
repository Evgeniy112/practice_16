from classes import Cat

c1 = Cat('Барон', 'Кот', 2)
c2 = Cat('Муся', 'Кошка', 5)
pet_list = [c1,c2]
for pet in pet_list:
    print(pet.get_pet())