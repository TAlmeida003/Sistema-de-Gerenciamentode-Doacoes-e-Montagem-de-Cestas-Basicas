class Item:
    """
    A classe Item tem o objetivo de representar um item, com características como nome, peso na cesta básica e
    quantidade de itens armazenados.
    """
    def __init__(self, name: str, weight_in_the_basket: int, unit_of_measurement: str) -> None:
        """
        Inicializa um objeto Item recém-criado para representar os dados de um item.
        :param name: String - O nome do item.
        :param weight_in_the_basket: Integer - O peso do item na cesta básica.
        """
        self.__unit_of_measurement__ = unit_of_measurement
        self.__item_name__ = name
        self.__weight_in_the_basket__: int = weight_in_the_basket
        self.__amount_per_individual__: int = 0
        self.__amount_per_legal_entity__: int = 0
        self.__total_amount__: int = 0

    def store_the_item(self, quantity: int, type_person: str) -> None:
        """
        Armazena o item na estrutura de dados, atualizando as quantidades e a quantidade nos cestos.
        :param quantity: Integer - A quantidade do item a ser armazenada.
        :param type_person: String - O tipo de pessoa (PF ou PJ) que fez a doação.
        :return: None
        """
        self.__total_amount__ += quantity
        self.set_type_person(quantity, type_person)

    def set_type_person(self, quantity: int, type_person: str):
        """
        Define o tipo de pessoa (física ou jurídica) para atualizar as quantidades correspondentes.
        :param quantity: Integer - A quantidade do item doada.
        :param type_person: String - O tipo de pessoa (PF ou PJ) que fez a doação.
        :return: None
        """
        if type_person == "PF":
            self.__amount_per_individual__ += quantity
        else:
            self.__amount_per_legal_entity__ += quantity

    def calculate_the_amount_of_items_left_after(self, number_basket: int) -> int:
        """
        Calcula a quantidade de itens restantes após o número de cestos especificado.
        :param number_basket: Integer - O número de cestos.
        :return: Integer - A quantidade de itens restantes.
        """
        if self.__total_amount__ < number_basket:
            return 0
        return self.__total_amount__ - number_basket * self.__weight_in_the_basket__

    def get_quantity_in_baskets(self) -> int:
        """
        Retorna a quantidade de itens nos cestos.
        :return: Integer - A quantidade de itens nos cestos.
        """
        return self.__total_amount__ // self.__weight_in_the_basket__

    def get_amount_per_individual(self) -> int:
        """
        Retorna a quantidade do item doada por pessoa física (PF).
        :return: Integer - A quantidade do item doada por pessoa física (PF).
        """
        return self.__amount_per_individual__

    def get_amount_per_legal_entity(self) -> int:
        """
        Retorna a quantidade do item doada por pessoa jurídica (PJ).
        :return: Integer - A quantidade do item doada por pessoa jurídica (PJ).
        """
        return self.__amount_per_legal_entity__

    def get_total_amount(self) -> int:
        """
        Retorna a quantidade total do item doada.
        :return: Integer - A quantidade total do item doada.
        """
        return self.__total_amount__

    def get_unit_of_measurement(self) -> str:
        """
        Retorna a unidade de medida do item com base em seu nome.
        :return: String - A unidade de medida do item.
        """
        return self.__unit_of_measurement__

    def __repr__(self) -> str:
        """
        Retorna uma representação em string do objeto Item.
        :return: String - Representação em string do objeto Item.
        """
        return str(self.__dict__)
