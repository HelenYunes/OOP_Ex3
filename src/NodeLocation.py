import math


class NodeLocation:

    def __init__(self, pos=None):

        # Constructor:
        try:
            self.__x = pos[0]
            self.__y = pos[1]
            self.__z = pos[2]
            self.pos = (self.__x, self.__y, self.__z)
        except TypeError:
            print("TypeError")

    def get_x(self):
        return self.__x

    def get_pos(self):
        return self.pos

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_z(self):
        return self.__z

    def set_z(self, z):
        self.__z = z

    def set_point(self, pos=None):
        if pos.__class__ is str:
            self.set_point_from_string(pos)
        elif pos is not None:
            self.__x = float(pos[0])
            self.__y = float(pos[1])
            self.__z = float(pos[2])

    def set_point_from_string(self, point):
        pos = point.split(',')
        self.__x = float(pos[0])
        self.__y = float(pos[1])
        self.__z = float(pos[2])

    def distance(self, point) -> float:
        dx = self.__x - point.get_x()
        dy = self.__y - point.get_y()
        dz = self.__z - point.get_z()
        t = (dx * dx + dy * dy + dz * dz)
        return math.sqrt(t)

    def get_point(self):
        if self.get_x is None and self.get_y is None and self.get_y is None:
            return None
        return self.get_x, self.get_y, self.get_z

    def __str__(self):
        return f" ({self.__x},{self.__y},{self.__z})"

    def __repr__(self):
        str(self)
