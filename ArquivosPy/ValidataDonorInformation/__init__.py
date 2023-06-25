from ArquivosPy import ScreenPrints


def check_name(name_donor: str = "") -> None:

    NUMBER_OF_CHAR = len(name_donor)
    IS_BLANK: int = 0
    CHAR_LIMIT: int = 20

    if NUMBER_OF_CHAR == IS_BLANK:
        raise RuntimeError("O CAMPA NOME DO DOADOR ESTÁ VAZIO")
    elif NUMBER_OF_CHAR > CHAR_LIMIT:
        raise RuntimeError("O NOME INSERIDO NO CAMPO NOME ULTRAPASSOU OS 20 CARACTERES")
    elif not name_donor.isalpha():
        raise RuntimeError("POR FAVOR NÃO INSIRA NÚMEROS NO CAMPO NOME DO DOADOR")


def is_valid_name(name_donor: str = "") -> bool:

    try:
        check_name(name_donor)
        return True
    except RuntimeError as error:
        ScreenPrints.report_error(error.__str__())
        return False


def get_name_donor() -> str:

    name_donor: str = ScreenPrints.get_display_name_donor()

    while not is_valid_name(name_donor):
        name_donor = ScreenPrints.get_display_name_donor()

    return name_donor


def check_type_of_donor(type_of_donor: str = "") -> None:

    set_option: set[str] = {"1", "2"}

    if type_of_donor not in set_option:
        raise RuntimeError("OPÇÃO INVALIDA")


def is_valid_type_of_donor(type_of_donor: str = "") -> bool:

    try:
        check_type_of_donor(type_of_donor)
        return True
    except RuntimeError as error:
        ScreenPrints.report_error(error.__str__())
        return False


def get_type_of_donor() -> str:

    type_of_donor: str = ScreenPrints.get_display_type_of_donor()

    while not is_valid_type_of_donor(type_of_donor):
        type_of_donor = ScreenPrints.get_display_type_of_donor()

    list_type_person: list[str] = ["PF", "PJ"]

    return list_type_person[int(type_of_donor) - 1]


def check_donated_item(donated_item: str = "") -> None:

    set_option_items_donation: set[str] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}

    if donated_item not in set_option_items_donation:
        raise RuntimeError("OPÇÃO INFORMADA É INVALIDA")


def is_valid_donated_item(donated_item: str = "") -> bool:

    try:
        check_donated_item(donated_item)
        return True
    except RuntimeError as error:
        ScreenPrints.report_error(error.__str__())
        return False


def get_donated_item() -> str:

    donated_item: str = ScreenPrints.get_display_donation_items()

    while not is_valid_donated_item(donated_item):
        donated_item = ScreenPrints.get_display_donation_items()

    list_of_items: list[str] = ["AÇÚCAR", "ARROZ", "CAFÉ", "EXTRATO DE TOMATE", "MACARRÃO", "BOLACHA",
                                "ÓLEO", "FARINHA DE TRIGO", "FEIJÃO", "SAL", "OUTROS"]

    return list_of_items[int(donated_item)]


def check_quantity_of_items(quantity_of_items: int = 0) -> None:

    QUANTITY_POSITIVE: int = 1

    if quantity_of_items < QUANTITY_POSITIVE:
        raise RuntimeError("QUANTIDADE INFORMADA É INVALIDA")


def is_valid_quantity_of_items(quantity_of_items: int = 0):

    try:
        check_quantity_of_items(quantity_of_items)
        return True
    except RuntimeError as error:
        ScreenPrints.report_error(error.__str__())
        return False


def get_quantity_of_items() -> int:

    quantity_of_items: int = ScreenPrints.get_display_quantity_of_items()

    while not is_valid_quantity_of_items(quantity_of_items):
        quantity_of_items: int = ScreenPrints.get_display_quantity_of_items()

    return quantity_of_items
