from tkinter import messagebox
from helper.turbo_db import Turbo_db
import psycopg2
from .dashboard_page import DashboardPage


class UserController:
    def __init__(self) -> None:
        self._connection = Turbo_db.turbo_connection()

    def registration_control(self, user, signup_frame):
        if self.authenticate(user):
            self.registration_sucess(signup_frame)

    def authenticate(self, user):
        try:
            cursor = self._connection.cursor()
            statement = """CREATE TABLE IF NOT EXISTS users(
                userID  SERIAL PRIMARY KEY,
                firstname   VARCHAR(50) NOT NULL,
                lastname    VARCHAR(50) NOT NULL,
                contact VARCHAR(20) NOT NULL,
                address VARCHAR(50) NOT NULL,
                email   VARCHAR(50) NOT NULL UNIQUE,
                username    VARCHAR(20) NOT NULL UNIQUE,
                password    VARCHAR(20) NOT NULL,
                profile BYTEA
            );"""

            defult_image = open(
                "/home/vivu/Class Stuff V2/ISD_Files/TurboTB_System/img/profile.png",
                "rb",
            ).read()

            data_insert = """INSERT INTO users(firstname, lastname, contact, 
            address, email, username, password, profile) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """
            data_values = (
                user.firstname,
                user.lastname,
                user.contact,
                user.address,
                user.email,
                user.username,
                user.password,
                psycopg2.Binary(defult_image),
            )
            cursor.execute(statement)
            cursor.execute(data_insert, data_values)
            self._connection.commit()
            return True
        except Exception as error:
            if "username" in str(error):
                messagebox.showerror(
                    "Invalid Data",
                    "username already exist!!",
                )
            elif "email" in str(error):
                messagebox.showerror(
                    "Invalid Data",
                    "Already have account linked \
                    to this account.",
                )
            else:
                print(error)
        finally:
            if cursor is not None:
                cursor.close()
            if self._connection is not None:
                self._connection.close()

    def registration_sucess(self, signup_frame):
        messagebox.showinfo(
            "Account Created",
            "Congatulation, Your Accunt Has Been Created",
        )
        signup_frame.destroy()

    def login_control(self, user, root):
        if self.login_authenticate(user):
            self.login_sucess(root)
        else:
            messagebox.showerror("Invalid Data", "username or password not matched")

    def login_authenticate(self, user):
        cursor = self._connection.cursor()
        statement = "SELECT * FROM users WHERE username=%s AND password = %s;"
        data = (user.username, user.password)
        cursor.execute(statement, data)
        self.record = cursor.fetchall()
        if self.record:
            for data in self.record:
                self.fetch_user_id = data[0]
                self.fetched_firstname = data[1].rstrip()
                self.fetched_lastname = data[2].rstrip()
                self.fetch_username = data[6]
                self.fetch_password = data[7].rstrip()
                self.fetched_profile = data[8]
            return True
        return False

    def login_sucess(self, root):
        DashboardPage(
            root,
            self.record,
            UserController,
        ),

    def delete_account(
        self,
        profile_frame,
        dashboard_frame,
        edit_bio_frame,
        record,
    ):
        for data in record:
            fetched_username = data[6]
        try:

            cursor = self._connection.cursor()
            statement = """DELETE FROM users WHERE username = %s;"""
            data_values = (fetched_username,)
            cursor.execute(statement, data_values)
            self._connection.commit()

            messagebox.showinfo(
                "Sucess!!",
                "Account Sucessfully deleted !",
            )

            edit_bio_frame.destroy()
            profile_frame.destroy()
            dashboard_frame.destroy()

        except Exception as e:
            print(e)
        finally:
            if cursor is not None:
                cursor.close()
            if self._connection is not None:
                self._connection.close()

    def change_profile(
        self,
        user,
        record,
        profile_frame,
        dashboard_frame,
    ):

        for data in record:
            fetched_firstname = data[6]
        try:
            image_path = user.profile
            new_profile = open(image_path, "rb").read()
            cursor = self._connection.cursor()
            statement = """UPDATE users
            SET profile = %s WHERE username = %s;"""
            dataValues = (
                psycopg2.Binary(new_profile),
                fetched_firstname,
            )

            cursor.execute(statement, dataValues)
            self._connection.commit()

            messagebox.showinfo(
                "Sucess!!",
                "Profile Picture Changed !",
            )

            # profile_frame.destroy()
            # dashboard_frame.destroy()

        except Exception as e:
            print(e)
        finally:
            if cursor is not None:
                cursor.close()
            if self._connection is not None:
                self._connection.close()

    def update_user_bio(
        self,
        user,
        record,
        edit_bio_frame,
        profile_frame,
        dashboard_frame,
    ):
        for data in record:
            fetched_username = data[6]
        try:
            cursor = self._connection.cursor()
            statement = """UPDATE users
            SET contact = COALESCE(NULLIF(%s,''),contact),
            address = COALESCE(NULLIF(%s,''),address),
            username = COALESCE(NULLIF(%s,''),username),
            password = COALESCE(NULLIF(%s,''),password)
            WHERE username = %s;"""

            dataValues = (
                user.contact,
                user.address,
                user.username,
                user.new_password,
                fetched_username,
            )

            cursor.execute(statement, dataValues)
            self._connection.commit()

            messagebox.showinfo(
                "Sucess!!",
                "Updated !",
            )

            edit_bio_frame.destroy()

        except Exception as error:
            if "username" in str(error):
                messagebox.showerror(
                    "Invalid Data",
                    "username already exist!!",
                    parent=edit_bio_frame,
                )
            else:
                print(error)
        finally:
            if cursor is not None:
                cursor.close()
            if self._connection is not None:
                self._connection.close()

    def upcoming_trip_detail_fetcher(self, user_id):

        try:
            cursor = self._connection.cursor()
            statement = "SELECT * FROM booking as b JOIN drivers as d on b.driver_id = d.driverid JOIN taxi as t on d.taxi_number = t.taxi_number WHERE user_id = %s AND b.booking_status = 'Pending' OR b.booking_status = 'Accepted';"
            uid = str(user_id)
            data = uid
            cursor.execute(statement, data)
            self.record = cursor.fetchall()
            return self.record
        except Exception as error:
            print(error)
