from datetime import datetime
from decimal import Decimal
from typing import Optional
import uuid
from pydantic import BaseModel


def create_id():
    random_uuid = uuid.uuid4()
    uuid_str = str(random_uuid)
    return uuid_str


class Product(BaseModel):
    id: Optional[str] = create_id()
    name: str
    description: str
    price: Decimal
    creation_date: str = datetime.now().isoformat()
