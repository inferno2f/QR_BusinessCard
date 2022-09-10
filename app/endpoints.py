from fastapi import APIRouter, Form

from app.core.vcf_generator import make_vcard_body, write_vcard_file
from app.schemas import ContactCard

router = APIRouter()


@router.post("/card")
def create_card(contact: ContactCard):
    # details = f"{contact.first_name} {contact.last_name}: {contact.mobile_number}"
    card = make_vcard_body(contact.first_name, contact.last_name, contact.phone)
    card_file = write_vcard_file(f"{contact.first_name}_{contact.last_name}.vcf", card)
    return {"Card": card_file}

@router.post("/login")
def login(username: str = Form(), password: str = Form()):
    return {'username': username}
