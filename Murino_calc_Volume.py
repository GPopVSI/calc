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
total_walls_volume_without_hole = Walls_1.volume() + Walls_2.volume() + Walls_3.volume() + Walls_4.volume() + \
                                  Walls_5.volume() + Walls_6.volume() + Walls_7.volume() + Walls_8.volume() + \
                                  Walls_9_10.volume() + Walls_11.volume() + Walls_12.volume()
print("Объем стен для 1-го этажа (без учёта проёма)", round(total_walls_volume_without_hole, 2))


# Проёмы 1-го этажа
class Hole_wall:
    def __init__(self, L=0.0, w=0.2, h=0.0):
        self.long_hole = L
        self.width_hole = w
        self.height_hole = h

    def volume(self):
        return self.long_hole * self.width_hole * self.height_hole


print("Объем проёмов для 1-го этажа\n")

hole_type1 = Hole_wall(1.8, 0.2, 2.3)
amount_hole_type1 = 33
total_hole_type1 = hole_type1.volume() * amount_hole_type1
print("1. Проёмы 1800х2300", amount_hole_type1, "шт =", total_hole_type1, "м3")

hole_type2 = Hole_wall(1.0, 0.2, 2.3)
amount_hole_type2 = 24
total_hole_type2 = hole_type2.volume() * amount_hole_type2
print("2. Проёмы 1000х2300", amount_hole_type2, "шт =", total_hole_type2, "м3")

hole_type3 = Hole_wall(1.55, 0.2, 2.3)
amount_hole_type3 = 29
total_hole_type3 = hole_type3.volume() * amount_hole_type3
print("3. Проёмы 1550х2300", amount_hole_type3, "шт =", total_hole_type3, "м3")

hole_type4 = Hole_wall(1.95, 0.2, 2.3)
amount_hole_type4 = 9
total_hole_type4 = hole_type4.volume() * amount_hole_type4
print("4. Проёмы 1950х2300", amount_hole_type4, "шт =", total_hole_type4, "м3")

hole_type5 = Hole_wall(1.64, 0.2, 2.75)
amount_hole_type5 = 83
total_hole_type5 = hole_type5.volume() * amount_hole_type5
print("5. Проёмы 1640х2750", amount_hole_type5, "шт =", total_hole_type5, "м3")

hole_type6 = Hole_wall(1.20, 0.2, 2.75)
amount_hole_type6 = 2
total_hole_type6 = hole_type6.volume() * amount_hole_type6
print("6. Проёмы 1200х2750", amount_hole_type6, "шт =", total_hole_type6, "м3")

hole_type7 = Hole_wall(1.41, 0.2, 2.70)
amount_hole_type7 = 13
total_hole_type7 = hole_type7.volume() * amount_hole_type7
print("7. Проёмы 1410х2700", amount_hole_type7, "шт =", total_hole_type7, "м3")

hole_type8 = Hole_wall(1.50, 0.2, 2.90)
amount_hole_type8 = 26
total_hole_type8 = hole_type8.volume() * amount_hole_type8
print("8. Проёмы 1500х2900", amount_hole_type8, "шт =", total_hole_type8, "м3")

hole_type9 = Hole_wall(1.05, 0.2, 2.10)
amount_hole_type9 = 36
total_hole_type9 = hole_type9.volume() * amount_hole_type9
print("9. Проёмы 1050х2100", amount_hole_type9, "шт =", total_hole_type9, "м3")

hole_type10 = Hole_wall(2.41, 0.2, 3.43)
amount_hole_type10 = 11
total_hole_type10 = hole_type10.volume() * amount_hole_type10
print("10. Проёмы 2410х3430", amount_hole_type10, "шт =", total_hole_type10, "м3")

hole_type11 = Hole_wall(1.36, 0.2, 2.10)
amount_hole_type11 = 12
total_hole_type11 = hole_type11.volume() * amount_hole_type11
print("11. Проёмы 1360х2100", amount_hole_type11, "шт =", total_hole_type11, "м3")

hole_type12 = Hole_wall(1.2, 0.2, 2.1)
amount_hole_type12 = 5
total_hole_type12 = hole_type12.volume() * amount_hole_type12
print("12. Проёмы 1200х2100", amount_hole_type12, "шт =", total_hole_type12, "м3")

hole_type13 = Hole_wall(1.41, 0.2, 2.10)
amount_hole_type13 = 12
total_hole_type13 = hole_type13.volume() * amount_hole_type13
print("13. Проёмы 1410х2100", amount_hole_type13, "шт =", total_hole_type13, "м3")

hole_type14 = Hole_wall(0.9, 0.2, 2.10)
amount_hole_type14 = 8
total_hole_type14 = hole_type14.volume() * amount_hole_type14
print("14. Проёмы 900х2100", amount_hole_type14, "шт =", total_hole_type14, "м3")

hole_type15 = Hole_wall(1.3, 0.2, 2.10)
amount_hole_type15 = 6
total_hole_type15 = hole_type15.volume() * amount_hole_type15
print("15. Проёмы 1300х2100", amount_hole_type15, "шт =", total_hole_type15, "м3")

