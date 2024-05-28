class House:
    def __init__(self):
        self.number_of_floors = 0

    def set_new_num_of_fl(self, floors):
        self.number_of_floors = floors
        print(f'Построил дом. Этажей: {floors}')


h1 = House()
h1.set_new_num_of_fl(input('Введите количество этажей: '))

