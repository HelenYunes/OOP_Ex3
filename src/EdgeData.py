
class EdgeData:
    def __init__(self, src: int, dst: int, w: float):
        self.__source = src
        self.__destination = dst
        self.__weight = w

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def get_weight(self):
        return self.__weight

    def __repr__(self):
        return "{Source:" + self.__source.__str__() + ", Destination:" + self.__destination.__str__() + ", Weight:" \
               + self.__weight.__str__() + "}"
