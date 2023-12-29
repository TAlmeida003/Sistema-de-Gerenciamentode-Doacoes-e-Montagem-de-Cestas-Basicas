from ArquivosPy.Class.DataBase import DataBase
from Menu import MainMenu
import Report


if __name__ == '__main__':

    data_base: DataBase = DataBase()
    user_choice: str = MainMenu.inicialize()

    while not MainMenu.exit_main_menu_option(user_choice):
        MainMenu.open_option(user_choice, data_base)
        user_choice: str = MainMenu.inicialize()

    Report.final_report(data_base)

