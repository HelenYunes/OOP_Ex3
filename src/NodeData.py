from src.NodeLocation import NodeLocation


class NodeData(object):

    # Constructor:

    def __init__(self, key: int, tag=0, pos: tuple = None, w=1):
        self.__key: int = key
        self.__tag = tag
        self.__info = "no"
        self.__weight = w
        self.__parent = None
        self.__counter = None
        self.__connected_components = None
        if pos is not None:
            self.__location = NodeLocation(pos).get_pos()
        else:
            self.__location = None

    def get_location(self) -> [tuple]:

        return self.__location

    def set_location(self, x, y, z):
        self.__location = (x, y, z)

    def get_key(self) -> int:
        return self.__key

    def set_key(self, key: int):
        self.__key = key

    def set_tag(self, tag: int):
        self.__tag = tag

    def get_tag(self) -> float:
        return self.__tag

    def get_parent(self) -> int:
        return self.__parent

    def set_parent(self, parent):
        self.__parent = parent

    def get_info(self) -> str:
        return self.__info

    def set_info(self, info: str):
        self.__info = info

    def get_counter(self) -> int:
        return self.__counter

    def set_counter(self, index: int):
        self.__counter = index

    def get_connected_components(self) -> int:
        return self.__connected_components

    def set_connected_components(self, connected_components: int):
        self.__connected_components = connected_components

    def __repr__(self):
        if self.__location is None:
            return '{ID:' + self.__key.__str__() + '}'
        else:
            return '{ID:' + self.__key.__str__() + ', Location:' + self.__location.__str__() + '}'

    def __lt__(self, other):
        return self.__tag < other.__tag

    def __gt__(self, other):
        return self.__tag > other.__tag
