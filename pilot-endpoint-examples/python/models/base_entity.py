from .audit_entity import AuditEntity
from typing import Optional

class BaseEntity(AuditEntity):  
    id: Optional[int] = None
