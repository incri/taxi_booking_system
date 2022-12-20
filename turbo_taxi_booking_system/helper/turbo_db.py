import psycopg2


class Turbo_db:
    message = ""

    @staticmethod
    def turbo_connection():
        try:
            conn = psycopg2.connect(
                host="localhost",
                dbname="turbo_db",
                user="incri",
                password="fastrack",
                port=5432,
            )
            return conn

        except Exception as error:
            Turbo_db.message = error
