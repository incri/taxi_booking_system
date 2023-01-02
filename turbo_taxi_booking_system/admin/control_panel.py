from select import select
from sre_parse import State
import tkinter as tk
from tkinter import W, Scrollbar, ttk
from tkinter import messagebox
from tkinter.messagebox import NO

from click import command

from taxi.taxi_register import TaxiRegisterPage
from driver.driver_register import DriverRegisterPage
from tkintermapview import TkinterMapView


class ControlPanelPage:
    def __init__(self, root, login_frame, admin_controller):
        self.root = root
        self.admin_controller = admin_controller
        self.login_frame = login_frame
        self.create_control_panel_frame()

    def create_control_panel_frame(self):
        self.control_panel_frame = tk.Frame(self.root)
        self.control_panel_frame.configure(background="#FFFFFF")
        self.control_panel_frame.place(relx=-0.07, rely=0, height=768, width=1366)
        self.build_control_panel_frame(
            self.root, self.control_panel_frame, self.admin_controller
        )

    @staticmethod
    def build_control_panel_frame(root, control_panel_frame, admin_controller):
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

        taxi_register_button = tk.Button(control_panel_frame)
        taxi_register_button.place(relx=0.850, rely=0.130, height=33, width=101)
        taxi_register_button.configure(
            activebackground="beige",
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 9 -weight bold",
            foreground="#FFFFFF",
            text="""Taxi Register""",
            command=lambda: TaxiRegisterPage(
                root,
                control_panel_frame,
            ),
        )

        driver_register_button = tk.Button(control_panel_frame)
        driver_register_button.place(relx=0.750, rely=0.130, height=33, width=110)
        driver_register_button.configure(
            activebackground="beige",
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 9 -weight bold",
            foreground="#FFFFFF",
            text="""Driver Register""",
            command=lambda: DriverRegisterPage(
                root,
                control_panel_frame,
            ),
        )

        customer_table_button = tk.Button(control_panel_frame)
        customer_table_button.place(relx=0.130, rely=0.850, height=33, width=101)
        customer_table_button.configure(
            activebackground="beige",
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 9 -weight bold",
            foreground="#FFFFFF",
            text="""Customer""",
            command=lambda: ControlPanelPage.customer_tabel_data_fetcher(
                admin_controller, control_panel_frame
            ),
        )

        driver_table_button = tk.Button(control_panel_frame)
        driver_table_button.place(relx=0.220, rely=0.850, height=33, width=101)
        driver_table_button.configure(
            activebackground="beige",
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 9 -weight bold",
            foreground="#FFFFFF",
            text="""Driver""",
            command=lambda: ControlPanelPage.driver_tabel_data_fetcher(
                admin_controller,
                control_panel_frame,
            ),
        )

        ControlPanelPage.customer_tabel_data_fetcher(
            admin_controller, control_panel_frame
        )
        control_panel_frame.mainloop()

    @staticmethod
    def customer_table_frame_build(
        record,
        control_panel_frame,
        admin_controller,
    ):

        customer_table_frame = tk.Frame(control_panel_frame)

        customer_table_frame.place(
            relx=0.130,
            rely=0.200,
            height=470,
            width=1095,
        )

        customer_table_frame.config(
            background="#FFFFFF",
            borderwidth=2,
            relief="solid",
            highlightbackground="#000000",
        )

        table_title = tk.Label(customer_table_frame)
        table_title.place(relx=0.020, rely=0.010, height=60, width=200)
        table_title.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="""Customer Table""",
        )

        search_entry = tk.Entry(customer_table_frame)
        search_entry.place(relx=0.200, rely=0.050, height=25, relwidth=0.150)
        search_entry.configure(
            background="#EFF0F2", font="TkFixedFont", selectbackground="#c4c4c4"
        )

        search_button = tk.Button(customer_table_frame)
        search_button.place(relx=0.360, rely=0.050, height=25, relwidth=0.069)
        search_button.configure(
            activebackground="beige",
            borderwidth="1",
            compound="left",
            font="-family {Noto Sans} -size 10",
            text="""Search""",
            command=lambda: ControlPanelPage.customer_tabel_search_fetcher(
                admin_controller,
                search_entry,
                selected_sort_by,
                customer_table_frame,
            ),
        )

        selected_sort_by = tk.StringVar()

        sort_by_combo = ttk.Combobox(
            customer_table_frame,
            textvariable=selected_sort_by,
            state="readonly",
            values=(
                "Pending",
                "Accepted",
                "Canceled",
                "All",
            ),
        )

        sort_by_combo.place(relx=0.460, rely=0.050, height=25, relwidth=0.150)
        sort_by_combo.current(0)

        sort_by_combo.bind(
            "<<ComboboxSelected>>",
            lambda event: ControlPanelPage.customer_tabel_search_fetcher(
                admin_controller,
                search_entry,
                selected_sort_by,
                customer_table_frame,
            ),
        ),

        sort_by_label = tk.Label(
            customer_table_frame,
            text=": View",
            anchor=W,
            background="#FFFFFF",
            foreground="#4A4A4A",
        )

        sort_by_label.place(
            relx=0.620,
            rely=0.050,
            height=25,
            relwidth=0.060,
        )

        ControlPanelPage.customer_table_build(
            customer_table_frame,
            record,
            admin_controller,
        )

    @staticmethod
    def driver_table_frame_build(record, control_panel_frame, admin_controller):
        driver_table_frame = tk.Frame(control_panel_frame)

        driver_table_frame.place(
            relx=0.130,
            rely=0.200,
            height=470,
            width=1095,
        )

        driver_table_frame.config(
            background="#FFFFFF",
            borderwidth=2,
            relief="solid",
            highlightbackground="#000000",
        )

        table_title = tk.Label(driver_table_frame)
        table_title.place(relx=0.020, rely=0.010, height=60, width=200)
        table_title.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            text="""Driver Table""",
        )

        search_entry = tk.Entry(driver_table_frame)

        search_entry.place(relx=0.200, rely=0.050, height=25, relwidth=0.150)
        search_entry.configure(
            background="#EFF0F2", font="TkFixedFont", selectbackground="#c4c4c4"
        )

        search_button = tk.Button(driver_table_frame)

        search_button.place(relx=0.360, rely=0.050, height=25, relwidth=0.069)
        search_button.configure(
            activebackground="beige",
            borderwidth="1",
            compound="left",
            font="-family {Noto Sans} -size 10",
            text="""Search""",
            command=lambda: ControlPanelPage.driver_tabel_search_fetcher(
                admin_controller,
                search_entry,
                selected_sort_by,
                driver_table_frame,
            ),
        )

        selected_sort_by = tk.StringVar()

        sort_by_combo = ttk.Combobox(
            driver_table_frame,
            textvariable=selected_sort_by,
            state="readonly",
            values=("Driver ID", "Full Name", "Available", "Booked"),
        )

        sort_by_combo.place(relx=0.460, rely=0.050, height=25, relwidth=0.150)
        sort_by_combo.current(0)

        sort_by_combo.bind(
            "<<ComboboxSelected>>",
            lambda event: ControlPanelPage.driver_tabel_search_fetcher(
                admin_controller,
                search_entry,
                selected_sort_by,
                driver_table_frame,
            ),
        ),

        sort_by_label = tk.Label(
            driver_table_frame,
            text=": sort by",
            anchor=W,
            background="#FFFFFF",
            foreground="#4A4A4A",
        )

        sort_by_label.place(
            relx=0.620,
            rely=0.050,
            height=25,
            relwidth=0.060,
        )
        ControlPanelPage.driver_table_build(driver_table_frame, record)

    @staticmethod
    def driver_table_build(dirver_table_frame, record):

        # Driver TABLE LOOK
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

        table_scroll_bar = Scrollbar(dirver_table_frame)
        table_scroll_bar.place(relx=0.980, rely=0.020, height=450, width=15)

        # driver Table Build

        driver_booking_table = ttk.Treeview(
            dirver_table_frame,
            yscrollcommand=table_scroll_bar.set,
            selectmode="extended",
        )
        driver_booking_table.place(
            relx=0.020,
            rely=0.150,
            height=375,
            width=1025,
        )
        # driver a scroll bar

        table_scroll_bar.config(
            command=driver_booking_table.yview,
        )
        # Define Column

        driver_booking_table["columns"] = (
            "Driver ID",
            "Full Name",
            "License Number",
            "Contact",
            "Taxi Number",
            "Status",
        )
        # Format Our Columns

        driver_booking_table.column("#0", width=0, stretch=NO)
        driver_booking_table.column("Driver ID", width=70, anchor=W)
        driver_booking_table.column("Full Name", width=140, anchor=W)
        driver_booking_table.column("License Number", width=120, anchor=W)
        driver_booking_table.column("Contact", width=120, anchor=W)
        driver_booking_table.column("Taxi Number", width=120, anchor=W)
        driver_booking_table.column("Status", width=120, anchor=W)

        # Create Heading

        driver_booking_table.heading("#0", text="", anchor=W)
        driver_booking_table.heading("Driver ID", text="Driver ID", anchor=W)
        driver_booking_table.heading("Full Name", text="Full Name", anchor=W)
        driver_booking_table.heading("License Number", text="License Number", anchor=W)
        driver_booking_table.heading("Contact", text="Contact", anchor=W)
        driver_booking_table.heading("Taxi Number", text="Taxi Number", anchor=W)
        driver_booking_table.heading("Status", text="Status", anchor=W)

        for data in record:
            driver_booking_table.insert(
                "",
                index="end",
                values=(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                ),
            )
        dirver_table_frame.mainloop()

    @staticmethod
    def customer_table_build(customer_table_frame, record, admin_controller):

        # CUSTOMISING TABLE LOOK
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

        # Customer Table Scroll Bar

        table_scroll_bar = Scrollbar(customer_table_frame)
        table_scroll_bar.place(relx=0.980, rely=0.020, height=450, width=15)

        # Customer Table Build

        customer_booking_table = ttk.Treeview(
            customer_table_frame,
            yscrollcommand=table_scroll_bar.set,
            selectmode="extended",
        )
        customer_booking_table.place(
            relx=0.020,
            rely=0.150,
            height=375,
            width=1025,
        )

        customer_booking_table.bind(
            "<Double-1>",
            lambda event: ControlPanelPage.assign_taxi_to_user(
                event,
                customer_booking_table,
                admin_controller,
            ),
        )

        # Configure a scroll bar

        table_scroll_bar.config(
            command=customer_booking_table.yview,
        )

        # Define Column

        customer_booking_table["columns"] = (
            "User ID",
            "Booking ID",
            "Created At",
            "Full Name",
            "Contact",
            "Address",
            "Email",
            "Booking Status",
        )

        # Format Our Columns

        customer_booking_table.column("#0", width=0, stretch=NO)
        customer_booking_table.column("User ID", width=70, anchor=W)
        customer_booking_table.column("Booking ID", width=70, anchor=W)
        customer_booking_table.column("Created At", width=120, anchor=W)
        customer_booking_table.column("Full Name", width=140, anchor=W)
        customer_booking_table.column("Contact", width=70, anchor=W)
        customer_booking_table.column("Address", width=170, anchor=W)
        customer_booking_table.column("Email", width=180, anchor=W)
        customer_booking_table.column("Booking Status", width=100, anchor=W)

        # Create Heading

        customer_booking_table.heading("#0", text="", anchor=W)
        customer_booking_table.heading("User ID", text="User ID", anchor=W)
        customer_booking_table.heading("Booking ID", text="Booking ID", anchor=W)
        customer_booking_table.heading("Created At", text="Created At", anchor=W)
        customer_booking_table.heading("Full Name", text="Full Name", anchor=W)
        customer_booking_table.heading("Contact", text="Contact", anchor=W)
        customer_booking_table.heading("Address", text="Address", anchor=W)
        customer_booking_table.heading("Email", text="Email", anchor=W)
        customer_booking_table.heading(
            "Booking Status", text="Booking Status", anchor=W
        )

        for data in record:
            customer_booking_table.insert(
                parent="",
                index="end",
                text="",
                values=(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6],
                    data[7],
                ),
            )

        customer_table_frame.mainloop()

    @staticmethod
    def customer_tabel_data_fetcher(admin_controller, control_panel_frame):
        user_booking = admin_controller()
        required_customer_data = user_booking.customer_data_fetcher()

        ControlPanelPage.customer_table_frame_build(
            required_customer_data,
            control_panel_frame,
            admin_controller,
        )

    @staticmethod
    def driver_tabel_data_fetcher(admin_controller, control_panel_frame):
        user_booking = admin_controller()
        required_customer_data = user_booking.driver_data_fetcher()

        ControlPanelPage.driver_table_frame_build(
            required_customer_data,
            control_panel_frame,
            admin_controller,
        )

    @staticmethod
    def customer_tabel_search_fetcher(
        admin_controller,
        search_entry,
        selected_sort_by,
        customer_table_frame,
    ):
        user_booking = admin_controller()
        required_customer_search = user_booking.customer_search_fetcher(
            search_entry,
            selected_sort_by,
        )

        ControlPanelPage.customer_table_build(
            customer_table_frame,
            required_customer_search,
            admin_controller,
        )

    @staticmethod
    def driver_tabel_search_fetcher(
        admin_controller,
        search_entry,
        selected_sort_by,
        driver_table_frame,
    ):
        user_booking = admin_controller()
        required_customer_search = user_booking.driver_search_fetcher(
            search_entry,
            selected_sort_by,
        )

        ControlPanelPage.driver_table_build(
            driver_table_frame,
            required_customer_search,
        )

    @staticmethod
    def assign_taxi_to_user(event, customer_booking_table, admin_controller):

        selected = customer_booking_table.focus()
        selected_row = customer_booking_table.item(
            selected,
            "values",
        )
        selected_booking_id = selected_row[1]

        # Booking Details Data Fetcher

        booking_data_control = admin_controller()
        fetched_booking_details = booking_data_control.booking_details_data_fetcher(
            selected_booking_id,
        )

        data = fetched_booking_details[0]

        assign_taxi_frame = tk.Toplevel(customer_booking_table)
        assign_taxi_frame.title("Assign Taxi")
        assign_taxi_frame.geometry("682x641+193+31")
        assign_taxi_frame.resizable(0, 0)
        assign_taxi_frame.configure(background="#FFFFFF")

        # BUILDING BOOKING DETAIL PAGE

        title = tk.Label(assign_taxi_frame)
        title.place(relx=0.360, rely=0.031, height=43, width=250)
        title.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 18 -weight bold",
            text="""Booking Details""",
        )

        fullname_label = tk.Label(assign_taxi_frame)
        fullname_label.place(relx=0.029, rely=0.156, height=34, width=122)
        fullname_label.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            text="""Full Name :""",
        )

        fullname_data = tk.Label(assign_taxi_frame)
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

        map_view_frame = tk.Frame(assign_taxi_frame)
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

        passenger_no_label = tk.Label(assign_taxi_frame)
        passenger_no_label.place(relx=0.029, rely=0.234, height=34, width=175)
        passenger_no_label.configure(
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            text="""No of Passenger :""",
        )

        passenger_no_data = tk.Label(assign_taxi_frame)
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

        taxi_number = tk.Label(assign_taxi_frame)
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

        taxi_number_data = tk.Label(assign_taxi_frame)
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

        pick_up_date_lable = tk.Label(assign_taxi_frame)
        pick_up_date_lable.place(relx=0.029, rely=0.39, height=34, width=133)
        pick_up_date_lable.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            text="""Pick Up Date :""",
        )

        pick_up_date_data = tk.Label(assign_taxi_frame)
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

        pick_up_address_label = tk.Label(assign_taxi_frame)
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
        time_label = tk.Label(assign_taxi_frame)
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
        time_data = tk.Label(assign_taxi_frame)
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

        pickup_address_data = tk.Label(assign_taxi_frame)
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

        destination_label = tk.Label(assign_taxi_frame)
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

        destination_address_lable = tk.Label(assign_taxi_frame)
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

        total_cost_label = tk.Label(assign_taxi_frame)
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

        total_cost_data = tk.Label(assign_taxi_frame)
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

        payment_method_lable = tk.Label(assign_taxi_frame)
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

        payment_method_data = tk.Label(assign_taxi_frame)
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

        credit_number_lable = tk.Label(assign_taxi_frame)
        credit_number_lable.place(relx=0.029, rely=0.78, height=34, width=236)
        credit_number_lable.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            text=data[13],
            highlightthickness="2",
            foreground="#4A4A4A",
            font="-family {Noto Sans} -size 14",
            compound="left",
        )

        exp_date_lable = tk.Label(assign_taxi_frame)
        exp_date_lable.place(relx=0.411, rely=0.78, height=34, width=96)
        exp_date_lable.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            highlightthickness="2",
            text=data[14],
        )

        cvv_lable = tk.Label(assign_taxi_frame)
        cvv_lable.place(relx=0.587, rely=0.78, height=34, width=96)
        cvv_lable.configure(
            activebackground="#f9f9f9",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            font="-family {Noto Sans} -size 14",
            foreground="#4A4A4A",
            highlightthickness="2",
            text=data[15],
        )

        show_credit_detail_lable = tk.Checkbutton(assign_taxi_frame)
        show_credit_detail_lable.place(
            relx=0.748, rely=0.78, relheight=0.051, relwidth=0.164
        )
        show_credit_detail_lable.configure(
            activebackground="beige",
            anchor="w",
            background="#FFFFFF",
            compound="left",
            highlightthickness="0",
            justify="left",
            selectcolor="#d9d9d9",
            text="""Show Details""",
        )

        assign_taxi_button = tk.Button(assign_taxi_frame)
        assign_taxi_button.place(relx=0.264, rely=0.889, height=33, width=141)
        assign_taxi_button.configure(
            activebackground="beige",
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 10 -weight bold",
            foreground="#FFFFFF",
            text="""Assign Taxi""",
            command=lambda: ControlPanelPage.taxi_assign_final_frame(
                assign_taxi_frame, admin_controller, data
            ),
        )

        cancel_booking_button = tk.Button(assign_taxi_frame)
        cancel_booking_button.place(relx=0.499, rely=0.889, height=33, width=141)
        cancel_booking_button.configure(
            activebackground="beige",
            background="#007074",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 10 -weight bold",
            text="""Cancel Booking""",
            foreground="#FFFFFF",
            command=lambda: ControlPanelPage.cancel_booking_request(
                admin_controller, data, assign_taxi_frame
            ),
        )
        if data[16] == "Canceled":
            assign_taxi_button.config(state="disable")
            cancel_booking_button.config(state="disable")

        if data[16] == "Accepted":
            assign_taxi_button.config(state="disable")

        back_button = tk.Button(assign_taxi_frame)
        back_button.place(relx=0.865, rely=0.031, height=33, width=71)
        back_button.configure(
            activebackground="beige",
            borderwidth="2",
            compound="left",
            font="-family {Noto Sans} -size 10",
            foreground="#FFFFFF",
            text="""Back""",
            command=lambda: ControlPanelPage.exit_assign_taxi_page(
                assign_taxi_frame,
            ),
        )

        assign_taxi_frame.wait_visibility()
        assign_taxi_frame.grab_set()
        assign_taxi_frame.mainloop()

    @staticmethod
    def exit_assign_taxi_page(assign_taxi_frame):
        assign_taxi_frame.destroy()

    @staticmethod
    def cancel_booking_request(admin_controller, data, assign_taxi_frame):

        booking_id = data[0]

        response = messagebox.askquestion(
            "Warning",
            "Do you really want to cancele this booking?",
            parent=assign_taxi_frame,
        )

        if response == "yes":
            cancel_booking_control = admin_controller()
            cancel_booking_control.cancel_booking(booking_id)
            assign_taxi_frame.destroy()

    @staticmethod
    def taxi_assign_final_frame(assign_taxi_frame, admin_controller, booking_id):

        assign_table_frame = tk.Toplevel(assign_taxi_frame)
        assign_table_frame.geometry("600x400+193+31")
        assign_table_frame.resizable(0, 0)
        assign_table_frame.configure(background="#FFFFFF")

        search_entry = tk.Entry(assign_table_frame)

        search_entry.place(relx=0.030, rely=0.070, height=25, relwidth=0.200)
        search_entry.configure(
            background="#EFF0F2", font="TkFixedFont", selectbackground="#c4c4c4"
        )

        search_button = tk.Button(assign_table_frame)

        search_button.place(relx=0.250, rely=0.070, height=25, relwidth=0.100)
        search_button.configure(
            activebackground="beige",
            borderwidth="1",
            compound="left",
            font="-family {Noto Sans} -size 10",
            text="""Search""",
        )

        selected_driver_type = tk.StringVar()

        sort_by_combo = ttk.Combobox(
            assign_table_frame,
            textvariable=selected_driver_type,
            state="readonly",
            values=(
                "Avalable",
                "Booked",
            ),
        )

        sort_by_combo.place(relx=0.370, rely=0.070, height=25, relwidth=0.200)
        sort_by_combo.current(0)

        sort_by_combo.bind(
            "<<ComboboxSelected>>",
            lambda event: ControlPanelPage.available_driver_table_view(
                assign_table_frame,
                admin_controller,
                selected_driver_type,
                booking_id,
                assign_taxi_frame,
            ),
        )

        # Define Column

        if selected_driver_type.get() == "Avalable":
            ControlPanelPage.available_driver_table_view(
                assign_table_frame,
                admin_controller,
                selected_driver_type,
                booking_id,
                assign_taxi_frame,
            )

        assign_table_frame.wait_visibility()
        assign_table_frame.grab_set()
        assign_table_frame.mainloop()

    @staticmethod
    def available_driver_table_view(
        assign_table_frame,
        admin_controller,
        selected_driver_type,
        booking_id,
        assign_taxi_frame,
    ):

        if selected_driver_type.get() == "Avalable":

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

            table_scroll_bar = Scrollbar(assign_table_frame)
            table_scroll_bar.place(relx=0.970, rely=0.150, height=280, width=15)

            # driver Table Build

            driver_booking_table = ttk.Treeview(
                assign_table_frame,
                yscrollcommand=table_scroll_bar.set,
                selectmode="extended",
            )
            driver_booking_table.place(
                relx=0.030,
                rely=0.150,
                height=280,
                width=550,
            )
            # driver a scroll bar

            table_scroll_bar.config(
                command=driver_booking_table.yview,
            )

            driver_booking_table["columns"] = (
                "Driver ID",
                "Full Name",
                "Contact",
                "Taxi Number",
            )
            # Format Our Columns

            driver_booking_table.column("#0", width=0, stretch=NO)
            driver_booking_table.column("Driver ID", width=40, anchor=W)
            driver_booking_table.column("Full Name", width=70, anchor=W)
            driver_booking_table.column("Contact", width=70, anchor=W)
            driver_booking_table.column("Taxi Number", width=80, anchor=W)

            # Create Heading

            driver_booking_table.heading("#0", text="", anchor=W)
            driver_booking_table.heading("Driver ID", text="Driver ID", anchor=W)
            driver_booking_table.heading("Full Name", text="Full Name", anchor=W)
            driver_booking_table.heading("Contact", text="Contact", anchor=W)
            driver_booking_table.heading("Taxi Number", text="Taxi Number", anchor=W)

            availavble_driver_control = admin_controller()
            record = availavble_driver_control.available_driver_fetcher()

            for data in record:
                driver_booking_table.insert(
                    "",
                    index="end",
                    values=(
                        data[0],
                        data[1],
                        data[3],
                        data[4],
                    ),
                )

            assign_button = tk.Button(assign_table_frame)
            assign_button.place(relx=0.400, rely=0.880, height=35, width=120)
            assign_button.configure(
                background="#007074",
                borderwidth="2",
                compound="left",
                font="-family {Noto Sans} -size 14",
                foreground="#FFFFFF",
                text="""Assign""",
                command=lambda: ControlPanelPage.selcted_driver_row_assign(
                    driver_booking_table,
                    admin_controller,
                    booking_id,
                    assign_taxi_frame,
                ),
            )

        else:

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

            table_scroll_bar = Scrollbar(assign_table_frame)
            table_scroll_bar.place(relx=0.970, rely=0.150, height=280, width=15)

            # driver Table Build

            driver_booking_table = ttk.Treeview(
                assign_table_frame,
                yscrollcommand=table_scroll_bar.set,
                selectmode="extended",
            )
            driver_booking_table.place(
                relx=0.030,
                rely=0.150,
                height=280,
                width=550,
            )
            # driver a scroll bar

            table_scroll_bar.config(
                command=driver_booking_table.yview,
            )

            driver_booking_table["columns"] = (
                "Driver ID",
                "Full Name",
                "Contact",
                "Taxi Number",
            )
            # Format Our Columns

            driver_booking_table.column("#0", width=0, stretch=NO)
            driver_booking_table.column("Driver ID", width=40, anchor=W)
            driver_booking_table.column("Full Name", width=70, anchor=W)
            driver_booking_table.column("Contact", width=70, anchor=W)
            driver_booking_table.column("Taxi Number", width=80, anchor=W)

            # Create Heading

            driver_booking_table.heading("#0", text="", anchor=W)
            driver_booking_table.heading("Driver ID", text="Driver ID", anchor=W)
            driver_booking_table.heading("Full Name", text="Full Name", anchor=W)
            driver_booking_table.heading("Contact", text="Contact", anchor=W)
            driver_booking_table.heading("Taxi Number", text="Taxi Number", anchor=W)

            availavble_driver_control = admin_controller()
            record = availavble_driver_control.booked_driver_fetcher()

            for data in record:
                driver_booking_table.insert(
                    "",
                    index="end",
                    values=(
                        data[0],
                        data[1],
                        data[3],
                        data[4],
                    ),
                )

            assign_button = tk.Button(assign_table_frame)
            assign_button.place(relx=0.400, rely=0.880, height=35, width=120)
            assign_button.configure(
                background="#007074",
                borderwidth="2",
                compound="left",
                font="-family {Noto Sans} -size 14",
                foreground="#FFFFFF",
                text="""Not Now""",
                state="disabled",
            )

    @staticmethod
    def selcted_driver_row_assign(
        driver_booking_table,
        admin_controller,
        booking_details,
        assign_taxi_frame,
    ):
        selected_row = driver_booking_table.focus()
        driver_id = driver_booking_table.item(selected_row, "values")
        seleted_driver_id = driver_id[0]
        booking_id = booking_details[0]

        assign_taxi_controll = admin_controller()
        assign_taxi_controll.assign_controller(seleted_driver_id, booking_id)

        messagebox.showinfo(
            "Sucess",
            "Driver ID "
            + str(seleted_driver_id)
            + " Sucessfully  assigned to booking id "
            + str(booking_id),
        )

        assign_taxi_frame.destroy()
