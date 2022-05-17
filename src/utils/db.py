"""
database handy functions
"""


import logging


from loguru import logger
from mysql.connector import connect, Error


from src.utils.connect import DBConnect



logging.basicConfig()
class BotDB:
    def __init__(self):
        self.db_obj = DBConnect()

    def create_db(self, db_name: str):
        with self.db_obj as (connection, crs):
            crs.execute(f"CREATE DATABASE {db_name}")
            logging.info(f"{db_name} is created")

    def show_tables(self):
        with self.db_obj as (connection, crs):
            crs.execute("SHOW TABLES")
            print(" - ".join(crs.fetchall()))


    def create_users_table(self):
        with self.db_obj as (connection, crs):
            crs.execute(
                "CREATE TABLE users (\
                id INT NOT NULL, \
                username VARCHAR(100), \
                firstname VARCHAR(100), \
                lastname VARCHAR(100), \
                status VARCHAR(20) NOT NULL DEFAULT 'disconnect', \
                PRIMARY KEY(id)\
                )"
            )
            # TODO: Add custum Error
            logging.info("user table is created")

    def create_user(self, id_: int, username: str, firstname: str, lastname: str):
        with self.db_obj as (connection, crs):
            crs.execute("INSERT INTO users (id, username, first_name, last_name)\
                          VLAUES ({id_}, {username}, {firstname}, {lastname})")

    def get_first_user(self, user: str):
        with self.db_obj as (connection, crs):
            crs.execute("SELECT * FROM users WHERE status = 'active' limit 1")

    def update_status(self, id_: int, status: str):
        with self.db_obj as (connection, crs):
            crs.execute(f"UPDATE users SET status = '{status}' WHERE id = {id_}")

    def show_table(self, table: str):
        with self.db_obj as (connection, crs):
            crs.execute(f"SHOW COLUMNS FROM {table}")
            print(crs.fethall())


if __name__ == "__main__":
    MyDB = BotDB()
    MyDB.show_tables()
