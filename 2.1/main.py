from abc import ABC, abstractmethod
import doctest

class GPU(ABC):
    """
    Абстрактный класс, описывающий видеокарту.
    """
    def __init__(self, model: str, memory: int):
        """
        :param model: Модель видеокарты (например, "RTX 3060").
        :param memory: Объём видеопамяти в ГБ (должен быть больше 0).
        """
        if memory <= 0:
            raise ValueError("Объём памяти должен быть больше 0.")
        self.model = model
        self.memory = memory

    @abstractmethod
    def render(self) -> None:
        """
        Метод для выполнения рендеринга.

        Пример:
        >>> gpu.render()
        """
        ...

    @abstractmethod
    def overclock(self, mhz: int) -> None:
        """
        Разгоняет видеокарту на указанное количество МГц.

        :param mhz: Количество МГц для разгона (должно быть больше 0).
        :raises ValueError: Если значение <= 0.

        Пример:
        >>> gpu.overclock(100)
        """
        ...


class RTX3060(GPU):
    """
    Класс, описывающий видеокарту RTX 3060.
    """
    def render(self) -> None:
        """
        Выполняет рендеринг с использованием RTX 3060.

        Пример:
        >>> gpu = RTX3060("RTX 3060", 12)
        >>> gpu.render()
        """
        ...

    def overclock(self, mhz: int) -> None:
        """
        Разгоняет RTX 3060 на указанное количество МГц.

        :param mhz: Количество МГц для разгона.

        Пример:
        >>> gpu = RTX3060("RTX 3060", 12)
        >>> gpu.overclock(100)
        """
        ...


class RTX4060(GPU):
    """
    Класс, описывающий видеокарту RTX 4060.
    """
    def render(self) -> None:
        """
        Выполняет рендеринг с использованием RTX 4060.

        Пример:
        >>> gpu = RTX4060("RTX 4060", 16)
        >>> gpu.render()
        """
        ...

    def overclock(self, mhz: int) -> None:
        """
        Разгоняет RTX 4060 на указанное количество МГц.

        :param mhz: Количество МГц для разгона.

        Пример:
        >>> gpu = RTX4060("RTX 4060", 16)
        >>> gpu.overclock(150)
        """
        ...


class RTX2080(GPU):
    """
    Класс, описывающий видеокарту RTX 2080.
    """
    def render(self) -> None:
        """
        Выполняет рендеринг с использованием RTX 2080.

        Пример:
        >>> gpu = RTX2080("RTX 2080", 8)
        >>> gpu.render()
        """
        ...

    def overclock(self, mhz: int) -> None:
        """
        Разгоняет RTX 2080 на указанное количество МГц.

        :param mhz: Количество МГц для разгона.

        Пример:
        >>> gpu = RTX2080("RTX 2080", 8)
        >>> gpu.overclock(200)
        """
        ...

if __name__ == "__main__":
    # Проверка работоспособности экземпляров классов с помощью doctest
    doctest.testmod()
