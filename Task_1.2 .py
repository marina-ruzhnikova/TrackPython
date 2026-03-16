import doctest


class Box:
    def __init__(self, volume: float, material: str, current_load: float):
        """Инициализация экземпляра коробки
        Атрибуты:
            volume (float): Объем коробки.
            material (str): Материал коробки.
            current_load (float): Заполненность коробки."""
        if not isinstance(volume, float):
            raise TypeError
        if volume <= 0:
            raise ValueError
        self.volume = volume

        if not isinstance(material, str):
            raise TypeError
        if material.strip():
            raise ValueError
        self.material = material

        if not isinstance(current_load, float):
            raise TypeError
        self.current_load = current_load

    def add_item (self, item_volume: float):
        """Добавление предмета в коробку
        Атрибут item_volume (float): Объем предмета, который помещают в коробку.
        return: None"""
        if not isinstance(item_volume, float) or item_volume <= 0:
            raise ValueError("Объем предмета должен быть положительным числом.")
        if self.current_load + item_volume > self.volume:
            raise ValueError("Превышена вместимость коробки.")


    def full_box (self):
        """Проверка, заполнена ли коробка"""
        return self.volume - self.current_load

class Account:
    def __init__(self, name: str, personal_id: int, subscription: bool):
        """Инициализация аккауна в соцсети
        Атрибуты:
            name (str): Имя пользователя.
            personal_id (int): Номер пользователя в базе данных.
            subscription (bool): Имеется ли платная подписка."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError ("Имя пользователя не может быть пустым")
        if not isinstance(personal_id, int) or personal_id <= 0:
            raise ValueError("ID пользователя должен быть положительным целым числом")
        if not isinstance(subscription, bool):
            raise ValueError ("Статус пользователя должен быть булевым значением")
        self.name = name
        self.personal_id = personal_id
        self.subscription = subscription

    def information (self, age: int, gender: str):
        """Добавление личной информации о пользователе
        Атрибуты:
            age (int): Возраст.
            gender (str): Пол.
        return: None"""
        if not isinstance(age, int) or age <= 0:
            raise ValueError ("Возраст должен быть положительным целым числом")
        if not isinstance(gender, str):
            raise TypeError

    def share(self) -> str:
        """Получение ссылки на аккаунт
        :return: Строка с ссылкой"""

class Plant:
    def __init__(self, name: str, height: float, water_days: int):
        """Инициализация растения
        Атрибуты:
            name (str): Название растения.
            height (float): Высота растения.
            water_days (int): Частота полива в днях."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название растения должно быть непустой строкой")
        if not isinstance(height, float) or height <= 0:
            raise ValueError("Высота растения должна быть положительным числом")
        if not isinstance(water_days, int) or water_days <= 0:
            raise ValueError("Частота полива растения должна быть целым положительным числом")
        self.name = name
        self.height = height
        self.water_days = water_days

    def grow(self, amount: float) -> None:
        """Рост растения.
        Атрибут amount: Прирост высоты.
        return: None
        raises ValueError: Если прирост отрицательный."""
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Прирост высоты должен быть положительным.")

    def water(self):
        """Полив растения.
        return: None"""

if __name__ == "__main__":
    doctest.testmod()