from ArquivosPy import ScreenPrints
from ArquivosPy.Class.Donation import Donation
from ArquivosPy.Class.Donor import Donor


def display_donation(donation_list: list[Donation]) -> None:
    ScreenPrints.display_sub_title("Lista de Doações")
    print("\n")

    for donation in donation_list:
        print(f"[ {donation.get_quantity_of_items()} ] - de {donation.get_donated_item()}".center(170))
        print("\n")

    ScreenPrints.get_baseboard()


def report_dict_blank() -> None:
    print("\n" * 6)
    print("Nenhum doador foi registrado!!!".center(170))
    print("Por Favor, registre um doador para visualizar seu histórico  de doação.".center(170))
    print("\n" * 6)


def display_information_donor(donor: Donor) -> None:
    print("\n")
    print(("Nome: " + donor.get_name_donor()).center(170))
    print(("Tipo de Pessoa: " + ("Física" if donor.get_type_of_donor() == "PF" else "Jurídica")).center(170))
    print("\n")
    display_donation(donor.get_list_donation())


def display_donors(dict_donor: dict[str, Donor]) -> None:
    for kay_donor in dict_donor:
        donor: Donor = dict_donor[kay_donor]
        display_information_donor(donor)


def display_donor_report(dict_donor: dict[str, Donor]) -> None:
    IS_BLANK: int = 0

    if len(dict_donor) != IS_BLANK:
        display_donors(dict_donor)
    else:
        report_dict_blank()


def inicialize(dict_donor: dict[str, Donor]) -> None:
    ScreenPrints.display_header("Livro de Registro")
    display_donor_report(dict_donor)

    input(" Pressione [ENTER] para retorna para o menu principal ".center(170, "-"))
    ScreenPrints.clear_prompt()
