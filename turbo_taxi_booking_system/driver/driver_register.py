import tkinter as tk
from tkinter import ttk


class DriverRegisterPage:
    def __init__(self, root, control_panel_frame):
        self.root = root
        self.control_panel_frame = control_panel_frame
        self.create_driver_register_frame()

    def create_driver_register_frame(self):
        self.driver_register_frame = tk.Toplevel(self.root)
        self.driver_register_frame.title("Driver Register")
        self.driver_register_frame.configure(background="#FFFFFF")
        self.driver_register_frame.resizable(0, 0)
        self.driver_register_frame.geometry("460x579+420+91")
        self.build_driver_register_frame(
            driver_register_frame=self.driver_register_frame,
        )

    @staticmethod
    def build_driver_register_frame(driver_register_frame):

        driver_register_frame.grab_set()
        driver_register_frame.mainloop()
