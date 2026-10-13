bugs = [
    {"id": 1, "title": "Не работает вход", "severity": "high", "status": "open"},
    {"id": 2, "title": "Опечатка на главной", "severity": "low", "status": "closed"},
    {"id": 3, "title": "Не сохраняется расписание", "severity": "high", "status": "open"},
    {"id": 4, "title": "Неверный цвет кнопки", "severity": "medium", "status": "open"}
]

def find_bug(bugs, bug_id):
    for b in bugs:
        if b["id"] == bug_id:
            return b
    return None


def filter_bugs(bugs, status, severity):
    res = []
    for b in bugs:
        if b["status"] == status and b["severity"] == severity:
            res.append(b)
    return res


def add_bug(bugs, title, severity):
    if len(title) < 5:
        return None

    max_id = 0
    for b in bugs:
        if b["id"] > max_id:
            max_id = b["id"]

    new_bug = {
        "id": max_id + 1,
        "title": title,
        "severity": severity,
        "status": "open"
    }
    bugs.append(new_bug)
    return new_bug["id"]

def change_status(bugs, bug_id, new_status):
    b = find_bug(bugs, bug_id)
    if b is None:
        return "not_found"

    curr = b["status"]
    if curr == new_status:
        return "forbidden"

    if curr == "open" and new_status == "in_progress":
        b["status"] = new_status
        return "updated"
    elif curr == "in_progress" and new_status in ["open", "closed"]:
        b["status"] = new_status
        return "updated"
    elif curr == "closed" and new_status == "open":
        b["status"] = new_status
        return "updated"

    return "forbidden"

def main():
    while True:
        print("\n1. Показать все")
        print("2. Найти по ID")
        print("3. Фильтр")
        print("4. Добавить")
        print("5. Изменить статус")
        print("0. Выход")

        choice = input("Выбор: ")

        if choice == "1":
            for b in bugs:
                print(b)
        elif choice == "2":
            bid = int(input("Введите ID: "))
            print(find_bug(bugs, bid))
        elif choice == "3":
            st = input("Статус (open/in_progress/closed): ")
            sev = input("Серьезность (low/medium/high): ")
            for b in filter_bugs(bugs, st, sev):
                print(b)
        elif choice == "4":
            title = input("Название (от 5 символов): ")
            sev = input("Серьезность: ")
            print("Новый ID:", add_bug(bugs, title, sev))
        elif choice == "5":
            bid = int(input("ID ошибки: "))
            st = input("Новый статус: ")
            print("Результат:", change_status(bugs, bid, st))
        elif choice == "0":
            break


if __name__ == "__main__":
    main()
