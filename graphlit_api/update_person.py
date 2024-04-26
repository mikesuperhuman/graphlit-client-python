# Generated by ariadne-codegen
# Source: ./documents

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class UpdatePerson(BaseModel):
    update_person: Optional["UpdatePersonUpdatePerson"] = Field(alias="updatePerson")


class UpdatePersonUpdatePerson(BaseModel):
    id: str
    name: str


UpdatePerson.model_rebuild()
