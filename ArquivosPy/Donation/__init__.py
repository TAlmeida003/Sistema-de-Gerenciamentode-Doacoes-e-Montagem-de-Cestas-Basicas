class Donation:

    def __init__(self, donated_item: str = "", quantity_of_items: int = 0):

        self.__donated_item__: str = donated_item
        self.__quantity_of_items__: int = quantity_of_items

    def get_donated_item(self) -> str:

        return self.__donated_item__

    def get_quantity_of_items(self) -> int:

        return self.__quantity_of_items__

    def __repr__(self) -> str:

        return str(self.__dict__)
