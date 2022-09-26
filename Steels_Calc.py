# По объекту Мурино_Стелс
# Стена 1
square_1_1 = 2.64 * 56.62 + 2.59 * 4.02  # Площадь для утеплителя
square_2_1 = 2.29 * 4.02 + 2.34 * (56.62 + 2.75 + 1.9)  # Площадь для штукатурки
square_3_1 = 2.64 * 56.62 + 2.59 * 4.02  # Площадь для грунтовки
# print(square_1_1, square_2_1, square_3_1)
# Стена 2
square_1_2 = 334.1 + 27.34 + 11.55 - 1.995 - 0.22 - 0.313 * 17 - 0.49 + 1.21  # Площадь для утеплителя
square_2_2 = 334.1 + 27.34 + 11.55 - 1.995 - 0.22 - 0.313 * 17 - 0.49  # Площадь для штукатурки
square_3_2 = 334.1 + 27.34 + 11.55 - 1.995 - 0.22 - 0.313 * 17 - 0.49 + 10.31  # Площадь для грунтовки
# print(square_1_2, square_2_2, square_3_2)
# Стена 3
square_1_3 = 334.1 + 27.34 + 11.55 - 1.995 - 0.22 - 0.313 * 17 - 0.49 + 1.21  # Площадь для утеплителя
square_2_3 = 334.1 + 27.34 + 11.55 - 1.995 - 0.22 - 0.313 * 17 - 0.49  # Площадь для штукатурки
square_3_3 = 334.1 + 27.34 + 11.55 - 1.995 - 0.22 - 0.313 * 17 - 0.49 + 10.31  # Площадь для грунтовки
# print(square_1_3, square_2_3, square_3_3)
# Зеркальная
square_insulation = square_1_1 + square_1_2 + square_1_3
square_grunt = square_3_1 + square_3_2 + square_3_3


# Заново
# Утеплитель
square_insul = 16.19 * 4.02 + 56.62 * 14.44 + 4.2 * 2.75 * 2 - 1.995 - 17 * 0.313 - 0.493
print('Утеплитель м2 = ', square_insul)
# Потолок штукатурка
square_top = (4.2 + 1.3 + 0.36) * 2.34
print('Потолок штукатурка м2 = ', square_top)
# Штукатурка боковой поверхности марша
square_side_ladder = 1.137 + 0.916 + 0.767 + (0.842 + 0.767) * 16 + 0.646 + 0.677 + 0.2 * 0.26 * 17 + 0.15 * 0.26 + \
                     0.2 * 0.2 + 0.2 * 1.27 + 0.2 * 0.26 * 17 + 0.2 * 0.38
print('Штукатурка бок м2 = ', square_side_ladder)
# Штукатурка нижней поверхности марша
square_bottom_ladder = (0.965 * 2.25) + (0.96 * 1.25 + 1.23 * 1.05) * 17 + (2.415 * 1.25 + 2.135 * 1.05) + \
                       (2.135 * 1.05 + 2.465 * 1.25) + (1.565 * 2.3) * 17 + (0.835 + 2.33) + \
                       (4.45 * 1.05 + 3.995 * 1.05) + (3.324 * 1.05 + 3.66 * 1.05) * 17 + (2.755 * 1.05 + 2.997 * 1.05)
print('Штукатурка низ м2 = ', square_bottom_ladder)
# Штукатурка по стене на площадке (там где проёмы)
square_ladder_with_hole = (2.29 * 3.67 - 2.88 * 1.2) + (2.34 * 2.89 - 2.64 * 1.2) * 18
square_plaster = square_side_ladder + square_insul + square_bottom_ladder + square_ladder_with_hole
print('Штукатурка м2 = ', square_plaster)
