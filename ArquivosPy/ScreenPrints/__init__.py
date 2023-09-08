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


def display_header(text: str) -> None:
    """
        Exibe um cabeçalho formatado.
        :param text: O texto do cabeçalho.
        :return: None
        """
    SIZE_CENTER_TEXT: int = 170

    display_sub_title("dispensário santana")

    print(("= " * 24).center(SIZE_CENTER_TEXT + 2, " "))
    print((("==" * 10) + " " + text + " " + ("==" * 10)).center(SIZE_CENTER_TEXT))
    print(("= " * 20).center(SIZE_CENTER_TEXT, " "))
    print(("= " * 15).center(SIZE_CENTER_TEXT, " "))
    print(("= " * 5).center(SIZE_CENTER_TEXT, " "))
    print(("= " * 3).center(SIZE_CENTER_TEXT, " "))


def clear_prompt() -> None:
    """
    Limpa a tela do console.
    :return: None
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_baseboard() -> None:
    """
    Obtém o rodapé da tela.
    :return: None
    """
    SIZE_CENTER: int = 170
    print("\n")
    print(("-=" * 40).center(SIZE_CENTER))


def get_display_option(num_option: str, name_option: str) -> None:
    SIZE_CENTER_TEXT: int = 170

    print()
    print("\n", f"[ {num_option} ] — {name_option}".center(SIZE_CENTER_TEXT))


def format_string(word: str) -> str:
    formatted_words = [w.capitalize() for w in word.split()]
    return ' '.join(formatted_words)
