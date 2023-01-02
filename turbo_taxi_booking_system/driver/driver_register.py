import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from helper.exceptions import CustomException
from taxi.taxi_register_controller import TaxiController
from .driver_model import DriverModel
from .driver_controller import DriverController


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

        welcome = tk.Label(driver_register_frame)
        welcome.place(relx=0.313, rely=0.060, height=41, width=250)
        welcome.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            text="""Driver Register""",
            font="-family {Noto Sans} -size 16 -weight bold",
        )

        fullname = tk.Label(driver_register_frame)
        fullname.place(relx=0.065, rely=0.19, height=41, width=104)
        fullname.configure(
            activebackground="#f9f9f9",
            anchor="w",
            font="-family {Noto Sans} -size 14",
            compound="left",
            background="#FFFFFF",
            text="""Full Name""",
        )

        fullname_entry = tk.Entry(driver_register_frame)
        fullname_entry.place(
            relx=0.065,
            rely=0.259,
            height=23,
            relwidth=0.404,
        )
        fullname_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
        )

        license_label = tk.Label(driver_register_frame)
        license_label.place(relx=0.543, rely=0.19, height=41, width=200)
        license_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="""License Number""",
        )

        license_entry = tk.Entry(driver_register_frame)
        license_entry.place(
            relx=0.543,
            rely=0.259,
            height=23,
            relwidth=0.404,
        )
        license_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
        )

        contact = tk.Label(driver_register_frame)
        contact.place(relx=0.065, rely=0.311, height=41, width=104)
        contact.configure(
            activebackground="#f9f9f9",
            anchor="w",
            compound="left",
            background="#FFFFFF",
            font="-family {Noto Sans} -size 14",
            text="""Contact""",
        )

        contact_entry = tk.Entry(driver_register_frame)
        contact_entry.place(
            relx=0.065,
            rely=0.38,
            height=23,
            relwidth=0.404,
        )
        contact_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
        )

        taxi_number_label = tk.Label(driver_register_frame)
        taxi_number_label.place(
            relx=0.543,
            rely=0.311,
            height=41,
            width=200,
        )
        taxi_number_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="""Taxi Number""",
        )

        selected_taxi_number = tk.StringVar()

        taxi_number_entry = ttk.Combobox(
            driver_register_frame,
            textvariable=selected_taxi_number,
            state="readonly",
            values=("taxi_number"),
        )
        taxi_number_entry.place(
            relx=0.543,
            rely=0.38,
            height=23,
            relwidth=0.404,
        )
        taxi_number_entry.bind(
            "<<ComboboxSelected>>",
            lambda event: DriverRegisterPage.taxi_number_fetcher(
                event,
                driver_register_frame,
                taxi_number_entry,
                selected_taxi_number,
            ),
        )

        username = tk.Label(driver_register_frame)
        username.place(relx=0.065, rely=0.430, height=41, width=104)
        username.configure(
            activebackground="#f9f9f9",
            anchor="w",
            compound="left",
            background="#FFFFFF",
            font="-family {Noto Sans} -size 14",
            text="""username""",
        )

        username_entry = tk.Entry(driver_register_frame)
        username_entry.place(
            relx=0.065,
            rely=0.500,
            height=23,
            relwidth=0.404,
        )
        username_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
        )

        password = tk.Label(driver_register_frame)
        password.place(relx=0.543, rely=0.430, height=41, width=104)
        password.configure(
            activebackground="#f9f9f9",
            anchor="w",
            compound="left",
            background="#FFFFFF",
            font="-family {Noto Sans} -size 14",
            text="""password""",
        )

        password_entry = tk.Entry(driver_register_frame)
        password_entry.place(
            relx=0.543,
            rely=0.500,
            height=23,
            relwidth=0.404,
            show="*",
        )
        password_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
        )

        update_button = tk.Button(driver_register_frame)
        update_button.place(relx=0.522, rely=0.864, height=43, width=111)
        update_button.configure(
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 12 -weight bold",
            foreground="#FFFFFF",
            text="""Register""",
            command=lambda: DriverRegisterPage.driver_registration(
                driver_register_frame,
                fullname_entry,
                license_entry,
                contact_entry,
                selected_taxi_number,
                username_entry,
                password_entry,
            ),
        )

        cancel_button = tk.Button(driver_register_frame)
        cancel_button.place(relx=0.250, rely=0.864, height=43, width=111)
        cancel_button.configure(
            activebackground="beige",
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#FFFFFF",
            text="""Cancel""",
            command=lambda: DriverRegisterPage.cancel_button(
                driver_register_frame,
            ),
        )
        driver_register_frame.grab_set()
        driver_register_frame.mainloop()

    @staticmethod
    def taxi_number_fetcher(
        event,
        driver_register_frame,
        taxi_number_entry,
        selected_taxi_number,
    ):
        TaxiController.taxi_number_fetcher(taxi_number_entry)

        DriverRegisterPage.taxi_detail_viewer(
            driver_register_frame,
            selected_taxi_number,
        )

    @staticmethod
    def taxi_detail_viewer(
        driver_register_frame,
        selected_taxi_number,
    ):
        driver_register_frame = tk.Frame(driver_register_frame)
        driver_register_frame.place(
            relx=0.065,
            rely=0.570,
            height=150,
            relwidth=0.883,
        )
        driver_register_frame.config(
            background="#FFFFFF",
            borderwidth=2,
            relief="solid",
            highlightbackground="#000000",
        )

        welcome = tk.Label(driver_register_frame)
        welcome.place(relx=0.065, rely=0.10, height=41, width=365)
        welcome.configure(
            background="#FFFFFF",
            compound="left",
            text="""Driver Register""",
            font="-family {Noto Sans} -size 14 -weight bold",
            anchor="center",
        )

        taxi_number = tk.Label(driver_register_frame)
        taxi_number.place(relx=0.065, rely=0.35, height=41, width=110)
        taxi_number.configure(
            activebackground="#f9f9f9",
            anchor="w",
            font="-family {Noto Sans} -size 12",
            compound="left",
            background="#FFFFFF",
            text="""Taxi Number :""",
        )

        taxi_number_data = tk.Label(driver_register_frame)
        taxi_number_data.place(relx=0.360, rely=0.35, height=41, width=110)
        taxi_number_data.configure(
            activebackground="#f9f9f9",
            anchor="w",
            font="-family {Noto Sans} -size 12",
            compound="left",
            background="#FFFFFF",
        )

        taxi_age = tk.Label(driver_register_frame)
        taxi_age.place(relx=0.680, rely=0.35, height=41, width=75)
        taxi_age.configure(
            activebackground="#f9f9f9",
            anchor="w",
            font="-family {Noto Sans} -size 12",
            compound="left",
            background="#FFFFFF",
            text="""Taxi Age :""",
        )

        taxi_age_data = tk.Label(driver_register_frame)
        taxi_age_data.place(relx=0.880, rely=0.35, height=41, width=40)
        taxi_age_data.configure(
            activebackground="#f9f9f9",
            anchor="w",
            font="-family {Noto Sans} -size 12",
            compound="left",
            background="#FFFFFF",
        )

        taxi_discription = tk.Label(driver_register_frame)
        taxi_discription.place(relx=0.065, rely=0.65, height=41, width=100)
        taxi_discription.configure(
            activebackground="#f9f9f9",
            anchor="w",
            font="-family {Noto Sans} -size 12",
            compound="left",
            background="#FFFFFF",
            text="""Discription :""",
        )
        taxi_discription_data = tk.Label(driver_register_frame)
        taxi_discription_data.place(relx=0.360, rely=0.70, height=41, width=250)
        taxi_discription_data.configure(
            activebackground="#f9f9f9",
            anchor="w",
            font="-family {Noto Sans} -size 12",
            compound="left",
            background="#FFFFFF",
        )

        DriverRegisterPage.taxi_data_fetcher(
            welcome,
            taxi_number_data,
            taxi_age_data,
            taxi_discription_data,
            selected_taxi_number,
        )

    @staticmethod
    def taxi_data_fetcher(
        welcome,
        taxi_number_data,
        taxi_age_data,
        taxi_discription_data,
        selected_taxi_number,
    ):
        TaxiController.taxi_data_fetcher(
            welcome,
            taxi_number_data,
            taxi_age_data,
            taxi_discription_data,
            selected_taxi_number,
        )

    @staticmethod
    def cancel_button(driver_register_frame):
        driver_register_frame.destroy()

    @staticmethod
    def driver_registration(
        driver_register_frame,
        fullname_entry,
        license_entry,
        contact_entry,
        selected_taxi_number,
        username_entry,
        password_entry,
    ):
        try:
            driver = DriverModel(
                fullname=fullname_entry.get(),
                license_number=license_entry.get(),
                contact=contact_entry.get(),
                taxi_number=selected_taxi_number.get(),
                username=username_entry.get(),
                password=password_entry.get(),
            )

            driver_control = DriverController()
            driver_control.driver_registration_control(
                driver,
                driver_register_frame,
            )

        except CustomException as error:
            messagebox.showerror("invalid", error, parent=driver_register_frame)
