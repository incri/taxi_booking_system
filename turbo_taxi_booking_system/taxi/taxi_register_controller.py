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
                discription   VARCHAR(50) NOT NULL ,
                status  VARCHAR(40)
                
            );"""

            data_insert = """INSERT INTO taxi(brand, model, taxi_number, 
            taxi_age, discription,status) VALUES (%s, %s, %s, %s, %s, %s);
            """
            data_values = (
                taxi.brand,
                taxi.model,
                taxi.taxi_number,
                taxi.taxi_age,
                taxi.discription,
                "Available",
            )
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
            print(error)
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

    @staticmethod
    def taxi_number_fetcher(taxi_number_entry):
        _connection = Turbo_db.turbo_connection()
        try:
            cursor = _connection.cursor()
            statement = "SELECT taxi_number FROM taxi WHERE status='Available';"
            cursor.execute(statement)
            taxi_number = cursor.fetchall()
            taxi_number_entry["values"] = taxi_number
            taxi_number_entry.update()

        except Exception as error:
            print(error)
        finally:
            if cursor is not None:
                cursor.close()
            if _connection is not None:
                _connection.close()

    @staticmethod
    def taxi_data_fetcher(
        welcome,
        taxi_number_data,
        taxi_age_data,
        taxi_discription_data,
        selected_taxi_number,
    ):
        _connection = Turbo_db.turbo_connection()
        try:

            cursor = _connection.cursor()
            statement = "SELECT * FROM taxi WHERE taxi_number=%s;"
            data = (selected_taxi_number.get(),)

            cursor.execute(statement, data)
            taxi_data = cursor.fetchall()
            if taxi_data:
                for data in taxi_data:
                    fetched_car_brand = data[1]
                    fetched_car_model = data[2]
                    fetched_car_number = data[3]
                    fetched_car_age = data[4]
                    fetched_car_discription = data[5]
            else:
                return False

            welcome.config(text=fetched_car_brand + " " + fetched_car_model)
            taxi_number_data.config(text=fetched_car_number)
            taxi_age_data.config(text=fetched_car_age)
            taxi_discription_data.config(text=fetched_car_discription)
            welcome.update()
            taxi_number_data.update()
            taxi_number_data.update()
            taxi_discription_data.update()

        except Exception as error:
            print(error)
        finally:
            if cursor is not None:
                cursor.close()
            if _connection is not None:
                _connection.close()
