"""
Enterprise Document & Records Management - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    DocumentFolderService,
    DocumentFileService,
    DocumentVersionService,
    DocumentMetadataSchemaService,
    AccessControlACLService,
    DocumentTagTaxonomyService,
    OCRTextExtractionService,
    DocumentSignatureRequestService,
    AuditLogDocumentService,
    RetentionSchedulePolicyService,
    LegalHoldNoticeService,
    ArchivalVaultService,
    DocumentShareLinkService,
    WatermarkTemplateService,
    ApprovalSignoffFlowService,
    BatchScanningJobService,
)
from .schemas import (
    DocumentFolderCreateSchema, DocumentFolderUpdateSchema, DocumentFolderResponseSchema,
    DocumentFileCreateSchema, DocumentFileUpdateSchema, DocumentFileResponseSchema,
    DocumentVersionCreateSchema, DocumentVersionUpdateSchema, DocumentVersionResponseSchema,
    DocumentMetadataSchemaCreateSchema, DocumentMetadataSchemaUpdateSchema, DocumentMetadataSchemaResponseSchema,
    AccessControlACLCreateSchema, AccessControlACLUpdateSchema, AccessControlACLResponseSchema,
    DocumentTagTaxonomyCreateSchema, DocumentTagTaxonomyUpdateSchema, DocumentTagTaxonomyResponseSchema,
    OCRTextExtractionCreateSchema, OCRTextExtractionUpdateSchema, OCRTextExtractionResponseSchema,
    DocumentSignatureRequestCreateSchema, DocumentSignatureRequestUpdateSchema, DocumentSignatureRequestResponseSchema,
    AuditLogDocumentCreateSchema, AuditLogDocumentUpdateSchema, AuditLogDocumentResponseSchema,
    RetentionSchedulePolicyCreateSchema, RetentionSchedulePolicyUpdateSchema, RetentionSchedulePolicyResponseSchema,
    LegalHoldNoticeCreateSchema, LegalHoldNoticeUpdateSchema, LegalHoldNoticeResponseSchema,
    ArchivalVaultCreateSchema, ArchivalVaultUpdateSchema, ArchivalVaultResponseSchema,
    DocumentShareLinkCreateSchema, DocumentShareLinkUpdateSchema, DocumentShareLinkResponseSchema,
    WatermarkTemplateCreateSchema, WatermarkTemplateUpdateSchema, WatermarkTemplateResponseSchema,
    ApprovalSignoffFlowCreateSchema, ApprovalSignoffFlowUpdateSchema, ApprovalSignoffFlowResponseSchema,
    BatchScanningJobCreateSchema, BatchScanningJobUpdateSchema, BatchScanningJobResponseSchema,
)

router = APIRouter(prefix="/document_management", tags=["Enterprise Document & Records Management"])

# ==================== DocumentFolder Endpoints ====================
@router.get("/documentfolders", response_model=List[Dict[str, Any]])
def list_documentfolders(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DocumentFolder records with pagination and filtering."""
    svc = DocumentFolderService()
    items = svc.list_documentfolders(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/documentfolders/{item_id}", response_model=Dict[str, Any])
def get_documentfolder_by_id(item_id: int):
    """Retrieve detailed record for DocumentFolder by ID."""
    svc = DocumentFolderService()
    item = svc.get_documentfolder_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DocumentFolder with ID {item_id} not found")
    return item.to_dict()

@router.post("/documentfolders", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_documentfolder(payload: DocumentFolderCreateSchema):
    """Create new DocumentFolder instance in enterprise repository."""
    svc = DocumentFolderService()
    try:
        item = svc.create_documentfolder(
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

@router.put("/documentfolders/{item_id}", response_model=Dict[str, Any])
def update_documentfolder(item_id: int, payload: DocumentFolderUpdateSchema):
    """Update existing DocumentFolder record fields."""
    svc = DocumentFolderService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_documentfolder(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DocumentFolder with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/documentfolders/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_documentfolder(item_id: int, hard: bool = Query(False)):
    """Delete DocumentFolder record (soft-delete by default)."""
    svc = DocumentFolderService()
    ok = svc.delete_documentfolder(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DocumentFolder with ID {item_id} not found")
    return None

@router.get("/documentfolders/analytics/metrics", response_model=Dict[str, Any])
def get_documentfolder_metrics():
    """Calculate summary statistical KPIs for DocumentFolder collection."""
    svc = DocumentFolderService()
    return svc.calculate_aggregate_metrics()

# ==================== DocumentFile Endpoints ====================
@router.get("/documentfiles", response_model=List[Dict[str, Any]])
def list_documentfiles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DocumentFile records with pagination and filtering."""
    svc = DocumentFileService()
    items = svc.list_documentfiles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/documentfiles/{item_id}", response_model=Dict[str, Any])
def get_documentfile_by_id(item_id: int):
    """Retrieve detailed record for DocumentFile by ID."""
    svc = DocumentFileService()
    item = svc.get_documentfile_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DocumentFile with ID {item_id} not found")
    return item.to_dict()

@router.post("/documentfiles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_documentfile(payload: DocumentFileCreateSchema):
    """Create new DocumentFile instance in enterprise repository."""
    svc = DocumentFileService()
    try:
        item = svc.create_documentfile(
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

@router.put("/documentfiles/{item_id}", response_model=Dict[str, Any])
def update_documentfile(item_id: int, payload: DocumentFileUpdateSchema):
    """Update existing DocumentFile record fields."""
    svc = DocumentFileService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_documentfile(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DocumentFile with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/documentfiles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_documentfile(item_id: int, hard: bool = Query(False)):
    """Delete DocumentFile record (soft-delete by default)."""
    svc = DocumentFileService()
    ok = svc.delete_documentfile(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DocumentFile with ID {item_id} not found")
    return None

@router.get("/documentfiles/analytics/metrics", response_model=Dict[str, Any])
def get_documentfile_metrics():
    """Calculate summary statistical KPIs for DocumentFile collection."""
    svc = DocumentFileService()
    return svc.calculate_aggregate_metrics()

# ==================== DocumentVersion Endpoints ====================
@router.get("/documentversions", response_model=List[Dict[str, Any]])
def list_documentversions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DocumentVersion records with pagination and filtering."""
    svc = DocumentVersionService()
    items = svc.list_documentversions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/documentversions/{item_id}", response_model=Dict[str, Any])
def get_documentversion_by_id(item_id: int):
    """Retrieve detailed record for DocumentVersion by ID."""
    svc = DocumentVersionService()
    item = svc.get_documentversion_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DocumentVersion with ID {item_id} not found")
    return item.to_dict()

@router.post("/documentversions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_documentversion(payload: DocumentVersionCreateSchema):
    """Create new DocumentVersion instance in enterprise repository."""
    svc = DocumentVersionService()
    try:
        item = svc.create_documentversion(
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

@router.put("/documentversions/{item_id}", response_model=Dict[str, Any])
def update_documentversion(item_id: int, payload: DocumentVersionUpdateSchema):
    """Update existing DocumentVersion record fields."""
    svc = DocumentVersionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_documentversion(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DocumentVersion with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/documentversions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_documentversion(item_id: int, hard: bool = Query(False)):
    """Delete DocumentVersion record (soft-delete by default)."""
    svc = DocumentVersionService()
    ok = svc.delete_documentversion(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DocumentVersion with ID {item_id} not found")
    return None

@router.get("/documentversions/analytics/metrics", response_model=Dict[str, Any])
def get_documentversion_metrics():
    """Calculate summary statistical KPIs for DocumentVersion collection."""
    svc = DocumentVersionService()
    return svc.calculate_aggregate_metrics()

# ==================== DocumentMetadataSchema Endpoints ====================
@router.get("/documentmetadataschemas", response_model=List[Dict[str, Any]])
def list_documentmetadataschemas(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DocumentMetadataSchema records with pagination and filtering."""
    svc = DocumentMetadataSchemaService()
    items = svc.list_documentmetadataschemas(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/documentmetadataschemas/{item_id}", response_model=Dict[str, Any])
def get_documentmetadataschema_by_id(item_id: int):
    """Retrieve detailed record for DocumentMetadataSchema by ID."""
    svc = DocumentMetadataSchemaService()
    item = svc.get_documentmetadataschema_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DocumentMetadataSchema with ID {item_id} not found")
    return item.to_dict()

@router.post("/documentmetadataschemas", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_documentmetadataschema(payload: DocumentMetadataSchemaCreateSchema):
    """Create new DocumentMetadataSchema instance in enterprise repository."""
    svc = DocumentMetadataSchemaService()
    try:
        item = svc.create_documentmetadataschema(
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

@router.put("/documentmetadataschemas/{item_id}", response_model=Dict[str, Any])
def update_documentmetadataschema(item_id: int, payload: DocumentMetadataSchemaUpdateSchema):
    """Update existing DocumentMetadataSchema record fields."""
    svc = DocumentMetadataSchemaService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_documentmetadataschema(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DocumentMetadataSchema with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/documentmetadataschemas/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_documentmetadataschema(item_id: int, hard: bool = Query(False)):
    """Delete DocumentMetadataSchema record (soft-delete by default)."""
    svc = DocumentMetadataSchemaService()
    ok = svc.delete_documentmetadataschema(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DocumentMetadataSchema with ID {item_id} not found")
    return None

@router.get("/documentmetadataschemas/analytics/metrics", response_model=Dict[str, Any])
def get_documentmetadataschema_metrics():
    """Calculate summary statistical KPIs for DocumentMetadataSchema collection."""
    svc = DocumentMetadataSchemaService()
    return svc.calculate_aggregate_metrics()

# ==================== AccessControlACL Endpoints ====================
@router.get("/accesscontrolacls", response_model=List[Dict[str, Any]])
def list_accesscontrolacls(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AccessControlACL records with pagination and filtering."""
    svc = AccessControlACLService()
    items = svc.list_accesscontrolacls(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/accesscontrolacls/{item_id}", response_model=Dict[str, Any])
def get_accesscontrolacl_by_id(item_id: int):
    """Retrieve detailed record for AccessControlACL by ID."""
    svc = AccessControlACLService()
    item = svc.get_accesscontrolacl_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AccessControlACL with ID {item_id} not found")
    return item.to_dict()

@router.post("/accesscontrolacls", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_accesscontrolacl(payload: AccessControlACLCreateSchema):
    """Create new AccessControlACL instance in enterprise repository."""
    svc = AccessControlACLService()
    try:
        item = svc.create_accesscontrolacl(
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

@router.put("/accesscontrolacls/{item_id}", response_model=Dict[str, Any])
def update_accesscontrolacl(item_id: int, payload: AccessControlACLUpdateSchema):
    """Update existing AccessControlACL record fields."""
    svc = AccessControlACLService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_accesscontrolacl(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AccessControlACL with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/accesscontrolacls/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_accesscontrolacl(item_id: int, hard: bool = Query(False)):
    """Delete AccessControlACL record (soft-delete by default)."""
    svc = AccessControlACLService()
    ok = svc.delete_accesscontrolacl(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AccessControlACL with ID {item_id} not found")
    return None

@router.get("/accesscontrolacls/analytics/metrics", response_model=Dict[str, Any])
def get_accesscontrolacl_metrics():
    """Calculate summary statistical KPIs for AccessControlACL collection."""
    svc = AccessControlACLService()
    return svc.calculate_aggregate_metrics()

# ==================== DocumentTagTaxonomy Endpoints ====================
@router.get("/documenttagtaxonomys", response_model=List[Dict[str, Any]])
def list_documenttagtaxonomys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DocumentTagTaxonomy records with pagination and filtering."""
    svc = DocumentTagTaxonomyService()
    items = svc.list_documenttagtaxonomys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/documenttagtaxonomys/{item_id}", response_model=Dict[str, Any])
def get_documenttagtaxonomy_by_id(item_id: int):
    """Retrieve detailed record for DocumentTagTaxonomy by ID."""
    svc = DocumentTagTaxonomyService()
    item = svc.get_documenttagtaxonomy_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DocumentTagTaxonomy with ID {item_id} not found")
    return item.to_dict()

@router.post("/documenttagtaxonomys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_documenttagtaxonomy(payload: DocumentTagTaxonomyCreateSchema):
    """Create new DocumentTagTaxonomy instance in enterprise repository."""
    svc = DocumentTagTaxonomyService()
    try:
        item = svc.create_documenttagtaxonomy(
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

@router.put("/documenttagtaxonomys/{item_id}", response_model=Dict[str, Any])
def update_documenttagtaxonomy(item_id: int, payload: DocumentTagTaxonomyUpdateSchema):
    """Update existing DocumentTagTaxonomy record fields."""
    svc = DocumentTagTaxonomyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_documenttagtaxonomy(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DocumentTagTaxonomy with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/documenttagtaxonomys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_documenttagtaxonomy(item_id: int, hard: bool = Query(False)):
    """Delete DocumentTagTaxonomy record (soft-delete by default)."""
    svc = DocumentTagTaxonomyService()
    ok = svc.delete_documenttagtaxonomy(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DocumentTagTaxonomy with ID {item_id} not found")
    return None

@router.get("/documenttagtaxonomys/analytics/metrics", response_model=Dict[str, Any])
def get_documenttagtaxonomy_metrics():
    """Calculate summary statistical KPIs for DocumentTagTaxonomy collection."""
    svc = DocumentTagTaxonomyService()
    return svc.calculate_aggregate_metrics()

# ==================== OCRTextExtraction Endpoints ====================
@router.get("/ocrtextextractions", response_model=List[Dict[str, Any]])
def list_ocrtextextractions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List OCRTextExtraction records with pagination and filtering."""
    svc = OCRTextExtractionService()
    items = svc.list_ocrtextextractions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/ocrtextextractions/{item_id}", response_model=Dict[str, Any])
def get_ocrtextextraction_by_id(item_id: int):
    """Retrieve detailed record for OCRTextExtraction by ID."""
    svc = OCRTextExtractionService()
    item = svc.get_ocrtextextraction_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"OCRTextExtraction with ID {item_id} not found")
    return item.to_dict()

@router.post("/ocrtextextractions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_ocrtextextraction(payload: OCRTextExtractionCreateSchema):
    """Create new OCRTextExtraction instance in enterprise repository."""
    svc = OCRTextExtractionService()
    try:
        item = svc.create_ocrtextextraction(
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

@router.put("/ocrtextextractions/{item_id}", response_model=Dict[str, Any])
def update_ocrtextextraction(item_id: int, payload: OCRTextExtractionUpdateSchema):
    """Update existing OCRTextExtraction record fields."""
    svc = OCRTextExtractionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_ocrtextextraction(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"OCRTextExtraction with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/ocrtextextractions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ocrtextextraction(item_id: int, hard: bool = Query(False)):
    """Delete OCRTextExtraction record (soft-delete by default)."""
    svc = OCRTextExtractionService()
    ok = svc.delete_ocrtextextraction(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"OCRTextExtraction with ID {item_id} not found")
    return None

@router.get("/ocrtextextractions/analytics/metrics", response_model=Dict[str, Any])
def get_ocrtextextraction_metrics():
    """Calculate summary statistical KPIs for OCRTextExtraction collection."""
    svc = OCRTextExtractionService()
    return svc.calculate_aggregate_metrics()

# ==================== DocumentSignatureRequest Endpoints ====================
@router.get("/documentsignaturerequests", response_model=List[Dict[str, Any]])
def list_documentsignaturerequests(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DocumentSignatureRequest records with pagination and filtering."""
    svc = DocumentSignatureRequestService()
    items = svc.list_documentsignaturerequests(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/documentsignaturerequests/{item_id}", response_model=Dict[str, Any])
def get_documentsignaturerequest_by_id(item_id: int):
    """Retrieve detailed record for DocumentSignatureRequest by ID."""
    svc = DocumentSignatureRequestService()
    item = svc.get_documentsignaturerequest_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DocumentSignatureRequest with ID {item_id} not found")
    return item.to_dict()

@router.post("/documentsignaturerequests", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_documentsignaturerequest(payload: DocumentSignatureRequestCreateSchema):
    """Create new DocumentSignatureRequest instance in enterprise repository."""
    svc = DocumentSignatureRequestService()
    try:
        item = svc.create_documentsignaturerequest(
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

@router.put("/documentsignaturerequests/{item_id}", response_model=Dict[str, Any])
def update_documentsignaturerequest(item_id: int, payload: DocumentSignatureRequestUpdateSchema):
    """Update existing DocumentSignatureRequest record fields."""
    svc = DocumentSignatureRequestService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_documentsignaturerequest(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DocumentSignatureRequest with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/documentsignaturerequests/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_documentsignaturerequest(item_id: int, hard: bool = Query(False)):
    """Delete DocumentSignatureRequest record (soft-delete by default)."""
    svc = DocumentSignatureRequestService()
    ok = svc.delete_documentsignaturerequest(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DocumentSignatureRequest with ID {item_id} not found")
    return None

@router.get("/documentsignaturerequests/analytics/metrics", response_model=Dict[str, Any])
def get_documentsignaturerequest_metrics():
    """Calculate summary statistical KPIs for DocumentSignatureRequest collection."""
    svc = DocumentSignatureRequestService()
    return svc.calculate_aggregate_metrics()

# ==================== AuditLogDocument Endpoints ====================
@router.get("/auditlogdocuments", response_model=List[Dict[str, Any]])
def list_auditlogdocuments(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AuditLogDocument records with pagination and filtering."""
    svc = AuditLogDocumentService()
    items = svc.list_auditlogdocuments(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/auditlogdocuments/{item_id}", response_model=Dict[str, Any])
def get_auditlogdocument_by_id(item_id: int):
    """Retrieve detailed record for AuditLogDocument by ID."""
    svc = AuditLogDocumentService()
    item = svc.get_auditlogdocument_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AuditLogDocument with ID {item_id} not found")
    return item.to_dict()

@router.post("/auditlogdocuments", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_auditlogdocument(payload: AuditLogDocumentCreateSchema):
    """Create new AuditLogDocument instance in enterprise repository."""
    svc = AuditLogDocumentService()
    try:
        item = svc.create_auditlogdocument(
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

@router.put("/auditlogdocuments/{item_id}", response_model=Dict[str, Any])
def update_auditlogdocument(item_id: int, payload: AuditLogDocumentUpdateSchema):
    """Update existing AuditLogDocument record fields."""
    svc = AuditLogDocumentService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_auditlogdocument(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AuditLogDocument with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/auditlogdocuments/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_auditlogdocument(item_id: int, hard: bool = Query(False)):
    """Delete AuditLogDocument record (soft-delete by default)."""
    svc = AuditLogDocumentService()
    ok = svc.delete_auditlogdocument(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AuditLogDocument with ID {item_id} not found")
    return None

@router.get("/auditlogdocuments/analytics/metrics", response_model=Dict[str, Any])
def get_auditlogdocument_metrics():
    """Calculate summary statistical KPIs for AuditLogDocument collection."""
    svc = AuditLogDocumentService()
    return svc.calculate_aggregate_metrics()

# ==================== RetentionSchedulePolicy Endpoints ====================
@router.get("/retentionschedulepolicys", response_model=List[Dict[str, Any]])
def list_retentionschedulepolicys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RetentionSchedulePolicy records with pagination and filtering."""
    svc = RetentionSchedulePolicyService()
    items = svc.list_retentionschedulepolicys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/retentionschedulepolicys/{item_id}", response_model=Dict[str, Any])
def get_retentionschedulepolicy_by_id(item_id: int):
    """Retrieve detailed record for RetentionSchedulePolicy by ID."""
    svc = RetentionSchedulePolicyService()
    item = svc.get_retentionschedulepolicy_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RetentionSchedulePolicy with ID {item_id} not found")
    return item.to_dict()

@router.post("/retentionschedulepolicys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_retentionschedulepolicy(payload: RetentionSchedulePolicyCreateSchema):
    """Create new RetentionSchedulePolicy instance in enterprise repository."""
    svc = RetentionSchedulePolicyService()
    try:
        item = svc.create_retentionschedulepolicy(
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

@router.put("/retentionschedulepolicys/{item_id}", response_model=Dict[str, Any])
def update_retentionschedulepolicy(item_id: int, payload: RetentionSchedulePolicyUpdateSchema):
    """Update existing RetentionSchedulePolicy record fields."""
    svc = RetentionSchedulePolicyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_retentionschedulepolicy(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RetentionSchedulePolicy with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/retentionschedulepolicys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_retentionschedulepolicy(item_id: int, hard: bool = Query(False)):
    """Delete RetentionSchedulePolicy record (soft-delete by default)."""
    svc = RetentionSchedulePolicyService()
    ok = svc.delete_retentionschedulepolicy(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RetentionSchedulePolicy with ID {item_id} not found")
    return None

@router.get("/retentionschedulepolicys/analytics/metrics", response_model=Dict[str, Any])
def get_retentionschedulepolicy_metrics():
    """Calculate summary statistical KPIs for RetentionSchedulePolicy collection."""
    svc = RetentionSchedulePolicyService()
    return svc.calculate_aggregate_metrics()

# ==================== LegalHoldNotice Endpoints ====================
@router.get("/legalholdnotices", response_model=List[Dict[str, Any]])
def list_legalholdnotices(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List LegalHoldNotice records with pagination and filtering."""
    svc = LegalHoldNoticeService()
    items = svc.list_legalholdnotices(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/legalholdnotices/{item_id}", response_model=Dict[str, Any])
def get_legalholdnotice_by_id(item_id: int):
    """Retrieve detailed record for LegalHoldNotice by ID."""
    svc = LegalHoldNoticeService()
    item = svc.get_legalholdnotice_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"LegalHoldNotice with ID {item_id} not found")
    return item.to_dict()

@router.post("/legalholdnotices", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_legalholdnotice(payload: LegalHoldNoticeCreateSchema):
    """Create new LegalHoldNotice instance in enterprise repository."""
    svc = LegalHoldNoticeService()
    try:
        item = svc.create_legalholdnotice(
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

@router.put("/legalholdnotices/{item_id}", response_model=Dict[str, Any])
def update_legalholdnotice(item_id: int, payload: LegalHoldNoticeUpdateSchema):
    """Update existing LegalHoldNotice record fields."""
    svc = LegalHoldNoticeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_legalholdnotice(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"LegalHoldNotice with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/legalholdnotices/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_legalholdnotice(item_id: int, hard: bool = Query(False)):
    """Delete LegalHoldNotice record (soft-delete by default)."""
    svc = LegalHoldNoticeService()
    ok = svc.delete_legalholdnotice(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"LegalHoldNotice with ID {item_id} not found")
    return None

@router.get("/legalholdnotices/analytics/metrics", response_model=Dict[str, Any])
def get_legalholdnotice_metrics():
    """Calculate summary statistical KPIs for LegalHoldNotice collection."""
    svc = LegalHoldNoticeService()
    return svc.calculate_aggregate_metrics()

# ==================== ArchivalVault Endpoints ====================
@router.get("/archivalvaults", response_model=List[Dict[str, Any]])
def list_archivalvaults(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ArchivalVault records with pagination and filtering."""
    svc = ArchivalVaultService()
    items = svc.list_archivalvaults(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/archivalvaults/{item_id}", response_model=Dict[str, Any])
def get_archivalvault_by_id(item_id: int):
    """Retrieve detailed record for ArchivalVault by ID."""
    svc = ArchivalVaultService()
    item = svc.get_archivalvault_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ArchivalVault with ID {item_id} not found")
    return item.to_dict()

@router.post("/archivalvaults", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_archivalvault(payload: ArchivalVaultCreateSchema):
    """Create new ArchivalVault instance in enterprise repository."""
    svc = ArchivalVaultService()
    try:
        item = svc.create_archivalvault(
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

@router.put("/archivalvaults/{item_id}", response_model=Dict[str, Any])
def update_archivalvault(item_id: int, payload: ArchivalVaultUpdateSchema):
    """Update existing ArchivalVault record fields."""
    svc = ArchivalVaultService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_archivalvault(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ArchivalVault with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/archivalvaults/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_archivalvault(item_id: int, hard: bool = Query(False)):
    """Delete ArchivalVault record (soft-delete by default)."""
    svc = ArchivalVaultService()
    ok = svc.delete_archivalvault(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ArchivalVault with ID {item_id} not found")
    return None

@router.get("/archivalvaults/analytics/metrics", response_model=Dict[str, Any])
def get_archivalvault_metrics():
    """Calculate summary statistical KPIs for ArchivalVault collection."""
    svc = ArchivalVaultService()
    return svc.calculate_aggregate_metrics()

# ==================== DocumentShareLink Endpoints ====================
@router.get("/documentsharelinks", response_model=List[Dict[str, Any]])
def list_documentsharelinks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DocumentShareLink records with pagination and filtering."""
    svc = DocumentShareLinkService()
    items = svc.list_documentsharelinks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/documentsharelinks/{item_id}", response_model=Dict[str, Any])
def get_documentsharelink_by_id(item_id: int):
    """Retrieve detailed record for DocumentShareLink by ID."""
    svc = DocumentShareLinkService()
    item = svc.get_documentsharelink_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DocumentShareLink with ID {item_id} not found")
    return item.to_dict()

@router.post("/documentsharelinks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_documentsharelink(payload: DocumentShareLinkCreateSchema):
    """Create new DocumentShareLink instance in enterprise repository."""
    svc = DocumentShareLinkService()
    try:
        item = svc.create_documentsharelink(
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

@router.put("/documentsharelinks/{item_id}", response_model=Dict[str, Any])
def update_documentsharelink(item_id: int, payload: DocumentShareLinkUpdateSchema):
    """Update existing DocumentShareLink record fields."""
    svc = DocumentShareLinkService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_documentsharelink(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DocumentShareLink with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/documentsharelinks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_documentsharelink(item_id: int, hard: bool = Query(False)):
    """Delete DocumentShareLink record (soft-delete by default)."""
    svc = DocumentShareLinkService()
    ok = svc.delete_documentsharelink(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DocumentShareLink with ID {item_id} not found")
    return None

@router.get("/documentsharelinks/analytics/metrics", response_model=Dict[str, Any])
def get_documentsharelink_metrics():
    """Calculate summary statistical KPIs for DocumentShareLink collection."""
    svc = DocumentShareLinkService()
    return svc.calculate_aggregate_metrics()

# ==================== WatermarkTemplate Endpoints ====================
@router.get("/watermarktemplates", response_model=List[Dict[str, Any]])
def list_watermarktemplates(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List WatermarkTemplate records with pagination and filtering."""
    svc = WatermarkTemplateService()
    items = svc.list_watermarktemplates(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/watermarktemplates/{item_id}", response_model=Dict[str, Any])
def get_watermarktemplate_by_id(item_id: int):
    """Retrieve detailed record for WatermarkTemplate by ID."""
    svc = WatermarkTemplateService()
    item = svc.get_watermarktemplate_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"WatermarkTemplate with ID {item_id} not found")
    return item.to_dict()

@router.post("/watermarktemplates", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_watermarktemplate(payload: WatermarkTemplateCreateSchema):
    """Create new WatermarkTemplate instance in enterprise repository."""
    svc = WatermarkTemplateService()
    try:
        item = svc.create_watermarktemplate(
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

@router.put("/watermarktemplates/{item_id}", response_model=Dict[str, Any])
def update_watermarktemplate(item_id: int, payload: WatermarkTemplateUpdateSchema):
    """Update existing WatermarkTemplate record fields."""
    svc = WatermarkTemplateService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_watermarktemplate(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"WatermarkTemplate with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/watermarktemplates/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_watermarktemplate(item_id: int, hard: bool = Query(False)):
    """Delete WatermarkTemplate record (soft-delete by default)."""
    svc = WatermarkTemplateService()
    ok = svc.delete_watermarktemplate(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"WatermarkTemplate with ID {item_id} not found")
    return None

@router.get("/watermarktemplates/analytics/metrics", response_model=Dict[str, Any])
def get_watermarktemplate_metrics():
    """Calculate summary statistical KPIs for WatermarkTemplate collection."""
    svc = WatermarkTemplateService()
    return svc.calculate_aggregate_metrics()

# ==================== ApprovalSignoffFlow Endpoints ====================
@router.get("/approvalsignoffflows", response_model=List[Dict[str, Any]])
def list_approvalsignoffflows(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ApprovalSignoffFlow records with pagination and filtering."""
    svc = ApprovalSignoffFlowService()
    items = svc.list_approvalsignoffflows(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/approvalsignoffflows/{item_id}", response_model=Dict[str, Any])
def get_approvalsignoffflow_by_id(item_id: int):
    """Retrieve detailed record for ApprovalSignoffFlow by ID."""
    svc = ApprovalSignoffFlowService()
    item = svc.get_approvalsignoffflow_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ApprovalSignoffFlow with ID {item_id} not found")
    return item.to_dict()

@router.post("/approvalsignoffflows", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_approvalsignoffflow(payload: ApprovalSignoffFlowCreateSchema):
    """Create new ApprovalSignoffFlow instance in enterprise repository."""
    svc = ApprovalSignoffFlowService()
    try:
        item = svc.create_approvalsignoffflow(
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

@router.put("/approvalsignoffflows/{item_id}", response_model=Dict[str, Any])
def update_approvalsignoffflow(item_id: int, payload: ApprovalSignoffFlowUpdateSchema):
    """Update existing ApprovalSignoffFlow record fields."""
    svc = ApprovalSignoffFlowService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_approvalsignoffflow(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ApprovalSignoffFlow with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/approvalsignoffflows/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_approvalsignoffflow(item_id: int, hard: bool = Query(False)):
    """Delete ApprovalSignoffFlow record (soft-delete by default)."""
    svc = ApprovalSignoffFlowService()
    ok = svc.delete_approvalsignoffflow(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ApprovalSignoffFlow with ID {item_id} not found")
    return None

@router.get("/approvalsignoffflows/analytics/metrics", response_model=Dict[str, Any])
def get_approvalsignoffflow_metrics():
    """Calculate summary statistical KPIs for ApprovalSignoffFlow collection."""
    svc = ApprovalSignoffFlowService()
    return svc.calculate_aggregate_metrics()

# ==================== BatchScanningJob Endpoints ====================
@router.get("/batchscanningjobs", response_model=List[Dict[str, Any]])
def list_batchscanningjobs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BatchScanningJob records with pagination and filtering."""
    svc = BatchScanningJobService()
    items = svc.list_batchscanningjobs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/batchscanningjobs/{item_id}", response_model=Dict[str, Any])
def get_batchscanningjob_by_id(item_id: int):
    """Retrieve detailed record for BatchScanningJob by ID."""
    svc = BatchScanningJobService()
    item = svc.get_batchscanningjob_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BatchScanningJob with ID {item_id} not found")
    return item.to_dict()

@router.post("/batchscanningjobs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_batchscanningjob(payload: BatchScanningJobCreateSchema):
    """Create new BatchScanningJob instance in enterprise repository."""
    svc = BatchScanningJobService()
    try:
        item = svc.create_batchscanningjob(
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

@router.put("/batchscanningjobs/{item_id}", response_model=Dict[str, Any])
def update_batchscanningjob(item_id: int, payload: BatchScanningJobUpdateSchema):
    """Update existing BatchScanningJob record fields."""
    svc = BatchScanningJobService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_batchscanningjob(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BatchScanningJob with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/batchscanningjobs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_batchscanningjob(item_id: int, hard: bool = Query(False)):
    """Delete BatchScanningJob record (soft-delete by default)."""
    svc = BatchScanningJobService()
    ok = svc.delete_batchscanningjob(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BatchScanningJob with ID {item_id} not found")
    return None

@router.get("/batchscanningjobs/analytics/metrics", response_model=Dict[str, Any])
def get_batchscanningjob_metrics():
    """Calculate summary statistical KPIs for BatchScanningJob collection."""
    svc = BatchScanningJobService()
    return svc.calculate_aggregate_metrics()

