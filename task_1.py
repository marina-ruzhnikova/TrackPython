class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Бумажная книга"""
    def __init__(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}."



class AudioBook:
    """Аудио книга"""
    def __init__(self, duration: float):
        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"
