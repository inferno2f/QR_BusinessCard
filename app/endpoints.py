from fastapi import APIRouter, Body

from app.schemas import ContactCard

router = APIRouter()


@router.post("/card")
def create_card(contact: ContactCard):
    details = f"{contact.first_name} {contact.last_name}: {contact.mobile_number}"
    return {"Card": details}
