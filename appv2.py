vyidano = 0

while True:
    print("1 - Выдать книгу")
    print("2 - Показать сколько книг выдано")
    print("3 - Сбросить счётчик")
    print("4 - Вернуть книгу")
    print("0 - Выход")
    
    komanda = input("Введите команду: ")
    
    if komanda == "1":
        vyidano = vyidano + 2
        print("Книга выдана")
    elif komanda == "2":
        print("Выдано книг:", vyidano)
    elif komanda == "3":
        vyidano = 0
        print("Счётчик сброшен до 0")
    elif komanda == "4":
        if vyidano > 0:
            vyidano = vyidano - 4
            print("Книга возвращена")
        else:
            print("Нет выданных книг")
    elif komanda == "0":
        break
    else:
        print("Неизвестная команда")
