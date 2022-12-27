from pydantic import BaseModel, validator
from helper.exceptions import CustomException
import re


name_reg = re.compile(
    "^[A-Z][a-zA-Z]{3,}(?: [A-Z][a-zA-Z]*){0,2}$",
)  # fullname regex
contact_reg = re.compile("^[0-9]{10}$")  # contact regex


class DriverModel(BaseModel):

    fullname: str = ""
    license_number: str = ""
    contact: str = ""
    taxi_number: str = ""

    @validator("fullname")
    def fullname_validator(cls, value):
        if not value:
            raise CustomException("please enter your fullname !!")
        if not name_reg.match(value):
            raise CustomException("invalid firname format !!")
        return value

    @validator("license_number")
    def validate_license_number(cls, value):
        if not value:
            raise CustomException("license number cannot be empty")
        return value

    @validator("contact")
    def validate_contact(cls, value):
        if not value:
            raise CustomException("contact cannot be empty")
        if not contact_reg.match(value):
            raise CustomException("invalid format for contact")
        return value

    @validator("taxi_number")
    def validate_taxi_number(cls, value):
        if not value:
            raise CustomException("taxi number cannot be empty !!")
        if value == "taxi_number":
            raise CustomException("please select taxi number!!")
        return value
