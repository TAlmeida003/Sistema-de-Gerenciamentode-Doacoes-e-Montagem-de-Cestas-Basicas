from ArquivosPy import ValidataDonorInformation
from ArquivosPy.Donor import Donor
from ArquivosPy.Item import Item


def store_the_item(dict_item: dict[str, Item], donor: Donor = None) -> None:

    index_item: str = donor.get_donation().get_donated_item()
    dict_item[index_item].store_the_item(donor.get_donation().get_quantity_of_items(), donor.get_type_of_donor())


def register_donor() -> Donor:

    name_donor: str = ValidataDonorInformation.get_name_donor()
    type_of_donor: str = ValidataDonorInformation.get_type_of_donor()
    donated_item: str = ValidataDonorInformation.get_donated_item()
    quantity_of_items: int = ValidataDonorInformation.get_quantity_of_items()

    donor: Donor = Donor(name_donor, type_of_donor)
    donor.add_donation(donated_item, quantity_of_items)

    return donor


def start_donation(dict_item: dict[str, Item]) -> None:

    donor: Donor = register_donor()
    store_the_item(dict_item, donor)
