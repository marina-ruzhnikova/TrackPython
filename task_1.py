import doctest


class Box:
    def __init__(self, volume: float, completed: float):
        """Инициализация экземпляра коробки"""
        if not isinstance(volume, float):
            raise TypeError
        if volume <= 0:
            raise ValueError
        self.volume = volume

        if not isinstance(completed, float):
            raise TypeError
        if completed < 0:
            raise ValueError
        self.completed = completed

    def add_item_to_box (self, item_volume: float):
        """Добавление предметов в коробку"""
    def full_box (self):
        """Проверка, заполнена ли коробка"""

if __name__ == "__main__":
    doctest.testmod()