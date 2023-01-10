from pydantic import BaseModel


class AdminModel(BaseModel):

    username: str = ""
    password: str = ""
