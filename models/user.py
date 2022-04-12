from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str
    name: str
    bio: str
    disabled: bool

    class Config:
        orm_mode = True
