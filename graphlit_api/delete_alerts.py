# Generated by ariadne-codegen
# Source: ./documents

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityState


class DeleteAlerts(BaseModel):
    delete_alerts: Optional[List[Optional["DeleteAlertsDeleteAlerts"]]] = Field(
        alias="deleteAlerts"
    )


class DeleteAlertsDeleteAlerts(BaseModel):
    id: str
    state: EntityState


DeleteAlerts.model_rebuild()