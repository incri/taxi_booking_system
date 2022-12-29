from ast import Return
import re
from pydantic import BaseModel, ValidationError, root_validator, validator
from helper.exceptions import CustomException


name_reg = re.compile("^[A-Z][a-z]+$")  # firstname, lastname regex


class BookingModel(BaseModel):

    booking_id: str = ""
    user_id: str = ""
    firstname: str = ""
    lastname: str = ""
    no_of_pass: str = ""
    no_of_taxi: str = ""
    pick_up_date: str = ""
    pick_up_hrs: int = 0
    pick_up_min: int = 0
    pick_up_location: str = ""
    destination: str = ""
    total_cost: str = ""
    payment_method: str = ""
    card_number: str = ""
    exp_date: str = ""
    cvv: str = ""
    pickup_coordinates: str = ""
    destination_coordinates: str = ""

    @validator("firstname", "lastname")
    def validate_name(cls, value):
        if not value:
            raise CustomException("name cannot be empty")
        if not name_reg.match(value):
            raise CustomException("invalid format for name")
        return value

    @root_validator
    def validate_time(cls, value):
        pick_up_hrs = value.get("pick_up_hrs")
        pick_up_min = value.get("pick_up_min")
        if pick_up_hrs == "" and pick_up_hrs:
            raise CustomException("time(Hour) cannot be empty")
        if pick_up_min == "":
            raise CustomException("time(Minutes) cannot be empty")

        if pick_up_hrs == str:
            raise CustomException("time(Hour) invalid")
        if pick_up_min == str:
            raise CustomException("time(Minutes) invalid")

        if pick_up_hrs >= 24:
            raise CustomException("time(Hour) invalid")
        if pick_up_min >= 60:
            raise CustomException("time(Minutes) invalid")
        return value

    @root_validator
    def validate_location(cls, value):
        pick_up_location = value.get("pick_up_location")
        destination = value.get("destination")
        if not pick_up_location:
            raise CustomException("pickup location cannot be empty")
        if not destination:
            raise CustomException("destination location cannot be empty")
        return value

    @root_validator
    def validate_card_details(cls, value):
        payment_method = value.get("payment_method")
        credit_number = value.get("card_number")
        exp_date = value.get("exp_date")
        cvv = value.get("cvv")
        if payment_method == "Credit Card":
            if credit_number == "":
                raise CustomException("credit number cannot be empty!!")
            if exp_date == "":
                raise CustomException("exp date cannot be empty!!")
            if cvv == "":
                raise CustomException("cvv cannot be empty!!")
            return value
        else:
            return value
