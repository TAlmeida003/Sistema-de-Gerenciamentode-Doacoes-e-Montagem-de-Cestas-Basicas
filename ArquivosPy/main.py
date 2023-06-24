import ValidataUserInputInMainMenu
import BasicBasketDonation
from Item import Item
import Stock
import Report


def open_option(user_choice_option: str = "", dict_items_stock: dict[str, Item] = None):

    OPTION_ONE: str = "1"

    if user_choice_option == OPTION_ONE:
        BasicBasketDonation.start_donation(dict_items_stock)
    else:
        Report.inicialize_report(dict_items_stock)


if __name__ == '__main__':

    dict_items: dict[str, Item] = Stock.create_dict_itens()
    user_choice: str = ValidataUserInputInMainMenu.get_main_manu_entry()

    while not ValidataUserInputInMainMenu.exit_main_menu_option(user_choice):
        open_option(user_choice, dict_items)
        user_choice: str = ValidataUserInputInMainMenu.get_main_manu_entry()

    Report.final_report(dict_items)
