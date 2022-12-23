import tkinter as tk
from tkinter import ttk


class TaxiRegisterPage:
    def __init__(self, root, control_panel_frame):
        self.root = root
        self.control_panel_frame = control_panel_frame
        self.create_taxi_register_frame()

    def create_taxi_register_frame(self):
        self.taxi_register_frame = tk.Toplevel(self.root)
        self.taxi_register_frame.title("Taxi Register")
        self.taxi_register_frame.configure(background="#FFFFFF")
        self.taxi_register_frame.resizable(0, 0)
        self.taxi_register_frame.geometry("460x440+420+91")
        self.build_taxi_register_frame(
            taxi_register_frame=self.taxi_register_frame,
        )

    @staticmethod
    def build_taxi_register_frame(taxi_register_frame):

        welcome = tk.Label(taxi_register_frame)
        welcome.place(relx=0.340, rely=0.069, height=41, width=200)
        welcome.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            text="""Taxi Register""",
            font="-family {Noto Sans} -size 16 -weight bold",
        )

        brand_label = tk.Label(taxi_register_frame)
        brand_label.place(relx=0.065, rely=0.19, height=41, width=104)
        brand_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            font="-family {Noto Sans} -size 14",
            compound="left",
            background="#FFFFFF",
            text="""Brand""",
        )

        brand_entry = tk.Entry(taxi_register_frame)
        brand_entry.place(
            relx=0.065,
            rely=0.29,
            height=25,
            relwidth=0.404,
        )
        brand_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
        )

        model_user = tk.Label(taxi_register_frame)
        model_user.place(relx=0.543, rely=0.19, height=41, width=104)
        model_user.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="""Model""",
        )

        model_entry = tk.Entry(taxi_register_frame)
        model_entry.place(
            relx=0.543,
            rely=0.29,
            height=25,
            relwidth=0.404,
        )
        model_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
        )

        taxi_number_label = tk.Label(taxi_register_frame)
        taxi_number_label.place(relx=0.065, rely=0.370, height=41, width=170)
        taxi_number_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            compound="left",
            background="#FFFFFF",
            font="-family {Noto Sans} -size 14",
            text="""Taxi Number""",
        )

        taxi_number_entry = tk.Entry(taxi_register_frame)
        taxi_number_entry.place(
            relx=0.065,
            rely=0.470,
            height=25,
            relwidth=0.404,
        )
        taxi_number_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
        )

        taxi_age_label = tk.Label(taxi_register_frame)
        taxi_age_label.place(relx=0.543, rely=0.370, height=41, width=104)
        taxi_age_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="""Age""",
        )

        taxi_age_entry = tk.Entry(taxi_register_frame)
        taxi_age_entry.place(
            relx=0.543,
            rely=0.470,
            height=25,
            relwidth=0.404,
        )
        taxi_age_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
        )

        discription_label = tk.Label(taxi_register_frame)
        discription_label.place(relx=0.065, rely=0.550, height=41, width=300)
        discription_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="Discription",
        )

        discription_entry = tk.Text(taxi_register_frame)
        discription_entry.place(
            relx=0.065,
            rely=0.650,
            height=60,
            relwidth=0.883,
        )
        discription_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
        )

        register_taxi_button = tk.Button(taxi_register_frame)
        register_taxi_button.place(relx=0.522, rely=0.850, height=35, width=95)
        register_taxi_button.configure(
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#FFFFFF",
            text="""Register""",
        )

        cancel_button = tk.Button(taxi_register_frame)
        cancel_button.place(relx=0.250, rely=0.850, height=35, width=95)
        cancel_button.configure(
            activebackground="beige",
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#FFFFFF",
            text="""Cancel""",
        )

        taxi_register_frame.grab_set()
        taxi_register_frame.mainloop()
