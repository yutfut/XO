from colorama import Fore, Style


def custom_ValueError(item):
    move = None
    try:
        move = int(item)
    except ValueError:
        print(Fore.RED + "ValueError input number 1-9" + Style.RESET_ALL)
    return move


def custom_KeyError(item, class_dict):
    move = True
    try:
        class_dict[item]
    except KeyError:
        print(Fore.RED + "ValueError input number 1-9", Style.RESET_ALL)
        move = False
    return move
