from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    bio: str | None = None
    disabled: bool | None = None
    deleted: bool | None = None


class User (UserBase):
    id: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str
    password_confirmation: str
