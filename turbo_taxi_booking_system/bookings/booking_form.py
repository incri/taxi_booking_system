from datetime import date, timedelta

from helper.exceptions import CustomException
from .booking_model import BookingModel
from .booking_controllers import BookingController
import math
from tkcalendar import DateEntry
from tkinter import StringVar, messagebox
from tkintermapview import TkinterMapView, convert_coordinates_to_address
import haversine as hs


import tkinter as tk


class BookingPage:
    def __init__(self, root, dashboard_frame, record) -> None:
        self.root = root
        self.dashboard_frame = dashboard_frame
        self.record = record
        self.create_booking_form_frame()

    def create_booking_form_frame(self):
        self.booking_form_frame = tk.Frame(self.root)
        self.booking_form_frame.configure(background="#FFFFFF")
        self.booking_form_frame.place(
            relx=-0.010,
            rely=0,
            height=768,
            width=1366,
        )
        self.build_booking_form_frame(
            dashboard_frame=self.dashboard_frame,
            record=self.record,
            booking_form_frame=self.booking_form_frame,
        )

    pickup_location_coordinates = None
    destination_coordinates = None
    button_name = None

    @staticmethod
    def build_booking_form_frame(
        dashboard_frame,
        record,
        booking_form_frame,
    ):
        title_label = tk.Label(booking_form_frame)
        title_label.place(relx=0.052, rely=0.042, height=59, width=143)
        title_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 18 -weight bold",
            text="""Book Now""",
        )

        message_label = tk.Message(booking_form_frame)
        message_label.place(relx=0.052, rely=0.122, relheight=0.067, relwidth=0.671)
        message_label.configure(
            anchor="w",
            background="#FFFFFF",
            foreground="#637381",
            padx="1",
            pady="1",
            text="""some information""",
            width=907,
        )

        for data in record:
            fetched_firstname = data[1].rstrip()
            fetched_lastname = data[2].rstrip()
            fetched_user_id = data[0]

        fullname = tk.Label(booking_form_frame)
        fullname.place(relx=0.044, rely=0.312, height=31, width=93)
        fullname.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            text="""Full Name :""",
        )

        firstname_entry = tk.Entry(booking_form_frame)
        firstname_entry.place(relx=0.126, rely=0.312, height=33, relwidth=0.173)
        firstname_entry.configure(
            background="#EFF0F2", font="TkFixedFont", selectbackground="#c4c4c4"
        )
        firstname_entry.insert(0, fetched_firstname)

        lastname_entry = tk.Entry(booking_form_frame)
        lastname_entry.place(relx=0.318, rely=0.312, height=33, relwidth=0.173)
        lastname_entry.configure(
            background="#EFF0F2", selectbackground="#c4c4c4", font="TkFixedFont"
        )
        lastname_entry.insert(0, fetched_lastname)

        firstname = tk.Label(booking_form_frame)
        firstname.place(relx=0.126, rely=0.366, height=20, width=93)
        firstname.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            foreground="#637381",
            text="""First Name""",
        )

        lastname = tk.Label(booking_form_frame)
        lastname.place(relx=0.318, rely=0.366, height=20, width=93)
        lastname.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            foreground="#637381",
            text="""Last Name""",
        )

        no_of_passenger = tk.Label(booking_form_frame)
        no_of_passenger.place(relx=0.044, rely=0.421, height=31, width=205)
        no_of_passenger.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            text="""Number Of Passenger :""",
        )

        no_of_passenger_entry = tk.Spinbox(
            booking_form_frame, from_=1.0, to=4.0, state="readonly"
        )
        no_of_passenger_entry.place(
            relx=0.192, rely=0.421, relheight=0.038, relwidth=0.079
        )
        no_of_passenger_entry.configure(
            background="#EFF0F2",
            font="TkDefaultFont",
            highlightbackground="black",
            selectbackground="#c4c4c4",
        )

        no_of_taxi_label = tk.Label(booking_form_frame)
        no_of_taxi_label.place(relx=0.044, rely=0.488, height=31, width=175)
        no_of_taxi_label.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            text="""Number Of Taxi :""",
        )

        no_of_taxi_entry = tk.Spinbox(
            booking_form_frame, from_=1.0, to=2.0, state="disable"
        )
        no_of_taxi_entry.place(relx=0.192, rely=0.488, relheight=0.038, relwidth=0.079)
        no_of_taxi_entry.configure(
            activebackground="#f9f9f9",
            background="#EFF0F2",
            font="TkDefaultFont",
            highlightbackground="black",
            selectbackground="#c4c4c4",
        )

        taxi_message = tk.Message(booking_form_frame)
        taxi_message.place(relx=0.281, rely=0.501, relheight=0.028, relwidth=0.152)
        taxi_message.configure(
            anchor="w",
            background="#FFFFFF",
            foreground="#637381",
            padx="1",
            pady="1",
            text="""a taxi can carry only upto 4 people""",
            width=205,
        )

        pickup_date = tk.Label(booking_form_frame)
        pickup_date.place(relx=0.044, rely=0.556, height=30, width=134)
        pickup_date.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            text="""Pick Up Date :""",
        )

        today_date = date.today()
        last_date = date.today() + timedelta(days=5)

        date_entry = DateEntry(
            booking_form_frame,
            selectmode="day",
            mindate=today_date,
            maxdate=last_date,
            state="readonly",
        )
        date_entry.place(relx=0.185, rely=0.556, height=33, relwidth=0.092)

        date_label = tk.Label(booking_form_frame)
        date_label.place(relx=0.185, rely=0.612, height=20, width=93)
        date_label.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            foreground="#637381",
            text="""MM/DD/YY""",
        )

        hour_entry = tk.Spinbox(booking_form_frame, from_=0.0, to=23.0)
        hour_entry.place(relx=0.285, rely=0.556, relheight=0.038, relwidth=0.079)
        hour_entry.configure(
            activebackground="#f9f9f9",
            background="#EFF0F2",
            font="TkDefaultFont",
            highlightbackground="black",
            selectbackground="#c4c4c4",
        )

        minute_entry = tk.Spinbox(booking_form_frame, from_=0.0, to=55.0, increment=5.0)
        minute_entry.place(relx=0.370, rely=0.556, relheight=0.038, relwidth=0.079)
        minute_entry.configure(
            activebackground="#f9f9f9",
            background="#EFF0F2",
            font="TkDefaultFont",
            highlightbackground="black",
            selectbackground="#c4c4c4",
        )

        time_label = tk.Label(booking_form_frame)
        time_label.place(relx=0.320, rely=0.612, height=20, width=93)
        time_label.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            foreground="#637381",
            text="""HH(24hrs) : MM""",
        )

        pickup_address = tk.Label(booking_form_frame)
        pickup_address.place(relx=0.044, rely=0.651, height=31, width=134)
        pickup_address.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            text="""Pick Up Address :""",
        )

        pickup_address_entry = tk.Entry(booking_form_frame, state="readonly")
        pickup_address_entry.place(relx=0.185, rely=0.651, height=33, relwidth=0.265)
        pickup_address_entry.configure(
            background="#EFF0F2", font="TkFixedFont", selectbackground="#c4c4c4"
        )

        pickup_address_button = tk.Button(booking_form_frame)
        pickup_address_button.place(
            relx=0.47,
            rely=0.651,
            height=33,
            relwidth=0.122,
        )
        pickup_address_button.configure(
            activebackground="beige",
            borderwidth="1",
            compound="left",
            font="-family {Noto Sans} -size 12",
            text="""Select Address""",
        )

        pickup_address_button.bind(
            "<ButtonRelease-1>",
            lambda event: BookingPage.create_location_picker(
                event,
                booking_form_frame,
                pickup_address_entry,
            ),
        )

        pickup_address_button.bind("<Button-1>", BookingPage.button_name_finder)

        destination = tk.Label(booking_form_frame)
        destination.place(relx=0.044, rely=0.746, height=31, width=134)
        destination.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            text="""Destination :""",
        )

        destination_entry = tk.Entry(booking_form_frame, state="readonly")
        destination_entry.place(relx=0.185, rely=0.746, height=33, relwidth=0.265)
        destination_entry.configure(
            background="#EFF0F2", font="TkFixedFont", selectbackground="#c4c4c4"
        )

        destination_button = tk.Button(booking_form_frame)
        destination_button.place(relx=0.47, rely=0.746, height=33, relwidth=0.122)
        destination_button.configure(
            activebackground="beige",
            borderwidth="1",
            compound="left",
            font="-family {Noto Sans} -size 12",
            text="""Select Address""",
        )
        destination_button.bind(
            "<ButtonRelease-1>",
            lambda event: BookingPage.create_location_picker(
                event,
                booking_form_frame,
                destination_entry,
            ),
        )
        destination_button.bind("<Button-1>", BookingPage.button_name_finder_2)

        total_cost = tk.Label(booking_form_frame)
        total_cost.place(relx=0.044, rely=0.855, height=40, width=144)
        total_cost.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="""Total Charge :""",
        )

        cost = tk.Label(booking_form_frame)
        cost.place(relx=0.155, rely=0.855, height=40, width=143)
        cost.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="""XXXXXX""",
        )

        view_total_cost_button = tk.Button(booking_form_frame)
        view_total_cost_button.place(
            relx=0.260,
            rely=0.855,
            height=33,
            relwidth=0.122,
        )
        view_total_cost_button.configure(
            activebackground="beige",
            borderwidth="1",
            compound="left",
            font="-family {Noto Sans} -size 12",
            text="""View Cost""",
        )

        view_total_cost_button.bind(
            "<Button-1>",
            lambda event: BookingPage.show_cost(
                event,
                no_of_taxi_entry,
                cost,
            ),
        )

        view_total_cost_button.bind(
            "<ButtonRelease-1>",
            lambda event: BookingPage.hide_cost(
                event,
                cost,
            ),
        )

        book_now_button = tk.Button(booking_form_frame)
        book_now_button.place(relx=0.820, rely=0.840, height=53, width=141)
        book_now_button.configure(
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 16",
            foreground="#FFFFFF",
            text="""Book Now""",
            command=lambda: BookingPage.user_booking_register(
                booking_form_frame,
                record,
                firstname_entry,
                lastname_entry,
                no_of_passenger_entry,
                no_of_taxi_entry,
                date_entry,
                hour_entry,
                minute_entry,
                pickup_address_entry,
                destination_entry,
                rb_valv,
                card_number_entry,
                exp_entry,
                cvv_entry,
                cost,
            ),
        )

        payment_method = tk.LabelFrame(booking_form_frame)
        payment_method.place(relx=0.570, rely=0.285, relheight=0.21, relwidth=0.34)
        payment_method.configure(
            relief="groove", background="#FFFFFF", text="""Payment Method"""
        )

        card_number_entry = tk.Entry(payment_method)
        card_number_entry.place(
            relx=0.047, rely=0.583, height=33, relwidth=0.508, bordermode="ignore"
        )
        card_number_entry.configure(
            background="#EFF0F2", font="TkFixedFont", selectbackground="#c4c4c4"
        )

        exp_entry = tk.Entry(payment_method)
        exp_entry.place(
            relx=0.611, rely=0.583, height=33, relwidth=0.142, bordermode="ignore"
        )
        exp_entry.configure(
            background="#EFF0F2", font="TkFixedFont", selectbackground="#c4c4c4"
        )

        cvv_entry = tk.Entry(payment_method)
        cvv_entry.place(
            relx=0.806, rely=0.583, height=33, relwidth=0.142, bordermode="ignore"
        )
        cvv_entry.configure(
            background="#EFF0F2", font="TkFixedFont", selectbackground="#c4c4c4"
        )

        card_number = tk.Label(payment_method)
        card_number.place(
            relx=0.043, rely=0.84, height=20, width=93, bordermode="ignore"
        )
        card_number.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            foreground="#637381",
            text="""Card Number""",
        )

        exp_date = tk.Label(payment_method)
        exp_date.place(relx=0.611, rely=0.84, height=20, width=62, bordermode="ignore")
        exp_date.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            foreground="#637381",
            text="""Exp Date""",
        )

        cvv = tk.Label(payment_method)
        cvv.place(relx=0.806, rely=0.84, height=20, width=63, bordermode="ignore")
        cvv.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            foreground="#637381",
            text="""CVV""",
        )

        rb_valv = StringVar()

        credit_card = tk.Radiobutton(
            payment_method,
            value="Credit Card",
            variable=rb_valv,
            command=lambda: BookingPage.enable_card_details(
                card_number_entry,
                exp_entry,
                cvv_entry,
            ),
        )
        credit_card.place(relx=0.043, rely=0.256, relheight=0.212, relwidth=0.267)
        credit_card.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 10",
            justify="left",
            selectcolor="#d9d9d9",
            text="""Credit Card""",
        )

        cashInHand = tk.Radiobutton(
            payment_method,
            value="Cash In Hand",
            variable=rb_valv,
        )
        cashInHand.place(relx=0.350, rely=0.256, relheight=0.212, relwidth=0.267)
        cashInHand.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 10",
            justify="left",
            selectcolor="#d9d9d9",
            text="""Cash In Hand""",
            command=lambda: BookingPage.disable_card_details(
                card_number_entry,
                exp_entry,
                cvv_entry,
            ),
        )
        rb_valv.set("Credit Card")

        back = tk.Button(booking_form_frame)
        back.place(x=1165, y=60, height=35, width=90)
        back.config(
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#FFFFFF",
            text="""Back""",
            command=lambda: BookingPage.redirect_to_dashboard(
                booking_form_frame,
            ),
        )

        booking_form_frame.mainloop()

    @staticmethod
    def redirect_to_dashboard(booking_form_frame):
        booking_form_frame.destroy()

    @staticmethod
    def disable_card_details(
        card_number_entry,
        exp_entry,
        cvv_entry,
    ):
        card_number_entry.delete(0, "end")
        card_number_entry.config(state="disabled")
        exp_entry.delete(0, "end")
        exp_entry.config(state="disabled")
        cvv_entry.delete(0, "end")
        cvv_entry.config(state="disabled")

        card_number_entry.update()
        exp_entry.update()
        cvv_entry.update()

    @staticmethod
    def enable_card_details(card_number_entry, exp_entry, cvv_entry):
        card_number_entry.config(state="normal")
        exp_entry.config(state="normal")
        cvv_entry.config(state="normal")
        card_number_entry.update()
        exp_entry.update()
        cvv_entry.update()

    @staticmethod
    def create_location_picker(
        event,
        booking_form_frame,
        location_entry,
    ):
        location_picker_frame = tk.Toplevel(booking_form_frame)
        location_picker_frame.title("Location Picker")
        location_picker_frame.resizable(0, 0)
        location_picker_frame.configure(background="#FFFFFF")
        location_picker_frame.geometry("580x580")
        BookingPage.build_location_picker_frame(
            location_picker_frame,
            location_entry,
        )

    @staticmethod
    def build_location_picker_frame(
        location_picker_frame,
        location_entry,
    ):
        google_map_view = TkinterMapView(
            location_picker_frame,
            width=580,
            height=480,
        )
        google_map_view.set_tile_server(
            "https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
            max_zoom=22,
        )
        google_map_view.place(relx=0, rely=0.07)
        google_map_view.set_address("kathmandu, nepal")
        google_map_view.set_zoom(13)

        selected_address = tk.Label(location_picker_frame)
        selected_address.place(relx=0.0, rely=0.010, height=33, relwidth=0.999)
        selected_address.config(background="#FFFFFF")

        google_map_view.add_left_click_map_command(
            lambda coordinates: BookingPage.location_marker(
                coordinates,
                selected_address,
            ),
        )

        search_entry = tk.Entry(location_picker_frame)
        search_entry.place(relx=0.060, rely=0.920, height=33, relwidth=0.300)
        search_entry.configure(
            background="#EFF0F2", font="TkFixedFont", selectbackground="#c4c4c4"
        )

        search_button = tk.Button(location_picker_frame)
        search_button.place(relx=0.400, rely=0.920, height=33, relwidth=0.122)
        search_button.configure(
            activebackground="beige",
            borderwidth="1",
            compound="left",
            font="-family {Noto Sans} -size 12",
            text="""Search""",
            command=lambda: BookingPage.search_location(
                google_map_view,
                search_entry,
            ),
        )

        select_location_button = tk.Button(location_picker_frame)
        select_location_button.place(
            relx=0.550,
            rely=0.920,
            height=33,
            relwidth=0.290,
        )
        select_location_button.configure(
            activebackground="beige",
            borderwidth="1",
            compound="left",
            font="-family {Noto Sans} -size 12",
            text="""Select Location""",
            command=lambda: BookingPage.address_selected_display(
                location_entry,
                location_picker_frame,
            ),
        )
        location_picker_frame.grab_set()
        location_picker_frame.mainloop()

    @staticmethod
    def search_location(google_map_view, search_entry):
        google_map_view.set_address(search_entry.get())
        google_map_view.set_zoom(15)

    clicked_address = None

    @staticmethod
    def location_marker(
        coordinates,
        selected_address,
    ):
        if BookingPage.button_name == "pickup_button":
            BookingPage.pickup_location_coordinates = coordinates
        else:
            BookingPage.destination_coordinates = coordinates

        clicked_coordinates_1 = coordinates[0]
        clicked_coordinates_2 = coordinates[1]
        BookingPage.clicked_address = convert_coordinates_to_address(
            clicked_coordinates_1,
            clicked_coordinates_2,
        )
        selected_address.config(
            text=(
                BookingPage.clicked_address.street,
                BookingPage.clicked_address.postal,
                BookingPage.clicked_address.city,
                BookingPage.clicked_address.country,
            ),
            font="-family {Noto Sans} -size 14",
        )

    @staticmethod
    def address_selected_display(
        location_entry,
        location_picker_frame,
    ):
        location_entry.config(state="normal")
        location_entry.delete(0, "end")
        location_entry.insert(
            0,
            (
                BookingPage.clicked_address.street,
                BookingPage.clicked_address.postal,
                BookingPage.clicked_address.city,
                BookingPage.clicked_address.country,
            ),
        )
        location_entry.config(state="readonly")
        location_picker_frame.destroy()

    final_cost = ""

    @staticmethod
    def calculate_total_cost(no_of_taxi_entry, cost):

        try:
            total_cost = (
                math.ceil(
                    hs.haversine(
                        BookingPage.pickup_location_coordinates,
                        BookingPage.destination_coordinates,
                    )
                )
                * 59.25
            )
            no_of_taxi = int(no_of_taxi_entry.get())

            showCost = total_cost * no_of_taxi

            BookingPage.final_cost = str(round(showCost, 2))
            cost.config(text="NPR. " + BookingPage.final_cost)
        except Exception as error:
            cost.config(text="XXXXXX")

    @staticmethod
    def button_name_finder(event):
        BookingPage.button_name = "pickup_button"

    @staticmethod
    def button_name_finder_2(event):
        BookingPage.button_name = "destination_button"

    @staticmethod
    def show_cost(
        event,
        no_of_taxi_entry,
        cost,
    ):
        BookingPage.calculate_total_cost(no_of_taxi_entry, cost)

    @staticmethod
    def hide_cost(
        event,
        cost,
    ):
        cost.config(text="XXXXXX")

    @staticmethod
    def user_booking_register(
        booking_form_frame,
        record,
        firstname_entry,
        lastname_entry,
        no_of_passenger_entry,
        no_of_taxi_entry,
        date_entry,
        hour_entry,
        minute_entry,
        pickup_address_entry,
        destination_entry,
        rb_valv,
        card_number_entry,
        exp_entry,
        cvv_entry,
        cost,
    ):
        for data in record:
            fetched_user_id = data[0]

        BookingPage.calculate_total_cost(no_of_taxi_entry, cost)
        try:
            user_booking = BookingModel(
                user_id=fetched_user_id,
                firstname=firstname_entry.get(),
                lastname=lastname_entry.get(),
                no_of_pass=no_of_passenger_entry.get(),
                no_of_taxi=no_of_taxi_entry.get(),
                pick_up_date=date_entry.get(),
                pick_up_hrs=hour_entry.get(),
                pick_up_min=minute_entry.get(),
                pick_up_location=pickup_address_entry.get(),
                destination=destination_entry.get(),
                payment_method=rb_valv.get(),
                card_number=card_number_entry.get(),
                exp_date=exp_entry.get(),
                cvv=cvv_entry.get(),
                total_cost=BookingPage.final_cost,
                pickup_coordinates=str(BookingPage.pickup_location_coordinates),
                destination_coordinates=str(BookingPage.destination_coordinates),
            )
            booking_control = BookingController()
            booking_control.booking_control(user_booking, booking_form_frame)

        except CustomException as e:
            messagebox.showerror("Invalid Data", e)
