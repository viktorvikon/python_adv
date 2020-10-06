import re
from datetime import datetime

LOGIN_PAGE = """
=-==-==-==-=   Социальная сеть - "My Posts"  =-==-==-==-==-=
   [ 1 ] Зарегистрироваться    [ 2 ] Войти     [ 3 ] Выйти      
=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=
"""

USER_PAGE = """
=-==-==-==-=-==-==-==-=   Социальная сеть - "My Posts"  =-==-==-==-==-=-==-==-==-=
[ 1 ] Создать публикацию  [ 2 ] Просмотреть мои публикации  [ 3 ] Главная страница      
=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=-==-==-==-=-==-==-==-=
"""

ADMIN_PAGE = """
=-==-==-==-=-==-==-==-=   Социальная сеть - "My Posts"  =-==-==-==-==-=-==-==-==-=
[ 1 ] Пользователи системы [ 2 ] Просмотреть все публикации [ 3 ] Главная страница      
=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=-==-==-==-=-==-==-==-=
"""

DATE = "Дата публикации: "
SEPARATOR = f"-" * 50
FORMAT_DATE = "%m.%d.%Y, %H:%M:%S"
NO_PUBLICATION = "У Вас нет публикаций"
NO_USER_PUBLICATION = "Нет публикаций"
SELECT_NUM = "Выберите действие, указав соответствующую цифру: "
INCORRECT_DATA = "Некорректные данные. Пожалуйста, попробуйте еще раз! "
INCORRECT_CHOICE = "Некорректные данные. Пожалуйста, попробуйте еще раз! "
NOT_USERS = "Нет зарегистрированных пользователей"
INCORRECT_INPUT = "Неправильный логин или пароль"


class DataBase:

    _instance = None
    _users_list = {}
    _admin = {"admin": "admin_123"}
    _posts_list = {}

    def add_user(self, user):
        self.get_users[user.get_login] = {
                "password": user.get_password,
                "date_registration": datetime.now().strftime(FORMAT_DATE)
                }
        return user

    def all_users(self):
        users = ''
        if self._users_list:
            for user, info in self.get_users.items():
                for k, v in info.items():
                    if k == "date_registration":
                        users += f"{user} - {v}\n"
            return users
        else:
            return NOT_USERS

    def add_post(self, user, post):
        if user.get_login in self.get_posts:
            for k, v in self._posts_list.items():
                if k == user.get_login:
                    v.update({datetime.now().strftime(FORMAT_DATE): post})
        else:
            self._posts_list[user.get_login] = {datetime.now().strftime(FORMAT_DATE): post}

    def get_user_post(self, user):
        user_post = ''
        if user.get_login in self.get_posts:
            for key, value in self._posts_list.items():
                for k, v in value.items():
                    if key == user.get_login:
                        user_post += f"{DATE} - {k}\n{v}\n{SEPARATOR}\n"
            return user_post
        else:
            return NO_PUBLICATION

    def get_all_posts(self):
        if self._posts_list:
            users_posts = ''
            for key, value in self.get_posts.items():
                for k, v in value.items():
                    users_posts += f"{key}\n{k}\n{v}\n{SEPARATOR}\n"
            return users_posts
        else:
            return NO_USER_PUBLICATION

    @property
    def get_users(self):
        return self._users_list

    @property
    def get_admin(self):
        return self._admin

    @property
    def get_posts(self):
        return self._posts_list


class Registration(DataBase):

    def __init__(self, login, password):
        self._login = login
        self._password = password

    @property
    def get_login(self):
        return self._login

    @property
    def get_password(self):
        return self._password


class User(DataBase):

    def __init__(self, login, password):
        self._login = login
        self._password = password

    def is_admin(self):
        for login, password in self.get_admin.items():
            if (self._login, self._password) == (login, password):
                return True
            else:
                return False

    def is_user(self):
        for login, data in self.get_users.items():
            for password in data.values():
                if (self._login, self._password) == (login, password):
                    return True
                else:
                    return INCORRECT_INPUT

    @property
    def get_login(self):
        return self._login

    @property
    def get_password(self):
        return self._password


def main():
    data = DataBase()
    while True:
        print(LOGIN_PAGE)
        main_choice = input(SELECT_NUM)
        try:
            index = int(main_choice)
        except ValueError:
            print(INCORRECT_DATA)
        else:
            if index == 1:
                print(f"Регистрация\n{SEPARATOR}")
                login = input("Логин: ").strip()
                password = input("Пароль: ").strip()
                confirm_password = input("Подтверждение пароля: ").strip()
                if login in data.get_users or login in data.get_admin:
                    print("Пользователь с таким логином уже существует!")
                    continue
                if not (re.search(r'[a-zA-Z]', password) and re.search(r'\d', password)):
                    print("Пароль должен содержать латинские буквы и цифры!")
                    continue
                else:
                    if password != confirm_password:
                        print("Пароли не совпадают. Попробуй еще раз.")
                        continue
                    else:
                        new_user = Registration(login, password)
                        user = data.add_user(new_user)
                        if user:
                            print(SEPARATOR)
                            print("Поздравляем - Вы успешно зарегистрировались!")
                            print(SEPARATOR)
                            while True:
                                print(USER_PAGE)
                                user_choice = input(SELECT_NUM)
                                try:
                                    user_index = int(user_choice)
                                except ValueError:
                                    print(INCORRECT_DATA)
                                else:
                                    if user_index == 1:
                                        post = input("Напишите текст публикации: ")
                                        data.add_post(new_user, post)
                                        print("Опубликован!")
                                    elif user_index == 2:
                                        print(f"\nМои публикации:\n{SEPARATOR}")
                                        print(data.get_user_post(new_user))
                                    elif user_index == 3:
                                        break
                                    else:
                                        print(INCORRECT_CHOICE)

            elif index == 2:
                login = input("Логин: ").strip()
                password = input("Пароль: ").strip()
                user = User(login, password)
                if user.is_admin() is True:
                    print("\nВы вошли как администратор!")
                    while True:
                        print(ADMIN_PAGE)
                        admin_choice = input(SELECT_NUM)
                        try:
                            admin_index = int(admin_choice)
                        except ValueError:
                            print(INCORRECT_DATA)
                        else:
                            if admin_index == 1:
                                print(f"\nПользователи:\n{SEPARATOR}")
                                print(data.all_users())
                            elif admin_index == 2:
                                print(f"\nПубликации всех ользователей:\n{SEPARATOR}")
                                print(data.get_all_posts())
                            elif admin_index == 3:
                                break
                            else:
                                print(INCORRECT_CHOICE)
                if user.is_user() is True:
                    while True:
                        print(USER_PAGE)
                        user_choice = input(SELECT_NUM)
                        try:
                            user_index = int(user_choice)
                        except ValueError:
                            print(INCORRECT_DATA)
                        else:
                            if user_index == 1:
                                post = input("Напишите текст публикации: ")
                                data.add_post(user, post)
                                print("Опубликован!")
                            elif user_index == 2:
                                print(f"\nМои публикации:\n{SEPARATOR}")
                                print(data.get_user_post(user))
                            elif user_index == 3:
                                break
                            else:
                                print(INCORRECT_CHOICE)
            elif index == 3:
                print("\nВыход....")
                break
            else:
                print(INCORRECT_CHOICE)


if __name__ == "__main__":
    main()
