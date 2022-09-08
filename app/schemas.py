from pydantic import BaseModel, Field, EmailStr, constr
from typing import Optional


class ContactCard(BaseModel):
    first_name: str
    last_name: str
    mobile_number: Optional[
        constr(
            strip_whitespace=True,
            regex=r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        )
    ] = Field(min_length=7, max_length=19, description='Phone number')
    email: Optional[EmailStr] = Field(description='Email address')
    website: Optional[str]

    class Config:
        title = 'Basic class for business card info'
        schema_extra = {
            'example': {
                'first_name': 'John',
                'last_name': 'Doe',
                'mobile_number': '+1 (305) 409 39 31',
                'email': 'john@doe.com',
                'website': 'github.com/johndoe'
            }
        }
