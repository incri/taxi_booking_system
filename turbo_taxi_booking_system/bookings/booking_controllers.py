from tkinter import messagebox
from helper.turbo_db import Turbo_db
from datetime import date, datetime


class BookingController:
    def __init__(self) -> None:
        self._connection = Turbo_db.turbo_connection()

    def booking_control(self, user_booking, booking_form_frame):
        if self.authenticate_booking(user_booking):
            self.booking_sucess(booking_form_frame)

    def authenticate_booking(self, user_booking):

        booking_created_at_date = date.today()
        now = datetime.now()
        booking_created_at_time = now.strftime("%H:%M:%S")

        try:
            cursor = self._connection.cursor()
            statement = """CREATE TABLE IF NOT EXISTS booking(
                booking_id          SERIAL PRIMARY KEY,
                user_id             INT NOT NULL,
                firstname           VARCHAR(50) NOT NULL,
                lastname            VARCHAR(50) NOT NULL,
                no_of_passenger     VARCHAR(10) NOT NULL,
                no_of_taxi          VARCHAR(10) NOT NULL,
                pickup_date         VARCHAR(20) NOT NULL,
                pickup_time_hrs      VARCHAR(10) NOT NULL,
                pickup_time_min      VARCHAR(10) NOT NULL,
                pickup_location     VARCHAR(100) NOT NULL,
                destination         VARCHAR(100) NOT NULL,
                total_cost          VARCHAR(20) NOT NULL,
                payment_method      VARCHAR(20) NOT NULL,
                card_number         VARCHAR(50),
                card_exp            VARCHAR(20),
                card_cvv            VARCHAR(10),
                booking_status      VARCHAR(20),
                created_at_date     VARCHAR(30),
                created_at_time     VARCHAR(30),
                pickup_coordinate   VARCHAR(100),
                destination_coordinate  VARCHAR(100)


            );"""

            dataInsert = """INSERT INTO booking(user_id, firstname, lastname, \
                no_of_passenger, no_of_taxi, pickup_date, pickup_time_hrs, \
                pickup_time_min, pickup_location, destination, total_cost, \
                payment_method, card_number, card_exp, card_cvv, booking_status, created_at_date, created_at_time, \
                pickup_coordinate, destination_coordinate) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

            dataValues = (
                user_booking.user_id,
                user_booking.firstname,
                user_booking.lastname,
                user_booking.no_of_pass,
                user_booking.no_of_taxi,
                user_booking.pick_up_date,
                user_booking.pick_up_hrs,
                user_booking.pick_up_min,
                user_booking.pick_up_location,
                user_booking.destination,
                user_booking.total_cost,
                user_booking.payment_method,
                user_booking.card_number,
                user_booking.exp_date,
                user_booking.cvv,
                "Pending",
                booking_created_at_date,
                booking_created_at_time,
                user_booking.pickup_coordinates,
                user_booking.destination_coordinates,
            )
            cursor.execute(statement)
            cursor.execute(dataInsert, dataValues)
            self._connection.commit()
        except Exception as error:
            print(error)
        finally:
            if cursor is not None:
                cursor.close()
            if self._connection is not None:
                self._connection.close()
                return True

    def booking_sucess(self, booking_form_frame):
        messagebox.showinfo(
            "Booking Completed",
            "Congatulation, Your Booking Request Has Been Sent",
        )
        booking_form_frame.destroy()
