# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    AzureDocumentIntelligenceModels,
    ContentTypes,
    DeepgramModels,
    EntityEnrichmentServiceTypes,
    EntityExtractionServiceTypes,
    EntityState,
    FilePreparationServiceTypes,
    FileTypes,
    IntegrationServiceTypes,
    LinkTypes,
    ObservableTypes,
    OpenAIVisionDetailLevels,
    SummarizationTypes,
)


class Workflow(BaseModel):
    workflow: Optional["WorkflowWorkflow"]


class WorkflowWorkflow(BaseModel):
    id: str
    name: str
    creation_date: Any = Field(alias="creationDate")
    owner: "WorkflowWorkflowOwner"
    state: EntityState
    ingestion: Optional["WorkflowWorkflowIngestion"]
    preparation: Optional["WorkflowWorkflowPreparation"]
    extraction: Optional["WorkflowWorkflowExtraction"]
    enrichment: Optional["WorkflowWorkflowEnrichment"]
    actions: Optional[List[Optional["WorkflowWorkflowActions"]]]


class WorkflowWorkflowOwner(BaseModel):
    id: str


class WorkflowWorkflowIngestion(BaseModel):
    if_: Optional["WorkflowWorkflowIngestionIf"] = Field(alias="if")
    collections: Optional[List[Optional["WorkflowWorkflowIngestionCollections"]]]


class WorkflowWorkflowIngestionIf(BaseModel):
    types: Optional[List[Optional[ContentTypes]]]
    file_types: Optional[List[Optional[FileTypes]]] = Field(alias="fileTypes")


class WorkflowWorkflowIngestionCollections(BaseModel):
    id: str


class WorkflowWorkflowPreparation(BaseModel):
    disable_smart_capture: Optional[bool] = Field(alias="disableSmartCapture")
    summarizations: Optional[
        List[Optional["WorkflowWorkflowPreparationSummarizations"]]
    ]
    jobs: Optional[List[Optional["WorkflowWorkflowPreparationJobs"]]]


class WorkflowWorkflowPreparationSummarizations(BaseModel):
    type: SummarizationTypes
    specification: Optional["WorkflowWorkflowPreparationSummarizationsSpecification"]
    tokens: Optional[int]
    items: Optional[int]


class WorkflowWorkflowPreparationSummarizationsSpecification(BaseModel):
    id: str


class WorkflowWorkflowPreparationJobs(BaseModel):
    connector: Optional["WorkflowWorkflowPreparationJobsConnector"]


class WorkflowWorkflowPreparationJobsConnector(BaseModel):
    type: FilePreparationServiceTypes
    file_types: Optional[List[FileTypes]] = Field(alias="fileTypes")
    azure_document: Optional[
        "WorkflowWorkflowPreparationJobsConnectorAzureDocument"
    ] = Field(alias="azureDocument")
    deepgram: Optional["WorkflowWorkflowPreparationJobsConnectorDeepgram"]
    document: Optional["WorkflowWorkflowPreparationJobsConnectorDocument"]
    email: Optional["WorkflowWorkflowPreparationJobsConnectorEmail"]


class WorkflowWorkflowPreparationJobsConnectorAzureDocument(BaseModel):
    model: Optional[AzureDocumentIntelligenceModels]


class WorkflowWorkflowPreparationJobsConnectorDeepgram(BaseModel):
    model: Optional[DeepgramModels]
    key: Optional[str]
    enable_redaction: Optional[bool] = Field(alias="enableRedaction")
    enable_speaker_diarization: Optional[bool] = Field(alias="enableSpeakerDiarization")


class WorkflowWorkflowPreparationJobsConnectorDocument(BaseModel):
    include_images: Optional[bool] = Field(alias="includeImages")


class WorkflowWorkflowPreparationJobsConnectorEmail(BaseModel):
    include_attachments: Optional[bool] = Field(alias="includeAttachments")


class WorkflowWorkflowExtraction(BaseModel):
    jobs: Optional[List[Optional["WorkflowWorkflowExtractionJobs"]]]


class WorkflowWorkflowExtractionJobs(BaseModel):
    connector: Optional["WorkflowWorkflowExtractionJobsConnector"]


