"""
Partner Relationship Management (PRM) - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    ChannelPartnerProfileService,
    PartnerTierLevelService,
    DealRegistrationLeadService,
    MDFMarketFundRequestService,
    CoMarketingCampaignService,
    PartnerCommissionPayoutService,
    CertificationCredentialService,
    PartnerSalesGoalService,
    ResellerAgreementContractService,
    LeadDistributionRuleService,
    PartnerPortalCredentialService,
    ChannelConflictDisputeService,
    TerritoryPartnerExclusivityService,
    PartnerTrainingProgressService,
    JointSolutionListingService,
    ChannelRevenueForecastService,
)
from .schemas import (
    ChannelPartnerProfileCreateSchema, ChannelPartnerProfileUpdateSchema, ChannelPartnerProfileResponseSchema,
    PartnerTierLevelCreateSchema, PartnerTierLevelUpdateSchema, PartnerTierLevelResponseSchema,
    DealRegistrationLeadCreateSchema, DealRegistrationLeadUpdateSchema, DealRegistrationLeadResponseSchema,
    MDFMarketFundRequestCreateSchema, MDFMarketFundRequestUpdateSchema, MDFMarketFundRequestResponseSchema,
    CoMarketingCampaignCreateSchema, CoMarketingCampaignUpdateSchema, CoMarketingCampaignResponseSchema,
    PartnerCommissionPayoutCreateSchema, PartnerCommissionPayoutUpdateSchema, PartnerCommissionPayoutResponseSchema,
    CertificationCredentialCreateSchema, CertificationCredentialUpdateSchema, CertificationCredentialResponseSchema,
    PartnerSalesGoalCreateSchema, PartnerSalesGoalUpdateSchema, PartnerSalesGoalResponseSchema,
    ResellerAgreementContractCreateSchema, ResellerAgreementContractUpdateSchema, ResellerAgreementContractResponseSchema,
    LeadDistributionRuleCreateSchema, LeadDistributionRuleUpdateSchema, LeadDistributionRuleResponseSchema,
    PartnerPortalCredentialCreateSchema, PartnerPortalCredentialUpdateSchema, PartnerPortalCredentialResponseSchema,
    ChannelConflictDisputeCreateSchema, ChannelConflictDisputeUpdateSchema, ChannelConflictDisputeResponseSchema,
    TerritoryPartnerExclusivityCreateSchema, TerritoryPartnerExclusivityUpdateSchema, TerritoryPartnerExclusivityResponseSchema,
    PartnerTrainingProgressCreateSchema, PartnerTrainingProgressUpdateSchema, PartnerTrainingProgressResponseSchema,
    JointSolutionListingCreateSchema, JointSolutionListingUpdateSchema, JointSolutionListingResponseSchema,
    ChannelRevenueForecastCreateSchema, ChannelRevenueForecastUpdateSchema, ChannelRevenueForecastResponseSchema,
)

router = APIRouter(prefix="/partner_network", tags=["Partner Relationship Management (PRM)"])

# ==================== ChannelPartnerProfile Endpoints ====================
@router.get("/channelpartnerprofiles", response_model=List[Dict[str, Any]])
def list_channelpartnerprofiles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ChannelPartnerProfile records with pagination and filtering."""
    svc = ChannelPartnerProfileService()
    items = svc.list_channelpartnerprofiles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/channelpartnerprofiles/{item_id}", response_model=Dict[str, Any])
def get_channelpartnerprofile_by_id(item_id: int):
    """Retrieve detailed record for ChannelPartnerProfile by ID."""
    svc = ChannelPartnerProfileService()
    item = svc.get_channelpartnerprofile_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ChannelPartnerProfile with ID {item_id} not found")
    return item.to_dict()

