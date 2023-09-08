from ArquivosPy.Class.Donation import Donation


class Donor:
    """
    A classe Donor tem o objetivo de representar um doador, com características como nome, tipo e doação.
    """
    def __init__(self, name_donor: str, type_of_donor: str, donation: Donation = None) -> None:
        """
        Inicializa um objeto Donor recém-criado para representar os dados de um doador.
        :param name_donor: String - O nome do doador.
        :param type_of_donor: String - O tipo de doador.
        :param donation: Donation - Um objeto Donation representando a doação do doador.
        """
        self.__type_of_donor__: str = type_of_donor
        self.__name_donor__: str = name_donor
        self.__last_donation__: Donation = donation
        self.__donation_list__: list[Donation] = []

        if donation is not None:
            self.add_list_donation(donation)

    def add_donation(self, donated_item: str, quantity_of_items: int) -> None:
        """
        Adiciona uma doação ao doador.
        :param donated_item: String - O nome do item doado.
        :param quantity_of_items: Integer - A quantidade de itens doados.
        :return: None
        """
        donation: Donation = Donation(donated_item, quantity_of_items)
        self.__last_donation__ = donation
        self.add_list_donation(donation)

    def add_list_donation(self, donation: Donation) -> None:
        """
        Esta função adiciona uma doação à lista de doações. Se a doação já existe na lista, a quantidade de itens
        doados é atualizada. Caso contrário, a doação é adicionada como um novo item na lista.
        :param donation: Donation - Um objeto Donation representando a doação a ser adicionada.
        :return: None
        """
        for item in self.__donation_list__:
            if donation.get_donated_item() == item.get_donated_item():
                item.add_quantity(donation.get_quantity_of_items())
                return

        self.__donation_list__.append(donation)

    def get_name_donor(self) -> str:
        """
        Retorna o nome do doador.
        :return: String - O nome do doador.
        """
        return self.__name_donor__

    def get_type_of_donor(self) -> str:
        """
        Retorna o tipo de doador.
        :return: String - O tipo de doador.
        """
        return self.__type_of_donor__

    def get_last_donation(self) -> Donation:
        """
        Retorna o objeto Donation representando a doação do doador.
        :return: Donation - O objeto Donation representando a doação do doador.
        """
        return self.__last_donation__

    def get_list_donation(self) -> list[Donation]:
        return self.__donation_list__

    def __repr__(self) -> str:
        """
        Retorna uma representação em string do objeto Donor.
        :return: String - Representação em String do objeto Donor.
        """
        return str(self.__dict__)
