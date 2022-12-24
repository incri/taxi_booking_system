from tkinter import messagebox
from helper.turbo_db import Turbo_db


class TaxiController:
    def __init__(self) -> None:
        self._connection = Turbo_db.turbo_connection()

    def taxi_registration_control(self, taxi, taxi_register_frame):
        if self.authenticate(taxi, taxi_register_frame):
            self.registration_sucess(taxi_register_frame)

    def authenticate(self, taxi, taxi_register_frame):
        try:
            cursor = self._connection.cursor()
            statement = """CREATE TABLE IF NOT EXISTS taxi(
                taxiID  SERIAL PRIMARY KEY,
                brand   VARCHAR(50) NOT NULL,
                model    VARCHAR(50) NOT NULL,
                taxi_number VARCHAR(20) NOT NULL UNIQUE,
                taxi_age VARCHAR(50) NOT NULL,
                discription   VARCHAR(50) NOT NULL
                
            );"""

            data_insert = """INSERT INTO taxi(brand, model, taxi_number, 
            taxi_age, discription) VALUES (%s, %s, %s, %s, %s);
            """
            data_values = (
                taxi.brand,
                taxi.model,
                taxi.taxi_number,
                taxi.taxi_age,
                taxi.discription,
            )
            print(taxi.taxi_age)
            cursor.execute(statement)
            cursor.execute(data_insert, data_values)
            self._connection.commit()
            return True

        except Exception as error:
            messagebox.showerror(
                "Invalid",
                "taxi number already exits",
                parent=taxi_register_frame,
            )
        finally:
            if cursor is not None:
                cursor.close()
            if self._connection is not None:
                self._connection.close()

    def registration_sucess(self, taxi_register_frame):
        messagebox.showinfo(
            "sucess",
            "taxi register",
            parent=taxi_register_frame,
        )
