import tkinter as tk
from tkinter import ttk
from taxi.taxi_register import TaxiRegisterPage


class ControlPanelPage:
    def __init__(self, root, login_frame):
        self.root = root
        self.login_frame = login_frame
        self.create_control_panel_frame()

    def create_control_panel_frame(self):
        self.control_panel_frame = tk.Frame(self.root)
        self.control_panel_frame.configure(background="#FFFFFF")
        self.control_panel_frame.place(relx=-0.07, rely=0, height=768, width=1366)
        self.build_control_panel_frame(self.root, self.control_panel_frame)

    @staticmethod
    def build_control_panel_frame(root, control_panel_frame):
        title = tk.Label(control_panel_frame)
        title.place(relx=0.450, rely=0.025, height=71, width=224)
        title.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 22 -weight bold",
            text="""Control Panel""",
        )

        line_seperator = ttk.Separator(control_panel_frame)
        line_seperator.place(relx=0.130, rely=0.123, relwidth=0.800)

        register_button = tk.Button(control_panel_frame)
        register_button.place(relx=0.850, rely=0.130, height=33, width=101)
        register_button.configure(
            activebackground="beige",
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 9 -weight bold",
            foreground="#FFFFFF",
            text="""Register""",
            command=lambda: TaxiRegisterPage(
                root,
                control_panel_frame,
            ),
        )
