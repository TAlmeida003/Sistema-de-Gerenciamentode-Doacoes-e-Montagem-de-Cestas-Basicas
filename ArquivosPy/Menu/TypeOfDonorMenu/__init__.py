from ArquivosPy import ScreenPrints


def convert_option_in_person(type_of_donor: str) -> str:
    list_type_person: list[str] = ["PF", "PJ"]

    return list_type_person[int(type_of_donor) - 1]


def check_type_of_donor(type_of_donor: str) -> None:
    """
    Função para verificar se o tipo de doador é válido.
    :param type_of_donor: String - Tipo de doador
    :raises RuntimeError: Se o tipo de doador for uma opção inválida
    """
    set_option: set[str] = {"1", "2"}

    if type_of_donor not in set_option:
        raise RuntimeError("OPÇÃO INVALIDA")


def is_valid_type_of_donor(type_of_donor: str) -> bool:
    """
    Função para verificar se o tipo de doador é válido.
    :param type_of_donor: String - Tipo de doador
    :return: Boolean - True se o tipo de doador é válido, False caso contrário
    """
    try:
        check_type_of_donor(type_of_donor)
        return True
    except RuntimeError as error:
        ScreenPrints.report_error(error.__str__())
        return False


def display_type_person() -> None:
    """
    Exibe as opções de tipo de pessoa (física ou jurídica).
    :return: None
    """
    SIZE_CENTER_TEXT: int = 170

    ScreenPrints.display_header("INFORMAÇÕES DO DOADOR")
    print("\n" * 4)
    print("\n", "[ 1 ] — PESSOA FÍSICA".center(SIZE_CENTER_TEXT))
    print("\n", "[ 2 ] — PESSOA JURÍDICA".center(SIZE_CENTER_TEXT))

    print("\n" * 5, ("-=" * 40).center(SIZE_CENTER_TEXT))
    print(" " * 50, end="* ")


def input_type_of_donor() -> str:
    """
    Obtém o tipo de pessoa do doador.
    :return: String - Tipo de doador
    """
    display_type_person()
    type_of_donor: str = input("INFORME QUAL O TIPE DE PESSOA PERTENCE O DOADOR: ")
    ScreenPrints.clear_prompt()

    return type_of_donor


def inicialize() -> str:
    """
    Função para obter o tipo de doador.
    :return: String - Tipo de doador
    """
    type_of_donor: str = input_type_of_donor()

    while not is_valid_type_of_donor(type_of_donor):
        type_of_donor = input_type_of_donor()

    return convert_option_in_person(type_of_donor)
