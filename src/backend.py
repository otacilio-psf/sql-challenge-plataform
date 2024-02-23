import pandas as pd
import sqlite3

class ChallengeDB():
    invalid_query_exception = pd.errors.DatabaseError

    def __init__(self):
        self.conn = sqlite3.connect('data/chinook.db')

    def retrive_results(self, query):
        return pd.read_sql_query(query, self.conn)

    def retrive_solution(self, challenge_number):
        query = f"SELECT * FROM solution_{challenge_number}"
        return pd.read_sql_query(query, self.conn)

class BackendDB():

    def __init__(self):
        pass
