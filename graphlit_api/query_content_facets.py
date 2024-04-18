# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from .base_model import BaseModel
from .enums import ContentFacetTypes, FacetValueTypes, ObservableTypes


class QueryContentFacets(BaseModel):
    contents: Optional["QueryContentFacetsContents"]


class QueryContentFacetsContents(BaseModel):
    facets: Optional[List[Optional["QueryContentFacetsContentsFacets"]]]


class QueryContentFacetsContentsFacets(BaseModel):
    facet: Optional[ContentFacetTypes]
    type: Optional[FacetValueTypes]
    observable: Optional["QueryContentFacetsContentsFacetsObservable"]
    count: Optional[Any]


class QueryContentFacetsContentsFacetsObservable(BaseModel):
    type: Optional[ObservableTypes]
    observable: Optional["QueryContentFacetsContentsFacetsObservableObservable"]


class QueryContentFacetsContentsFacetsObservableObservable(BaseModel):
    id: str
    name: Optional[str]


QueryContentFacets.model_rebuild()
QueryContentFacetsContents.model_rebuild()
QueryContentFacetsContentsFacets.model_rebuild()
QueryContentFacetsContentsFacetsObservable.model_rebuild()