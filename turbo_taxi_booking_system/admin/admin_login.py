import tkinter as tk
from admin.admin_controllers import AdminController
from helper.constants import BG_LOCATION
from .admin_model import AdminModel


class LogInPage:
    def __init__(self):
        self.root = tk.Tk()
        self.build_root()
        self.create_login_frame()

    def build_root(self):
        self.root.title("Main Frame")
        self.root.resizable(0, 0)
        self.root.configure(background="#FFFFFF")
        self.root.attributes("-fullscreen", True)

    def create_login_frame(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.configure(background="#FFFFFF")
        self.login_frame.place(relx=-0.07, rely=0, height=768, width=1366)
        self.build_login_frame(login_frame=self.login_frame, root=self.root)

    @staticmethod
    def build_login_frame(login_frame, root):

        welcome = tk.Label(login_frame)
        welcome.place(relx=0.650, rely=0.149, height=59, width=200)
        welcome.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 22 -weight bold",
            text="""Admin Log In""",
        )

        username_label = tk.Label(login_frame)
        username_label.place(relx=0.585, rely=0.299, height=21, width=206)
        username_label.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 16",
            text="""Username""",
        )

        username_entry = tk.Entry(login_frame)
        username_entry.place(relx=0.585, rely=0.353, height=33, relwidth=0.301)
        username_entry.configure(
            background="#EFF0F2", font="TkFixedFont", selectbackground="#c4c4c4"
        )

        password_label = tk.Label(login_frame)
        password_label.place(relx=0.585, rely=0.434, height=20, width=185)
        password_label.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 16",
            text="""Password""",
        )

        password_entry = tk.Entry(login_frame)
        password_entry.place(relx=0.585, rely=0.488, height=33, relwidth=0.301)
        password_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
            show="*",
        )

        login_button = tk.Button(login_frame)
        login_button.place(relx=0.674, rely=0.611, height=43, width=201)
        login_button.configure(
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 12 -weight bold",
            foreground="#FFFFFF",
            text="""Log In""",
            command=lambda: LogInPage.admin_login(
                username_entry,
                password_entry,
                login_frame,
                root,
            ),
        )

        background_label = tk.Label(login_frame)
        background_label.place(relx=-0.029, rely=0.0, height=739, width=700)
        background_label.configure(anchor="w", compound="left")
        background_image = tk.PhotoImage(file=BG_LOCATION)
        background_label.configure(image=background_image)

        exit_button = tk.Button(login_frame)
        exit_button.place(relx=0.100, rely=0.865, height=43, width=111)
        exit_button.configure(
            activebackground="beige",
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#FFFFFF",
            text="""Exit""",
            command=lambda: LogInPage.exit_application(root),
        )

        show_pass_button = tk.Button(login_frame)
        show_pass_button.place(relx=0.900, rely=0.500, height=23, width=51)
        show_pass_button.configure(
            activebackground="beige",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="""OO""",
        )

        show_pass_button.bind(
            "<Button-1>",
            lambda event: LogInPage.show_pass(
                event,
                password_entry,
            ),
        )

        show_pass_button.bind(
            "<ButtonRelease-1>",
            lambda event: LogInPage.hide_pass(
                event,
                password_entry,
            ),
        )

        login_frame.mainloop()

    @staticmethod
    def show_pass(
        event,
        password_entry,
    ):
        password = password_entry.get()
        password_entry.config(show="", text=password)

    @staticmethod
    def hide_pass(
        event,
        password_entry,
    ):
        password_entry.config(show="*")

    def exit_application(root):
        root.destroy()

    @staticmethod
    def admin_login(
        username_entry,
        password_entry,
        login_frame,
        root,
    ):
        admin = AdminModel(
            username=username_entry.get(),
            password=password_entry.get(),
        )
        user_control = AdminController()
        user_control.admin_login_control(admin, login_frame, root)
