list_users = []
class User:
    def __init__(self, id, name, access_level):
        self._id = id
        self._name = name
        self._access_level = access_level

    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_access_level(self):
        return self._access_level
    def info(self):
        return self._id, self._name, self._access_level
    def display_info(self):
        print(f"ID: {self._id}, Имя: {self._name}, Уровень: {self._access_level}")

class Admin(User):
    def __init__(self, id, name, access_level):
        super().__init__(id, name, access_level)
        self.special_access = "admin"

    def add_user(self, user_id, name, access_level):
        new_user = User(user_id, name, access_level)
        list_users.append(new_user)
        print(f"Пользователь {name} добавлен")
    def remove_user(self, user_id):
        for user in list_users:
            if user.get_id() == user_id:
                list_users.remove(user)
                print(f"Пользователь с ID {user_id} удален")
                return
        print(f"Пользователь с ID {user_id} не найден")


user1 = User(156498, "Маша", "user")
admin1 = Admin(12324, "Павел", "admin")

admin1.add_user(1001, "Иван", "user")
admin1.add_user(1002, "Петр", "user")
admin1.add_user(1003, "Елена", "user")

print("\nВсе пользователи:")
for user in list_users:
    user.display_info()

admin1.remove_user(1003)

print("\nПользователи после удаления:")
for user in list_users:
    user.display_info()
