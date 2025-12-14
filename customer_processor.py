import csv


class Customer:
    """Класс для представления покупателя"""

    def __init__(self, row):
        self.name = row.get('name', '').strip()
        self.device_type = row.get('device_type', '').strip()
        self.browser = row.get('browser', '').strip()
        self.sex = row.get('sex', '').strip()
        self.age = row.get('age', '').strip()
        self.bill = row.get('bill', '').strip()
        self.region = row.get('region', '').strip()

    def get_gender_form(self):
        """Возвращает форму слова в зависимости от пола"""
        if self.sex == 'female':
            return 'женского'
        elif self.sex == 'male':
            return 'мужского'
        return ''

    def get_age_form(self):
        """Определяет правильное склонение слова 'лет'"""
        if not self.age or not self.age.replace('.', '').isdigit():
            return ''

        try:
            age_num = float(self.age)
            if age_num.is_integer():
                age_int = int(age_num)
                last_digit = age_int % 10
                last_two_digits = age_int % 100

                if last_digit == 1 and last_two_digits != 11:
                    return 'год'
                elif 2 <= last_digit <= 4 and not (12 <= last_two_digits <= 14):
                    return 'года'
                else:
                    return 'лет'
            return 'лет'
        except:
            return 'лет'

    def get_verb_form(self):
        """Возвращает правильную форму глагола 'совершить'"""
        if self.sex == 'female':
            return 'совершила'
        elif self.sex == 'male':
            return 'совершил'
        return 'совершил(а)'

    def format_description(self):
        """Формирует текстовое описание покупателя"""
        gender_form = self.get_gender_form()
        age_form = self.get_age_form()
        verb_form = self.get_verb_form()

        # Форматируем возраст
        age_text = ''
        if self.age and self.age.replace('.', '').isdigit():
            try:
                age_num = float(self.age)
                if age_num.is_integer():
                    age_text = f"{int(age_num)} {age_form}"
                else:
                    age_text = f"{age_num} {age_form}"
            except:
                pass

        # Формируем описание
        description = f"Пользователь {self.name}"

        if gender_form and age_text:
            description += f" {gender_form} пола, {age_text} {verb_form} покупку на {self.bill} у.е."
        elif gender_form:
            description += f" {gender_form} пола {verb_form} покупку на {self.bill} у.е."
        elif age_text:
            description += f", {age_text} {verb_form} покупку на {self.bill} у.е."
        else:
            description += f" {verb_form} покупку на {self.bill} у.е."

        # Добавляем информацию об устройстве и регионе
        if self.region and self.region != '-':
            description += f" с {self.device_type} в {self.region}."
        elif self.device_type:
            description += f" с {self.device_type}."
        else:
            description += "."

        return description


def load_csv_data(file_path):
    """Загружает данные из CSV файла"""
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        print(f"Загружено {len(data)} записей из {file_path}")
        return data
    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден")
        print("Убедитесь, что файл web_clients_correct.csv находится в той же папке")
        return []
    except Exception as e:
        print(f"Ошибка при загрузке CSV: {e}")
        return []


def main():
    """Основная функция программы"""
    print("Программа для обработки данных о покупателях")
    print("=" * 50)

    input_file = "web_clients_correct.csv"
    output_file = "customers_descriptions.txt"

    # Загружаем данные
    csv_data = load_csv_data(input_file)

    if not csv_data:
        print("Не удалось загрузить данные. Программа завершена.")
        return

    # Создаем объекты покупателей и генерируем описания
    descriptions = []
    for row in csv_data:
        customer = Customer(row)
        descriptions.append(customer.format_description())

    # Сохраняем в файл
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for i, description in enumerate(descriptions, 1):
                file.write(f"{description}\n")
                if i < len(descriptions):
                    file.write("\n")
        print(f"\nСохранено {len(descriptions)} описаний в файл {output_file}")

        # Показываем несколько примеров
        print("\nПримеры сгенерированных описаний:")
        print("-" * 80)
        for i in range(min(3, len(descriptions))):
            print(f"{i + 1}. {descriptions[i]}")

        if len(descriptions) > 3:
            print(f"\n... и еще {len(descriptions) - 3} записей")

    except Exception as e:
        print(f"Ошибка при сохранении в файл: {e}")


if __name__ == "__main__":
    main()