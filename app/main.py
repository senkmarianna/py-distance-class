from __future__ import annotations
from ctypes import Union


class Distance:
    def __init__(self: Distance, km: Union[float, int]) -> None:
        self.km = km

    def __str__(self: Distance) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self: Union[int, float, Distance]) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float, Distance]) -> Distance:
        if type(other) == float:
            return Distance(self.km + other)
        elif type(other) == int:
            return Distance(self.km + other)
        else:
            return Distance(self.km + other.km)

    def __iadd__(self, other: Union[int, float, Distance]) -> Distance:
        if type(other) == float:
            self.km += other
        elif type(other) == int:
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other: Union[int, float, Distance]) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float, Distance]) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[int, float, Distance]) -> bool:
        return self.km < other

    def __gt__(self, other: Union[int, float, Distance]) -> bool:
        return self.km > other

    def __eq__(self, other: Union[int, float, Distance]) -> bool:
        return self.km == other

    def __le__(self, other: Union[int, float, Distance]) -> bool:
        return self.km <= other

    def __ge__(self, other: Union[int, float, Distance]) -> bool:
        return self.km >= other
