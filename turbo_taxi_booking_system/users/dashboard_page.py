import imp
import tkinter as tk
from helper.constants import LOGO_LOCATION
from PIL import Image, ImageTk
from io import BytesIO
from .profile_page import ProfilePage
from bookings.booking_form import BookingPage
from .user_model import UserModel


class DashboardPage:
    def __init__(self, root, record, user_controller):
        self.root = root
        self.record = record
        self.user_controller = user_controller
        self.create_dashboard_frame()

    def create_dashboard_frame(self):
        self.dashboard_frame = tk.Frame(self.root)
        self.dashboard_frame.configure(background="#FFFFFF")
        self.dashboard_frame.place(relx=-0.07, rely=0, height=768, width=1366)
        self.build_dashboard_frame(
            dashboard_frame=self.dashboard_frame,
            root=self.root,
            record=self.record,
            user_controller=self.user_controller,
        )

    @staticmethod
    def build_dashboard_frame(
        dashboard_frame,
        root,
        record,
        user_controller,
    ):

        title = tk.Label(dashboard_frame)
        title.place(relx=0.452, rely=0.285, height=40, width=212)
        title.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 18 -weight bold",
            foreground="#3056D3",
            text="""Your Trip History""",
        )

        profile_label = tk.Label(dashboard_frame)
        profile_label.place(relx=0.91, rely=0.068, height=61, width=70)
        profile_label.configure(
            anchor="w",
            compound="left",
            borderwidth=2,
            relief="solid",
        )

        for data in record:
            fetched_username = data[6].rstrip()
            fetched_profile_picture = data[8]

        profile_img = Image.open(BytesIO(fetched_profile_picture))
        small_img = profile_img.resize((70, 61))
        view_profile = ImageTk.PhotoImage(small_img)
        profile_label.configure(image=view_profile)

        logo_label = tk.Label(dashboard_frame)
        logo_label.place(relx=0.110, rely=0.068, height=71, width=80)
        logo_label.configure(
            anchor="w",
            compound="left",
            text="""Logo""",
            background="#FFFFFF",
        )
        photo_location = tk.PhotoImage(file=LOGO_LOCATION)
        logo_label.configure(image=photo_location)

        username_button = tk.Button(dashboard_frame)
        username_button.place(relx=0.799, rely=0.095, height=33, width=131)
        username_button.configure(
            background="#007074",
            borderwidth="2",
            compound="left",
            text=fetched_username,
            font="-family {Noto Sans} -size 12 -weight bold",
            foreground="#FFFFFF",
            command=lambda: DashboardPage.redirect_to_profile_page(
                root,
                dashboard_frame,
                record,
                user_controller,
            ),
        )

        tabel_label = tk.Label(dashboard_frame)
        tabel_label.place(relx=0.110, rely=0.407, height=229, width=1160)
        tabel_label.configure(anchor="w", compound="left", text="""Table""")

        book_now_button = tk.Button(dashboard_frame)
        book_now_button.place(relx=0.466, rely=0.814, height=43, width=171)
        book_now_button.configure(
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#FFFFFF",
            text="""Book Now""",
            command=lambda: DashboardPage.redirect_to_booking_form(
                root,
                dashboard_frame,
                record,
            ),
        )

        refresh_button = tk.Button(dashboard_frame)
        refresh_button.place(relx=0.799, rely=0.814, height=33, width=131)
        refresh_button.configure(
            background="#007074",
            borderwidth="2",
            compound="left",
            text="Refresh Page",
            font="-family {Noto Sans} -size 12 -weight bold",
            foreground="#FFFFFF",
            command=lambda: DashboardPage.refresh_page(
                user_controller,
                record,
                root,
                dashboard_frame,
            ),
        )

        dashboard_frame.mainloop()

    @staticmethod
    def redirect_to_profile_page(
        root,
        dashboard_frame,
        record,
        user_controller,
    ):
        ProfilePage(root, dashboard_frame, record, user_controller)

    @staticmethod
    def redirect_to_booking_form(
        root,
        dashboard_frame,
        record,
    ):
        BookingPage(
            root,
            dashboard_frame,
            record,
        )

    @staticmethod
    def refresh_page(user_controller, record, root, dashboard_frame):

        dashboard_frame.destroy()
        for data in record:
            fetched_username = data[6]
            fetched_password = data[7]

        user = UserModel(
            username=fetched_username,
            password=fetched_password,
            confirm_password=fetched_password,
        )
        user_control = user_controller()
        user_control.login_control(user, root)
