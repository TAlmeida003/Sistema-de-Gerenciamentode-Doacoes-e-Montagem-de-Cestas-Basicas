from ArquivosPy.Item import Item


def create_dict_itens() -> dict[str, Item]:
    SIZE_OF_LIST: int = 11

    dict_items: dict[str, Item] = dict()
    weight_items_list: list[int] = [1, 4, 2, 2, 3, 1, 1, 1, 1, 4, 1, 1]
    list_of_items: list[str] = ["AÇÚCAR", "ARROZ", "CAFÉ", "EXTRATO DE TOMATE", "MACARRÃO", "BOLACHA",
                                "ÓLEO", "FARINHA DE TRIGO", "FEIJÃO", "SAL", "OUTROS"]

    for item in range(SIZE_OF_LIST):
        dict_items[list_of_items[item]] = Item(list_of_items[item], weight_items_list[item])

    return dict_items


def get_number_basket(dict_items: dict[str, Item] = None):
    KAY_SUGAR: str = "AÇÚCAR"

    num_basket: int = dict_items[KAY_SUGAR].get_quantity_in_baskets()

    for kay_item in dict_items:
        if dict_items[kay_item].get_quantity_in_baskets() < num_basket:
            num_basket = dict_items[kay_item].get_quantity_in_baskets()

    return num_basket


def get_quantity_in_type_person(dict_items: dict[str, Item] = None) -> tuple[int, int]:
    num_person_individual: int = 0
    num_person_legal_entity: int = 0

    for kay_item in dict_items:
        num_person_individual += dict_items[kay_item].get_amount_per_individual()
        num_person_legal_entity += dict_items[kay_item].get_amount_per_legal_entity()

    return num_person_individual, num_person_legal_entity


def get_baskets_with_extra_item(dict_items: dict[str, Item] = None) -> int:
    KAY_ITEM_EXTRA: str = "OUTROS"

    number_basket_with_extra: int = get_number_basket(dict_items)

    if number_basket_with_extra >= dict_items[KAY_ITEM_EXTRA].get_total_amount():
        number_basket_with_extra = dict_items[KAY_ITEM_EXTRA].get_total_amount()

    return number_basket_with_extra


def get_baskets_without_extra_item(dict_items: dict[str, Item] = None) -> int:
    KAY_ITEM_EXTRA: str = "OUTROS"

    numbers_baskets_without_extra: int = 0
    number_basket: int = get_number_basket(dict_items)

    if number_basket >= dict_items[KAY_ITEM_EXTRA].get_total_amount():
        numbers_baskets_without_extra = number_basket - dict_items[KAY_ITEM_EXTRA].get_total_amount()

    return numbers_baskets_without_extra
