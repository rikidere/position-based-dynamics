import taichi as ti
from abc import ABCMeta, abstractmethod



@ti.data_oriented
class Object(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass
    """
    @ABSTRACT METHOD
    draws the object
        scene: ti.scene
            the scene object
    """
    @abstractmethod
    def draw(self, scene):
        pass

    """
    @ABSTRACT METHOD
    check if p collides with the object
        p : ti.Vector([x, y, z])
            the point which collides
    """
    @abstractmethod
    def solve_collision_constraint(self, p, x):
        pass
