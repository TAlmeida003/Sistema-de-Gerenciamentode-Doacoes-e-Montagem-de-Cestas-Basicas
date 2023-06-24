class Donation:

    def __init__(self, donated_item: int = None, quantity_of_items: int = None):

        self.__donated_item__: str = str()
        self.set_donation_item(donated_item)
        self.__quantity_of_items__: int = quantity_of_items

    def set_donation_item(self, donated_item: int = None):

        list_of_items: list[str] = ["AÇÚCAR", "ARROZ", "CAFÉ", "EXTRATO DE TOMATE", "MACARRÃO", "BOLACHA",
                                    "ÓLEO", "FARINHA DE TRIGO", "FEIJÃO", "SAL", "OUTROS"]

        self.__donated_item__: str = list_of_items[donated_item]

    def get_donated_item(self) -> str:

        return self.__donated_item__

    def get_quantity_of_items(self) -> int:

        return self.__quantity_of_items__

    def __repr__(self) -> str:

        return str(self.__dict__)
