from ArquivosPy.Donation import Donation


class Donor:

    def __init__(self, name_donor: str = "", type_of_donor: str = "", donation: Donation = None) -> None:

        self.__type_of_donor__: str = type_of_donor
        self.__name_donor__: str = name_donor
        self.__donation__: Donation = donation

    def add_donation(self, donated_item: str = "", quantity_of_items: int = 0) -> None:

        self.__donation__ = Donation(donated_item, quantity_of_items)

    def get_name_donor(self) -> str:

        return self.__name_donor__

    def get_type_of_donor(self) -> str:

        return self.__type_of_donor__

    def get_donation(self) -> Donation:

        return self.__donation__

    def __repr__(self) -> str:

        return str(self.__dict__)
