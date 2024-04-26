# Generated by ariadne-codegen
# Source: ./documents

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class UpdateOrganization(BaseModel):
    update_organization: Optional["UpdateOrganizationUpdateOrganization"] = Field(
        alias="updateOrganization"
    )


class UpdateOrganizationUpdateOrganization(BaseModel):
    id: str
    name: str
    founding_date: Optional[Any] = Field(alias="foundingDate")
    industries: Optional[List[Optional[str]]]
    revenue: Optional[Any]
    revenue_currency: Optional[str] = Field(alias="revenueCurrency")
    investment: Optional[Any]
    investment_currency: Optional[str] = Field(alias="investmentCurrency")


UpdateOrganization.model_rebuild()
