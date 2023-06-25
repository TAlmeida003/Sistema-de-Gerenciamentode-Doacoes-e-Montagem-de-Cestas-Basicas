from ArquivosPy import ScreenPrints


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
    :return: None
    """
    set_option: set[str] = {"1", "2", "3"}

    if user_choice not in set_option:
        raise RuntimeError("OPÇÃO INVALIDA")


def is_a_valid_main_menu_option(user_choice: str) -> bool:
    """
    Verifica se a opção selecionada no menu principal é válida.

    :param user_choice: String - Opção selecionada pelo usuário.
    :return: Boolean - True se a opção for válida, False caso contrário.
    """
    try:
        check_option_main_menu(user_choice)
        return True
    except RuntimeError as error:
        ScreenPrints.report_error(error.__str__())
        return False


def get_main_manu_entry() -> str:
    """
    Obtém a entrada do usuário para o menu principal, verificando se a opção é válida.

    :return: String - Opção selecionada pelo usuário.
    """
    user_choice: str = ScreenPrints.get_display_main_menu_option()

    while not is_a_valid_main_menu_option(user_choice):
        user_choice = ScreenPrints.get_display_main_menu_option()

    return user_choice
