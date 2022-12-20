from tkinter import messagebox
from helper.exceptions import CustomException
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
                messagebox.showerror("Invalid Data", "username already exist!!")
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

    def login_control(self, user, login_frame, root):
        if not self.login_authenticate(user):
            messagebox.showerror("Invalid Data", "Bad Data !!")
        self.login_sucess(root, login_frame)

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

    def login_sucess(self, root, login_page):
        messagebox.showinfo(
            title="Congratulation",
            message="Welcome " + self.fetched_firstname + " " + self.fetched_lastname,
        )
        login_page.destroy(),
        DashboardPage(
            root,
            self.record,
        ),

    def delete_account():
        pass
