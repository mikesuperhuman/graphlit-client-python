# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class QuerySoftware(BaseModel):
    softwares: Optional["QuerySoftwareSoftwares"]


class QuerySoftwareSoftwares(BaseModel):
    results: Optional[List[Optional["QuerySoftwareSoftwaresResults"]]]


class QuerySoftwareSoftwaresResults(BaseModel):
    id: str
    name: str
    alternate_names: Optional[List[Optional[str]]] = Field(alias="alternateNames")
    creation_date: Any = Field(alias="creationDate")
    release_date: Optional[Any] = Field(alias="releaseDate")
    developer: Optional[str]


QuerySoftware.model_rebuild()
QuerySoftwareSoftwares.model_rebuild()