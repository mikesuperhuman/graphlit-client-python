# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class CreateSoftware(BaseModel):
    create_software: Optional["CreateSoftwareCreateSoftware"] = Field(
        alias="createSoftware"
    )


class CreateSoftwareCreateSoftware(BaseModel):
    id: str
    name: str


CreateSoftware.model_rebuild()
