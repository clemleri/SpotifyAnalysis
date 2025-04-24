# models/owner.py
from models.linked_from import LinkedFromUser
from typing import Optional

class Owner(LinkedFromUser):
    display_name : Optional[str] = None