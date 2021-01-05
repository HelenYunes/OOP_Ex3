class NodeData:

    # Constructor:

    def __init__(self, key: int, distance: float, location: () = None):
        self.__key: int = key
        self.__location: NodeLocation = NodeLocation()
        self.__location.set_point(location)
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
