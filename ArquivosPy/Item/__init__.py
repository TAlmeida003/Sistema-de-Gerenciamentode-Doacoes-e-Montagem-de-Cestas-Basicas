class Item:

    def __init__(self, name: str = "", weight_in_the_basket: int = 0) -> None:

        self.__item_name__ = name
        self.__weight_in_the_basket__: int = weight_in_the_basket
        self.__amount_per_individual__: int = 0
        self.__amount_per_legal_entity__: int = 0
        self.__total_amount__: int = 0
        self.__quantity_in_baskets__: int = 0

    def store_the_item(self, quantity: int = 0, type_person: int = 0) -> None:

        self.__total_amount__ += quantity
        self.__quantity_in_baskets__ += self.__total_amount__ // self.__weight_in_the_basket__

        self.set_type_person(quantity, type_person)

    def set_type_person(self, quantity: int = 0, type_person: int = 0):

        if type_person == 1:
            self.__amount_per_individual__ += quantity
        else:
            self.__amount_per_legal_entity__ += quantity

    def calculate_the_amount_of_items_left_after(self, number_basket: int = 0) -> int:

        return self.__total_amount__ - number_basket * self.__weight_in_the_basket__

    def get_quantity_in_baskets(self) -> int:

        return self.__quantity_in_baskets__

    def get_amount_per_individual(self) -> int:

        return self.__amount_per_individual__

    def get_amount_per_legal_entity(self) -> int:

        return self.__amount_per_legal_entity__

    def get_total_amount(self) -> int:

        return self.__total_amount__

    def __repr__(self) -> str:

        return str(self.__dict__)