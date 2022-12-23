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
        cursor = self._connection.cursor()
        statement = "SELECT * FROM admin WHERE username=%s AND password = %s;"
        data = (admin.username, admin.password)
        cursor.execute(statement, data)
        self.record = cursor.fetchall()
        if self.record:
            return True
        return False

    def login_sucess(self, root, login_page):
        messagebox.showinfo(title="Congratulation", message="Welcome ")
        login_page.destroy()
        ControlPanelPage(root, login_page)