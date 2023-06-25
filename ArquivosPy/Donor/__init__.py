from ArquivosPy.Donation import Donation


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
        self.__donation__: Donation = donation

    def add_donation(self, donated_item: str, quantity_of_items: int) -> None:
        """
        Adiciona uma doação ao doador.
        :param donated_item: String - O nome do item doado.
        :param quantity_of_items: Integer - A quantidade de itens doados.
        :return: None
        """

        self.__donation__ = Donation(donated_item, quantity_of_items)

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

    def get_donation(self) -> Donation:
        """
        Retorna o objeto Donation representando a doação do doador.
        :return: Donation - O objeto Donation representando a doação do doador.
        """
        return self.__donation__

    def __repr__(self) -> str:
        """
        Retorna uma representação em string do objeto Donor.
        :return: String - Representação em String do objeto Donor.
        """
        return str(self.__dict__)
