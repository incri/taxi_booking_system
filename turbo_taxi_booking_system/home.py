import tkinter as tk
from tkinter import messagebox
from helper.constants import LOGO_LOCATION, BG_LOCATION
from users import sign_up_page
from users import log_in_page
from users import dashboard_page


class HomePage:
    def __init__(self):

        self.root = tk.Tk()
        self.build_root()
        self.create_home_frame()

    def build_root(self):
        self.root.title("Main Frame")
        self.root.resizable(0, 0)
        self.root.configure(background="#FFFFFF")
        self.root.attributes("-fullscreen", True)

    def create_home_frame(self):
        self.home_frame = tk.Frame(self.root)
        self.home_frame.configure(background="#FFFFFF")
        self.home_frame.place(relx=-0.07, rely=0, height=768, width=1366)
        self.build_home_frame(home_frame=self.home_frame, root=self.root)

    @staticmethod
    def build_home_frame(home_frame, root):

        top_title = tk.Label(home_frame)
        top_title.place(relx=0.17, rely=0.068, height=51, width=153)
        top_title.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 22",
            foreground="#3650D3",
            text="""Turbo TB""",
        )

        hp_sub_title_1 = tk.Label(home_frame)
        hp_sub_title_1.place(relx=0.104, rely=0.163, height=61, width=353)
        hp_sub_title_1.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 18 -weight bold",
            text="""Turbo Taxi Booking System""",
        )

        hp_sub_title_2 = tk.Label(home_frame)
        hp_sub_title_2.place(relx=0.348, rely=0.176, height=41, width=396)
        hp_sub_title_2.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 18 -weight bold",
            foreground="#3650D3",
            text="""Online Taxi Booking""",
        )

        hp_sub_title_3 = tk.Label(home_frame)
        hp_sub_title_3.place(relx=0.104, rely=0.244, height=40, width=597)
        hp_sub_title_3.configure(activebackground="#f9f9f9")
        hp_sub_title_3.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 18 -weight bold",
            foreground="#3650D3",
            text="""BEST TAXI SERVICE PROVIDER COMANY""",
        )

        top_logo_lable = tk.Label(home_frame)
        top_logo_lable.place(relx=0.110, rely=0.068, height=71, width=80)
        top_logo_lable.configure(
            anchor="w",
            compound="left",
            background="#FFFFFF",
        )
        logo_image = tk.PhotoImage(file=LOGO_LOCATION)
        top_logo_lable.configure(image=logo_image)

        sub_logo_label_1 = tk.Label(home_frame)
        sub_logo_label_1.place(relx=0.110, rely=0.407, height=71, width=80)
        sub_logo_label_1.configure(anchor="w", compound="left", background="#FFFFFF")
        sub_logo_label_1.configure(image=logo_image)

        info_level_1 = tk.Label(home_frame)
        info_level_1.place(relx=0.17, rely=0.393, height=39, width=153)
        info_level_1.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12 -weight bold",
            text="""Why Turbo TB ?""",
        )

        sub_info_level_1 = tk.Label(home_frame)
        sub_info_level_1.place(relx=0.17, rely=0.448, height=45, width=510)
        sub_info_level_1.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            foreground="#637381",
        )
        sub_info_level_1.configure(text="""some information""")

        sub_logo_label_2 = tk.Label(home_frame)
        sub_logo_label_2.place(relx=0.110, rely=0.583, height=71, width=80)
        sub_logo_label_2.configure(anchor="w", compound="left", background="#FFFFFF")
        sub_logo_label_2.configure(image=logo_image)

        info_level_2 = tk.Label(home_frame)
        info_level_2.place(relx=0.17, rely=0.57, height=39, width=153)
        info_level_2.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12 -weight bold",
            text="""Services""",
        )

        sub_info_level_2 = tk.Label(home_frame)
        sub_info_level_2.place(relx=0.17, rely=0.624, height=45, width=510)
        sub_info_level_2.configure(
            anchor="w",
            foreground="#637381",
            background="#FFFFFF",
            compound="left",
            text="some information",
        )

        homebg_lable = tk.Label(home_frame)
        homebg_lable.place(relx=0.538, rely=0.0, height=770, width=664)
        homebg_lable.configure(anchor="w", compound="left")
        background_image = tk.PhotoImage(file=BG_LOCATION)
        homebg_lable.configure(image=background_image)

        signup_redirect_button = tk.Button(home_frame)
        signup_redirect_button.place(relx=0.783, rely=0.054, height=43, width=111)
        signup_redirect_button.configure(
            activebackground="beige",
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#FFFFFF",
            text="""Sign Up""",
            command=lambda: HomePage.redirect_to_signup_page(root),
        )

        login_redirect_button = tk.Button(home_frame)
        login_redirect_button.place(relx=0.893, rely=0.054, height=43, width=111)
        login_redirect_button.configure(
            activebackground="beige",
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#FFFFFF",
            text="""Log In""",
            command=lambda: HomePage.redirect_to_login_page(root),
        )

        app_exit_button = tk.Button(home_frame)
        app_exit_button.place(relx=0.100, rely=0.865, height=43, width=111)
        app_exit_button.configure(
            activebackground="beige",
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#FFFFFF",
            text="""EXIT""",
            command=lambda: HomePage.app_exit(root),
        )

        home_frame.mainloop()

    @staticmethod
    def app_exit(root):
        response = messagebox.askquestion(
            title="Exit !", message="Do you really want to exit ?", icon="warning"
        )
        if response == "yes":
            root.destroy()

    @staticmethod
    def redirect_to_signup_page(root):
        sign_up_page.SignUpPage(root)

    @staticmethod
    def redirect_to_login_page(root):
        log_in_page.LogInPage(root)
