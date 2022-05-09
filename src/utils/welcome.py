from src.data import DATA_DIR


def welcome():
    """
    Create welcome message to user
    """
    with open(DATA_DIR / "welcome.txt") as wel_msg:
        welcome_msg = wel_msg.read()
    return welcome_msg
