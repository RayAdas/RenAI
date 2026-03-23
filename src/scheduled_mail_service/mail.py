from typing import Any, TYPE_CHECKING
import datetime

if TYPE_CHECKING:
    from .address import Address

class Mail:
    def __init__(self, sender: "Address", recipient: "Address", payload: Any, scheduled_time: datetime.datetime):
        self.sender = sender
        self.recipient = recipient
        self.payload = payload
        self.scheduled_time = scheduled_time
