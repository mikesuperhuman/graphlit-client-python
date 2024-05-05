# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    ContentFacetTypes,
    ContentTypes,
    ConversationRoleTypes,
    EntityState,
    FacetValueTypes,
    FileTypes,
    ModelServiceTypes,
    ObservableTypes,
)


class PromptConversation(BaseModel):
    prompt_conversation: Optional["PromptConversationPromptConversation"] = Field(
        alias="promptConversation"
    )


class PromptConversationPromptConversation(BaseModel):
    conversation: Optional["PromptConversationPromptConversationConversation"]
    message: Optional["PromptConversationPromptConversationMessage"]
    message_count: Optional[int] = Field(alias="messageCount")
    facets: Optional[List[Optional["PromptConversationPromptConversationFacets"]]]


class PromptConversationPromptConversationConversation(BaseModel):
    id: str


class PromptConversationPromptConversationMessage(BaseModel):
    role: ConversationRoleTypes
    author: Optional[str]
    message: str
    citations: Optional[
        List[Optional["PromptConversationPromptConversationMessageCitations"]]
    ]
    tokens: int
    throughput: Optional[float]
    completion_time: Optional[Any] = Field(alias="completionTime")
    timestamp: Any
    model_service: Optional[ModelServiceTypes] = Field(alias="modelService")
    model: Optional[str]


class PromptConversationPromptConversationMessageCitations(BaseModel):
    content: Optional["PromptConversationPromptConversationMessageCitationsContent"]
    index: Optional[int]
    text: Optional[str]
    start_time: Optional[Any] = Field(alias="startTime")
    end_time: Optional[Any] = Field(alias="endTime")
    page_number: Optional[int] = Field(alias="pageNumber")
    frame_number: Optional[int] = Field(alias="frameNumber")


class PromptConversationPromptConversationMessageCitationsContent(BaseModel):
    id: str
    name: str
    state: EntityState
    type: Optional[ContentTypes]
    file_type: Optional[FileTypes] = Field(alias="fileType")
    file_name: Optional[str] = Field(alias="fileName")
    original_date: Optional[Any] = Field(alias="originalDate")
    uri: Optional[Any]


class PromptConversationPromptConversationFacets(BaseModel):
    type: Optional[FacetValueTypes]
    value: Optional[str]
    range: Optional["PromptConversationPromptConversationFacetsRange"]
    count: Optional[Any]
    facet: Optional[ContentFacetTypes]
    observable: Optional["PromptConversationPromptConversationFacetsObservable"]


class PromptConversationPromptConversationFacetsRange(BaseModel):
    from_: Optional[str] = Field(alias="from")
    to: Optional[str]


class PromptConversationPromptConversationFacetsObservable(BaseModel):
    type: Optional[ObservableTypes]
    observable: Optional[
        "PromptConversationPromptConversationFacetsObservableObservable"
    ]


class PromptConversationPromptConversationFacetsObservableObservable(BaseModel):
    id: str
    name: Optional[str]


PromptConversation.model_rebuild()
PromptConversationPromptConversation.model_rebuild()
PromptConversationPromptConversationMessage.model_rebuild()
PromptConversationPromptConversationMessageCitations.model_rebuild()
PromptConversationPromptConversationFacets.model_rebuild()
PromptConversationPromptConversationFacetsObservable.model_rebuild()
