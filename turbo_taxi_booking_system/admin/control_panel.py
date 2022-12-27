import tkinter as tk
from tkinter import W, Scrollbar, ttk
from tkinter.messagebox import NO
from taxi.taxi_register import TaxiRegisterPage
from driver.driver_register import DriverRegisterPage


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

        ControlPanelPage.customer_tabel_data_fetcher(
            admin_controller, control_panel_frame
        )

        control_panel_frame.mainloop()

    @staticmethod
    def customer_tabel_data_fetcher(admin_controller, control_panel_frame):
        user_booking = admin_controller()
        required_customer_data = user_booking.customer_data_fetcher()

        ControlPanelPage.customer_table_frame_build(
            required_customer_data, control_panel_frame
        )

    @staticmethod
    def customer_table_frame_build(record, control_panel_frame):

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
