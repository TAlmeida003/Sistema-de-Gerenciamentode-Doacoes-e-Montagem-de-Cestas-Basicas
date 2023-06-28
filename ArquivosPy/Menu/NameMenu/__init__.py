from ArquivosPy import ScreenPrints


def check_name(name_donor: str) -> None:
    """
    Função para verificar se o nome do doador é válido.
    :param name_donor: String - Nome do doador
    :raises RuntimeError: Se o nome do doador estiver vazio, exceder 20 caracteres ou conter números
    :return: None
    """
    NUMBER_OF_CHAR = len(name_donor)
    IS_BLANK: int = 0
    CHAR_LIMIT: int = 20

    if NUMBER_OF_CHAR == IS_BLANK:
        raise RuntimeError("O CAMPA NOME DO DOADOR ESTÁ VAZIO")
    elif NUMBER_OF_CHAR > CHAR_LIMIT:
        raise RuntimeError("O NOME INSERIDO NO CAMPO NOME ULTRAPASSOU OS 20 CARACTERES")
    elif not name_donor.isalpha():
        raise RuntimeError("POR FAVOR NÃO INSIRA NÚMEROS NO CAMPO NOME DO DOADOR")


def is_valid_name(name_donor: str) -> bool:
    """
    Função para verificar se o nome do doador é válido.
    :param name_donor: String - Nome do doador
    :return: Boolean - True se o nome é válido, False caso contrário
    """
    try:
        check_name(name_donor)
        return True
    except RuntimeError as error:
        ScreenPrints.report_error(error.__str__())
        return False


def display_name_donor() -> None:
    """
    Exibe o formulário de informações do doador.
    :return: None
    """
    SIZE_CENTER_TEXT: int = 170

    ScreenPrints.display_header("INFORMAÇÕES DO DOADOR")

    print("\n" * 14, ("-=" * 40).center(SIZE_CENTER_TEXT))
    print(" " * 50, end="* ")


def input_name_donor() -> str:
    """
    Obtém o nome do doador.
    :return: String - Nome do doador.
    """
    display_name_donor()
    name_donor: str = input("INFORME O NOME DO DOADOR: ")
    ScreenPrints.clear_prompt()

    return name_donor


def inicialize() -> str:
    """
    Função para obter o nome do doador.
    :return: String - Nome do doador
    """
    name_donor: str = input_name_donor()

    while not is_valid_name(name_donor):
        name_donor = input_name_donor()

    return name_donor
