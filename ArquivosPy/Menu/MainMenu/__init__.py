from ArquivosPy import ScreenPrints, BasicBasketDonation, Report
from ArquivosPy.Class.Item import Item


def open_option(user_choice_option: str, dict_items_stock: dict[str, Item]) -> None:
    """
    Procedimento para abrir a opção desejada pelo usuário.
    :return: None
    """
    OPTION_ONE: str = "1"

    if user_choice_option == OPTION_ONE:
        BasicBasketDonation.start_donation(dict_items_stock)
    else:
        Report.inicialize_report(dict_items_stock)


def exit_main_menu_option(user_choice: str) -> bool:
    """
    Verifica se a opção selecionada no menu principal é a opção de saída.
    :param user_choice: String - Opção selecionada pelo usuário.
    :return: Boolean - true se a opção for a de saída, false caso contrário.
    """
    OPTION_EXIT: str = "3"

    if user_choice != OPTION_EXIT:
        return False

    return True


def check_option_main_menu(user_choice: str) -> None:
    """
    Verifica se a opção selecionada no menu principal é uma opção válida.
    :param user_choice: String - Opção selecionada pelo usuário.
    :raises RuntimeError: Se a opção selecionada for inválida.
    """
    set_option: set[str] = {"1", "2", "3"}

    if user_choice not in set_option:
        raise RuntimeError("OPÇÃO INVALIDA")


def is_a_valid_main_menu_option(user_choice: str) -> bool:
    """
    Verifica se a opção selecionada no menu principal é válida.
    :param user_choice: String - Opção selecionada pelo usuário.
    :return: Boolean - True se a opção for válida, false caso contrário.
    """
    try:
        check_option_main_menu(user_choice)
        return True
    except RuntimeError as error:
        ScreenPrints.report_error(error.__str__())
        return False


def display_menu() -> None:
    """
    Exibe o menu principal.
    :return: None
    """
    SIZE_CENTER_TEXT: int = 170

    ScreenPrints.display_header('MENU PRINCIPAL')

    print(str("\n\n"), "[ 1 ] — INICIAR DOAÇÃO".center(SIZE_CENTER_TEXT))
    print(str("\n\n\n"), "[ 2 ] — VISUALIZAR RELATORIO".center(SIZE_CENTER_TEXT))
    print(str("\n\n\n"), "[ 3 ] — FECHA O PROGRAMA".center(SIZE_CENTER_TEXT))

    print("\n", "\n", "\n", ("-=" * 40).center(SIZE_CENTER_TEXT))
    print(" " * 50, end="* ")


def input_main_menu() -> str:
    """
    Obtém a opção do menu principal.
    :return: String - Opção escolhida pelo usuário.
    """
    display_menu()
    user_choice = input("INFORME QUAL A OPÇÃO DESEJADA: ")
    ScreenPrints.clear_prompt()

    return user_choice


def inicialize() -> str:
    """
    Obtém a entrada do usuário para o menu principal, verificando se a opção é válida.
    :return: String - Opção selecionada pelo usuário.
    """
    user_choice: str = input_main_menu()

    while not is_a_valid_main_menu_option(user_choice):
        user_choice = input_main_menu()

    return user_choice
