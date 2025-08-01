from pydantic import BaseModel
from datetime import datetime

class RecordAccessTokenResponse(BaseModel):
    recordId: str
    accessToken: str
    createdAt: datetime
    active: bool