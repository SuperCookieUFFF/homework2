import matplotlib.pyplot as plt

years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
precip = [440, 530, 460, 500, 450, 510, 470, 490, 520, 480]
water_level = [430, 540, 450, 505, 440, 525, 465, 495, 510, 485]

plt.scatter(precip, water_level, color='blue')
plt.title('Зависимость уровня воды от осадков (Тура, Тюмень)')
plt.xlabel('Осадки (мм)')
plt.ylabel('Уровень воды (см)')
plt.grid(True)
plt.show()