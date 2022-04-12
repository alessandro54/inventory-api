from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    bio: str | None = None
    disabled: bool | None = None

    class Config:
        orm_mode = True


class UserForm(User):
    password_confirmation: str
