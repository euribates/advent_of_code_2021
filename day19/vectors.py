from dataclasses import dataclass


@dataclass(frozen=True)
class Vector2():
    x: int = 0
    y: int = 0
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    
    
@dataclass(frozen=True)
class Vector3():
    x: int = 0
    y: int = 0
    z: int = 0
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)