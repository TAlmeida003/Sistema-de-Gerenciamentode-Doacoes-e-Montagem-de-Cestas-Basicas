class Donation:
    """
    A classe Donation tem o objetivo de representar uma doação, tendo como características o nome do item e
    sua quantidade doada.
    """

    def __init__(self, donated_item: str, quantity_of_items: int) -> None:
        """
        Inicializa um objeto Donation recém-criado para representar os dados de uma doação.
        :param donated_item: String - O nome do item doado.
        :param quantity_of_items: Integer - A quantidade de itens doados.
        """
        self.__donated_item__: str = donated_item
        self.__quantity_of_items__: int = quantity_of_items

    def get_donated_item(self) -> str:
        """
        Retorna o nome do item doado.
        :return: String - O nome do item doado.
        """
        return self.__donated_item__

    def get_quantity_of_items(self) -> int:
        """
        Retorna a quantidade de itens doados.
        :return: Integer - A quantidade de itens doados.
        """
        return self.__quantity_of_items__

    def __repr__(self) -> str:
        """
        Retorna uma representação em string do objeto Donation.
        :return: String - Representação em string do objeto Donation.
        """
        return str(self.__dict__)
