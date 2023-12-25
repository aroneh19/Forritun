import math
TOLERANCE = 0.000_000_1

class Vector:
    def __init__(self, x=0, y=0, z=0) -> None:
        self._vector = [x, y, z]

    def __str__(self) -> str:
        return f"[[ {self._vector[0]} {self._vector[1]} {self._vector[2]} ]]" 

    def __abs__(self) -> float:
        return math.sqrt(self._vector[0]**2 + self._vector[1]**2 + self._vector[2]**2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self._vector[0] + other._vector[0], self._vector[1] + other._vector[1], self._vector[2] + other._vector[2])

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self._vector[0] - other._vector[0], self._vector[1] - other._vector[1], self._vector[2] - other._vector[2])

    def __eq__(self, other: "Vector") -> bool:
        return abs(self - other) <= TOLERANCE

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self._vector[0] * scalar, self._vector[1] * scalar, self._vector[2] * scalar)

    def __rmul__(self, scalar: float) -> "Vector":
        return self * scalar

    def __repr__(self) -> str:
        return f'Vector({self._vector[0]}, {self._vector[1]}, {self._vector[2]})'

    def __gt__(self, other: "Vector") -> bool:
        return abs(self) > abs(other)

    def __ge__(self, other: "Vector") -> bool:
        return abs(self) >= abs(other)

    def __lt__(self, other: "Vector") -> bool:
        return abs(self) < abs(other)

    def __le__(self, other: "Vector") -> bool:
        return abs(self) <= abs(other)

    def dot(self, other: "Vector") -> float:
        return sum(i * j for i, j in zip(self._vector, other._vector))

    def cross(self, other: "Vector") -> "Vector":
        x = self._vector[1] * other._vector[2] - self._vector[2] * other._vector[1]
        y = self._vector[2] * other._vector[0] - self._vector[0] * other._vector[2]
        z = self._vector[0] * other._vector[1] - self._vector[1] * other._vector[0]
        return Vector(x, y, z)
    
