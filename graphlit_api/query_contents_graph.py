# Generated by ariadne-codegen
# Source: ./documents

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import EntityTypes


class QueryContentsGraph(BaseModel):
    contents: Optional["QueryContentsGraphContents"]


class QueryContentsGraphContents(BaseModel):
    graph: Optional["QueryContentsGraphContentsGraph"]


class QueryContentsGraphContentsGraph(BaseModel):
    nodes: Optional[List[Optional["QueryContentsGraphContentsGraphNodes"]]]
    edges: Optional[List[Optional["QueryContentsGraphContentsGraphEdges"]]]


class QueryContentsGraphContentsGraphNodes(BaseModel):
    id: str
    name: str
    type: EntityTypes
    metadata: Optional[str]


class QueryContentsGraphContentsGraphEdges(BaseModel):
    from_: str = Field(alias="from")
    to: str
    relation: Optional[str]


QueryContentsGraph.model_rebuild()
QueryContentsGraphContents.model_rebuild()
QueryContentsGraphContentsGraph.model_rebuild()