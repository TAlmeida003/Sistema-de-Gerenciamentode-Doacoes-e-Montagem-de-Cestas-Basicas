from ArquivosPy.Item import Item
from ArquivosPy import ScreenPrints
from ArquivosPy import Stock


def display_items_received(dict_items: dict[str, Item]) -> None:
    """
        Exibe os itens recebidos.

        :param dict_items: Dict[str, Item] - Dicionário contendo os itens recebidos.
        :return: None
        """
    cont: int = 1
    line_string: str = ""
    SIZE_CENTER: int = 180

    print("\n")
    ScreenPrints.display_sub_title("Total de items recebidos")

    for item in dict_items:
        line_string += f"| [ {dict_items[item].get_total_amount()} ] {dict_items[item].get_unit_of_measurement()} " \
                       f"de {item} |   "

        cont += 1

        if cont == 4:
            print(line_string.center(SIZE_CENTER))
            line_string = ""
            cont = 1
            print("\n")

    print(line_string.center(SIZE_CENTER))
    print("\n")


def display_items_in_type_person(dict_items: dict[str, Item]) -> None:
    """
        Exibe os itens doados por tipo de pessoa (física ou jurídica).

        :param dict_items: Dict[str, Item] - Dicionário contendo os itens doados.
        :return: None
    """
    type_individual, type_legal_entity = Stock.get_quantity_in_type_person(dict_items)
    SIZE_CENTER: int = 170

    ScreenPrints.display_sub_title("Total de items doados por pessoas físicas")
    print(("Foram doados: " + str(type_individual)).center(SIZE_CENTER))
    print("\n")

    ScreenPrints.display_sub_title("Total de items doados por pessoas jurídica")
    print(("Foram doados: " + str(type_legal_entity)).center(SIZE_CENTER))
    print("\n")


def display_items_left(dict_items: dict[str, Item]) -> None:
    """
    Exibe os itens que sobraram após a montagem das cestas básicas.

    :param dict_items: Dict[str, Item] - Dicionário contendo os itens do estoque.
    :return: None
    """
    cont: int = 1
    line_string: str = ""

    NUMBER_BASKET: int = Stock.get_number_basket(dict_items)
    SIZE_CENTER: int = 180

    ScreenPrints.display_sub_title("Total de items que sobraram após a montagem das cestas básica")

    for item in dict_items:
        line_string += f"| [ " \
                       f"{dict_items[item].calculate_the_amount_of_items_left_after(NUMBER_BASKET)} " \
                       f"] {dict_items[item].get_unit_of_measurement()} de {item} |   "

        cont += 1

        if cont == 4:
            print(line_string.center(SIZE_CENTER))
            line_string: str = ""
            cont = 1
            print("\n")

    print(line_string.center(SIZE_CENTER))
    print("\n")
    ScreenPrints.get_baseboard()


def display_information_basket(dict_items: dict[str, Item]) -> None:
    """
    Exibe informações sobre as cestas básicas.

    :param dict_items: Dict[str, Item] - Dicionário contendo os itens do estoque.
    :return: None
    """
    SIZE_CENTER: int = 170

    ScreenPrints.display_sub_title("Informações das cestas básicas")

    print(f"[ {Stock.get_number_basket(dict_items)} ]"
          f" - Total de cesta".center(SIZE_CENTER))
    print("\n")
    print(f"[ {Stock.get_baskets_with_extra_item(dict_items)} ]"
          f" - Total de cestas com item extra".center(SIZE_CENTER))
    print("\n")
    print(f"[ {Stock.get_baskets_without_extra_item(dict_items)} ]"
          f" - Total de cestas sem item extra".center(SIZE_CENTER))
    print("\n")


def print_out_report(dict_items: dict[str, Item]) -> None:
    """
    Imprime o relatório com as informações sobre os itens recebidos, doados, cestas básicas e itens restantes.

    :param dict_items: dict[str, Item] - Dicionário contendo os itens do estoque.
    :return: None
    """
    display_items_received(dict_items)
    display_items_in_type_person(dict_items)
    display_information_basket(dict_items)
    display_items_left(dict_items)


def inicialize_report(dict_items: dict[str, Item]) -> None:
    """
    Inicializa o relatório parcial exibindo as informações sobre os itens recebidos, doados, cestas básicas e itens restantes.

    :param dict_items:  dict[str, Item] - Dicionário contendo os itens do estoque.
    :return: None
    """
    ScreenPrints.display_header("Relatorio parcial")
    print_out_report(dict_items)

    input(" Pressione [ENTER] para retorna para o menu principal ".center(170, "-"))
    ScreenPrints.clear_prompt()


def final_report(dict_items: dict[str, Item]) -> None:
    """
    Imprime o relatório final com as informações sobre os itens recebidos, doados, cestas básicas e itens restantes.

    :param dict_items: Dict[str, Item] - Dicionário contendo os itens do estoque.
    :return: None
    """
    ScreenPrints.display_header("Relatorio final")
    print_out_report(dict_items)

    print(" Obrigado por usar esse programa!!! :) ".center(170, "-"))
