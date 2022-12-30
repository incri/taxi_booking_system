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
            statement = "SELECT u.userid, b.booking_id, b.created_at_date, CONCAT(u.firstname,' ',u.lastname) as fullname, u.contact, u.address, u.email, b.booking_status from users as u JOIN booking as b on u.userid = b.user_id where b.booking_status = 'Pending' order by b.created_at_date, b.created_at_time;"
            cursor.execute(statement)
            self.record = cursor.fetchall()
            return self.record
        except Exception as error:
            print(error)

    def customer_search_fetcher(self, search_entry, selected_sort_by):

        if selected_sort_by.get() == "Pending":
            statement = "SELECT u.userid, b.booking_id, b.created_at_date, CONCAT(u.firstname,' ',u.lastname) as fullname, u.contact, u.address, u.email, b.booking_status from users as u JOIN booking as b on u.userid = b.user_id where concat(u.firstname , ' ' , u.lastname) like concat('%%',%s,'%%') and b.booking_status = 'Pending' order by b.created_at_date, b.created_at_time;"
        else:
            if selected_sort_by.get() == "Accepted":
                statement = "SELECT u.userid, b.booking_id, b.created_at_date, CONCAT(u.firstname,' ',u.lastname) as fullname, u.contact, u.address, u.email, b.booking_status from users as u JOIN booking as b on u.userid = b.user_id where concat(u.firstname , ' ' , u.lastname) like concat('%%',%s,'%%') and b.booking_status = 'Accepted' order by b.created_at_date, b.created_at_time;"

            else:
                if selected_sort_by.get() == "Canceled":
                    statement = "SELECT u.userid, b.booking_id, b.created_at_date, CONCAT(u.firstname,' ',u.lastname) as fullname, u.contact, u.address, u.email, b.booking_status from users as u JOIN booking as b on u.userid = b.user_id where concat(u.firstname , ' ' , u.lastname) like concat('%%',%s,'%%') and b.booking_status = 'Canceled' order by b.created_at_date, b.created_at_time;"

                else:
                    if selected_sort_by.get() == "All":
                        statement = "SELECT u.userid, b.booking_id, b.created_at_date, CONCAT(u.firstname,' ',u.lastname) as fullname, u.contact, u.address, u.email, b.booking_status from users as u JOIN booking as b on u.userid = b.user_id where concat(u.firstname , ' ' , u.lastname) like concat('%%',%s,'%%') order by b.created_at_date, b.created_at_time;"

        try:
            cursor = self._connection.cursor()
            data = (search_entry.get(),)
            cursor.execute(statement, data)
            self.record = cursor.fetchall()
            return self.record
        except Exception as error:
            print(error)

    def driver_data_fetcher(self):

        try:
            cursor = self._connection.cursor()
            statement = "SELECT * FROM drivers;"
            cursor.execute(statement)
            self.record = cursor.fetchall()
            return self.record
        except Exception as error:
            print(error)

    def driver_search_fetcher(self, search_entry, selected_sort_by):

        if selected_sort_by.get() == "Driver ID":
            statement = "SELECT * FROM drivers WHERE fullname like concat('%%',%s,'%%') ORDER BY driverid;"
        else:
            if selected_sort_by.get() == "Full Name":
                statement = "SELECT * FROM drivers WHERE fullname like concat('%%',%s,'%%') ORDER BY fullname;"
            else:
                if selected_sort_by.get() == "Available":
                    statement = "SELECT * FROM drivers WHERE fullname like concat('%%',%s,'%%') and driver_status = 'Available' ORDER BY driverid;"
                else:
                    if selected_sort_by.get() == "Booked":
                        statement = "SELECT * FROM drivers WHERE fullname like concat('%%',%s,'%%') and driver_status = 'Booked' ORDER BY driverid;"
                    else:
                        return
        try:
            cursor = self._connection.cursor()
            data = (search_entry.get(),)
            cursor.execute(statement, data)
            self.record = cursor.fetchall()
            return self.record
        except Exception as error:
            print(error)

    def booking_details_data_fetcher(self, selected_booking_id):

        try:
            statement = "SELECT * FROM booking WHERE booking_id = %s"
            cursor = self._connection.cursor()
            data = selected_booking_id
            cursor.execute(statement, data)
            self.record = cursor.fetchall()
            return self.record
        except Exception as error:
            print(error)

    def cancel_booking(self, booking_id):
        try:
            statement = "UPDATE booking SET booking_status = 'Canceled' WHERE booking_id = %s AND booking_status = 'Pending';"

            b_id = str(booking_id)
            cursor = self._connection.cursor()
            data = b_id
            cursor.execute(statement, data)
            self._connection.commit()

        except Exception as error:
            print(error)

    def available_driver_fetcher(self):
        try:
            statement = "SELECT * FROM drivers WHERE driver_status = 'Available'"
            cursor = self._connection.cursor()
            cursor.execute(statement)
            self.record = cursor.fetchall()
            return self.record
        except Exception as error:
            print(error)
