from ArquivosPy import ScreenPrints
from ArquivosPy.Class.DataBase import DataBase
from ArquivosPy.Class.Donation import Donation
from ArquivosPy.Menu import NameMenu, TypeOfDonorMenu, DonatedItemMenu, QuantityOfItemsMenu
from ArquivosPy.Class.Donor import Donor
from ArquivosPy.Class.Item import Item


def insert_donor(dict_donor: dict[str, Donor], donor: Donor) -> None:
    """
    Insere um doador em um dicionário de doadores ou atualiza a doação de um doador existente.

    :param dict_donor: Dict[str, Donor] - Um dicionário que mapeia nomes de doadores (str) para objetos do tipo Donor.
    :param donor: Donor - Um objeto Donor contendo informações do doador e detalhes da doação.
    :return: None
    """

    if donor.get_name_donor() not in dict_donor:
        dict_donor[donor.get_name_donor()] = donor
    else:
        donation: Donation = donor.get_last_donation()
        dict_donor[donor.get_name_donor()].add_donation(donation.get_donated_item(), donation.get_quantity_of_items())


def store_the_item(dict_item: dict[str, Item], donor: Donor) -> None:
    """
    Procedimento para armazenar os itens doados na estrutura de dados.

    :param dict_item: Dict[str, Item] - Um dicionário que mapeia nomes de itens (str) para objetos do tipo Item.
    :param donor: Donor - Um objeto Donor contendo informações sobre o doador e a doação.
    :return: None
    """

    index_item: str = donor.get_last_donation().get_donated_item()
    dict_item[index_item].store_the_item(donor.get_last_donation().get_quantity_of_items(), donor.get_type_of_donor())


def information_type_of_donor(dict_donor: dict[str, Donor], name_donor: str) -> str:
    """
    Obtém o tipo de doador com base em seu nome.

    :param dict_donor: Dict[str, Donor] - Um dicionário que mapeia nomes de doadores (str) para objetos do tipo Donor.
    :param name_donor: str - O nome do doador.
    :return: str - O tipo de doador.
    """

    if name_donor in dict_donor:
        return dict_donor[name_donor].get_type_of_donor()

    return TypeOfDonorMenu.inicialize()


def register_donor(dict_donor: dict[str, Donor]) -> Donor:
    """
    Função para receber as informações do doador e criar um objeto para representá-lo no sistema.

    :return: Donor - Um objeto Donor que representa o doador no sistema.
    """

    name_donor: str = ScreenPrints.format_string(NameMenu.inicialize())
    type_of_donor: str = information_type_of_donor(dict_donor, name_donor)
    donated_item: str = DonatedItemMenu.inicialize()
    quantity_of_items: int = QuantityOfItemsMenu.inicialize()

    donor: Donor = Donor(name_donor, type_of_donor)
    donor.add_donation(donated_item, quantity_of_items)

    return donor


def start_donation(data_base: DataBase) -> None:
    """
    Procedimento para iniciar o processo de doação.

    :param data_base: DataBase - banco de dados do programa
    :return: None
    """

    donor: Donor = register_donor(data_base.get_dict_donor())

    store_the_item(data_base.get_dict_items(), donor)
    insert_donor(data_base.get_dict_donor(), donor)
