"""Электронный деканат. МЖ-МИЭП, работа 1.
Анкета студента, проверка языка и короткий тест по дипломатии.
"""

import datetime
import random


FACULTIES = ("МО", "МЭО", "МП", "МЖ", "МИЭП", "ФУП", "ФФЭ", "ФЛМК", "МБ", "ИМТУР")

HELLO = {
    "en": "Good afternoon, {who}. The dean's office is back online.",
    "de": "Guten Tag, {who}. Das Dekanat funktioniert wieder.",
    "fr": "Bonjour, {who}. Le décanat vous écoute.",
    "ko": "안녕하세요, {who}. 학사 시스템이 복구되었습니다.",
    "pt": "Ola, {who}. A secretaria academica voltou a funcionar.",
    "tr": "Merhaba, {who}. Dekanlik yeniden calisiyor.",
}

LANG_TITLE = {
    "en": "английский",
    "de": "немецкий",
    "fr": "французский",
    "ko": "корейский",
    "pt": "португальский",
    "tr": "турецкий",
}

DIPLOMACY = {
    "ратификация": "утверждение международного договора высшим органом власти",
    "верительные грамоты": "документ, которым посол представляется главе государства",
    "демарш": "официальное дипломатическое выступление с протестом или предупреждением",
    "экстерриториальность": "особый статус помещений посольства на чужой территории",
    "агреман": "согласие принять конкретное лицо в качестве посла",
    "нота": "письменное дипломатическое обращение одного государства к другому",
}


def read_year():
    raw = input("Год рождения (например 2005): ").strip()
    now = datetime.date.today().year
    if not raw:
        return now - 19
    return int(raw)


def check_human():
    left = random.randint(3, 9)
    right = random.randint(3, 9)
    typed = input(f"Антибот: {left} x {right} = ").strip()
    expected = left * right
    if typed == str(expected):
        print("Проверка пройдена.")
        return True
    print(f"Мимо. Нужно было {expected}.")
    return False


def choose_language(who):
    print("Коды языков:", ", ".join(HELLO))
    code = input("Ваш язык (две буквы): ").strip().lower()
    if code not in HELLO:
        print("Код не найден, оставляю английский.")
        code = "en"
    print(HELLO[code].format(who=who))
    guess = input(f"Это {LANG_TITLE[code]}? да/нет: ").strip().lower()
    return code, guess.startswith("д")


def python_question():
    answer = input("На каком языке написана эта программа? ").strip().lower()
    ok = answer in {"python", "питон", "пайтон"}
    print("Да, это Python." if ok else "Сейчас мы чиним программу на Python.")
    return ok


def diplomacy_round():
    term = random.choice(list(DIPLOMACY))
    decoys = random.sample([item for item in DIPLOMACY if item != term], 2)
    choices = [term, *decoys]
    random.shuffle(choices)
    print("\nОпределение:", DIPLOMACY[term])
    for number, option in enumerate(choices, start=1):
        print(f"{number}) {option}")
    picked = input("Номер термина: ").strip()
    if picked.isdigit() and 1 <= int(picked) <= len(choices) and choices[int(picked) - 1] == term:
        print("Точно.")
        return True
    print("Правильный термин:", term)
    return False


def missing_word():
    sentence = (
        "Посол вручает верительные грамоты и после этого может официально "
        "представлять своё государство в стране пребывания."
    )
    words = [word for word in sentence.replace(".", "").split() if len(word) > 5]
    hidden = random.choice(words)
    shown = sentence.replace(hidden, "_" * len(hidden), 1)
    print("\n" + shown)
    typed = input("Вставьте пропущенное слово: ").strip()
    if typed.lower() == hidden.lower():
        print("Слово угадано.")
        return True
    print("Было слово:", hidden)
    return False


def room_bonus():
    room = input("\nБонус. Кабинет Цифровой кафедры: ").strip()
    if room in {"3053", "одинцово", "Одинцово"}:
        print("Бонусный балл есть.")
        return 1
    print("Кабинет не тот. Сайт кафедры: dd.mgimo.ru")
    return 0


def main():
    print("МГИМО / электронный деканат")
    print("Карточка студента МЖ-МИЭП\n")
    first = input("Имя: ").strip()
    last = input("Фамилия: ").strip()
    print("Факультеты:", " · ".join(FACULTIES))
    faculty = input("Ваш факультет: ").strip()
    year = read_year()
    age = datetime.date.today().year - year

    print(f"\nКарточка: {last} {first}")
    print(f"Факультет: {faculty}")
    print(f"Возраст: {age}")

    points = []
    points.append(check_human())
    code, language_ok = choose_language(f"{first} {last}")
    points.append(language_ok)
    points.append(python_question())
    points.append(diplomacy_round())
    points.append(diplomacy_round())
    points.append(missing_word())

    score = sum(points) + room_bonus()
    print("\n----- ведомость -----")
    print(f"{last} {first}, {faculty}, {age} лет")
    print(f"Язык анкеты: {LANG_TITLE[code]}")
    print(f"Баллы: {score} из {len(points) + 1}")


if __name__ == "__main__":
    main()
