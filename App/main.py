import os
import sqlite3

db = None
sql = None

def Init():
    global db, sql

    db = sqlite3.connect('DataBase/data.db')
    sql = db.cursor()

    sql.execute("""CREATE TABLE IF NOT EXISTS Users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            login TEXT,
                            password TEXT
                    )""")
    

def isValidUser(login):
    return sql.execute(
        f"SELECT login FROM Users WHERE login='{login}' ")

def finishQuestion():
    choice = input(
        "Хотите продолжить и вернуться в главное меню ('да'|'нет')?: ")
    if choice == 'да':
        main()
    else:
        print("Вы успешно вышли из программы.")
        exit()

def addUser(login, password):
    cursor = isValidUser(login)

    row = cursor.fetchone()
    if row is None:
        sql.execute(
            f"INSERT INTO Users (login, password) VALUES ('{login}', '{password}')")
        print(f'Пользователь {login} успешно добавлен!!')
        db.commit()
    else:
        print(f'{login} уже добавлен!!')

    finishQuestion()


def main():
    os.system('cls||clear')

    choice = input("Программа База Данных пользователей... \
        \n1)Добавить пользователя        - 'д [логин] [пароль]'\
        \n2)Удалить пользователя         - 'у [логин]'\
        \n3)Обновить пароль пользователя - 'о [логин] [новый пароль]'\
        \n4)Выход из программы           - 'в' \
        \n\nВведите действие: ")
    
    words = choice.split()  # разбиение текста на список слов

    if choice.lower() == 'в':
        print('Вы успешно вышли с программы.')
        exit()
    elif words[0].lower() == 'д' and len(words) == 3:
        addUser(words[1], words[2])
    elif words[0].lower() == 'у' and len(words) == 2:
        pass
        # removeUser(words[1])
    elif words[0].lower() == 'о' and len(words) == 3:
        pass
        # updatePasswordUser(words[1], words[2])
    else:
        print('Вы успешно вышли с программы.')

def start():
    Init()
    main()

if __name__ == '__main__':
    start()


