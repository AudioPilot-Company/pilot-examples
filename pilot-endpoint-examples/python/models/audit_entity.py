from datetime import datetime
from pydantic import BaseModel

class AuditEntity(BaseModel):  
    createdAt: datetime
    updatedAt: datetime
    createdBy: str
    updatedBy: str