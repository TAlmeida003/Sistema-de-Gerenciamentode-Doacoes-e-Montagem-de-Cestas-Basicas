import os


def report_error(text: str) -> None:
    """
    Exibe uma mensagem de erro formatada.

    :param text: O texto do erro.
    :return: None
    """
    SIZE_CENTER_TEXT: int = 170

    print("\033[1;31m", ('=-' * 40).center(SIZE_CENTER_TEXT))
    print("ERRO!!!".center(SIZE_CENTER_TEXT + 1))
    print(text.center(SIZE_CENTER_TEXT))
    print(('=-' * 40).center(SIZE_CENTER_TEXT + 3), "\033[1;97m")


def display_header(text: str) -> None:
    """
        Exibe um cabeçalho formatado.

        :param text: O texto do cabeçalho.
        :return: None
        """
    SIZE_CENTER_TEXT: int = 170

    print("\033[1;97m")
    display_sub_title("dispensário santana")

    print(("= " * 24).center(SIZE_CENTER_TEXT + 2, " "))
    print((("==" * 10) + " " + text + " " + ("==" * 10)).center(SIZE_CENTER_TEXT))
    print(("= " * 20).center(SIZE_CENTER_TEXT, " "))
    print(("= " * 15).center(SIZE_CENTER_TEXT, " "))
    print(("= " * 5).center(SIZE_CENTER_TEXT, " "))
    print(("= " * 3).center(SIZE_CENTER_TEXT, " "))


def display_menu() -> None:
    """
    Exibe o menu principal.

    :return: None
    """
    SIZE_CENTER_TEXT: int = 170

    display_header('MENU PRINCIPAL')

    print(str("\n\n"), "[ 1 ] — INICIAR DOAÇÃO".center(SIZE_CENTER_TEXT))
    print(str("\n\n\n"), "[ 2 ] — VISUALIZAR RELATORIO".center(SIZE_CENTER_TEXT))
    print(str("\n\n\n"), "[ 3 ] — FECHA O PROGRAMA".center(SIZE_CENTER_TEXT))

    print("\n", "\n", "\n", ("-=" * 40).center(SIZE_CENTER_TEXT))
    print(" " * 50, end="* ")


def display_sub_title(text: str) -> None:
    """
    Exibe um sub título formatado.
    :param text: O texto do sub título.
    :return: None
    """
    SIZE_CENTER_TEXT: int = 170

    print(("=-" * 40).center(SIZE_CENTER_TEXT + 2, " "))
    print(text.center(SIZE_CENTER_TEXT))
    print(("=-" * 40).center(SIZE_CENTER_TEXT + 2, " "))
    print("\n")


def clear_prompt() -> None:
    """
    Limpa a tela do console.

    :return: None
    """
    if os.name == 'nt':
        os.system('cls') or None
    else:
        os.system('clear') or None


def display_name_donor() -> None:
    """
    Exibe o formulário de informações do doador.

    :return: None
    """
    SIZE_CENTER_TEXT: int = 170

    display_header("INFORMAÇÕES DO DOADOR")

    print("\n" * 14, ("-=" * 40).center(SIZE_CENTER_TEXT))
    print(" " * 50, end="* ")


def get_display_name_donor() -> str:
    """
    Obtém o nome do doador.

    :return: String - Nome do doador.
    """
    display_name_donor()
    name_donor: str = input("INFORME O NOME DO DOADOR: ")
    clear_prompt()

    return name_donor


def get_display_main_menu_option() -> str:
    """
    Obtém a opção do menu principal.

    :return: String - Opção escolhida pelo usuário.
    """
    display_menu()
    user_choice = input("INFORME QUAL A OPÇÃO DESEJADA: ")
    clear_prompt()

    return user_choice


def display_type_person() -> None:
    """
    Exibe as opções de tipo de pessoa (física ou jurídica).

    :return: None
    """
    SIZE_CENTER_TEXT: int = 170

    display_header("INFORMAÇÕES DO DOADOR")
    print("\n" * 4)
    print("\n", "[ 1 ] — PESSOA FÍSICA".center(SIZE_CENTER_TEXT))
    print("\n", "[ 2 ] — PESSOA JURÍDICA".center(SIZE_CENTER_TEXT))

    print("\n" * 5, ("-=" * 40).center(SIZE_CENTER_TEXT))
    print(" " * 50, end="* ")


def get_display_type_of_donor() -> str:
    """
    Obtém o tipo de pessoa do doador.

    :return: String - Tipo de doador
    """
    display_type_person()
    type_of_donor: str = input("INFORME QUAL O TIPE DE PESSOA PERTENCE O DOADOR: ")
    clear_prompt()

    return type_of_donor


def display_donation_items() -> None:
    """
    Exibe as opções de itens de doação.

    :return: None
    """
    SIZE_CENTER_TEXT: int = 170

    cont: int = 1
    line_string: str = ""

    list_of_donation_options: list[str] = ["AÇÚCAR", "ARROZ", "CAFÉ", "EXTRATO DE TOMATE", "MACARRÃO", "BOLACHA",
                                           "ÓLEO", "FARINHA DE TRIGO", "FEIJÃO", "SAL", "OUTROS"]

    display_header("INFORMAÇÕES DA DOAÇÃO")
    for item_option in range(11):
        line_string += f"[ {item_option} ] — DOAR {(list_of_donation_options[item_option]) : ^9} "
        cont += 1

        if cont == 4:
            print("\n" * 2, line_string.center(SIZE_CENTER_TEXT))
            line_string = ""
            cont = 1

    print("\n" * 2, line_string.center(SIZE_CENTER_TEXT))
    print("\n" * 2, ("-=" * 40).center(SIZE_CENTER_TEXT))
    print(" " * 50, end="* ")


def get_display_donation_items() -> str:
    """
    Obtém a opção de doação escolhida.

    :return: String - Item doado.
    """
    display_donation_items()
    donation_items: str = input("INFORME QUAL OPÇÃO DE DOAÇÃO DESEJADA: ")
    clear_prompt()

    return donation_items


def display_quantity_item() -> None:
    """
    Exibe informações sobre a quantidade de itens doados.

    :return: None
    """
    SIZE_CENTER_TEXT: int = 170
    display_header("INFORMAÇÕES DE DOAÇÃO")
    print("\n" * 14, ("-=" * 40).center(SIZE_CENTER_TEXT))
    print(" " * 50, end="* ")


def get_display_quantity_of_items() -> int:
    """
    Obtém a quantidade de itens doados.

    :return: Integer - Quantidade de itens doados.
    """
    try:
        display_quantity_item()
        quantity_of_items: int = int(input("INFORME A QUANTIDADE DE ITENS DOADOS: "))
        clear_prompt()

        return quantity_of_items
    except ValueError:
        return 0


def get_baseboard() -> None:
    """
    Obtém o rodapé da tela.

    :return: None
    """
    SIZE_CENTER: int = 180
    print(("-=" * 40).center(SIZE_CENTER))
    print("\n")