class WorkflowWorkflowExtractionJobsConnector(BaseModel):
    type: EntityExtractionServiceTypes
    content_types: Optional[List[ContentTypes]] = Field(alias="contentTypes")
    file_types: Optional[List[FileTypes]] = Field(alias="fileTypes")
    extracted_types: Optional[List[ObservableTypes]] = Field(alias="extractedTypes")
    azure_text: Optional["WorkflowWorkflowExtractionJobsConnectorAzureText"] = Field(
        alias="azureText"
    )
    azure_image: Optional["WorkflowWorkflowExtractionJobsConnectorAzureImage"] = Field(
        alias="azureImage"
    )
    open_ai_image: Optional["WorkflowWorkflowExtractionJobsConnectorOpenAiImage"] = (
        Field(alias="openAIImage")
    )
    model_text: Optional["WorkflowWorkflowExtractionJobsConnectorModelText"] = Field(
        alias="modelText"
    )


class WorkflowWorkflowExtractionJobsConnectorAzureText(BaseModel):
    confidence_threshold: Optional[float] = Field(alias="confidenceThreshold")
    enable_pii: Optional[bool] = Field(alias="enablePII")


class WorkflowWorkflowExtractionJobsConnectorAzureImage(BaseModel):
    confidence_threshold: Optional[float] = Field(alias="confidenceThreshold")


class WorkflowWorkflowExtractionJobsConnectorOpenAiImage(BaseModel):
    confidence_threshold: Optional[float] = Field(alias="confidenceThreshold")
    detail_level: Optional[OpenAIVisionDetailLevels] = Field(alias="detailLevel")


class WorkflowWorkflowExtractionJobsConnectorModelText(BaseModel):
    specification: Optional[
        "WorkflowWorkflowExtractionJobsConnectorModelTextSpecification"
    ]


class WorkflowWorkflowExtractionJobsConnectorModelTextSpecification(BaseModel):
    id: str


class WorkflowWorkflowEnrichment(BaseModel):
    link: Optional["WorkflowWorkflowEnrichmentLink"]
    jobs: Optional[List[Optional["WorkflowWorkflowEnrichmentJobs"]]]


class WorkflowWorkflowEnrichmentLink(BaseModel):
    enable_crawling: Optional[bool] = Field(alias="enableCrawling")
    allowed_domains: Optional[List[str]] = Field(alias="allowedDomains")
    excluded_domains: Optional[List[str]] = Field(alias="excludedDomains")
    allowed_links: Optional[List[LinkTypes]] = Field(alias="allowedLinks")
    excluded_links: Optional[List[LinkTypes]] = Field(alias="excludedLinks")
    allowed_files: Optional[List[FileTypes]] = Field(alias="allowedFiles")
    excluded_files: Optional[List[FileTypes]] = Field(alias="excludedFiles")
    allow_content_domain: Optional[bool] = Field(alias="allowContentDomain")
    maximum_links: Optional[int] = Field(alias="maximumLinks")


class WorkflowWorkflowEnrichmentJobs(BaseModel):
    connector: Optional["WorkflowWorkflowEnrichmentJobsConnector"]


class WorkflowWorkflowEnrichmentJobsConnector(BaseModel):
    type: Optional[EntityEnrichmentServiceTypes]
    enriched_types: Optional[List[Optional[ObservableTypes]]] = Field(
        alias="enrichedTypes"
    )


class WorkflowWorkflowActions(BaseModel):
    connector: Optional["WorkflowWorkflowActionsConnector"]


class WorkflowWorkflowActionsConnector(BaseModel):
    type: IntegrationServiceTypes
    uri: Optional[str]
    slack: Optional["WorkflowWorkflowActionsConnectorSlack"]


class WorkflowWorkflowActionsConnectorSlack(BaseModel):
    token: str
    channel: str


Workflow.model_rebuild()
WorkflowWorkflow.model_rebuild()
WorkflowWorkflowIngestion.model_rebuild()
WorkflowWorkflowPreparation.model_rebuild()
WorkflowWorkflowPreparationSummarizations.model_rebuild()
WorkflowWorkflowPreparationJobs.model_rebuild()
WorkflowWorkflowPreparationJobsConnector.model_rebuild()
WorkflowWorkflowExtraction.model_rebuild()
WorkflowWorkflowExtractionJobs.model_rebuild()
WorkflowWorkflowExtractionJobsConnector.model_rebuild()
WorkflowWorkflowExtractionJobsConnectorModelText.model_rebuild()
WorkflowWorkflowEnrichment.model_rebuild()
WorkflowWorkflowEnrichmentJobs.model_rebuild()
WorkflowWorkflowActions.model_rebuild()
WorkflowWorkflowActionsConnector.model_rebuild()