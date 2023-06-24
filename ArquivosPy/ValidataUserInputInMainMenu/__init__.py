from ArquivosPy import ScreenPrints


def exit_main_menu_option(user_choice: str = "") -> bool:

    OPTION_EXIT: str = "3"

    if user_choice == OPTION_EXIT:
        return True
    else:
        return False


def check_option_main_menu(user_choice: str = "") -> None:

    set_option: set[str] = {"1", "2", "3"}

    if user_choice not in set_option:
        raise RuntimeError("OPÇÃO INVALIDA")


def is_a_valid_main_menu_option(user_choice: str = "3") -> bool:

    try:
        check_option_main_menu(user_choice)
        return True
    except RuntimeError as error:
        ScreenPrints.report_error(error.__str__())
        return False


def get_main_manu_entry() -> str:
    user_choice: str = ScreenPrints.get_display_main_menu_option()

    while not is_a_valid_main_menu_option(user_choice):
        user_choice = ScreenPrints.get_display_main_menu_option()

    return user_choice
