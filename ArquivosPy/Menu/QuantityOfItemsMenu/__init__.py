from ArquivosPy import ScreenPrints


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


def display_quantity_item() -> None:
    """
    Exibe informações sobre a quantidade de itens doados.

    :return: None
    """
    SIZE_CENTER_TEXT: int = 170
    ScreenPrints.display_header("INFORMAÇÕES DE DOAÇÃO")
    print("\n" * 14, ("-=" * 40).center(SIZE_CENTER_TEXT))
    print(" " * 50, end="* ")


def input_quantity_of_items() -> int:
    """
    Obtém a quantidade de itens doados.

    :return: Integer - Quantidade de itens doados.
    """
    try:
        display_quantity_item()
        quantity_of_items: int = int(input("INFORME A QUANTIDADE DE ITENS DOADOS: "))
        ScreenPrints.clear_prompt()

        return quantity_of_items
    except ValueError:
        return 0


def inicialize() -> int:
    """
    Função para obter a quantidade de itens doados.
    :return: Integer - Quantidade de itens doados
    """
    quantity_of_items: int = input_quantity_of_items()

    while not is_valid_quantity_of_items(quantity_of_items):
        quantity_of_items: int = input_quantity_of_items()

    return quantity_of_items
