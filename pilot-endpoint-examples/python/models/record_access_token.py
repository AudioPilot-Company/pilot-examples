from models.common import BaseEntity
from datetime import datetime

class RecordAccessTokenResponse(BaseEntity):
    recordId: str
    accessToken: str
    createdAt: datetime
    active: bool