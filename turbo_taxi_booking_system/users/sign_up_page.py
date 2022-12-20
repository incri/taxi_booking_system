import tkinter as tk
from tkinter import messagebox

from pydantic import ValidationError
from helper.constants import BG_LOCATION
from .user_model import UserModel
from .user_controllers import UserController
from helper.exceptions import CustomException


class SignUpPage:
    def __init__(self, root):
        self.root = root
        self.create_signup_frame()

    def create_signup_frame(self):
        self.signup_frame = tk.Frame(self.root)
        self.signup_frame.configure(background="#FFFFFF")
        self.signup_frame.place(relx=-0.07, rely=0, height=768, width=1366)
        self.build_signup_frame(signup_frame=self.signup_frame)

    @staticmethod
    def build_signup_frame(signup_frame):

        welcome = tk.Label(signup_frame)
        welcome.place(relx=0.593, rely=0.090, height=60, width=323)
        welcome.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            text="""Welcome To Turbo TB""",
            font="-family {Noto Sans} -size 22 -weight bold",
        )

        quoest = tk.Label(signup_frame)
        quoest.place(relx=0.644, rely=0.160, height=20, width=205)
        quoest.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14 -slant italic",
            text="""Travel For Your Heart""",
        )

        firstname_label = tk.Label(signup_frame)
        firstname_label.place(relx=0.538, rely=0.231, height=20, width=135)
        firstname_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            font="-family {Noto Sans} -size 16",
            compound="left",
            background="#FFFFFF",
            text="""First Name""",
        )

        firstname_entry = tk.Entry(signup_frame)
        firstname_entry.place(relx=0.538, rely=0.27, height=33, relwidth=0.189)
        firstname_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
        )

        lastname_label = tk.Label(signup_frame)
        lastname_label.place(relx=0.773, rely=0.231, height=20, width=135)
        lastname_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 16",
            text="""Last Name""",
        )

        lastname_entry = tk.Entry(signup_frame)
        lastname_entry.place(relx=0.773, rely=0.27, height=33, relwidth=0.189)
        lastname_entry.configure(
            background="#EFF0F2", font="TkFixedFont", selectbackground="#c4c4c4"
        )

        contact_label = tk.Label(signup_frame)
        contact_label.place(relx=0.538, rely=0.338, height=21, width=135)
        contact_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            compound="left",
            background="#FFFFFF",
            font="-family {Noto Sans} -size 16",
            text="""Contact""",
        )

        contact_entry = tk.Entry(signup_frame)
        contact_entry.place(relx=0.538, rely=0.379, height=33, relwidth=0.189)
        contact_entry.configure(
            background="#EFF0F2", font="TkFixedFont", selectbackground="#c4c4c4"
        )

        address_label = tk.Label(signup_frame)
        address_label.place(relx=0.773, rely=0.338, height=21, width=135)
        address_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 16",
            text="""Address""",
        )

        address_entry = tk.Entry(signup_frame)
        address_entry.place(relx=0.773, rely=0.379, height=33, relwidth=0.189)
        address_entry.configure(
            background="#EFF0F2", font="TkFixedFont", selectbackground="#c4c4c4"
        )

        email_label = tk.Label(signup_frame)
        email_label.place(relx=0.538, rely=0.446, height=20, width=185)
        email_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 16",
            text="""Email Address""",
        )

        email_entry = tk.Entry(signup_frame)
        email_entry.place(relx=0.538, rely=0.486, height=33, relwidth=0.419)
        email_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
        )

        username_label = tk.Label(signup_frame)
        username_label.place(relx=0.538, rely=0.554, height=31, width=135)
        username_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 16",
            text="""User Name""",
        )

        username_entry = tk.Entry(signup_frame)
        username_entry.place(relx=0.538, rely=0.608, height=33, relwidth=0.189)
        username_entry.configure(
            background="#EFF0F2", font="TkFixedFont", selectbackground="#c4c4c4"
        )

        password_label = tk.Label(signup_frame)
        password_label.place(relx=0.773, rely=0.554, height=21, width=135)
        password_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 16",
            text="""Password""",
        )

        password_entry = tk.Entry(signup_frame)
        password_entry.place(relx=0.773, rely=0.608, height=33, relwidth=0.189)
        password_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
            show="*",
        )

        confrim_password_label = tk.Label(signup_frame)
        confrim_password_label.place(relx=0.533, rely=0.678, height=20, width=205)
        confrim_password_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 16",
            text="""Confirm Password""",
        )

        confrim_password_entry = tk.Entry(signup_frame)
        confrim_password_entry.place(relx=0.538, rely=0.73, height=33, relwidth=0.189)
        confrim_password_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
            show="*",
        )

        show_pass_button = tk.Button(signup_frame)
        show_pass_button.place(relx=0.74, rely=0.735, height=23, width=51)
        show_pass_button.configure(
            activebackground="beige",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="""OO""",
        )
        show_pass_button.bind(
            "<Button-1>",
            lambda event: SignUpPage.show_pass(
                event,
                password_entry,
                confrim_password_entry,
            ),
        )

        show_pass_button.bind(
            "<ButtonRelease-1>",
            lambda event: SignUpPage.hide_pass(
                event,
                password_entry,
                confrim_password_entry,
            ),
        )

        signup_button = tk.Button(signup_frame)
        signup_button.place(relx=0.666, rely=0.855, height=43, width=201)
        signup_button.configure(
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 12 -weight bold",
            foreground="#FFFFFF",
            text="""Sign Up""",
            command=lambda: SignUpPage.user_register(
                firstname_entry,
                lastname_entry,
                contact_entry,
                address_entry,
                email_entry,
                username_entry,
                password_entry,
                confrim_password_entry,
                signup_frame,
            ),
        )

        background_label = tk.Label(signup_frame)
        background_label.place(relx=-0.029, rely=0.0, height=770, width=700)
        background_label.configure(anchor="w", compound="left")
        background_image = tk.PhotoImage(file=BG_LOCATION)
        background_label.configure(image=background_image)

        back_button = tk.Button(signup_frame)
        back_button.place(relx=0.100, rely=0.865, height=43, width=111)
        back_button.configure(
            activebackground="beige",
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#FFFFFF",
            text="""Back""",
            command=lambda: SignUpPage.redirect_to_homepage(signup_frame),
        )

        signup_frame.mainloop()

    @staticmethod
    def show_pass(
        event,
        password_entry,
        confrim_password_entry,
    ):
        password = password_entry.get()
        confrim_password = confrim_password_entry.get()
        password_entry.config(show="", text=password)
        confrim_password_entry.config(show="", text=confrim_password)

    @staticmethod
    def hide_pass(
        event,
        password_entry,
        confrim_password_entry,
    ):

        password_entry.config(show="*")
        confrim_password_entry.config(show="*")

    @staticmethod
    def redirect_to_homepage(signup_frame):
        signup_frame.destroy()

    @staticmethod
    def user_register(
        firstname_entry,
        lastname_entry,
        contact_entry,
        address_entry,
        email_entry,
        username_entry,
        password_entry,
        confrim_password_entry,
        signup_frame,
    ):
        try:
            user = UserModel(
                firstname=firstname_entry.get(),
                lastname=lastname_entry.get(),
                contact=contact_entry.get(),
                address=address_entry.get(),
                email=email_entry.get(),
                username=username_entry.get(),
                password=password_entry.get(),
                confirm_password=confrim_password_entry.get(),
            )
            user_control = UserController()
            user_control.registration_control(user, signup_frame)
        except CustomException as e:
            messagebox.showerror("Invalid Data", e)
