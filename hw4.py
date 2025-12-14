import csv


def process_visits():
    # Открываем файл с покупками для создания словаря категорий
    with open('purchase_log.txt', 'r', encoding='utf-8') as purchase_file:
        # Создаем словарь: user_id -> category
        purchase_dict = {}
        for line in purchase_file:
            # Пропускаем первую строку с заголовками если есть
            if line.strip().startswith('user_id'):
                continue
            data = line.strip().split(',')
            if len(data) >= 2:
                user_id = data[0].strip()
                category = data[1].strip()
                purchase_dict[user_id] = category

    # Обрабатываем основной файл построчно
    with open('visit_log.csv', 'r', encoding='utf-8') as visit_file, \
            open('funnel.csv', 'w', encoding='utf-8', newline='') as funnel_file:

        reader = csv.reader(visit_file)
        writer = csv.writer(funnel_file)

        # Записываем заголовок
        writer.writerow(['user_id', 'source', 'category'])

        # Обрабатываем каждую строку
        for row in reader:
            # Пропускаем заголовок если есть
            if row[0] == 'user_id':
                continue

            user_id = row[0]
            source = row[1]

            # Если пользователь совершал покупку, добавляем категорию
            if user_id in purchase_dict:
                category = purchase_dict[user_id]
                writer.writerow([user_id, source, category])


# Запускаем обработку
if __name__ == "__main__":
    process_visits()