# По объекту Шушары зона 21
# Посчитать объем бетона железобетонных конструкций
# 1-й этаж
# Плита над подвалом
S_plate_1 = 397  # секция 1
S_plate_2 = 418.85  # секция 2
S_plate_3 = 322.44  # секция 3
S_plate_4 = 358.25  # секция 4
S_plate_5 = 403.99  # секция 5
S_plate_6 = 407.73  # секция 6
S_plate_7 = 401.77  # секция 7
S_plate_8 = 408.46  # секция 8
S_plate_9_10 = 637.83  # секция 9 и 10
S_plate_11 = 323.45  # секция 11
S_plate_12 = 360.51  # секция 12
h_1st_floor = 0.22  # Высота перекрытия над подвалом


# Стены 1-го этажа
class Wall:
    def __init__(self, s=0.0, h=3.430):
        self.square_wall = s
        self.height_wall = h

    def volume(self):
        return self.square_wall * self.height_wall


print("Объем стен для 1-го этажа (без учёта проёма)")
Walls_1 = Wall(42.514)
print("Секция 1 =", Walls_1.volume(), "м3")
Walls_2 = Wall(44.6)
print("Секция 2 =", Walls_2.volume(), "м3")
Walls_3 = Wall(34.712)
print("Секция 3 =", Walls_3.volume(), "м3")
Walls_4 = Wall(38.78)
print("Секция 4 =", Walls_4.volume(), "м3")
Walls_5 = Wall(37.148)
print("Секция 5 =", Walls_5.volume(), "м3")
Walls_6 = Wall(38.997)
print("Секция 6 =", Walls_6.volume(), "м3")
Walls_7 = Wall(38.861)
print("Секция 7 =", Walls_7.volume(), "м3")
Walls_8 = Wall(43.084)
print("Секция 8 =", Walls_8.volume(), "м3")
Walls_9_10 = Wall(66.924)
print("Секция 9 и 10 =", Walls_9_10.volume(), "м3")
Walls_11 = Wall(34.818)
print("Секция 11 =", Walls_11.volume(), "м3")
Walls_12 = Wall(36.1)
print("Секция 12 =", Walls_12.volume(), "м3\n")
total_walls_volume = Walls_1.volume() + Walls_2.volume() + Walls_3.volume() + Walls_4.volume() + Walls_5.volume() + \
                     Walls_6.volume() + Walls_7.volume() + Walls_8.volume() + Walls_9_10.volume() + Walls_11.volume() \
                     + Walls_12.volume()
print("Объем стен для 1-го этажа (без учёта проёма)", round(total_walls_volume, 2))


# Проёмы 1-го этажа
class Hole_wall:
    def __init__(self, L=0.0, w=0.2, h=0.0):
        self.long_hole = L
        self.width_hole = w
        self.height_hole = h

    def volume(self):
        return self.long_hole * self.width_hole * self.height_hole


print("Объем проёмов для 1-го этажа")
hole_type1 = Hole_wall(1.8, 0.2, 2.3)
amount_hole_type1 = 33
total_hole_type1 = hole_type1.volume() * 33
print("Проёмы 1800х2300", amount_hole_type1, "шт =", total_hole_type1, "м3")
