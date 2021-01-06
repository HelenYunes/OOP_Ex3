from src.NodeLocation import NodeLocation


class NodeData:

    # Constructor:

    def __init__(self, key: int, distance: float, tag=0, info="", pos=None, w=1):
        self.__key: int = key
        self.__tag = tag
        self.__info = info
        self.__weight = w
        if pos is not None:
            self.__location = NodeLocation()(pos)
        else:
            self.__location = None
        self.__distance: float = distance

    def get_location(self) -> NodeLocation:
        return self.__location

    def get_pos(self) -> tuple:
        return self.__location.get_point()

    def set_pos(self, point):
        self.__location.set_point(point)

    def get_key(self) -> int:
        return self.__key

    def set_key(self, key: int):
        self.__key = key

    def get_distance(self) -> float:
        return self.__distance

    def set_distance(self, distance: float):
        self.__distance = distance

    def __repr__(self):
        if self.__location is None:
            return '{ID:' + self.__key.__str__() + '}'
        else:
            return '{ID:' + self.__key.__str__() + ', Location:' + self.__location.__str__() + '}'


