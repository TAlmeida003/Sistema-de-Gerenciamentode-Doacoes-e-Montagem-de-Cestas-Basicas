from ArquivosPy import ScreenPrints


def check_name(name_donor: str) -> None:
    """
    Função para verificar se o nome do doador é válido.
    :param name_donor: String - Nome do doador
    :raises RuntimeError: Se o nome do doador estiver vazio, exceder 20 caracteres ou conter números
    :return: None
    """
    NUMBER_OF_CHAR = len(name_donor)
    IS_BLANK: int = 0
    CHAR_LIMIT: int = 20

    if NUMBER_OF_CHAR == IS_BLANK:
        raise RuntimeError("O CAMPA NOME DO DOADOR ESTÁ VAZIO")
    elif NUMBER_OF_CHAR > CHAR_LIMIT:
        raise RuntimeError("O NOME INSERIDO NO CAMPO NOME ULTRAPASSOU OS 20 CARACTERES")
    elif not name_donor.isalpha():
        raise RuntimeError("POR FAVOR NÃO INSIRA NÚMEROS NO CAMPO NOME DO DOADOR")


def is_valid_name(name_donor: str) -> bool:
    """
    Função para verificar se o nome do doador é válido.
    :param name_donor: String - Nome do doador
    :return: Boolean - True se o nome é válido, False caso contrário
    """
    try:
        check_name(name_donor)
        return True
    except RuntimeError as error:
        ScreenPrints.report_error(error.__str__())
        return False


def get_name_donor() -> str:
    """
    Função para obter o nome do doador.
    :return: String - Nome do doador
    """
    name_donor: str = ScreenPrints.get_display_name_donor()

    while not is_valid_name(name_donor):
        name_donor = ScreenPrints.get_display_name_donor()

    return name_donor


def check_type_of_donor(type_of_donor: str) -> None:
    """
    Função para verificar se o tipo de doador é válido.
    :param type_of_donor: String - Tipo de doador
    :raises RuntimeError: Se o tipo de doador for uma opção inválida
    """
    set_option: set[str] = {"1", "2"}

    if type_of_donor not in set_option:
        raise RuntimeError("OPÇÃO INVALIDA")


def is_valid_type_of_donor(type_of_donor: str) -> bool:
    """
    Função para verificar se o tipo de doador é válido.
    :param type_of_donor: String - Tipo de doador
    :return: Boolean - True se o tipo de doador é válido, False caso contrário
    """
    try:
        check_type_of_donor(type_of_donor)
        return True
    except RuntimeError as error:
        ScreenPrints.report_error(error.__str__())
        return False


def get_type_of_donor() -> str:
    """
    Função para obter o tipo de doador.
    :return: String - Tipo de doador
    """
    type_of_donor: str = ScreenPrints.get_display_type_of_donor()

    while not is_valid_type_of_donor(type_of_donor):
        type_of_donor = ScreenPrints.get_display_type_of_donor()

    list_type_person: list[str] = ["PF", "PJ"]

    return list_type_person[int(type_of_donor) - 1]


def check_donated_item(donated_item: str) -> None:
    """
    Função para verificar se o item doado é válido.
    :param donated_item: String - Item doado
    :raises RuntimeError: Se o item doado for uma opção inválida
    """
    set_option_items_donation: set[str] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}

    if donated_item not in set_option_items_donation:
        raise RuntimeError("OPÇÃO INFORMADA É INVALIDA")


def is_valid_donated_item(donated_item: str) -> bool:
    """
    Função para verificar se o item doado é válido.
    :param donated_item: String - Item doado
    :return: Boolean - True se o item doado é válido, False caso contrário
    """
    try:
        check_donated_item(donated_item)
        return True
    except RuntimeError as error:
        ScreenPrints.report_error(error.__str__())
        return False


def get_donated_item() -> str:
    """
    Função para obter o item doado.
    :return: String - Item doado
    """
    donated_item: str = ScreenPrints.get_display_donation_items()

    while not is_valid_donated_item(donated_item):
        donated_item = ScreenPrints.get_display_donation_items()

    list_of_items: list[str] = ["AÇÚCAR", "ARROZ", "CAFÉ", "EXTRATO DE TOMATE", "MACARRÃO", "BOLACHA",
                                "ÓLEO", "FARINHA DE TRIGO", "FEIJÃO", "SAL", "OUTROS"]

    return list_of_items[int(donated_item)]


def check_quantity_of_items(quantity_of_items: int) -> None:
    """
    Função para verificar se a quantidade de itens doados é válida.
    :param quantity_of_items: Integer - Quantidade de itens doados
    :raises RuntimeError: Se a quantidade de itens doados for inválida
    """
    QUANTITY_POSITIVE: int = 1

    if quantity_of_items < QUANTITY_POSITIVE:
        raise RuntimeError("QUANTIDADE INFORMADA É INVALIDA")


def is_valid_quantity_of_items(quantity_of_items: int):
    """
    Função para verificar se a quantidade de itens doados é válida.
    :param quantity_of_items: Integer - Quantidade de itens doados
    :return: Boolean - True se a quantidade de itens doados é válida, False caso contrário
    """
    try:
        check_quantity_of_items(quantity_of_items)
        return True
    except RuntimeError as error:
        ScreenPrints.report_error(error.__str__())
        return False


def get_quantity_of_items() -> int:
    """
    Função para obter a quantidade de itens doados.
    :return: Integer - Quantidade de itens doados
    """
    quantity_of_items: int = ScreenPrints.get_display_quantity_of_items()

    while not is_valid_quantity_of_items(quantity_of_items):
        quantity_of_items: int = ScreenPrints.get_display_quantity_of_items()

    return quantity_of_items
