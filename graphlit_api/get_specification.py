# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    AnthropicModels,
    AzureOpenAIModels,
    ConversationStrategyTypes,
    EntityState,
    ModelServiceTypes,
    OpenAIModels,
    PromptStrategyTypes,
    ReplicateModels,
    RetrievalStrategyTypes,
    SpecificationTypes,
)


class GetSpecification(BaseModel):
    specification: Optional["GetSpecificationSpecification"]


class GetSpecificationSpecification(BaseModel):
    id: str
    name: str
    creation_date: Any = Field(alias="creationDate")
    owner: "GetSpecificationSpecificationOwner"
    state: EntityState
    type: Optional[SpecificationTypes]
    service_type: Optional[ModelServiceTypes] = Field(alias="serviceType")
    system_prompt: Optional[str] = Field(alias="systemPrompt")
    custom_guidance: Optional[str] = Field(alias="customGuidance")
    strategy: Optional["GetSpecificationSpecificationStrategy"]
    prompt_strategy: Optional["GetSpecificationSpecificationPromptStrategy"] = Field(
        alias="promptStrategy"
    )
    retrieval_strategy: Optional["GetSpecificationSpecificationRetrievalStrategy"] = (
        Field(alias="retrievalStrategy")
    )
    reranking_strategy: Optional["GetSpecificationSpecificationRerankingStrategy"] = (
        Field(alias="rerankingStrategy")
    )
    open_ai: Optional["GetSpecificationSpecificationOpenAi"] = Field(alias="openAI")
    azure_open_ai: Optional["GetSpecificationSpecificationAzureOpenAi"] = Field(
        alias="azureOpenAI"
    )
    anthropic: Optional["GetSpecificationSpecificationAnthropic"]
    replicate: Optional["GetSpecificationSpecificationReplicate"]
    tools: Optional[List["GetSpecificationSpecificationTools"]]


class GetSpecificationSpecificationOwner(BaseModel):
    id: str


class GetSpecificationSpecificationStrategy(BaseModel):
    type: Optional[ConversationStrategyTypes]
    message_limit: Optional[int] = Field(alias="messageLimit")
    embed_citations: Optional[bool] = Field(alias="embedCitations")
    enable_facets: Optional[bool] = Field(alias="enableFacets")
    messages_weight: Optional[float] = Field(alias="messagesWeight")
    contents_weight: Optional[float] = Field(alias="contentsWeight")


class GetSpecificationSpecificationPromptStrategy(BaseModel):
    type: PromptStrategyTypes


class GetSpecificationSpecificationRetrievalStrategy(BaseModel):
    type: RetrievalStrategyTypes
    content_limit: Optional[int] = Field(alias="contentLimit")


class GetSpecificationSpecificationRerankingStrategy(BaseModel):
    service_type: ModelServiceTypes = Field(alias="serviceType")


class GetSpecificationSpecificationOpenAi(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: OpenAIModels
    key: Optional[str]
    model_name: Optional[str] = Field(alias="modelName")
    temperature: Optional[float]
    probability: Optional[float]


class GetSpecificationSpecificationAzureOpenAi(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: AzureOpenAIModels
    key: Optional[str]
    endpoint: Optional[Any]
    deployment_name: Optional[str] = Field(alias="deploymentName")
    temperature: Optional[float]
    probability: Optional[float]


class GetSpecificationSpecificationAnthropic(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: AnthropicModels
    key: Optional[str]
    model_name: Optional[str] = Field(alias="modelName")
    temperature: Optional[float]
    probability: Optional[float]


class GetSpecificationSpecificationReplicate(BaseModel):
    token_limit: Optional[int] = Field(alias="tokenLimit")
    completion_token_limit: Optional[int] = Field(alias="completionTokenLimit")
    model: ReplicateModels
    key: Optional[str]
    model_name: Optional[str] = Field(alias="modelName")
    temperature: Optional[float]
    probability: Optional[float]


class GetSpecificationSpecificationTools(BaseModel):
    name: str
    description: Optional[str]
    schema_: str = Field(alias="schema")
    uri: Optional[Any]


GetSpecification.model_rebuild()
GetSpecificationSpecification.model_rebuild()