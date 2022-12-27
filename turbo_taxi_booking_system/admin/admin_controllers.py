from tkinter import messagebox
from helper.turbo_db import Turbo_db
from .control_panel import ControlPanelPage


class AdminController:
    def __init__(self) -> None:
        self._connection = Turbo_db.turbo_connection()

    def admin_login_control(self, admin, login_frame, root):
        if self.login_authenticate(admin):
            self.login_sucess(root, login_frame)
        else:
            messagebox.showerror(
                "Invalid Data",
                "username or password not matched",
            )

    def login_authenticate(self, admin):
        try:
            cursor = self._connection.cursor()
            statement = "SELECT * FROM admin WHERE username=%s AND password = %s;"
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
        ControlPanelPage(root, login_page, AdminController)

    def customer_data_fetcher(self):

        try:
            cursor = self._connection.cursor()
            statement = "SELECT u.userid, b.booking_id, b.created_at_date, CONCAT(u.firstname,' ',u.lastname) as fullname, u.contact, u.address, u.email, b.booking_status from users as u JOIN booking as b on u.userid = b.user_id order by b.created_at_date, b.created_at_time;"
            cursor.execute(statement)
            self.record = cursor.fetchall()
            selected = 1
            return self.record, selected
        except Exception as error:
            print(error)

    def customer_search_fetcher(self, search_entry, selected_sort_by):

        if selected_sort_by.get() == "Date":
            statement = "SELECT u.userid, b.booking_id, b.created_at_date, CONCAT(u.firstname,' ',u.lastname) as fullname, u.contact, u.address, u.email, b.booking_status from users as u JOIN booking as b on u.userid = b.user_id where concat(u.firstname , ' ' , u.lastname) like concat('%%',%s,'%%')  order by b.created_at_date, b.created_at_time;"
            selected = "1"
        else:
            if selected_sort_by.get() == "Full Name":
                statement = "SELECT u.userid, b.booking_id, b.created_at_date, CONCAT(u.firstname,' ',u.lastname) as fullname, u.contact, u.address, u.email, b.booking_status from users as u JOIN booking as b on u.userid = b.user_id where concat(u.firstname , ' ' , u.lastname) like concat('%%',%s,'%%')  order by u.firstname;"
                selected = "2"
            else:
                if selected_sort_by.get() == "User ID":
                    statement = "SELECT u.userid, b.booking_id, b.created_at_date, CONCAT(u.firstname,' ',u.lastname) as fullname, u.contact, u.address, u.email, b.booking_status from users as u JOIN booking as b on u.userid = b.user_id where concat(u.firstname , ' ' , u.lastname) like concat('%%',%s,'%%')  order by b.created_at_date, u.userid;"
                    selected = "4"

                else:
                    if selected_sort_by.get() == "Booking ID":
                        statement = "SELECT u.userid, b.booking_id, b.created_at_date, CONCAT(u.firstname,' ',u.lastname) as fullname, u.contact, u.address, u.email, b.booking_status from users as u JOIN booking as b on u.userid = b.user_id where concat(u.firstname , ' ' , u.lastname) like concat('%%',%s,'%%')  order by b.booking_id;"
                        selected = "3"
                    else:
                        if selected_sort_by.get() == "":
                            statement = "SELECT u.userid, b.booking_id, b.created_at_date, CONCAT(u.firstname,' ',u.lastname) as fullname, u.contact, u.address, u.email, b.booking_status from users as u JOIN booking as b on u.userid = b.user_id where concat(u.firstname , ' ' , u.lastname) like concat('%%',%s,'%%')  order by b.created_at_date, b.created_at_time;"
                            selected = "1"

        try:
            cursor = self._connection.cursor()
            data = (search_entry.get(),)
            cursor.execute(statement, data)
            self.record = cursor.fetchall()
            return self.record, selected
        except Exception as error:
            print(error)
