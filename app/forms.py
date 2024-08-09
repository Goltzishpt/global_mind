from pydantic import BaseModel, EmailStr


class DeviceForm(BaseModel):
    name: str
    type_data: str
    login: str
    password: str
    location_id: int
    api_user_id: int


class ApiUserForm(BaseModel):
    name: str
    email: EmailStr
    password: str


class LocationForm(BaseModel):
    name: str

