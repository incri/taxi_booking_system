from distutils.sysconfig import customize_compiler
import re

from pydantic import BaseModel, root_validator, validator
from tkinter import messagebox
from helper.exceptions import CustomException


name_reg = re.compile("^[A-Z][a-z]+$")  # firstname, lastname regex
contact_reg = re.compile("^[0-9]{10}$")  # contact regex
address_reg = re.compile(".+")  # address not null regex
email_reg = re.compile("[a-z0-9]+@[a-z]+\.[a-z]{2,3}")  # email address regex
username_reg = re.compile("[a-z][a-z0-9]*([._-][a-z0-9]+){0,3}$")  # username regex


class UserModel(BaseModel):

    firstname: str = ""
    lastname: str = ""
    contact: str = ""
    address: str = ""
    email: str = ""
    username: str = ""
    password: str = ""
    confirm_password: str = ""
    user_id: str = ""
    message: str = ""
    profile: str = ""

    @validator("firstname", "lastname")
    def validate_first_name(cls, value):
        if not value:
            raise CustomException(f"{value}cannot be empty")
        if not name_reg.match(value):
            raise CustomException(f"invalid format for {value}")
        return value

    @validator("contact")
    def validate_contact(cls, value):
        if not value:
            raise CustomException("contact cannot be empty")
        if not contact_reg.match(value):
            raise CustomException("invalid format for contact")
        return value

    @validator("address")
    def validate_address(cls, value):
        if not value:
            raise CustomException("address cannot be empty")
        if not address_reg.match(value):
            raise CustomException("invalid format for address")
        return value

    @validator("email")
    def validate_email(cls, value):
        if not value:
            raise CustomException("email cannot be empty")
        if not email_reg.match(value):
            raise CustomException("invalid format for email")
        return value

    @validator("username")
    def validate_username(cls, value):
        if not value:
            raise CustomException("username cannot be empty")
        if not username_reg.match(value):
            raise CustomException("invalid format for username")
        return value

    @root_validator
    def validate_password(cls, value):
        password = value.get("password")
        confirm_password = value.get("confirm_password")
        if not password:
            raise CustomException("password cannot be empty")
        if password != confirm_password:
            raise CustomException("The two passwords did not match.")
        return value