hole_type16 = Hole_wall(2.4, 0.2, 3.43)
amount_hole_type16 = 1
total_hole_type16 = hole_type16.volume() * amount_hole_type16
print("16. Проёмы 2400х3430", amount_hole_type16, "шт =", total_hole_type16, "м3")

hole_type17 = Hole_wall(2.5, 0.2, 3.43)
amount_hole_type17 = 29
total_hole_type17 = hole_type17.volume() * amount_hole_type17
print("17. Проёмы 2500х3430", amount_hole_type17, "шт =", total_hole_type17, "м3")

hole_type18 = Hole_wall(2.47, 0.2, 3.43)
amount_hole_type18 = 1
total_hole_type18 = hole_type18.volume() * amount_hole_type18
print("18. Проёмы 2470х3430", amount_hole_type18, "шт =", total_hole_type18, "м3")

hole_type19 = Hole_wall(2.43, 0.2, 3.43)
amount_hole_type19 = 5
total_hole_type19 = hole_type19.volume() * amount_hole_type19
print("19. Проёмы 2430х3430", amount_hole_type19, "шт =", total_hole_type19, "м3")

hole_type20 = Hole_wall(1.80, 0.2, 2.50)
amount_hole_type20 = 4
total_hole_type20 = hole_type20.volume() * amount_hole_type20
print("20. Проёмы 1800х2500", amount_hole_type20, "шт =", total_hole_type20, "м3")

hole_type21 = Hole_wall(1.5, 0.2, 2.3)
amount_hole_type21 = 3
total_hole_type21 = hole_type21.volume() * amount_hole_type21
print("21. Проёмы 1500х2300", amount_hole_type21, "шт =", total_hole_type21, "м3")

hole_type22 = Hole_wall(1.25, 0.2, 2.5)
amount_hole_type22 = 2
total_hole_type22 = hole_type22.volume() * amount_hole_type22
print("22. Проёмы 1250х2500", amount_hole_type22, "шт =", total_hole_type22, "м3")

hole_type23 = Hole_wall(1.25, 0.2, 2.5)
amount_hole_type23 = 2
total_hole_type23 = hole_type23.volume() * amount_hole_type23
print("23. Проёмы 1250х2500", amount_hole_type23, "шт =", total_hole_type23, "м3")

hole_type24 = Hole_wall(1.75, 0.2, 2.3)
amount_hole_type24 = 4
total_hole_type24 = hole_type24.volume() * amount_hole_type24
print("24. Проёмы 1750х2300", amount_hole_type24, "шт =", total_hole_type24, "м3")

hole_type25 = Hole_wall(1.62, 0.2, 2.1)
amount_hole_type25 = 1
total_hole_type25 = hole_type25.volume() * amount_hole_type25
print("25. Проёмы 1620х2100", amount_hole_type25, "шт =", total_hole_type25, "м3")

hole_type26 = Hole_wall(2.35, 0.2, 2.3)
amount_hole_type26 = 1
total_hole_type26 = hole_type26.volume() * amount_hole_type26
print("26. Проёмы 2350х2300", amount_hole_type26, "шт =", total_hole_type26, "м3\n")

holes_walls = total_hole_type1 + total_hole_type2 + total_hole_type3 + total_hole_type4 + total_hole_type5 + \
              total_hole_type6 + total_hole_type7 + total_hole_type8 + total_hole_type9 + total_hole_type10 + \
              total_hole_type11 + total_hole_type12 + total_hole_type13 + total_hole_type14 + total_hole_type15 + \
              total_hole_type16 + total_hole_type17 + total_hole_type18 + total_hole_type19 + total_hole_type20 + \
              total_hole_type21 + total_hole_type22 + total_hole_type23 + total_hole_type24 + total_hole_type25 + \
              total_hole_type26
total_walls_volume_with_hole = total_walls_volume_without_hole - holes_walls
print("Объем стен 1-го этажа с учётом проёмов", total_walls_volume_with_hole, "м3\n")


class Plate:
    def __init__(self, s=0.0, h=0.2):
        self.square_wall = s
        self.height_wall = h

    def volume(self):
        return self.square_wall * self.height_wall


# Плита над 1-м этажом
Plate_section_1_level_1 = Plate(435.143)
Plate_section_2_level_1 = Plate(440.511)
Plate_section_3_level_1 = Plate(349.535)
Plate_section_4_level_1 = Plate(394.691)
Plate_section_5_level_1 = Plate(430.390)
Plate_section_6_level_1 = Plate(458.453)
Plate_section_7_level_1 = Plate(441.466)
Plate_section_8_level_1 = Plate(438.542)
Plate_section_9_10_level_1 = Plate(689.259)
Plate_section_11_level_1 = Plate(345.857)
Plate_section_12_level_1 = Plate(387.898)
V_plate_section_1_12_level_1 = Plate_section_1_level_1.volume() + Plate_section_2_level_1.volume() + \
                               Plate_section_3_level_1.volume() + Plate_section_4_level_1.volume() + \
                               Plate_section_5_level_1.volume() + Plate_section_6_level_1.volume() + \
                               Plate_section_7_level_1.volume() + Plate_section_8_level_1.volume() + \
                               Plate_section_9_10_level_1.volume() + Plate_section_12_level_1.volume()
print("Объем перекрытий над 1-м этажом с учётом отверстий", V_plate_section_1_12_level_1, "м3\n")
