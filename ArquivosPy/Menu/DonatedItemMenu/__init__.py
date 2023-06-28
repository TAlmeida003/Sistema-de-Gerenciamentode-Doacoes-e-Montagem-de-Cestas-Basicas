from ArquivosPy import ScreenPrints


def convert_option_in_item(donated_item: str) -> str:
    list_of_items: list[str] = ["AÇÚCAR", "ARROZ", "CAFÉ", "EXTRATO DE TOMATE", "MACARRÃO", "BOLACHA", "ÓLEO",
                                "FARINHA DE TRIGO", "FEIJÃO", "SAL", "OUTROS"]

    return list_of_items[int(donated_item)]


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


def display_donation_items() -> None:
    """
    Exibe as opções de itens de doação.

    :return: None
    """
    SIZE_CENTER_TEXT: int = 170

    cont: int = 1
    line_string: str = ""

    list_of_donation_options: list[str] = ["AÇÚCAR", "ARROZ", "CAFÉ", "EXTRATO DE TOMATE", "MACARRÃO", "BOLACHA",
                                           "ÓLEO", "FARINHA DE TRIGO", "FEIJÃO", "SAL", "OUTROS"]

    ScreenPrints.display_header("INFORMAÇÕES DA DOAÇÃO")
    for item_option in range(11):
        line_string += f"[ {item_option} ] — DOAR {(list_of_donation_options[item_option]) : ^9} "
        cont += 1

        if cont == 4:
            print("\n" * 2, line_string.center(SIZE_CENTER_TEXT))
            line_string = ""
            cont = 1

    print("\n" * 2, line_string.center(SIZE_CENTER_TEXT))
    print("\n" * 2, ("-=" * 40).center(SIZE_CENTER_TEXT))
    print(" " * 50, end="* ")


def input_donation_items() -> str:
    """
    Obtém a opção de doação escolhida.
    :return: String - Item doado.
    """
    display_donation_items()
    donation_items: str = input("INFORME QUAL OPÇÃO DE DOAÇÃO DESEJADA: ")
    ScreenPrints.clear_prompt()

    return donation_items


def inicialize() -> str:
    """
    Função para obter o item doado.
    :return: String - Item doado
    """
    donated_item: str = input_donation_items()

    while not is_valid_donated_item(donated_item):
        donated_item = input_donation_items()

    return convert_option_in_item(donated_item)
