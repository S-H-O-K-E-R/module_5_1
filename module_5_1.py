class House():
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, floor):
        new_floor = 1
        if self.number_of_floors < floor or floor < 1:
            print("Такого этажа не существует")
        else:
            while self.number_of_floors >= floor and floor >= new_floor:
                print(new_floor)
                new_floor += 1

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)