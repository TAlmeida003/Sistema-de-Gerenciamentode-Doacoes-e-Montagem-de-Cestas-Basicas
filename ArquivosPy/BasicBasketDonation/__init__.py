from ArquivosPy import ValidataDonorInformation
from ArquivosPy.Donor import Donor
from ArquivosPy.Item import Item


def store_the_item(dict_item: dict[str, Item], donor: Donor) -> None:
    """
    Procedimento para armazenar os itens doados na estrutura de dados.
    :param dict_item: Dict[str, Item] - Um dicionário que mapeia nomes de itens (str) para objetos do tipo Item.
    :param donor: Donor - Um objeto Donor contendo informações sobre o doador e a doação.
    :return: None
    """
    index_item: str = donor.get_donation().get_donated_item()
    dict_item[index_item].store_the_item(donor.get_donation().get_quantity_of_items(), donor.get_type_of_donor())


def register_donor() -> Donor:
    """
    Função para receber as informações do doador e criar um objeto para representá-lo no sistema.
    :return: Donor - Um objeto Donor que representa o doador no sistema.
    """
    name_donor: str = ValidataDonorInformation.get_name_donor()
    type_of_donor: str = ValidataDonorInformation.get_type_of_donor()
    donated_item: str = ValidataDonorInformation.get_donated_item()
    quantity_of_items: int = ValidataDonorInformation.get_quantity_of_items()

    donor: Donor = Donor(name_donor, type_of_donor)
    donor.add_donation(donated_item, quantity_of_items)

    return donor


def start_donation(dict_item: dict[str, Item]) -> None:
    """
      Procedimento para iniciar o processo de doação.
      :param dict_item: Dict[str, Item] - Um dicionário que mapeia nomes de itens (str) para objetos do tipo Item.
      :return: None
      """
    donor: Donor = register_donor()
    store_the_item(dict_item, donor)
