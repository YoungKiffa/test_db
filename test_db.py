import pytest
import sqlite3 as sq


class TestDataBase:

    @pytest.fixture
    def db_connection(self):
        conn = sq.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, surname TEXT, age INTEGER)''')
        conn.commit()
        yield conn
        conn.close()

    def test_add(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO users (name, surname, age) VALUES ('Klimas', 'Sas', 18)")
        db_connection.commit()
        cursor.execute("SELECT * FROM users WHERE surname='Sas'")
        result = cursor.fetchone()
        assert result is not None

    def test_change(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO users (name, surname, age) VALUES ('Klimentiy', 'Dolmatov', 30)")
        db_connection.commit()
        cursor.execute("UPDATE users SET age=18, surname='Flikov' WHERE name='Klimentiy'")
        db_connection.commit()
        cursor.execute("SELECT age, surname FROM users WHERE name='Klimentiy'")
        result = cursor.fetchone()
        assert result[0] == 18

    def test_view(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        assert users == []
