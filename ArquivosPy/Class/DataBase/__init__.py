from ArquivosPy import Stock
from ArquivosPy.Class.Donor import Donor
from ArquivosPy.Class.Item import Item


class DataBase:
    """
    Classe que representa o banco de dados do sistema, que armazena informações sobre itens e doadores.
    """
    def __init__(self) -> None:
        """
        Inicializa uma instância da classe DataBase.
        Cria um dicionário para armazenar itens e um dicionário vazio para armazenar doadores.

        :return: None
        """
        self.__dict_items__: dict[str, Item] = Stock.create_dict_itens()
        self.__dict_donor__: dict[str, Donor] = {}

    def get_dict_items(self) -> dict[str, Item]:
        """
        Obtém o dicionário de itens armazenados no banco de dados.

        :return: dict[str, Item] - Um dicionário que mapeia nomes de itens (str) para objetos do tipo Item.
        """
        return self.__dict_items__

    def get_dict_donor(self) -> dict[str, Donor]:
        """
        Obtém o dicionário de doadores armazenados no banco de dados.

        :return: dict[str, Donor] - Um dicionário que mapeia nomes de doadores (str) para objetos do tipo Donor.
        """
        return self.__dict_donor__
