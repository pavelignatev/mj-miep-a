import datetime
import random
import re

print("=" * 45)
print("   ЭЛЕКТРОННЫЙ ДЕКАНАТ МГИМО")
print("   МЖ-МИЭП · проект про дипломатию")
print("=" * 45)

# Исправление: имя, фамилия и факультет больше не подменяются случайными
name = input(" Введи твое имя: ")
surname = input("   Твоя фамилия: ")
departments = ["МО", "МЭО", "МП", "МЖ", "МИЭП", "ФУП", "ФФЭ", "ФЛМК", "МБ", "ИМТУР"]
print("Факультеты:", ", ".join(departments))
faculty = input(" Твой факультет: ")
birth_year = input("   Год рождения: ")
current_year = datetime.date.today().year
if not birth_year:
    birth_year = current_year - 18
else:
    birth_year = int(birth_year)

# Исправление: возраст = текущий год минус год рождения
age = current_year - birth_year

print()
print(f"Вас зовут: {name} {surname}")
print("Факультет:", faculty)
print("Возраст:", age)

# Исправление: сравниваем число с суммой, а не int(True/False)
a = random.randint(2, 8)
b = random.randint(2, 8)
captcha = input(f"\nПодтверди, что ты человек, введи сумму {a}+{b}: ")
if int(captcha) == a + b:
    print("Теперь понятно, за компьютером человек.")
    is_human = True
else:
    print("Неправильный ответ, должно быть", a + b)
    is_human = False

# Свои языки: итальянский и немецкий добавлены к базовым
greetings = {
    "en": "Hello {name} {surname}! The dean's office is yours again.",
    "fr": "Bonjour {name} {surname}! Le décanat vous écoute.",
    "es": "Hola {name} {surname}! Bienvenida a MGIMO.",
    "de": "Hallo {name} {surname}! Willkommen am MGIMO.",
    "it": "Ciao {name} {surname}! Benvenuta al MGIMO!",
}
language_names = {
    "en": "английский",
    "fr": "французский",
    "es": "испанский",
    "de": "немецкий",
    "it": "итальянский",
}

lang = input("\nКод языка (en, fr, es, de, it): ").strip().lower()
if lang not in greetings:
    print("Такого кода нет, переходим на английский.")
    lang = "en"

# Исправление: показываем выбранный язык, а не случайный
shown = lang
print(greetings[shown].format(name=name, surname=surname))
detect = input(f"Это был {language_names[lang]} язык? (д/н): ").strip().lower()
language_ok = detect.startswith("д")
print("Язык определён верно." if language_ok else f"Это был {language_names[shown]}.")

results = [language_ok]
program = input("\nКакой язык программирования ты изучаешь? ").strip().lower()
if program in {"python", "питон", "пайтон"}:
    print("Верно!")
    results.append(True)
else:
    print("На этом практикуме нужен Python.")
    results.append(False)

# Свой словарь: дипломатия, не перепутанные определения
terms_dict = {
    "суверенитет": "верховенство власти государства внутри страны и независимость вовне.",
    "ратификация": "утверждение международного договора высшим органом власти.",
    "агреман": "согласие государства принять конкретного человека послом.",
    "верительные грамоты": "документ, с которым посол официально представляется.",
    "демарш": "официальный протест или предупреждение по дипломатическим каналам.",
    "нота": "письменное обращение одного государства к другому.",
}


def ask_for_term(terms_dict, term=None, n_options=3):
    if term is None:
        term = random.choice(list(terms_dict))
    others = [item for item in terms_dict if item != term]
    options = [term] + random.sample(others, min(n_options, len(terms_dict)) - 1)
    random.shuffle(options)
    print("\n" + terms_dict[term].capitalize())
    print("Это определение для термина:")
    for i, option in enumerate(options, start=1):
        print(f"  {i}. {option}")
    while True:
        answer = input("Ваш ответ: ")
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            break
        print("Введите номер из списка.")
    if options[int(answer) - 1] == term:
        print("Верно!")
        return True
    print("Неверно. Правильный ответ:", term)
    return False


for _ in range(2):
    results.append(ask_for_term(terms_dict))


def hide_word(text):
    parts = re.split(r"(\W+)", text)
    words = [(i, part) for i, part in enumerate(parts) if part.isalpha() and len(part) > 4]
    index, word = random.choice(words)
    return "".join(parts[:index] + ["_" * len(word)] + parts[index + 1 :]), word


passage = """
Все люди равны перед законом и имеют право на равную защиту
от дискриминации, нарушающей настоящую Декларацию.
"""
masked, missing = hide_word(passage)
print("\n" + masked)
guess = input("Какое слово пропущено? ")
if guess.lower() == missing.lower():
    print("Ответ верный")
    results.append(True)
else:
    print("Неверно. Правильный ответ:", missing)
    results.append(False)

correct = sum(results)
print("\n" + "=" * 45)
print(f"{name} {surname}, факультет {faculty}")
print(f"Год рождения: {birth_year}, возраст: {age}")
print(f"Язык: {language_names[lang]}")
print(f"Верных ответов: {correct} из {len(results)}")

bonus = input("Номер комнаты Цифровой кафедры: ").strip()
if bonus in {"3053", "Одинцово", "одинцово"}:
    correct += 1
    print("+1 балл")
else:
    print("Не угадали. Сайт: dd.mgimo.ru")
print("Итого баллов:", correct)

# Дополнительное задание: своя игра в том же файле,
# потому что в форму можно прикрепить только один .py
print("\n" + "=" * 45)
print("Игра: угадай столицу")
capitals = {
    "Франция": "Париж",
    "Япония": "Токио",
    "Бразилия": "Бразилиа",
    "Египет": "Каир",
    "Кения": "Найроби",
}
game_score = 0
for country in random.sample(list(capitals), 3):
    answer = input(f"Столица страны {country}: ").strip()
    if answer.lower() == capitals[country].lower():
        print("Верно!")
        game_score += 1
    else:
        print("Нет, это", capitals[country])
print(f"Игра закончена: {game_score} из 3")
