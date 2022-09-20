# class Area:
#     def __init__(self, h, w):
#         self.h = h
#         self.w = w
#
#     def Method1(self, x, y):
#         print(x*y)
#
#     def FindMaxRectangle(self):
#         self.max_rectangle = [(100, 200),  (150, 300)]
#
# a = 12
# b = 7
# Area_test = Area(100, 200)
# print(Area_test.h, Area_test.w)
# Area_test.FindMaxRectangle()
# print(Area_test.max_rectangle)
#
#
# class Human:
#     def __init__(self, age, sex):
#         self.age = age
#         self.sex = sex
#         self.home_planet = 'Земля'
#
#     def speek(self, message):
#         print(message)
#
#     def see(self, distance):
#         if distance > 100:
#             print('Нужен бинокль')
#         else:
#             print('Вижу что-то')
#
#
# Ilya = Human(27, 'M')
# print(Ilya.age, Ilya.sex)
#
# Andrew = Human(43, 'M')
# Andrew.age = 44
# print(Andrew.age, Andrew.sex)
#
# Ilya.age = 28
# print(Ilya.age)
#
# print(Ilya.home_planet, Andrew.home_planet)
#
# Ilya.speek('Привет')
# Andrew.see(120)
# Ilya.see(20)

class Stead:
    """Класс-словарь, содержащий координаты участка"""
    coordinates = {
    }  # Пустой словарь для координат участка


land_plot_1 = Stead()
print(land_plot_1.__doc__)
print(land_plot_1.coordinates)


class Building:
    """Класс, описывающий здание"""

    def __init__(self, building_volume, floors, total_flats_s, total_flats_1k, total_flats_2k, total_flats_3k,
                 total_area, amt_parking_spaces):
        self.building_volume = building_volume  # строительный объем
        self.floors = floors  # число этажей
        self.total_flats_s = total_flats_s  # число квартир-студий всего
        self.total_flats_1k = total_flats_1k  # число квартир-1к всего
        self.total_flats_2k = total_flats_2k  # число квартир-2к всего
        self.total_flats_3k = total_flats_3k  # число квартир-3к всего
        self.total_area = total_area  # общая площадь здания
        self.amt_parking_spaces = amt_parking_spaces  # число парковочных мест


class Floor:
    """Класс описывающий этаж"""

    def __init__(self, floor_area, flats_s, flats_1k, flats_2k, flats_3k, index):
        self.floor_area = floor_area  # площадь этажа
        self.flats_s = flats_s  # число квартир-студий
        self.flats_1k = flats_1k  # число квартир-1к
        self.flats_2k = flats_2k  # число квартир-2к
        self.flats_3k = flats_3k  # число квартир-3к
        self.index = index

        self.flats_array = [Flat(70, 110, 5, 2), Flat(75, 120, 7, 3)]


class Flat:
    """Класс описывающий квартиру"""

    def __init__(self, flat_living_area, flat_total_area, flat_total_area_balcony, room_numbers):
        self.flat_living_area = flat_living_area  # Жилая площадь квартиры
        self.flat_total_area = flat_total_area  # Общая площадь квартиры
        self.flat_total_area_balcony = flat_total_area_balcony  # Общая площадь квартиры с учетом балконов (у площади балконов есть свои коэффициенты)
        self.room_numbers = room_numbers  # Число комнат

        self.walls = [Wall(100, 200, 'FDF'), ]

    kitchen_separately = 'yes'  # Чтобы идентифицировать студию или квартиры евро-формата


Floor1 = Floor(... index = 1)
Flat1 = Flat(70, 110, 5, 2)
Floor1.flats_array.append(Flat1) # Добавление квартиры к этажу

Floor1.flats_arra[0].flat_living_area

