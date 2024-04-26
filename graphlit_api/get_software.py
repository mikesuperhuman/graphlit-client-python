# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetSoftware(BaseModel):
    software: Optional["GetSoftwareSoftware"]


class GetSoftwareSoftware(BaseModel):
    id: str
    name: str
    alternate_names: Optional[List[Optional[str]]] = Field(alias="alternateNames")
    creation_date: Any = Field(alias="creationDate")
    release_date: Optional[Any] = Field(alias="releaseDate")
    developer: Optional[str]


GetSoftware.model_rebuild()
