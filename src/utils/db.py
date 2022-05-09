"""
database handy functions
"""


from loguru import logger

from mysql.connector import connect, Error


class BotDB:
    def __init__(self, user: str, password: str, host: str="localhost"):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        logger.info(f"Your username : {user}")
        logger.info(f"Your host is : {host}")

    def create_db(self, db_name: str):
        try:
            self.executer(f"CREATE DATABASE {db_name}")
        except Exception as e:
            logger.error(e)
        else:
            logger.success(f"{db_name} database is created . . . ")

    def show_tables(self):
        try:
            logger.debug(list(self.executer("SHOW TABLES")))
        except Exception as err:
            logger.error(Error)


    def create_users_table(self):
        try:
            self.executer(
                f"CREATE TABLE users (\
                id INT NOT NULL, \
                username VARCHAR(100), \
                firstname VARCHAR(100), \
                lastname VARCHAR(100), \
                status VARCHAR(20) NOT NULL DEFAULT 'disconnect', \
                PRIMARY KEY(id)\
            )")
        except Error as err:
            logger.error(err)
        except Exception as err:
            logger.error(err)
        else:
            logger.success("users table is created. . .")

    def create_user(self, id_: int, username: str, firstname: str, lastname: str):
        try:
            self.executer("INSERT INTO users (id, username, first_name, last_name)\
                          VLAUES ({id_}, {username}, {firstname}, {lastname})")
        except Error as err:
            logger.error(err)
        else:
            logger.success(f"Create user by id : {id_}")

    def get_first_user(self, user: str):
        try:
            self.executer("SELECT * FROM users WHERE status = 'active' limit 1")
        except Error as err:
            logger.error(err)

    def update_status(self, id_: int, status: str):
        self.executer(f"UPDATE users SET status = '{status}' WHERE id = {id_}")

    def show_table(self, table: str):
        logger.debug(list(self.executer(f"SHOW COLUMNS FROM {table}")))

    def executer(self, db_command: str):
        with connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        ) as connection:
            with connection.cursor(buffered=True) as cursor:
                cursor.execute(db_command)
                return cursor


if __name__ == "__main__":
    import getpass
    username = input("Username : ")
    password = getpass.getpass()
    host = input('Host : ')
    database = input("Database : ")
    MyDB = BotDB(username, password)
    MyDB.show_table("users")
