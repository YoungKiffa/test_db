import pytest
import sqlite3 as sq


class TestDataBase:

    @pytest.fixture
    def db_connection(self):
        conn = sq.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
        conn.commit()
        yield conn
        conn.close()

    def test_add(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES ('Klimas', 18)")
        db_connection.commit()
        cursor.execute("SELECT * FROM users WHERE name='Klimas'")
        result = cursor.fetchone()
        assert result is not None

    def test_change(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES ('Vladimir', 25)")
        db_connection.commit()
        cursor.execute("UPDATE users SET age=25 WHERE name='Vladimir'")
        db_connection.commit()
        cursor.execute("SELECT age FROM users WHERE name='Vladimir'")
        result = cursor.fetchone()
        assert result[0] == 25
