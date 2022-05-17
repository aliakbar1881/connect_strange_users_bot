"""
context manager to connect database
"""


import logging


from mysql.connector import connect, Error
import getpass


logging.basicConfig(level=logging.DEBUG, format='%(name)s - (levelname)s - %(message)s')

class DBConnect:
    def __init__(self):
        self.username = input("Username : ")
        logging.debug(f"username is : {self.username}")
        self.password = getpass.getpass()
        self.host = input('Host : ')
        logging.debug(f"Host is : {self.host}")
        self.database = input("Database : ")
        logging.debug(f"database is : {self.database}")

    def __enter__(self):
        try:
            self.connection =  connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
            )
            crs = self.connection.cursor(buffered=True)
            return (self.connection, crs)
        except Error as db_err:
            logging.error(db_err)
            self.__enter__()
        else:
            logging.debug("__enter__ have been run . . .")


    def __exit__(self, *agrs):
        try:
            self.connection.commit()
            del self.connection
        except AttributeError as attr_err:
            logging.error(attr_err)
        else:
            logging.debug("__exit__: exit from wth statement")



if __name__ == "__main__":
    my_connection = DBConnect()
    with my_connection as (connection, crs):
        crs.execute("SHOW DATABASES")
        print(crs.fetchall())
