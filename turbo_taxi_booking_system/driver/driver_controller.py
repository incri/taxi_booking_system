from tkinter import messagebox
from helper.turbo_db import Turbo_db


class DriverController:
    def __init__(self) -> None:
        self._connection = Turbo_db.turbo_connection()

    def driver_registration_control(
        self,
        driver,
        driver_register_frame,
    ):
        if self.authenticate(driver):
            self.registration_sucess(driver_register_frame)

    def authenticate(self, driver):
        try:
            cursor = self._connection.cursor()
            statement = """CREATE TABLE IF NOT EXISTS drivers(
                driverID  SERIAL PRIMARY KEY,
                fullname   VARCHAR(50) NOT NULL,
                license_number    VARCHAR(50) NOT NULL UNIQUE,
                contact VARCHAR(20) NOT NULL,
                taxi_number VARCHAR(50) NOT NULL,
                driver_status   VARCHAR(50) NOT NULL
                
            );"""

            data_insert = """INSERT INTO drivers(fullname, license_number,
            contact, taxi_number, driver_status) VALUES (%s, %s, %s, %s, %s);
            """
            data_values = (
                driver.fullname,
                driver.license_number,
                driver.contact,
                driver.taxi_number,
                "Available",
            )

            cursor.execute(statement)
            cursor.execute(data_insert, data_values)

            taxi_statement = (
                """UPDATE taxi SET status = 'Assigned' WHERE taxi_number = %s;"""
            )
            data_taxi = (driver.taxi_number,)

            cursor.execute(taxi_statement, data_taxi)
            self._connection.commit()

            return True

        except Exception as e:
            print(e)
        finally:
            if cursor is not None:
                cursor.close()
            if self._connection is not None:
                self._connection.close()

    def registration_sucess(self, driver_register_frame):
        driver_register_frame.destroy()
