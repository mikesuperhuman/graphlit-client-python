# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import CollectionTypes, EntityState


class Collection(BaseModel):
    collection: Optional["CollectionCollection"]


class CollectionCollection(BaseModel):
    id: str
    name: str
    creation_date: Any = Field(alias="creationDate")
    owner: "CollectionCollectionOwner"
    state: EntityState
    type: Optional[CollectionTypes]
    contents: Optional[List[Optional["CollectionCollectionContents"]]]


class CollectionCollectionOwner(BaseModel):
    id: str


class CollectionCollectionContents(BaseModel):
    id: str
    name: str


Collection.model_rebuild()
CollectionCollection.model_rebuild()