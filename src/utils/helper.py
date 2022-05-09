from src.data import DATA_DIR


def helper():
    with open(str(DATA_DIR / "helper.txt")) as help_msg:
        helper = help_msg.read()
    return helper
