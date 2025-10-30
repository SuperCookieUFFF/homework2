import matplotlib.pyplot as plt

# Данные из таблицы (по годам 2016–2025)
years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
temp = [2.6, 3.4, 2.5, 3.0, 2.8, 3.3, 2.7, 3.1, 2.9, 3.5]  # Средняя температура (°C)
water_level = [430, 540, 450, 505, 440, 525, 465, 495, 510, 485]  # Уровень воды (см)

# Создание графика
plt.figure(figsize=(10, 6))  # Размер графика
plt.scatter(temp, water_level, color='red', s=60, alpha=0.7)  # Точки: красные, полупрозрачные
plt.plot(temp, water_level, color='red', linestyle='--', alpha=0.5)  # Опционально: линия для тренда (не линейная, но для наглядности)

# Подписи и заголовок
plt.title('Зависимость уровня воды от средней температуры (река Тура, Тюмень, 2016–2025)')
plt.xlabel('Средняя температура (°C)')
plt.ylabel('Уровень воды (см)')
plt.grid(True, alpha=0.3)  # Сетка для удобства
plt.xticks([2.0, 2.5, 3.0, 3.5])  # Шкала по температуре (исправлено)

# Добавим подписи к точкам (годы) для ясности
for i, year in enumerate(years):
    plt.annotate(str(year), (temp[i], water_level[i]), xytext=(5, 5), textcoords='offset points', fontsize=8)

plt.tight_layout()
plt.show()
