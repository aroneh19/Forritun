from typing import Any
from message import Message

class SignatureMessage(Message):
    def __init__(self, msg_from, msg_to, signature):
        super().__init__(msg_from, msg_to)
        self.signature = signature
    
    def __str__(self):
        return super().__str__() + f"\n{self.signature}"
