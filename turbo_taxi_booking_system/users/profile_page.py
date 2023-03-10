import tkinter as tk
from tkinter import NO, W, Scrollbar, messagebox, filedialog
from tkinter import ttk
from helper.constants import LOGO_LOCATION
from PIL import Image, ImageTk
from io import BytesIO
from .user_model import UserModel
from helper.exceptions import CustomException
from tkintermapview import TkinterMapView


class ProfilePage:
    def __init__(self, root, dashboard_frame, record, user_controller):
        self.root = root
        self.dashboard_frame = dashboard_frame
        self.record = record
        self.user_controller = user_controller
        self.create_profile_frame()

    def create_profile_frame(self):
        self.profile_frame = tk.Frame(self.root)
        self.profile_frame.configure(background="#FFFFFF")
        self.profile_frame.place(
            relx=-0.010,
            rely=0,
            height=768,
            width=1366,
        )
        self.build_profile_frame(
            profile_frame=self.profile_frame,
            root=self.root,
            dashboard_frame=self.dashboard_frame,
            record=self.record,
            user_controller=self.user_controller,
        )

    @staticmethod
    def build_profile_frame(
        profile_frame,
        root,
        dashboard_frame,
        record,
        user_controller,
    ):

        logo = tk.Label(profile_frame)
        logo.place(x=91, y=60, height=81, width=82)
        logo.configure(
            anchor="w",
            compound="left",
            text="""logo""",
            background="#FFFFFF",
        )

        photo_location = tk.PhotoImage(file=LOGO_LOCATION)
        logo.configure(image=photo_location)

        logout_button = tk.Button(profile_frame)
        logout_button.place(x=1159, y=60, height=43, width=111)
        logout_button.configure(
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#FFFFFF",
            text="""Log Out""",
            command=lambda: ProfilePage.log_out(
                profile_frame,
                dashboard_frame,
            ),
        )

        for data in record:
            featched_username = data[6].rstrip()
            fetched_email = data[5].rstrip()
            fetched_address = data[4].rstrip()
            fetched_contact = data[3].rstrip()
            fetched_profile = data[8]

        profile_img = Image.open(BytesIO(fetched_profile))
        big_img = profile_img.resize((153, 133))
        view_profile = ImageTk.PhotoImage(big_img)

        profile_photo = tk.Label(profile_frame)
        profile_photo.place(x=59, y=210, height=133, width=153)
        profile_photo.configure(
            anchor="w",
            compound="left",
            text="""profile""",
            borderwidth=2,
            relief="solid",
        )
        profile_photo.configure(image=view_profile)

        username = tk.Label(profile_frame)
        username.place(x=259, y=210, height=31, width=115)
        username.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 16 -weight bold",
            text=featched_username,
        )

        email = tk.Label(profile_frame)
        email.place(x=259, y=260, height=21, width=67)
        email.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            text="""Email :""",
        )

        contact = tk.Label(profile_frame)
        contact.place(x=259, y=290, height=20, width=95)
        contact.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            text="""Phone no :""",
        )

        address = tk.Label(profile_frame)
        address.place(x=259, y=320, height=20, width=87)
        address.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            text="""Address :""",
        )

        email_data = tk.Label(profile_frame)
        email_data.place(x=320, y=255, height=30, width=300)
        email_data.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            text=fetched_email,
        )

        contact_data = tk.Label(profile_frame)
        contact_data.place(x=359, y=290, height=20, width=95)
        contact_data.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            text=fetched_contact,
        )

        address_data = tk.Label(profile_frame)
        address_data.place(x=350, y=317, height=30, width=300)
        address_data.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            text=fetched_address,
        )

        edit_profile_picture = tk.Button(profile_frame)
        edit_profile_picture.place(x=59, y=380, height=23, width=91)
        edit_profile_picture.configure(
            background="#FFFFFF",
            borderwidth="2",
            compound="left",
            text="""Edit Profile >""",
            command=lambda: ProfilePage.edit_account_profile(
                user_controller,
                record,
                profile_frame,
                dashboard_frame,
            ),
        )

        edit_bio_button = tk.Button(profile_frame)
        edit_bio_button.place(x=259, y=380, height=23, width=101)
        edit_bio_button.configure(
            background="#FFFFFF",
            borderwidth="2",
            compound="left",
            text="""Edit Bio >""",
            command=lambda: ProfilePage.create_edit_bio_page(
                record,
                user_controller,
                profile_frame,
                dashboard_frame,
            ),
        )

        upcoming_trips = tk.Label(profile_frame)
        upcoming_trips.place(x=550, y=440, height=41, width=245)
        upcoming_trips.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 16",
            foreground="#3056D3",
            text="""Your Upcoming Trips""",
        )

        back_button = tk.Button(profile_frame)
        back_button.place(x=50, y=630, height=43, width=111)
        back_button.configure(
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#FFFFFF",
            text="""Back""",
            command=lambda: ProfilePage.redirect_to_dashboard(profile_frame),
        )

        ProfilePage.upcoming_trip_table_viwer(
            profile_frame,
            user_controller,
            record,
        )

        profile_frame.mainloop()

    @staticmethod
    def redirect_to_dashboard(profile_frame):
        profile_frame.destroy()

    @staticmethod
    def log_out(profile_frame, dashboard_frame):
        response = messagebox.askquestion(
            title="Log Out !",
            message="Do you really want to Log Out ?",
            icon="warning",
        )

        if response == "yes":
            profile_frame.destroy()
            dashboard_frame.destroy()

    @staticmethod
    def create_edit_bio_page(
        record,
        user_controller,
        profile_frame,
        dashboard_frame,
    ):
        edit_bio_frame = tk.Toplevel(profile_frame)
        edit_bio_frame.title("Edit Bio")
        edit_bio_frame.resizable(0, 0)
        edit_bio_frame.configure(background="#FFFFFF")
        edit_bio_frame.geometry("460x579+420+91")
        ProfilePage.build_edit_bio_page(
            edit_bio_frame,
            record,
            user_controller,
            profile_frame,
            dashboard_frame,
        )

    @staticmethod
    def build_edit_bio_page(
        edit_bio_frame,
        record,
        user_controller,
        profile_frame,
        dashboard_frame,
    ):

        welcome = tk.Label(edit_bio_frame)
        welcome.place(relx=0.413, rely=0.069, height=41, width=104)
        welcome.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            text="""Edit Bio""",
            font="-family {Noto Sans} -size 16 -weight bold",
        )

        for data in record:
            fetched_firstname = data[1].rstrip()
            fetched_lastname = data[2].rstrip()
            fetched_email = data[5].rstrip()

        firstname = tk.Label(edit_bio_frame)
        firstname.place(relx=0.065, rely=0.19, height=41, width=104)
        firstname.configure(
            activebackground="#f9f9f9",
            anchor="w",
            font="-family {Noto Sans} -size 14",
            compound="left",
            background="#FFFFFF",
            text="""First Name""",
        )

        firstname_entry = tk.Entry(edit_bio_frame)
        firstname_entry.insert(0, fetched_firstname)
        firstname_entry.place(
            relx=0.065,
            rely=0.259,
            height=23,
            relwidth=0.404,
        )
        firstname_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
            state="disabled",
        )

        lastname = tk.Label(edit_bio_frame)
        lastname.place(relx=0.543, rely=0.19, height=41, width=104)
        lastname.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="""Last Name""",
        )

        lastname_entry = tk.Entry(edit_bio_frame)
        lastname_entry.insert(0, fetched_lastname)
        lastname_entry.place(
            relx=0.543,
            rely=0.259,
            height=23,
            relwidth=0.404,
        )
        lastname_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
            state="disabled",
        )

        contact = tk.Label(edit_bio_frame)
        contact.place(relx=0.065, rely=0.311, height=41, width=104)
        contact.configure(
            activebackground="#f9f9f9",
            anchor="w",
            compound="left",
            background="#FFFFFF",
            font="-family {Noto Sans} -size 14",
            text="""Contact""",
        )

        contact_entry = tk.Entry(edit_bio_frame)
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

        address = tk.Label(edit_bio_frame)
        address.place(relx=0.543, rely=0.311, height=41, width=104)
        address.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="""Address""",
        )

        address_entry = tk.Entry(edit_bio_frame)
        address_entry.place(
            relx=0.543,
            rely=0.38,
            height=23,
            relwidth=0.404,
        )
        address_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
        )

        email = tk.Label(edit_bio_frame)
        email.place(relx=0.065, rely=0.432, height=41, width=300)
        email.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="""Email Address""",
        )

        email_entry = tk.Entry(edit_bio_frame)
        email_entry.insert(0, fetched_email)
        email_entry.place(
            relx=0.065,
            rely=0.501,
            height=23,
            relwidth=0.883,
        )
        email_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
            state="disabled",
        )

        username = tk.Label(edit_bio_frame)
        username.place(relx=0.065, rely=0.553, height=41, width=104)
        username.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="""User Name""",
        )

        username_entry = tk.Entry(edit_bio_frame)
        username_entry.place(
            relx=0.065,
            rely=0.622,
            height=23,
            relwidth=0.404,
        )
        username_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
        )

        password = tk.Label(edit_bio_frame)
        password.place(relx=0.543, rely=0.553, height=41, width=300)
        password.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="""Old Password""",
        )

        password_entry = tk.Entry(edit_bio_frame)
        password_entry.place(
            relx=0.543,
            rely=0.622,
            height=23,
            relwidth=0.404,
        )
        password_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
            show="*",
        )

        confirm_password = tk.Label(edit_bio_frame)
        confirm_password.place(
            relx=0.065,
            rely=0.674,
            height=41,
            width=300,
        )
        confirm_password.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="""New Password""",
        )

        confrim_password_entry = tk.Entry(edit_bio_frame)
        confrim_password_entry.place(
            relx=0.065,
            rely=0.76,
            height=23,
            relwidth=0.404,
        )
        confrim_password_entry.configure(
            background="#EFF0F2",
            font="TkFixedFont",
            selectbackground="#c4c4c4",
            show="*",
        )

        show_password = tk.Button(edit_bio_frame)
        show_password.place(
            relx=0.5,
            rely=0.757,
            height=23,
            width=51,
        )
        show_password.configure(
            activebackground="beige",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="""OO""",
        )
        show_password.bind(
            "<Button-1>",
            lambda event: ProfilePage.show_pass(
                event,
                password_entry,
                confrim_password_entry,
            ),
        )

        show_password.bind(
            "<ButtonRelease-1>",
            lambda event: ProfilePage.hide_pass(
                event,
                password_entry,
                confrim_password_entry,
            ),
        )

        update_button = tk.Button(edit_bio_frame)
        update_button.place(relx=0.522, rely=0.864, height=43, width=111)
        update_button.configure(
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 12 -weight bold",
            foreground="#FFFFFF",
            text="""Update""",
            command=lambda: ProfilePage.edit_user_bio(
                record,
                edit_bio_frame,
                profile_frame,
                dashboard_frame,
                user_controller,
                contact_entry,
                address_entry,
                username_entry,
                password_entry,
                confrim_password_entry,
            ),
        )

        delete_button = tk.Button(edit_bio_frame)
        delete_button.place(relx=0.690, rely=0.757, height=23, width=120)
        delete_button.configure(
            activebackground="beige",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 10",
            text="""Delete Account""",
            command=lambda: ProfilePage.delete_account(
                user_controller,
                profile_frame,
                dashboard_frame,
                edit_bio_frame,
                record,
            ),
        )

        cancel_button = tk.Button(edit_bio_frame)
        cancel_button.place(relx=0.250, rely=0.864, height=43, width=111)
        cancel_button.configure(
            activebackground="beige",
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#FFFFFF",
            text="""Cancel""",
            command=lambda: ProfilePage.cancel(edit_bio_frame),
        )

        edit_bio_frame.grab_set()
        edit_bio_frame.mainloop()

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
    def cancel(edit_bio_frame):
        edit_bio_frame.destroy()

    @staticmethod
    def delete_account(
        user_controller,
        profile_frame,
        dashboard_frame,
        edit_bio_frame,
        record,
    ):
        account_control = user_controller()
        response = messagebox.askquestion(
            "Delete Account",
            "Do you really want to delete your account? \n  \
            you wont be able to recover your account again",
        )
        if response == "yes":
            account_control.delete_account(
                profile_frame,
                dashboard_frame,
                edit_bio_frame,
                record,
            )

    @staticmethod
    def edit_account_profile(
        user_controller,
        record,
        profile_frame,
        dashboaard_frame,
    ):
        for data in record:
            fetched_password = data[7]

        file = filedialog.askopenfilename()
        if file:
            user = UserModel(
                profile=file,
                password=fetched_password,
                confirm_password=fetched_password,
            )
            profile_picture_control = user_controller()
            profile_picture_control.change_profile(
                user,
                record,
                profile_frame,
                dashboaard_frame,
            )

    @staticmethod
    def edit_user_bio(
        record,
        edit_bio_frame,
        profile_frame,
        dashboard_frame,
        user_controller,
        contact_entry,
        address_entry,
        username_entry,
        password_entry,
        confrim_password_entry,
    ):

        for data in record:
            fetched_contact = data[3]
            fetched_address = data[4]
            fetched_username = data[6]
            fetched_password = data[7]

        # checking if data is empty or not

        if contact_entry.get() == "":
            new_contact = fetched_contact
        else:
            new_contact = contact_entry.get()

        if address_entry.get() == "":
            new_address = fetched_address
        else:
            new_address = address_entry.get()
        if username_entry.get() == "":
            new_username = fetched_username
        else:
            new_username = username_entry.get()
        if confrim_password_entry.get() == "":
            new_password_update = fetched_password
        else:
            new_password_update = confrim_password_entry.get()
        if password_entry.get() == fetched_password:
            old_password = password_entry.get()
        else:
            old_password = password_entry.get()

        try:
            user = UserModel(
                contact=new_contact,
                address=new_address,
                username=new_username,
                password=old_password,
                confirm_password=old_password,
                new_password=new_password_update,
            )
            user_bio_control = user_controller()
            user_bio_control.update_user_bio(
                user,
                record,
                edit_bio_frame,
                profile_frame,
                dashboard_frame,
            )

        except CustomException as e:
            messagebox.showerror("Invalid Data", e, parent=edit_bio_frame)

    @staticmethod
    def upcoming_trip_table_viwer(profile_frame, user_controller, record):

        for data in record:
            userid = data[0]

        upcoming_trip_table = tk.Frame(profile_frame, bg="#FFFFFF")
        upcoming_trip_table.place(
            x=49,
            y=490,
            height=130,
            width=1212,
        )

        # Upcoming booking details table

        table_style = ttk.Style()
        table_style.theme_use("default")
        table_style.configure(
            "Treeview",
            background="#FFFFFF",
            foreground="#4A4A4A",
            rowheight="35",
            fieldbackground="#FFFFFF",
        )
        table_style.map("Treeview", background=[("selected", "#C9C9C9")])

        # driver Table Scroll Bar

        table_scroll_bar = Scrollbar(upcoming_trip_table)
        table_scroll_bar.place(relx=0.985, rely=0, height=130, width=15)

        # driver Table Build

        upcoming_booking_table = ttk.Treeview(
            upcoming_trip_table,
            yscrollcommand=table_scroll_bar.set,
            selectmode="extended",
        )
        upcoming_booking_table.place(
            relx=0,
            rely=0,
            height=280,
            width=1180,
        )
        # upcoming a scroll bar

        table_scroll_bar.config(
            command=upcoming_booking_table.yview,
        )

        upcoming_booking_table["columns"] = (
            "Booking ID",
            "Full Name",
            "Date and Time",
            "Destination",
            "Total Cost",
            "Status",
        )
        # Format Our Columns

        upcoming_booking_table.column("#0", width=0, stretch=NO)
        upcoming_booking_table.column("Booking ID", width=20, anchor=W)
        upcoming_booking_table.column("Full Name", width=70, anchor=W)
        upcoming_booking_table.column("Date and Time", width=70, anchor=W)
        upcoming_booking_table.column("Destination", width=240, anchor=W)
        upcoming_booking_table.column("Total Cost", width=40, anchor=W)
        upcoming_booking_table.column("Status", width=40, anchor=W)

        # Create Heading

        upcoming_booking_table.heading("#0", text="", anchor=W)
        upcoming_booking_table.heading("Booking ID", text="Booking ID", anchor=W)
        upcoming_booking_table.heading("Full Name", text="Full Name", anchor=W)
        upcoming_booking_table.heading("Date and Time", text="Date and Time", anchor=W)
        upcoming_booking_table.heading("Destination", text="Destination", anchor=W)
        upcoming_booking_table.heading("Total Cost", text="Total Cost", anchor=W)
        upcoming_booking_table.heading("Status", text="Status", anchor=W)

        upcoming_trip_control = user_controller()
        trip_fetched_data = upcoming_trip_control.upcoming_trip_detail_fetcher(userid)

        for data in trip_fetched_data:

            upcoming_booking_table.insert(
                "",
                index="end",
                values=(
                    data[0],
                    (data[2], data[3]),
                    (data[6], "---", data[7], ":", data[8]),
                    data[10],
                    data[11],
                    data[16],
                ),
            )

            upcoming_booking_table.bind(
                "<Double-1>",
                lambda event: ProfilePage.user_profile_booking_detail(
                    event,
                    upcoming_booking_table,
                    user_controller,
                ),
            )

    @staticmethod
    def user_profile_booking_detail(
        event,
        upcoming_booking_table,
        user_controller,
    ):

        selected = upcoming_booking_table.focus()
        selected_row = upcoming_booking_table.item(
            selected,
            "values",
        )
        selected_booking_id = selected_row[0]

        # Booking Details Data Fetcher

        booking_data_control = user_controller()
        fetched_booking_details = (
            booking_data_control.user_profile_booking_data_fetcher(
                selected_booking_id,
            )
        )

        data = fetched_booking_details[0]

        upcoming_booking_detail_frame = tk.Toplevel(upcoming_booking_table)
        upcoming_booking_detail_frame.title("Assign Taxi")
        upcoming_booking_detail_frame.geometry("682x641+193+31")
        upcoming_booking_detail_frame.resizable(0, 0)
        upcoming_booking_detail_frame.configure(background="#FFFFFF")

        # BUILDING BOOKING DETAIL PAGE

        title = tk.Label(upcoming_booking_detail_frame)
        title.place(relx=0.360, rely=0.031, height=43, width=250)
        title.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 18 -weight bold",
            text="""Booking Details""",
        )

        fullname_label = tk.Label(upcoming_booking_detail_frame)
        fullname_label.place(relx=0.029, rely=0.156, height=34, width=122)
        fullname_label.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            text="""Full Name :""",
        )

        fullname_data = tk.Label(upcoming_booking_detail_frame)
        fullname_data.place(relx=0.22, rely=0.156, height=34, width=280)
        fullname_data.configure(
            anchor="w",
            background="#FFFFFF",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            highlightthickness="2",
            text=data[2] + " " + data[3],
        )

        map_view_frame = tk.Frame(upcoming_booking_detail_frame)
        map_view_frame.place(relx=0.640, rely=0.156, height=140, width=220)
        map_view_frame.configure(
            background="#FFFFFF",
            borderwidth="2",
            highlightthickness="2",
        )

        location_detail_map_view = TkinterMapView(map_view_frame)
        location_detail_map_view.set_tile_server(
            "https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
            max_zoom=60,
        )

        pickup_cordinates = eval(data[19])
        destination_coordinates = eval(data[20])

        location_detail_map_view.set_marker(
            pickup_cordinates[0],
            pickup_cordinates[1],
        )

        location_detail_map_view.set_marker(
            destination_coordinates[0],
            destination_coordinates[1],
        )

        location_detail_map_view.set_position(
            pickup_cordinates[0],
            pickup_cordinates[1],
        )

        location_detail_map_view.set_path(
            position_list=[pickup_cordinates, destination_coordinates]
        )

        location_detail_map_view.pack()

        passenger_no_label = tk.Label(upcoming_booking_detail_frame)
        passenger_no_label.place(relx=0.029, rely=0.234, height=34, width=175)
        passenger_no_label.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            text="""No of Passenger :""",
        )

        passenger_no_data = tk.Label(upcoming_booking_detail_frame)
        passenger_no_data.place(relx=0.293, rely=0.234, height=34, width=48)
        passenger_no_data.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            highlightthickness="2",
            text=data[4],
        )

        booking_status = tk.Label(upcoming_booking_detail_frame)
        booking_status.place(relx=0.029, rely=0.312, height=35, width=180)
        booking_status.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            text="""Booking Status :""",
        )

        booking_status_data = tk.Label(upcoming_booking_detail_frame)
        booking_status_data.place(relx=0.250, rely=0.312, height=35, width=150)
        booking_status_data.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            highlightthickness="2",
            text=data[16],
        )

        pick_up_date_lable = tk.Label(upcoming_booking_detail_frame)
        pick_up_date_lable.place(relx=0.029, rely=0.39, height=34, width=133)
        pick_up_date_lable.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            text="""Pick Up Date :""",
        )

        pick_up_date_data = tk.Label(upcoming_booking_detail_frame)
        pick_up_date_data.place(relx=0.249, rely=0.39, height=35, width=163)
        pick_up_date_data.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            highlightthickness="2",
            text=data[6],
        )

        time_label = tk.Label(upcoming_booking_detail_frame)
        time_label.place(relx=0.513, rely=0.39, height=34, width=69)
        time_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            text="""Time :""",
        )

        data7 = str(data[7])
        data8 = str(data[8])
        time_data = tk.Label(upcoming_booking_detail_frame)
        time_data.place(relx=0.616, rely=0.39, height=34, width=100)
        time_data.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            highlightthickness="2",
            text=(data7 + ":" + data8),
        )

        pick_up_address_label = tk.Label(upcoming_booking_detail_frame)
        pick_up_address_label.place(relx=0.029, rely=0.468, height=35, width=175)
        pick_up_address_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            text="""Pick Up Address :""",
        )

        pickup_address_data = tk.Label(upcoming_booking_detail_frame)
        pickup_address_data.place(relx=0.293, rely=0.468, height=35, width=323)
        pickup_address_data.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 10",
            foreground="#4A4A4A",
            highlightthickness="2",
            text=data[9],
        )

        destination_label = tk.Label(upcoming_booking_detail_frame)
        destination_label.place(relx=0.029, rely=0.546, height=34, width=132)

        destination_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            text="""Destination :""",
        )

        destination_address_lable = tk.Label(upcoming_booking_detail_frame)
        destination_address_lable.place(relx=0.249, rely=0.546, height=34, width=323)
        destination_address_lable.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 10",
            foreground="#4A4A4A",
            highlightthickness="2",
            text=data[10],
        )

        total_cost_label = tk.Label(upcoming_booking_detail_frame)
        total_cost_label.place(relx=0.029, rely=0.624, height=34, width=111)
        total_cost_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            text="""Total Cost :""",
        )

        total_cost_data = tk.Label(upcoming_booking_detail_frame)
        total_cost_data.place(relx=0.22, rely=0.624, height=34, width=206)
        total_cost_data.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            highlightthickness="2",
            text=data[11] + " .NPR",
        )

        payment_method_lable = tk.Label(upcoming_booking_detail_frame)
        payment_method_lable.place(relx=0.029, rely=0.702, height=33, width=185)
        payment_method_lable.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            text="""Payment Method :""",
        )
        payment_method_data = tk.Label(upcoming_booking_detail_frame)
        payment_method_data.place(relx=0.293, rely=0.702, height=34, width=206)
        payment_method_data.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            highlightthickness="2",
            text=data[12],
        )

        driver_details_lable = tk.Label(upcoming_booking_detail_frame)
        driver_details_lable.place(relx=0.029, rely=0.780, height=33, width=185)
        driver_details_lable.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            text="""Driver Details :""",
        )
        driver_details_name = tk.Label(upcoming_booking_detail_frame)
        driver_details_name.place(relx=0.250, rely=0.780, height=34, width=206)
        driver_details_name.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            highlightthickness="2",
            text=data[23],
        )

        driver_details_number = tk.Label(upcoming_booking_detail_frame)
        driver_details_number.place(relx=0.600, rely=0.780, height=34, width=206)
        driver_details_number.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            highlightthickness="2",
            text=data[25],
        )

        taxi_details_lable = tk.Label(upcoming_booking_detail_frame)
        taxi_details_lable.place(relx=0.025, rely=0.858, height=33, width=185)
        taxi_details_lable.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            text="""Taxi Details :""",
        )

        data29 = str(data[31])
        data30 = str(data[32])

        if (data29) == "None":
            data29 = ""
        if (data30) == "None":
            data30 = ""

        taxi_details_name = tk.Label(upcoming_booking_detail_frame)
        taxi_details_name.place(relx=0.220, rely=0.858, height=34, width=465)
        taxi_details_name.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            highlightthickness="2",
            text=data29 + " " + data30,
        )

        taxi_details_number = tk.Label(upcoming_booking_detail_frame)
        taxi_details_number.place(relx=0.220, rely=0.936, height=34, width=206)
        taxi_details_number.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            highlightthickness="2",
            text=data[33],
        )

        back_button = tk.Button(upcoming_booking_detail_frame)
        back_button.place(relx=0.865, rely=0.031, height=33, width=71)
        back_button.configure(
            activebackground="beige",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 10",
            foreground="#FFFFFF",
            text="""Back""",
        )

        cancel_booking_button = tk.Button(upcoming_booking_detail_frame)
        cancel_booking_button.place(relx=0.580, rely=0.936, height=34, width=130)
        cancel_booking_button.configure(
            activebackground="beige",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 10 -weight bold",
            text="""Cancel Booking""",
            command=lambda: ProfilePage.user_cancel_booking(
                user_controller, upcoming_booking_detail_frame, data
            ),
        )

        if data[16] == "Accepted":
            cancel_booking_button.config(state="disable")

        upcoming_booking_detail_frame.wait_visibility()
        upcoming_booking_detail_frame.grab_set()
        upcoming_booking_detail_frame.mainloop()

    @staticmethod
    def user_cancel_booking(
        user_controller,
        upcoming_booking_detail_frame,
        data,
    ):

        booking_id = data[0]
        response = messagebox.askquestion(
            "Cancel Booking", "DO you really want to cancel this booking ?"
        )

        if response == "yes":
            user_booking_cancel_control = user_controller()
            user_booking_cancel_control.cancel_booking(booking_id)
            upcoming_booking_detail_frame.destroy()
