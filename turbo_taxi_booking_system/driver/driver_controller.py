from tkinter import messagebox
from helper.turbo_db import Turbo_db
from .driver_dashboard import DriverDashboard


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
                driver_status   VARCHAR(50) NOT NULL,
                username        VARCHAR(50) NOT NULL UNIQUE,
                password        VARCHAR(50) NOT NULL
                
            );"""

            data_insert = """INSERT INTO drivers(fullname, license_number,
            contact, taxi_number, driver_status, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
            data_values = (
                driver.fullname,
                driver.license_number,
                driver.contact,
                driver.taxi_number,
                "Available",
                driver.username,
                driver.password,
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

    def driver_login_control(self, driver, login_frame, root):
        if self.login_authenticate(driver):
            self.login_sucess(root, login_frame)
        else:
            messagebox.showerror(
                "Invalid Data",
                "username or password not matched",
            )

    def login_authenticate(self, admin):
        try:
            cursor = self._connection.cursor()
            statement = "SELECT * FROM drivers WHERE username=%s AND password = %s;"
            data = (admin.username, admin.password)
            cursor.execute(statement, data)
            self.record = cursor.fetchall()
            if self.record:
                return True
            return False
        except Exception as error:
            print(error)

    def login_sucess(self, root, login_page):
        messagebox.showinfo(title="Congratulation", message="Welcome ")
        login_page.destroy()
        DriverDashboard(root, DriverController, self.record)

    def upcoming_trip_detail_fetcher(self, driver_id):
        try:
            cursor = self._connection.cursor()
            statement = "SELECT * FROM booking as b LEFT JOIN drivers as d on b.driver_id = d.driverid LEFT JOIN taxi as t on d.taxi_number = t.taxi_number WHERE d.driverid = %s AND b.booking_status = 'Accepted';"
            did = str(driver_id)
            data = did
            cursor.execute(statement, data)
            self.record = cursor.fetchall()
            return self.record
        except Exception as error:
            print(error)

    def completed_trip_detail_fetcher(self, driver_id):
        try:
            cursor = self._connection.cursor()
            statement = "SELECT * FROM booking as b LEFT JOIN drivers as d on b.driver_id = d.driverid LEFT JOIN taxi as t on d.taxi_number = t.taxi_number WHERE d.driverid = %s AND b.booking_status = 'Completed';"
            did = str(driver_id)
            data = did
            cursor.execute(statement, data)
            self.record = cursor.fetchall()
            return self.record
        except Exception as error:
            print(error)

    def completed_trip_controller(self, booking_id, driver_id):

        try:
            cursor = self._connection.cursor()
            booking_statement = (
                "Update booking set booking_status = 'Completed' Where booking_id = %s;"
            )
            bid = str(booking_id)
            did = str(driver_id)
            booking_data = bid
            cursor.execute(booking_statement, booking_data)

            driver_statement = (
                "Update drivers set driver_status = 'Available' Where driverid = %s;"
            )
            driver_data = did
            cursor.execute(driver_statement, driver_data)

            self._connection.commit()
        except Exception as error:
            print(error)

    def driver_booking_data_fetcher(self, driver_id):
        try:
            cursor = self._connection.cursor()
            statement = "select sum(CAST(total_cost AS decimal)) from booking as b join drivers as d on b.driver_id = d.driverid where b.booking_status = 'Completed' AND d.driverid = %s; "
            did = str(driver_id)
            data = did
            cursor.execute(statement, data)
            self.record = cursor.fetchall()
            return self.record
        except Exception as error:
            print(error)

    def driver_profile_data_fetcher(self, driver_id):
        try:
            cursor = self._connection.cursor()
            statement = "select *  from drivers as d join taxi as t on d.taxi_number = t.taxi_number where d.driverid = %s;"
            did = str(driver_id)
            data = did
            cursor.execute(statement, data)
            self.record = cursor.fetchall()
            return self.record
        except Exception as error:
            print(error)

    def driver_monthly_data_fetcher(self, driver_id, today):
        try:
            cursor = self._connection.cursor()
            statement = "SELECT sum(CAST(total_cost AS decimal)) as gross_incrome, sum(CAST(total_cost AS decimal)/3) as service_cost, sum(CAST(total_cost AS decimal)-CAST(total_cost AS decimal)/3) as net_income from booking as b join drivers as d on b.driver_id = d.driverid where b.booking_status = 'Completed' AND d.driverid = %s AND CAST(b.pickup_date AS VARCHAR(50)) like concat('%%',%s,'%%');"
            did = str(driver_id)
            td = str(today)
            data = (did, td)

            cursor.execute(statement, data)
            self.record = cursor.fetchall()
            return self.record
        except Exception as error:
            print(error)
