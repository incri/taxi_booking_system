from datetime import datetime, date
import tkinter as tk
from tkinter import NO, W, Scrollbar, ttk
from tkinter import messagebox

from helper.constants import LOGO_LOCATION
from tkintermapview import TkinterMapView


class DriverDashboard:
    def __init__(self, root, driver_controller, record):
        self.root = root
        self.driver_controller = driver_controller
        self.record = record
        self.create_dashboard_frame()

    def create_dashboard_frame(self):
        self.dashboard_frame = tk.Frame(self.root)
        self.dashboard_frame.configure(background="#FFFFFF")
        self.dashboard_frame.place(relx=-0.07, rely=0, height=768, width=1366)
        self.build_dashboard_frame(
            dashboard_frame=self.dashboard_frame,
            root=self.root,
            driver_controller=self.driver_controller,
            record=self.record,
        )

    @staticmethod
    def build_dashboard_frame(
        dashboard_frame,
        root,
        driver_controller,
        record,
    ):

        logo_label = tk.Label(dashboard_frame)
        logo_label.place(relx=0.110, rely=0.068, height=71, width=80)
        logo_label.configure(
            anchor="w",
            compound="left",
            background="#FFFFFF",
        )
        photo_location = tk.PhotoImage(file=LOGO_LOCATION)
        logo_label.configure(image=photo_location)

        DriverDashboard.upcoming_trip_frame(
            dashboard_frame,
            driver_controller,
            record,
        )

        customer_table_button = tk.Button(dashboard_frame)
        customer_table_button.place(relx=0.110, rely=0.850, height=33, width=101)
        customer_table_button.configure(
            activebackground="beige",
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 9 -weight bold",
            foreground="#FFFFFF",
            text="""Upcoming""",
            command=lambda: DriverDashboard.upcoming_trip_frame(
                dashboard_frame,
                driver_controller,
                record,
            ),
        )

        driver_table_button = tk.Button(dashboard_frame)
        driver_table_button.place(relx=0.200, rely=0.850, height=33, width=101)
        driver_table_button.configure(
            activebackground="beige",
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 9 -weight bold",
            foreground="#FFFFFF",
            text="""Completed""",
            command=lambda: DriverDashboard.completed_trip_frame(
                dashboard_frame,
                driver_controller,
                record,
            ),
        )

        profile_refresh_button = tk.Button(dashboard_frame)
        profile_refresh_button.place(relx=0.720, rely=0.450, height=35, width=100)
        profile_refresh_button.configure(
            background="#FFFFFF",
            compound="left",
            text="Update",
            command=lambda: DriverDashboard.driver_profile_frame_create(
                dashboard_frame,
                driver_controller,
                record,
            ),
        )

        DriverDashboard.driver_profile_frame_create(
            dashboard_frame,
            driver_controller,
            record,
        )

        dashboard_frame.mainloop()

    @staticmethod
    def upcoming_trip_frame(dashboard_frame, driver_controller, record):

        table_frame = tk.Frame(dashboard_frame, bg="#FFFFFF")
        table_frame.place(relx=0.110, rely=0.590, height=160, width=1160)

        DriverDashboard.upcoming_trip_table(
            table_frame,
            driver_controller,
            record,
        )

    @staticmethod
    def upcoming_trip_table(table_frame, driver_controller, record):
        title = tk.Label(table_frame)
        title.place(relx=0, rely=0, height=40, width=212)
        title.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 18 -weight bold",
            foreground="#3056D3",
            text="""Upcoming Trip""",
        )

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

        table_scroll_bar = Scrollbar(table_frame)
        table_scroll_bar.place(relx=0.985, rely=0.250, height=118, width=15)

        upcoming_booking_table = ttk.Treeview(
            table_frame,
            yscrollcommand=table_scroll_bar.set,
            selectmode="extended",
        )

        upcoming_booking_table.bind(
            "<Double-1>",
            lambda event: DriverDashboard.driver_trip_detail(
                event, table_frame, trip_fetched_data, driver_controller
            ),
        )
        upcoming_booking_table.place(
            relx=0,
            rely=0.250,
            height=118,
            width=1125,
        )

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

        for data in record:
            driver_id = data[0]

        upcoming_trip_control = driver_controller()
        trip_fetched_data = upcoming_trip_control.upcoming_trip_detail_fetcher(
            driver_id
        )

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

    @staticmethod
    def completed_trip_frame(dashboard_frame, driver_controller, record):
        table_frame = tk.Frame(dashboard_frame, bg="#FFFFFF")
        table_frame.place(relx=0.110, rely=0.590, height=160, width=1160)

        DriverDashboard.completed_trip_table(
            table_frame,
            driver_controller,
            record,
        )

    @staticmethod
    def driver_trip_detail(
        event,
        table_frame,
        trip_fetched_data,
        driver_controller,
    ):

        for data in trip_fetched_data:

            driver_trip_frame = tk.Toplevel(table_frame)
            driver_trip_frame.title("Assign Taxi")
            driver_trip_frame.geometry("682x641+193+31")
            driver_trip_frame.resizable(0, 0)
            driver_trip_frame.configure(background="#FFFFFF")

            title = tk.Label(driver_trip_frame)
            title.place(relx=0.360, rely=0.031, height=43, width=250)
            title.configure(
                anchor="w",
                background="#FFFFFF",
                compound="left",
                font="-family {Noto Sans} -size 18 -weight bold",
                text="""Booking Details""",
            )

            fullname_label = tk.Label(driver_trip_frame)
            fullname_label.place(relx=0.029, rely=0.156, height=34, width=122)
            fullname_label.configure(
                anchor="w",
                background="#FFFFFF",
                compound="left",
                font="-family {Noto Sans} -size 14",
                foreground="#4A4A4A",
                text="""Full Name :""",
            )

            fullname_data = tk.Label(driver_trip_frame)
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

            map_view_frame = tk.Frame(driver_trip_frame)
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

            passenger_no_label = tk.Label(driver_trip_frame)
            passenger_no_label.place(relx=0.029, rely=0.234, height=34, width=175)
            passenger_no_label.configure(
                anchor="w",
                background="#FFFFFF",
                compound="left",
                font="-family {Noto Sans} -size 14",
                foreground="#4A4A4A",
                text="""No of Passenger :""",
            )

            passenger_no_data = tk.Label(driver_trip_frame)
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

            taxi_number = tk.Label(driver_trip_frame)
            taxi_number.place(relx=0.029, rely=0.312, height=35, width=111)
            taxi_number.configure(
                activebackground="#f9f9f9",
                anchor="w",
                background="#FFFFFF",
                compound="left",
                font="-family {Noto Sans} -size 14",
                foreground="#4A4A4A",
                text="""No of Taxi :""",
            )

            taxi_number_data = tk.Label(driver_trip_frame)
            taxi_number_data.place(relx=0.22, rely=0.312, height=35, width=48)
            taxi_number_data.configure(
                activebackground="#f9f9f9",
                anchor="w",
                background="#FFFFFF",
                compound="left",
                font="-family {Noto Sans} -size 14",
                foreground="#4A4A4A",
                highlightthickness="2",
                text=data[5],
            )

            pick_up_date_lable = tk.Label(driver_trip_frame)
            pick_up_date_lable.place(relx=0.029, rely=0.39, height=34, width=133)
            pick_up_date_lable.configure(
                activebackground="#f9f9f9",
                anchor="w",
                background="#FFFFFF",
                font="-family {Noto Sans} -size 14",
                foreground="#4A4A4A",
                text="""Pick Up Date :""",
            )

            pick_up_date_data = tk.Label(driver_trip_frame)
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

            pick_up_address_label = tk.Label(driver_trip_frame)
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
            time_label = tk.Label(driver_trip_frame)
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
            time_data = tk.Label(driver_trip_frame)
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

            pickup_address_data = tk.Label(driver_trip_frame)
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

            destination_label = tk.Label(driver_trip_frame)
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

            destination_address_lable = tk.Label(driver_trip_frame)
            destination_address_lable.place(
                relx=0.249, rely=0.546, height=34, width=323
            )
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

            total_cost_label = tk.Label(driver_trip_frame)
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

            total_cost_data = tk.Label(driver_trip_frame)
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

            payment_method_lable = tk.Label(driver_trip_frame)
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

            payment_method_data = tk.Label(driver_trip_frame)
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

            trip_completed_button = tk.Button(driver_trip_frame)
            trip_completed_button.place(relx=0.365, rely=0.880, height=33, width=160)
            trip_completed_button.configure(
                activebackground="beige",
                background="#007074",
                borderwidth="2",
                compound="left",
                font="-family {Noto Sans} -size 10 -weight bold",
                foreground="#FFFFFF",
                text="""Trip Completed""",
                command=lambda: DriverDashboard.trip_completed(
                    trip_fetched_data,
                    driver_controller,
                    driver_trip_frame,
                ),
            )

            # Comparing today date and trip date

            trip_date = data[6]
            trip_time = str(data[7]) + ":" + str(data[8]) + ":00"
            time_final = datetime.strptime(trip_time, "%H:%M:%S").time()

            trip_date_and_time = datetime.combine(trip_date, time_final)
            today = datetime.now().isoformat(" ", "seconds")
            today_date = datetime.strptime(today, "%Y-%m-%d %H:%M:%S")

            if today_date < trip_date_and_time:
                trip_completed_button.config(state="disable")
                trip_completed_button.update()
            else:
                trip_completed_button.config(state="normal")
                trip_completed_button.update()

            if data[16] == "Completed":
                trip_completed_button.config(state="disable")
                trip_completed_button.update()

            back_button = tk.Button(driver_trip_frame)
            back_button.place(relx=0.865, rely=0.031, height=33, width=71)
            back_button.configure(
                activebackground="beige",
                borderwidth="2",
                compound="left",
                font="-family {Noto Sans} -size 10",
                foreground="#FFFFFF",
                text="""Back""",
            )

            driver_trip_frame.wait_visibility()
            driver_trip_frame.grab_set()
            driver_trip_frame.mainloop()

    @staticmethod
    def trip_completed(trip_fetched_data, driver_controller, driver_trip_frame):
        for data in trip_fetched_data:

            booking_id = data[0]
            driver_id = data[22]

        trip_complete_control = driver_controller()
        trip_complete_control.completed_trip_controller(booking_id, driver_id)
        messagebox.showinfo("Sucess", "Marked as completed ")
        driver_trip_frame.destroy()

    @staticmethod
    def completed_trip_table(table_frame, driver_controller, record):
        title = tk.Label(table_frame)
        title.place(relx=0, rely=0, height=40, width=212)
        title.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 18 -weight bold",
            foreground="#3056D3",
            text="""completed Trip""",
        )

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

        table_scroll_bar = Scrollbar(table_frame)
        table_scroll_bar.place(relx=0.985, rely=0.250, height=118, width=15)

        completed_booking_table = ttk.Treeview(
            table_frame,
            yscrollcommand=table_scroll_bar.set,
            selectmode="extended",
        )

        completed_booking_table.bind(
            "<Double-1>",
            lambda event: DriverDashboard.driver_trip_detail(
                event, table_frame, trip_fetched_data, driver_controller
            ),
        )
        completed_booking_table.place(
            relx=0,
            rely=0.250,
            height=118,
            width=1125,
        )

        table_scroll_bar.config(
            command=completed_booking_table.yview,
        )

        completed_booking_table["columns"] = (
            "Booking ID",
            "Full Name",
            "Date and Time",
            "Destination",
            "Total Cost",
            "Status",
        )
        # Format Our Columns

        completed_booking_table.column("#0", width=0, stretch=NO)
        completed_booking_table.column("Booking ID", width=20, anchor=W)
        completed_booking_table.column("Full Name", width=70, anchor=W)
        completed_booking_table.column("Date and Time", width=70, anchor=W)
        completed_booking_table.column("Destination", width=240, anchor=W)
        completed_booking_table.column("Total Cost", width=40, anchor=W)
        completed_booking_table.column("Status", width=40, anchor=W)

        # Create Heading

        completed_booking_table.heading("#0", text="", anchor=W)
        completed_booking_table.heading("Booking ID", text="Booking ID", anchor=W)
        completed_booking_table.heading("Full Name", text="Full Name", anchor=W)
        completed_booking_table.heading("Date and Time", text="Date and Time", anchor=W)
        completed_booking_table.heading("Destination", text="Destination", anchor=W)
        completed_booking_table.heading("Total Cost", text="Total Cost", anchor=W)
        completed_booking_table.heading("Status", text="Status", anchor=W)

        for data in record:
            driver_id = data[0]

        completed_trip_control = driver_controller()
        trip_fetched_data = completed_trip_control.completed_trip_detail_fetcher(
            driver_id
        )

        for data in trip_fetched_data:

            completed_booking_table.insert(
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

    @staticmethod
    def driver_profile_frame_create(
        dashboard_frame,
        driver_controller,
        record,
    ):
        profile_details_label = tk.Frame(dashboard_frame)
        profile_details_label.place(relx=0.720, rely=0.068, height=280, width=325)
        profile_details_label.configure(
            background="#FFFFFF",
            highlightthickness="2",
            relief="flat",
        )

        for data in record:
            driver_id = data[0]

        driver_profile_data_control = driver_controller()
        profile_details = driver_profile_data_control.driver_profile_data_fetcher(
            driver_id
        )

        driver_profile_data_control = driver_controller()
        booking_details = driver_profile_data_control.driver_booking_data_fetcher(
            driver_id
        )

        profile_data = profile_details[0]
        booking_data = booking_details[0]

        username_data = tk.Label(profile_details_label)
        username_data.place(relx=0.215, rely=0.036, height=41, width=184)
        username_data.configure(
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14 -weight bold",
            foreground="#4A4A4A",
            text=profile_data[6],
        )

        name_label = tk.Label(profile_details_label)
        name_label.place(relx=0.062, rely=0.25, height=31, width=64)
        name_label.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#4A4A4A",
            text="""Name :""",
        )

        name_data = tk.Label(profile_details_label)
        name_data.place(relx=0.277, rely=0.25, height=31, width=184)
        name_data.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 11",
            foreground="#4A4A4A",
            text=profile_data[1],
        )

        contact_label = tk.Label(profile_details_label)
        contact_label.place(relx=0.062, rely=0.357, height=31, width=74)
        contact_label.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#4A4A4A",
            text="""Contact :""",
        )
        contact_data = tk.Label(profile_details_label)
        contact_data.place(relx=0.308, rely=0.357, height=31, width=104)
        contact_data.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 11",
            foreground="#4A4A4A",
            text=profile_data[3],
        )

        taxi_label = tk.Label(profile_details_label)
        taxi_label.place(relx=0.062, rely=0.464, height=31, width=54)
        taxi_label.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#4A4A4A",
            text="""Taxi :""",
        )
        taxi_data = tk.Label(profile_details_label)
        taxi_data.place(relx=0.246, rely=0.464, height=31, width=184)
        taxi_data.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 11",
            foreground="#4A4A4A",
            text=(profile_data[9] + " " + profile_data[10]),
        )

        taxi_number_label = tk.Label(profile_details_label)
        taxi_number_label.place(relx=0.062, rely=0.571, height=31, width=114)
        taxi_number_label.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#4A4A4A",
            text="""Taxi number :""",
        )

        taxi_number_data = tk.Label(profile_details_label)
        taxi_number_data.place(relx=0.431, rely=0.571, height=31, width=134)
        taxi_number_data.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 11",
            foreground="#4A4A4A",
            text=profile_data[11],
        )

        total_revenue_label = tk.Label(profile_details_label)
        total_revenue_label.place(relx=0.062, rely=0.714, height=41, width=154)
        total_revenue_label.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            text="""Total  Revenue :""",
        )

        total_revenue_data = tk.Label(profile_details_label)
        total_revenue_data.place(relx=0.031, rely=0.857, height=31, width=304)
        total_revenue_data.configure(
            anchor="center",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            text="XXXXX",
        )

        data_view_button = tk.Button(profile_details_label)
        data_view_button.place(relx=0.554, rely=0.75, height=23, width=41)
        data_view_button.configure(
            background="#FFFFFF",
            compound="left",
            text="""00""",
        )

        data_view_button.bind(
            "<Button-1>",
            lambda event: DriverDashboard.show_revenue(
                event,
                total_revenue_data,
                booking_data,
            ),
        )

        data_view_button.bind(
            "<ButtonRelease-1>",
            lambda event: DriverDashboard.hide_revenue(
                event,
                total_revenue_data,
            ),
        )

        DriverDashboard.driver_payment_frame_create(
            dashboard_frame,
            record,
            driver_controller,
        )

    @staticmethod
    def show_revenue(event, total_revenue_data, booking_data):
        total_revenue_data.config(text=booking_data)
        total_revenue_data.update()

    @staticmethod
    def hide_revenue(
        event,
        total_revenue_data,
    ):
        total_revenue_data.config(text="XXXXX")

    @staticmethod
    def driver_payment_frame_create(
        dashboard_frame,
        record,
        driver_controller,
    ):

        today = date.today().strftime("%Y-%m")

        for data in record:
            driver_id = data[0]

        driver_profile_data_control = driver_controller()
        monthly_revenue_details = (
            driver_profile_data_control.driver_monthly_data_fetcher(
                driver_id,
                today,
            )
        )

        monthly_income = monthly_revenue_details[0]

        profile_details_label = tk.Frame(dashboard_frame)
        profile_details_label.place(relx=0.470, rely=0.250, height=140, width=325)
        profile_details_label.configure(
            background="#FFFFFF",
            highlightthickness="2",
            relief="flat",
        )

        payment_label = tk.Label(profile_details_label)
        payment_label.place(relx=0.215, rely=0.036, height=41, width=184)
        payment_label.configure(
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14 -weight bold",
            foreground="#4A4A4A",
            text="Monthly Revenue",
        )

        gross_income_label = tk.Label(profile_details_label)
        gross_income_label.place(relx=0.062, rely=0.320, height=31, width=120)
        gross_income_label.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#4A4A4A",
            text="""Gross Income :""",
        )

        gross_income_data = tk.Label(profile_details_label)
        gross_income_data.place(relx=0.445, rely=0.320, height=31, width=160)
        gross_income_data.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 11",
            foreground="#4A4A4A",
            text="XXXXX",
        )

        service_cost_label = tk.Label(profile_details_label)
        service_cost_label.place(relx=0.062, rely=0.520, height=31, width=110)
        service_cost_label.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#4A4A4A",
            text="""Service Cost :""",
        )
        service_cost_data = tk.Label(profile_details_label)
        service_cost_data.place(relx=0.410, rely=0.520, height=31, width=160)
        service_cost_data.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 11",
            foreground="#4A4A4A",
            text="XXXXX",
        )

        net_income_label = tk.Label(profile_details_label)
        net_income_label.place(relx=0.062, rely=0.720, height=31, width=100)
        net_income_label.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 12",
            foreground="#4A4A4A",
            text="""Net Income :""",
        )
        net_income_data = tk.Label(profile_details_label)
        net_income_data.place(relx=0.380, rely=0.720, height=31, width=160)
        net_income_data.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 11",
            foreground="#4A4A4A",
            text="XXXXX",
        )

        data_view_button = tk.Button(profile_details_label)
        data_view_button.place(relx=0.850, rely=0.055, height=23, width=41)
        data_view_button.configure(
            background="#FFFFFF",
            compound="left",
            text="""00""",
        )

        data_view_button.bind(
            "<Button-1>",
            lambda event: DriverDashboard.show_monthly_revenue(
                event,
                gross_income_data,
                service_cost_data,
                net_income_data,
                monthly_income,
            ),
        )

        data_view_button.bind(
            "<ButtonRelease-1>",
            lambda event: DriverDashboard.hide_monthly_revenue(
                event,
                gross_income_data,
                service_cost_data,
                net_income_data,
            ),
        )

    @staticmethod
    def show_monthly_revenue(
        event,
        gross_income_data,
        service_cost_data,
        net_income_data,
        monthly_income,
    ):

        gross_income = str(round(monthly_income[0], 2))
        service_cost = str(round(monthly_income[1], 2))
        net_income = str(round(monthly_income[2], 2))

        gross_income_data.config(text=gross_income)
        gross_income_data.update()
        service_cost_data.config(text=service_cost)
        service_cost_data.update()
        net_income_data.config(text=net_income)
        net_income_data.update()

    @staticmethod
    def hide_monthly_revenue(
        event,
        gross_income_data,
        service_cost_data,
        net_income_data,
    ):
        gross_income_data.config(text="XXXXX")
        gross_income_data.update()
        service_cost_data.config(text="XXXXX")
        service_cost_data.update()
        net_income_data.config(text="XXXXX")
        net_income_data.update()
