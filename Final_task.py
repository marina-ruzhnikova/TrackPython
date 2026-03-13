class Students:
    """Базовый класс, представляющий любого студента университета"""
    def __init__(self, name: str, surname: str, student_id: int, base_grant: float) -> None:
        """Конструктор базового класса Students
        Атрибуты:
            name (str): Имя студента.
            surname (str): Фамилия студента.
            student_id (int): Уникальный номер студента в базе.
            base_grade (float): Базовая месячная стипендия"""
        self.name = name
        self.surname = surname
        self._student_id = student_id
        self._base_grade = base_grant

    def __str__(self) -> str:
        """Возвращает строковое представление объекта"""
        return f"Студент: {self.surname} {self.name}"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление объекта (для отладки)."""
        return f"Employee(name='{self.name}', surname='{self.surname}', id={self._student_id})"
    def calculate_salary(self) -> float:
        """Рассчитывает стипендию студента за месяц. В базовом варианте возвращает только базовую сумму"""
        return self._base_grade

class Activist(Students):
    """Дочерний класс, представляющий студента-активиста"""
    def __init__(self, name: str, surname: str, student_id: int, base_grade: float, activity: str, event_bonus: float):
        """Конструктор класса Activist
        Атрибуты:
            name (str): Имя студента.
            surname (str): Фамилия студента.
            student_id (int): Уникальный номер студента в базе.
            base_grade (float): Базовая месячная стипендия.
            activity (str): Роль студента как участника мероприятия.
            event_bonus (float): Надбавка за участие в мероприятиях."""
        super().__init__(name, surname, student_id, base_grade)
        self.activity = activity
        self._event_bonus = event_bonus

    def __str__(self):
        """Перезагружает метод __str__ из базового класса"""
        base_str = super().__str__()
        return f"{base_str} | Роль: {self.activity}"

    def __repr__(self):
        """Перезагружаем метод __repr__ из базового класса"""
        return (f"Activist(name='{self.name}', surname='{self.surname}', id={self._student_id}), "
                f"activity='{self.activity}'")
    def calculate_salary(self):
        """Перезагружаем метод __repr__ из базового класса
        В отличие от обычного студента, активист получает бонус за участие в мероприятиях, который необходимо учитывать
        """
        grade = super().calculate_salary()
        return grade + self._event_bonus
    def student_skills(self):
        """Метод, специфичный только для класса Activist"""
        return f"Навыки студента: {self.activity}"

if __name__ == "__main__":
    student_1 = Students(name="Владимир", surname="Кузнецов", student_id=743, base_grant=3000.0)
    student_2 = Activist(name="Никита", surname="Пономарев", student_id=935, base_grade=3000.0, activity="фотограф",
                         event_bonus=2500.0)

    print(student_1)
    print(repr(student_1))
    print(f"Стипендия: {student_1.calculate_salary()}")

    print(student_2)
    print(repr(student_2))
    print(f"Стипендия: {student_2.calculate_salary()}")
    print(student_2.student_skills())