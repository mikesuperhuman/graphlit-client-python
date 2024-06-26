# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class GetLabel(BaseModel):
    label: Optional["GetLabelLabel"]


class GetLabelLabel(BaseModel):
    id: str
    name: str
    description: Optional[str]
    creation_date: Any = Field(alias="creationDate")


GetLabel.model_rebuild()
