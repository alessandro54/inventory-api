from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    email: str
    first_name: str
    last_name: str
    bio: str
    disabled: bool

    class Config:
        orm_mode = True