@router.post("/channelpartnerprofiles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_channelpartnerprofile(payload: ChannelPartnerProfileCreateSchema):
    """Create new ChannelPartnerProfile instance in enterprise repository."""
    svc = ChannelPartnerProfileService()
    try:
        item = svc.create_channelpartnerprofile(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/channelpartnerprofiles/{item_id}", response_model=Dict[str, Any])
def update_channelpartnerprofile(item_id: int, payload: ChannelPartnerProfileUpdateSchema):
    """Update existing ChannelPartnerProfile record fields."""
    svc = ChannelPartnerProfileService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_channelpartnerprofile(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ChannelPartnerProfile with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/channelpartnerprofiles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_channelpartnerprofile(item_id: int, hard: bool = Query(False)):
    """Delete ChannelPartnerProfile record (soft-delete by default)."""
    svc = ChannelPartnerProfileService()
    ok = svc.delete_channelpartnerprofile(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ChannelPartnerProfile with ID {item_id} not found")
    return None

@router.get("/channelpartnerprofiles/analytics/metrics", response_model=Dict[str, Any])
def get_channelpartnerprofile_metrics():
    """Calculate summary statistical KPIs for ChannelPartnerProfile collection."""
    svc = ChannelPartnerProfileService()
    return svc.calculate_aggregate_metrics()

# ==================== PartnerTierLevel Endpoints ====================
@router.get("/partnertierlevels", response_model=List[Dict[str, Any]])
def list_partnertierlevels(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PartnerTierLevel records with pagination and filtering."""
    svc = PartnerTierLevelService()
    items = svc.list_partnertierlevels(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/partnertierlevels/{item_id}", response_model=Dict[str, Any])
def get_partnertierlevel_by_id(item_id: int):
    """Retrieve detailed record for PartnerTierLevel by ID."""
    svc = PartnerTierLevelService()
    item = svc.get_partnertierlevel_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PartnerTierLevel with ID {item_id} not found")
    return item.to_dict()

@router.post("/partnertierlevels", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_partnertierlevel(payload: PartnerTierLevelCreateSchema):
    """Create new PartnerTierLevel instance in enterprise repository."""
    svc = PartnerTierLevelService()
    try:
        item = svc.create_partnertierlevel(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/partnertierlevels/{item_id}", response_model=Dict[str, Any])
def update_partnertierlevel(item_id: int, payload: PartnerTierLevelUpdateSchema):
    """Update existing PartnerTierLevel record fields."""
    svc = PartnerTierLevelService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_partnertierlevel(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PartnerTierLevel with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/partnertierlevels/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_partnertierlevel(item_id: int, hard: bool = Query(False)):
    """Delete PartnerTierLevel record (soft-delete by default)."""
    svc = PartnerTierLevelService()
    ok = svc.delete_partnertierlevel(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PartnerTierLevel with ID {item_id} not found")
    return None

@router.get("/partnertierlevels/analytics/metrics", response_model=Dict[str, Any])
def get_partnertierlevel_metrics():
    """Calculate summary statistical KPIs for PartnerTierLevel collection."""
    svc = PartnerTierLevelService()
    return svc.calculate_aggregate_metrics()

# ==================== DealRegistrationLead Endpoints ====================
@router.get("/dealregistrationleads", response_model=List[Dict[str, Any]])
def list_dealregistrationleads(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DealRegistrationLead records with pagination and filtering."""
    svc = DealRegistrationLeadService()
    items = svc.list_dealregistrationleads(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dealregistrationleads/{item_id}", response_model=Dict[str, Any])
def get_dealregistrationlead_by_id(item_id: int):
    """Retrieve detailed record for DealRegistrationLead by ID."""
    svc = DealRegistrationLeadService()
    item = svc.get_dealregistrationlead_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DealRegistrationLead with ID {item_id} not found")
    return item.to_dict()

@router.post("/dealregistrationleads", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dealregistrationlead(payload: DealRegistrationLeadCreateSchema):
    """Create new DealRegistrationLead instance in enterprise repository."""
    svc = DealRegistrationLeadService()
    try:
        item = svc.create_dealregistrationlead(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/dealregistrationleads/{item_id}", response_model=Dict[str, Any])
def update_dealregistrationlead(item_id: int, payload: DealRegistrationLeadUpdateSchema):
    """Update existing DealRegistrationLead record fields."""
    svc = DealRegistrationLeadService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dealregistrationlead(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DealRegistrationLead with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dealregistrationleads/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dealregistrationlead(item_id: int, hard: bool = Query(False)):
    """Delete DealRegistrationLead record (soft-delete by default)."""
    svc = DealRegistrationLeadService()
    ok = svc.delete_dealregistrationlead(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DealRegistrationLead with ID {item_id} not found")
    return None

@router.get("/dealregistrationleads/analytics/metrics", response_model=Dict[str, Any])
def get_dealregistrationlead_metrics():
    """Calculate summary statistical KPIs for DealRegistrationLead collection."""
    svc = DealRegistrationLeadService()
    return svc.calculate_aggregate_metrics()

# ==================== MDFMarketFundRequest Endpoints ====================
@router.get("/mdfmarketfundrequests", response_model=List[Dict[str, Any]])
def list_mdfmarketfundrequests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List MDFMarketFundRequest records with pagination and filtering."""
    svc = MDFMarketFundRequestService()
    items = svc.list_mdfmarketfundrequests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/mdfmarketfundrequests/{item_id}", response_model=Dict[str, Any])
def get_mdfmarketfundrequest_by_id(item_id: int):
    """Retrieve detailed record for MDFMarketFundRequest by ID."""
    svc = MDFMarketFundRequestService()
    item = svc.get_mdfmarketfundrequest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"MDFMarketFundRequest with ID {item_id} not found")
    return item.to_dict()

@router.post("/mdfmarketfundrequests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_mdfmarketfundrequest(payload: MDFMarketFundRequestCreateSchema):
    """Create new MDFMarketFundRequest instance in enterprise repository."""
    svc = MDFMarketFundRequestService()
    try:
        item = svc.create_mdfmarketfundrequest(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/mdfmarketfundrequests/{item_id}", response_model=Dict[str, Any])
def update_mdfmarketfundrequest(item_id: int, payload: MDFMarketFundRequestUpdateSchema):
    """Update existing MDFMarketFundRequest record fields."""
    svc = MDFMarketFundRequestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_mdfmarketfundrequest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"MDFMarketFundRequest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/mdfmarketfundrequests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_mdfmarketfundrequest(item_id: int, hard: bool = Query(False)):
    """Delete MDFMarketFundRequest record (soft-delete by default)."""
    svc = MDFMarketFundRequestService()
    ok = svc.delete_mdfmarketfundrequest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"MDFMarketFundRequest with ID {item_id} not found")
    return None

@router.get("/mdfmarketfundrequests/analytics/metrics", response_model=Dict[str, Any])
def get_mdfmarketfundrequest_metrics():
    """Calculate summary statistical KPIs for MDFMarketFundRequest collection."""
    svc = MDFMarketFundRequestService()
    return svc.calculate_aggregate_metrics()

# ==================== CoMarketingCampaign Endpoints ====================
@router.get("/comarketingcampaigns", response_model=List[Dict[str, Any]])
def list_comarketingcampaigns(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CoMarketingCampaign records with pagination and filtering."""
    svc = CoMarketingCampaignService()
    items = svc.list_comarketingcampaigns(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/comarketingcampaigns/{item_id}", response_model=Dict[str, Any])
def get_comarketingcampaign_by_id(item_id: int):
    """Retrieve detailed record for CoMarketingCampaign by ID."""
    svc = CoMarketingCampaignService()
    item = svc.get_comarketingcampaign_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CoMarketingCampaign with ID {item_id} not found")
    return item.to_dict()

@router.post("/comarketingcampaigns", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_comarketingcampaign(payload: CoMarketingCampaignCreateSchema):
    """Create new CoMarketingCampaign instance in enterprise repository."""
    svc = CoMarketingCampaignService()
    try:
        item = svc.create_comarketingcampaign(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/comarketingcampaigns/{item_id}", response_model=Dict[str, Any])
def update_comarketingcampaign(item_id: int, payload: CoMarketingCampaignUpdateSchema):
    """Update existing CoMarketingCampaign record fields."""
    svc = CoMarketingCampaignService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_comarketingcampaign(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CoMarketingCampaign with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/comarketingcampaigns/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comarketingcampaign(item_id: int, hard: bool = Query(False)):
    """Delete CoMarketingCampaign record (soft-delete by default)."""
    svc = CoMarketingCampaignService()
    ok = svc.delete_comarketingcampaign(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CoMarketingCampaign with ID {item_id} not found")
    return None

@router.get("/comarketingcampaigns/analytics/metrics", response_model=Dict[str, Any])
def get_comarketingcampaign_metrics():
    """Calculate summary statistical KPIs for CoMarketingCampaign collection."""
    svc = CoMarketingCampaignService()
    return svc.calculate_aggregate_metrics()

# ==================== PartnerCommissionPayout Endpoints ====================
@router.get("/partnercommissionpayouts", response_model=List[Dict[str, Any]])
def list_partnercommissionpayouts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PartnerCommissionPayout records with pagination and filtering."""
    svc = PartnerCommissionPayoutService()
    items = svc.list_partnercommissionpayouts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/partnercommissionpayouts/{item_id}", response_model=Dict[str, Any])
def get_partnercommissionpayout_by_id(item_id: int):
    """Retrieve detailed record for PartnerCommissionPayout by ID."""
    svc = PartnerCommissionPayoutService()
    item = svc.get_partnercommissionpayout_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PartnerCommissionPayout with ID {item_id} not found")
    return item.to_dict()

@router.post("/partnercommissionpayouts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_partnercommissionpayout(payload: PartnerCommissionPayoutCreateSchema):
    """Create new PartnerCommissionPayout instance in enterprise repository."""
    svc = PartnerCommissionPayoutService()
    try:
        item = svc.create_partnercommissionpayout(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/partnercommissionpayouts/{item_id}", response_model=Dict[str, Any])
def update_partnercommissionpayout(item_id: int, payload: PartnerCommissionPayoutUpdateSchema):
    """Update existing PartnerCommissionPayout record fields."""
    svc = PartnerCommissionPayoutService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_partnercommissionpayout(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PartnerCommissionPayout with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/partnercommissionpayouts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_partnercommissionpayout(item_id: int, hard: bool = Query(False)):
    """Delete PartnerCommissionPayout record (soft-delete by default)."""
    svc = PartnerCommissionPayoutService()
    ok = svc.delete_partnercommissionpayout(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PartnerCommissionPayout with ID {item_id} not found")
    return None

@router.get("/partnercommissionpayouts/analytics/metrics", response_model=Dict[str, Any])
def get_partnercommissionpayout_metrics():
    """Calculate summary statistical KPIs for PartnerCommissionPayout collection."""
    svc = PartnerCommissionPayoutService()
    return svc.calculate_aggregate_metrics()

# ==================== CertificationCredential Endpoints ====================
@router.get("/certificationcredentials", response_model=List[Dict[str, Any]])
def list_certificationcredentials(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List CertificationCredential records with pagination and filtering."""
    svc = CertificationCredentialService()
    items = svc.list_certificationcredentials(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/certificationcredentials/{item_id}", response_model=Dict[str, Any])
def get_certificationcredential_by_id(item_id: int):
    """Retrieve detailed record for CertificationCredential by ID."""
    svc = CertificationCredentialService()
    item = svc.get_certificationcredential_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"CertificationCredential with ID {item_id} not found")
    return item.to_dict()

@router.post("/certificationcredentials", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_certificationcredential(payload: CertificationCredentialCreateSchema):
    """Create new CertificationCredential instance in enterprise repository."""
    svc = CertificationCredentialService()
    try:
        item = svc.create_certificationcredential(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/certificationcredentials/{item_id}", response_model=Dict[str, Any])
def update_certificationcredential(item_id: int, payload: CertificationCredentialUpdateSchema):
    """Update existing CertificationCredential record fields."""
    svc = CertificationCredentialService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_certificationcredential(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"CertificationCredential with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/certificationcredentials/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_certificationcredential(item_id: int, hard: bool = Query(False)):
    """Delete CertificationCredential record (soft-delete by default)."""
    svc = CertificationCredentialService()
    ok = svc.delete_certificationcredential(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"CertificationCredential with ID {item_id} not found")
    return None

@router.get("/certificationcredentials/analytics/metrics", response_model=Dict[str, Any])
def get_certificationcredential_metrics():
    """Calculate summary statistical KPIs for CertificationCredential collection."""
    svc = CertificationCredentialService()
    return svc.calculate_aggregate_metrics()

# ==================== PartnerSalesGoal Endpoints ====================
@router.get("/partnersalesgoals", response_model=List[Dict[str, Any]])
def list_partnersalesgoals(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PartnerSalesGoal records with pagination and filtering."""
    svc = PartnerSalesGoalService()
    items = svc.list_partnersalesgoals(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/partnersalesgoals/{item_id}", response_model=Dict[str, Any])
def get_partnersalesgoal_by_id(item_id: int):
    """Retrieve detailed record for PartnerSalesGoal by ID."""
    svc = PartnerSalesGoalService()
    item = svc.get_partnersalesgoal_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PartnerSalesGoal with ID {item_id} not found")
    return item.to_dict()

@router.post("/partnersalesgoals", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_partnersalesgoal(payload: PartnerSalesGoalCreateSchema):
    """Create new PartnerSalesGoal instance in enterprise repository."""
    svc = PartnerSalesGoalService()
    try:
        item = svc.create_partnersalesgoal(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/partnersalesgoals/{item_id}", response_model=Dict[str, Any])
def update_partnersalesgoal(item_id: int, payload: PartnerSalesGoalUpdateSchema):
    """Update existing PartnerSalesGoal record fields."""
    svc = PartnerSalesGoalService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_partnersalesgoal(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PartnerSalesGoal with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/partnersalesgoals/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_partnersalesgoal(item_id: int, hard: bool = Query(False)):
    """Delete PartnerSalesGoal record (soft-delete by default)."""
    svc = PartnerSalesGoalService()
    ok = svc.delete_partnersalesgoal(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PartnerSalesGoal with ID {item_id} not found")
    return None

@router.get("/partnersalesgoals/analytics/metrics", response_model=Dict[str, Any])
def get_partnersalesgoal_metrics():
    """Calculate summary statistical KPIs for PartnerSalesGoal collection."""
    svc = PartnerSalesGoalService()
    return svc.calculate_aggregate_metrics()

# ==================== ResellerAgreementContract Endpoints ====================
@router.get("/reselleragreementcontracts", response_model=List[Dict[str, Any]])
def list_reselleragreementcontracts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ResellerAgreementContract records with pagination and filtering."""
    svc = ResellerAgreementContractService()
    items = svc.list_reselleragreementcontracts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/reselleragreementcontracts/{item_id}", response_model=Dict[str, Any])
def get_reselleragreementcontract_by_id(item_id: int):
    """Retrieve detailed record for ResellerAgreementContract by ID."""
    svc = ResellerAgreementContractService()
    item = svc.get_reselleragreementcontract_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ResellerAgreementContract with ID {item_id} not found")
    return item.to_dict()

@router.post("/reselleragreementcontracts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_reselleragreementcontract(payload: ResellerAgreementContractCreateSchema):
    """Create new ResellerAgreementContract instance in enterprise repository."""
    svc = ResellerAgreementContractService()
    try:
        item = svc.create_reselleragreementcontract(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/reselleragreementcontracts/{item_id}", response_model=Dict[str, Any])
def update_reselleragreementcontract(item_id: int, payload: ResellerAgreementContractUpdateSchema):
    """Update existing ResellerAgreementContract record fields."""
    svc = ResellerAgreementContractService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_reselleragreementcontract(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ResellerAgreementContract with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/reselleragreementcontracts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reselleragreementcontract(item_id: int, hard: bool = Query(False)):
    """Delete ResellerAgreementContract record (soft-delete by default)."""
    svc = ResellerAgreementContractService()
    ok = svc.delete_reselleragreementcontract(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ResellerAgreementContract with ID {item_id} not found")
    return None

@router.get("/reselleragreementcontracts/analytics/metrics", response_model=Dict[str, Any])
def get_reselleragreementcontract_metrics():
    """Calculate summary statistical KPIs for ResellerAgreementContract collection."""
    svc = ResellerAgreementContractService()
    return svc.calculate_aggregate_metrics()

# ==================== LeadDistributionRule Endpoints ====================
@router.get("/leaddistributionrules", response_model=List[Dict[str, Any]])
def list_leaddistributionrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LeadDistributionRule records with pagination and filtering."""
    svc = LeadDistributionRuleService()
    items = svc.list_leaddistributionrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/leaddistributionrules/{item_id}", response_model=Dict[str, Any])
def get_leaddistributionrule_by_id(item_id: int):
    """Retrieve detailed record for LeadDistributionRule by ID."""
    svc = LeadDistributionRuleService()
    item = svc.get_leaddistributionrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LeadDistributionRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/leaddistributionrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_leaddistributionrule(payload: LeadDistributionRuleCreateSchema):
    """Create new LeadDistributionRule instance in enterprise repository."""
    svc = LeadDistributionRuleService()
    try:
        item = svc.create_leaddistributionrule(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/leaddistributionrules/{item_id}", response_model=Dict[str, Any])
def update_leaddistributionrule(item_id: int, payload: LeadDistributionRuleUpdateSchema):
    """Update existing LeadDistributionRule record fields."""
    svc = LeadDistributionRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_leaddistributionrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LeadDistributionRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/leaddistributionrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_leaddistributionrule(item_id: int, hard: bool = Query(False)):
    """Delete LeadDistributionRule record (soft-delete by default)."""
    svc = LeadDistributionRuleService()
    ok = svc.delete_leaddistributionrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LeadDistributionRule with ID {item_id} not found")
    return None

@router.get("/leaddistributionrules/analytics/metrics", response_model=Dict[str, Any])
def get_leaddistributionrule_metrics():
    """Calculate summary statistical KPIs for LeadDistributionRule collection."""
    svc = LeadDistributionRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== PartnerPortalCredential Endpoints ====================
@router.get("/partnerportalcredentials", response_model=List[Dict[str, Any]])
def list_partnerportalcredentials(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PartnerPortalCredential records with pagination and filtering."""
    svc = PartnerPortalCredentialService()
    items = svc.list_partnerportalcredentials(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/partnerportalcredentials/{item_id}", response_model=Dict[str, Any])
def get_partnerportalcredential_by_id(item_id: int):
    """Retrieve detailed record for PartnerPortalCredential by ID."""
    svc = PartnerPortalCredentialService()
    item = svc.get_partnerportalcredential_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PartnerPortalCredential with ID {item_id} not found")
    return item.to_dict()

@router.post("/partnerportalcredentials", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_partnerportalcredential(payload: PartnerPortalCredentialCreateSchema):
    """Create new PartnerPortalCredential instance in enterprise repository."""
    svc = PartnerPortalCredentialService()
    try:
        item = svc.create_partnerportalcredential(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/partnerportalcredentials/{item_id}", response_model=Dict[str, Any])
def update_partnerportalcredential(item_id: int, payload: PartnerPortalCredentialUpdateSchema):
    """Update existing PartnerPortalCredential record fields."""
    svc = PartnerPortalCredentialService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_partnerportalcredential(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PartnerPortalCredential with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/partnerportalcredentials/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_partnerportalcredential(item_id: int, hard: bool = Query(False)):
    """Delete PartnerPortalCredential record (soft-delete by default)."""
    svc = PartnerPortalCredentialService()
    ok = svc.delete_partnerportalcredential(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PartnerPortalCredential with ID {item_id} not found")
    return None

@router.get("/partnerportalcredentials/analytics/metrics", response_model=Dict[str, Any])
def get_partnerportalcredential_metrics():
    """Calculate summary statistical KPIs for PartnerPortalCredential collection."""
    svc = PartnerPortalCredentialService()
    return svc.calculate_aggregate_metrics()

# ==================== ChannelConflictDispute Endpoints ====================
@router.get("/channelconflictdisputes", response_model=List[Dict[str, Any]])
def list_channelconflictdisputes(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ChannelConflictDispute records with pagination and filtering."""
    svc = ChannelConflictDisputeService()
    items = svc.list_channelconflictdisputes(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/channelconflictdisputes/{item_id}", response_model=Dict[str, Any])
def get_channelconflictdispute_by_id(item_id: int):
    """Retrieve detailed record for ChannelConflictDispute by ID."""
    svc = ChannelConflictDisputeService()
    item = svc.get_channelconflictdispute_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ChannelConflictDispute with ID {item_id} not found")
    return item.to_dict()

@router.post("/channelconflictdisputes", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_channelconflictdispute(payload: ChannelConflictDisputeCreateSchema):
    """Create new ChannelConflictDispute instance in enterprise repository."""
    svc = ChannelConflictDisputeService()
    try:
        item = svc.create_channelconflictdispute(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/channelconflictdisputes/{item_id}", response_model=Dict[str, Any])
def update_channelconflictdispute(item_id: int, payload: ChannelConflictDisputeUpdateSchema):
    """Update existing ChannelConflictDispute record fields."""
    svc = ChannelConflictDisputeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_channelconflictdispute(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ChannelConflictDispute with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/channelconflictdisputes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_channelconflictdispute(item_id: int, hard: bool = Query(False)):
    """Delete ChannelConflictDispute record (soft-delete by default)."""
    svc = ChannelConflictDisputeService()
    ok = svc.delete_channelconflictdispute(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ChannelConflictDispute with ID {item_id} not found")
    return None

@router.get("/channelconflictdisputes/analytics/metrics", response_model=Dict[str, Any])
def get_channelconflictdispute_metrics():
    """Calculate summary statistical KPIs for ChannelConflictDispute collection."""
    svc = ChannelConflictDisputeService()
    return svc.calculate_aggregate_metrics()

# ==================== TerritoryPartnerExclusivity Endpoints ====================
@router.get("/territorypartnerexclusivitys", response_model=List[Dict[str, Any]])
def list_territorypartnerexclusivitys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TerritoryPartnerExclusivity records with pagination and filtering."""
    svc = TerritoryPartnerExclusivityService()
    items = svc.list_territorypartnerexclusivitys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/territorypartnerexclusivitys/{item_id}", response_model=Dict[str, Any])
def get_territorypartnerexclusivity_by_id(item_id: int):
    """Retrieve detailed record for TerritoryPartnerExclusivity by ID."""
    svc = TerritoryPartnerExclusivityService()
    item = svc.get_territorypartnerexclusivity_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TerritoryPartnerExclusivity with ID {item_id} not found")
    return item.to_dict()

@router.post("/territorypartnerexclusivitys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_territorypartnerexclusivity(payload: TerritoryPartnerExclusivityCreateSchema):
    """Create new TerritoryPartnerExclusivity instance in enterprise repository."""
    svc = TerritoryPartnerExclusivityService()
    try:
        item = svc.create_territorypartnerexclusivity(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/territorypartnerexclusivitys/{item_id}", response_model=Dict[str, Any])
def update_territorypartnerexclusivity(item_id: int, payload: TerritoryPartnerExclusivityUpdateSchema):
    """Update existing TerritoryPartnerExclusivity record fields."""
    svc = TerritoryPartnerExclusivityService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_territorypartnerexclusivity(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TerritoryPartnerExclusivity with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/territorypartnerexclusivitys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_territorypartnerexclusivity(item_id: int, hard: bool = Query(False)):
    """Delete TerritoryPartnerExclusivity record (soft-delete by default)."""
    svc = TerritoryPartnerExclusivityService()
    ok = svc.delete_territorypartnerexclusivity(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TerritoryPartnerExclusivity with ID {item_id} not found")
    return None

@router.get("/territorypartnerexclusivitys/analytics/metrics", response_model=Dict[str, Any])
def get_territorypartnerexclusivity_metrics():
    """Calculate summary statistical KPIs for TerritoryPartnerExclusivity collection."""
    svc = TerritoryPartnerExclusivityService()
    return svc.calculate_aggregate_metrics()

# ==================== PartnerTrainingProgress Endpoints ====================
@router.get("/partnertrainingprogresss", response_model=List[Dict[str, Any]])
def list_partnertrainingprogresss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PartnerTrainingProgress records with pagination and filtering."""
    svc = PartnerTrainingProgressService()
    items = svc.list_partnertrainingprogresss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/partnertrainingprogresss/{item_id}", response_model=Dict[str, Any])
def get_partnertrainingprogress_by_id(item_id: int):
    """Retrieve detailed record for PartnerTrainingProgress by ID."""
    svc = PartnerTrainingProgressService()
    item = svc.get_partnertrainingprogress_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PartnerTrainingProgress with ID {item_id} not found")
    return item.to_dict()

@router.post("/partnertrainingprogresss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_partnertrainingprogress(payload: PartnerTrainingProgressCreateSchema):
    """Create new PartnerTrainingProgress instance in enterprise repository."""
    svc = PartnerTrainingProgressService()
    try:
        item = svc.create_partnertrainingprogress(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/partnertrainingprogresss/{item_id}", response_model=Dict[str, Any])
def update_partnertrainingprogress(item_id: int, payload: PartnerTrainingProgressUpdateSchema):
    """Update existing PartnerTrainingProgress record fields."""
    svc = PartnerTrainingProgressService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_partnertrainingprogress(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PartnerTrainingProgress with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/partnertrainingprogresss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_partnertrainingprogress(item_id: int, hard: bool = Query(False)):
    """Delete PartnerTrainingProgress record (soft-delete by default)."""
    svc = PartnerTrainingProgressService()
    ok = svc.delete_partnertrainingprogress(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PartnerTrainingProgress with ID {item_id} not found")
    return None

@router.get("/partnertrainingprogresss/analytics/metrics", response_model=Dict[str, Any])
def get_partnertrainingprogress_metrics():
    """Calculate summary statistical KPIs for PartnerTrainingProgress collection."""
    svc = PartnerTrainingProgressService()
    return svc.calculate_aggregate_metrics()

# ==================== JointSolutionListing Endpoints ====================
@router.get("/jointsolutionlistings", response_model=List[Dict[str, Any]])
def list_jointsolutionlistings(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List JointSolutionListing records with pagination and filtering."""
    svc = JointSolutionListingService()
    items = svc.list_jointsolutionlistings(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/jointsolutionlistings/{item_id}", response_model=Dict[str, Any])
def get_jointsolutionlisting_by_id(item_id: int):
    """Retrieve detailed record for JointSolutionListing by ID."""
    svc = JointSolutionListingService()
    item = svc.get_jointsolutionlisting_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"JointSolutionListing with ID {item_id} not found")
    return item.to_dict()

@router.post("/jointsolutionlistings", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_jointsolutionlisting(payload: JointSolutionListingCreateSchema):
    """Create new JointSolutionListing instance in enterprise repository."""
    svc = JointSolutionListingService()
    try:
        item = svc.create_jointsolutionlisting(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/jointsolutionlistings/{item_id}", response_model=Dict[str, Any])
def update_jointsolutionlisting(item_id: int, payload: JointSolutionListingUpdateSchema):
    """Update existing JointSolutionListing record fields."""
    svc = JointSolutionListingService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_jointsolutionlisting(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"JointSolutionListing with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/jointsolutionlistings/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_jointsolutionlisting(item_id: int, hard: bool = Query(False)):
    """Delete JointSolutionListing record (soft-delete by default)."""
    svc = JointSolutionListingService()
    ok = svc.delete_jointsolutionlisting(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"JointSolutionListing with ID {item_id} not found")
    return None

@router.get("/jointsolutionlistings/analytics/metrics", response_model=Dict[str, Any])
def get_jointsolutionlisting_metrics():
    """Calculate summary statistical KPIs for JointSolutionListing collection."""
    svc = JointSolutionListingService()
    return svc.calculate_aggregate_metrics()

# ==================== ChannelRevenueForecast Endpoints ====================
@router.get("/channelrevenueforecasts", response_model=List[Dict[str, Any]])
def list_channelrevenueforecasts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ChannelRevenueForecast records with pagination and filtering."""
    svc = ChannelRevenueForecastService()
    items = svc.list_channelrevenueforecasts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/channelrevenueforecasts/{item_id}", response_model=Dict[str, Any])
def get_channelrevenueforecast_by_id(item_id: int):
    """Retrieve detailed record for ChannelRevenueForecast by ID."""
    svc = ChannelRevenueForecastService()
    item = svc.get_channelrevenueforecast_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ChannelRevenueForecast with ID {item_id} not found")
    return item.to_dict()

@router.post("/channelrevenueforecasts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_channelrevenueforecast(payload: ChannelRevenueForecastCreateSchema):
    """Create new ChannelRevenueForecast instance in enterprise repository."""
    svc = ChannelRevenueForecastService()
    try:
        item = svc.create_channelrevenueforecast(
            code=payload.code,
            title=payload.title,
            amount=payload.amount,
            quantity=payload.quantity,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            unit_price=payload.unit_price,
            unit_cost=payload.unit_cost,
        )
        return item.to_dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/channelrevenueforecasts/{item_id}", response_model=Dict[str, Any])
def update_channelrevenueforecast(item_id: int, payload: ChannelRevenueForecastUpdateSchema):
    """Update existing ChannelRevenueForecast record fields."""
    svc = ChannelRevenueForecastService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_channelrevenueforecast(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ChannelRevenueForecast with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/channelrevenueforecasts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_channelrevenueforecast(item_id: int, hard: bool = Query(False)):
    """Delete ChannelRevenueForecast record (soft-delete by default)."""
    svc = ChannelRevenueForecastService()
    ok = svc.delete_channelrevenueforecast(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ChannelRevenueForecast with ID {item_id} not found")
    return None

@router.get("/channelrevenueforecasts/analytics/metrics", response_model=Dict[str, Any])
def get_channelrevenueforecast_metrics():
    """Calculate summary statistical KPIs for ChannelRevenueForecast collection."""
    svc = ChannelRevenueForecastService()
    return svc.calculate_aggregate_metrics()

