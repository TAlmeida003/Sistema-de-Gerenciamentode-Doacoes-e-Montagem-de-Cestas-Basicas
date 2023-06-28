from ArquivosPy.Menu import MainMenu
from ArquivosPy.Class.Item import Item
import Stock
import Report


if __name__ == '__main__':

    dict_items: dict[str, Item] = Stock.create_dict_itens()
    user_choice: str = MainMenu.inicialize()

    while not MainMenu.exit_main_menu_option(user_choice):
        MainMenu.open_option(user_choice, dict_items)
        user_choice: str = MainMenu.inicialize()

    Report.final_report(dict_items)
