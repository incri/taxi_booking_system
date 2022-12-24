from pydantic import BaseModel, validator

from helper.exceptions import CustomException


class TaxiModel(BaseModel):

    brand: str = ""
    model: str = ""
    taxi_number: str = ""
    taxi_age: str = ""
    discription: str = ""

    @validator("brand")
    def validate_brand(cls, value):
        if not value:
            raise CustomException("brand cannot be empty")
        return value

    @validator("model")
    def validate_model(cls, value):
        if not value:
            raise CustomException("model cannot be empty")
        return value

    @validator("taxi_number")
    def validate_taxi_number(cls, value):
        if not value:
            raise CustomException("taxi number cannot be empty")
        return value
