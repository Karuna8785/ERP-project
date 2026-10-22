"""
Enterprise Knowledge Base & Standard Operations - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    KnowledgeBaseArticleService,
    StandardOperatingProcedureService,
    KnowledgeCategoryTopicService,
    ContentReviewWorkflowService,
    ArticleFeedbackVoteService,
    SearchQueryAnalyticsService,
    TechnicalFaqItemService,
    TroubleshootingGuideService,
    TranslationLocalizationService,
    ArticleAttachmentFileService,
    InternalWikiPageService,
    KnowledgeGraphNodeService,
    RevisionHistoryLogService,
    ExpertAuthorDirectoryService,
    DeprecatedNoticeService,
    AccessVisibilityTierService,
)
from .schemas import (
    KnowledgeBaseArticleCreateSchema, KnowledgeBaseArticleUpdateSchema, KnowledgeBaseArticleResponseSchema,
    StandardOperatingProcedureCreateSchema, StandardOperatingProcedureUpdateSchema, StandardOperatingProcedureResponseSchema,
    KnowledgeCategoryTopicCreateSchema, KnowledgeCategoryTopicUpdateSchema, KnowledgeCategoryTopicResponseSchema,
    ContentReviewWorkflowCreateSchema, ContentReviewWorkflowUpdateSchema, ContentReviewWorkflowResponseSchema,
    ArticleFeedbackVoteCreateSchema, ArticleFeedbackVoteUpdateSchema, ArticleFeedbackVoteResponseSchema,
    SearchQueryAnalyticsCreateSchema, SearchQueryAnalyticsUpdateSchema, SearchQueryAnalyticsResponseSchema,
    TechnicalFaqItemCreateSchema, TechnicalFaqItemUpdateSchema, TechnicalFaqItemResponseSchema,
    TroubleshootingGuideCreateSchema, TroubleshootingGuideUpdateSchema, TroubleshootingGuideResponseSchema,
    TranslationLocalizationCreateSchema, TranslationLocalizationUpdateSchema, TranslationLocalizationResponseSchema,
    ArticleAttachmentFileCreateSchema, ArticleAttachmentFileUpdateSchema, ArticleAttachmentFileResponseSchema,
    InternalWikiPageCreateSchema, InternalWikiPageUpdateSchema, InternalWikiPageResponseSchema,
    KnowledgeGraphNodeCreateSchema, KnowledgeGraphNodeUpdateSchema, KnowledgeGraphNodeResponseSchema,
    RevisionHistoryLogCreateSchema, RevisionHistoryLogUpdateSchema, RevisionHistoryLogResponseSchema,
    ExpertAuthorDirectoryCreateSchema, ExpertAuthorDirectoryUpdateSchema, ExpertAuthorDirectoryResponseSchema,
    DeprecatedNoticeCreateSchema, DeprecatedNoticeUpdateSchema, DeprecatedNoticeResponseSchema,
    AccessVisibilityTierCreateSchema, AccessVisibilityTierUpdateSchema, AccessVisibilityTierResponseSchema,
)

router = APIRouter(prefix="/knowledge_base", tags=["Enterprise Knowledge Base & Standard Operations"])

# ==================== KnowledgeBaseArticle Endpoints ====================
@router.get("/knowledgebasearticles", response_model=List[Dict[str, Any]])
def list_knowledgebasearticles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List KnowledgeBaseArticle records with pagination and filtering."""
    svc = KnowledgeBaseArticleService()
    items = svc.list_knowledgebasearticles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/knowledgebasearticles/{item_id}", response_model=Dict[str, Any])
def get_knowledgebasearticle_by_id(item_id: int):
    """Retrieve detailed record for KnowledgeBaseArticle by ID."""
    svc = KnowledgeBaseArticleService()
    item = svc.get_knowledgebasearticle_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"KnowledgeBaseArticle with ID {item_id} not found")
    return item.to_dict()

@router.post("/knowledgebasearticles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_knowledgebasearticle(payload: KnowledgeBaseArticleCreateSchema):
    """Create new KnowledgeBaseArticle instance in enterprise repository."""
    svc = KnowledgeBaseArticleService()
    try:
        item = svc.create_knowledgebasearticle(
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

@router.put("/knowledgebasearticles/{item_id}", response_model=Dict[str, Any])
def update_knowledgebasearticle(item_id: int, payload: KnowledgeBaseArticleUpdateSchema):
    """Update existing KnowledgeBaseArticle record fields."""
    svc = KnowledgeBaseArticleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_knowledgebasearticle(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"KnowledgeBaseArticle with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/knowledgebasearticles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_knowledgebasearticle(item_id: int, hard: bool = Query(False)):
    """Delete KnowledgeBaseArticle record (soft-delete by default)."""
    svc = KnowledgeBaseArticleService()
    ok = svc.delete_knowledgebasearticle(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"KnowledgeBaseArticle with ID {item_id} not found")
    return None

@router.get("/knowledgebasearticles/analytics/metrics", response_model=Dict[str, Any])
def get_knowledgebasearticle_metrics():
    """Calculate summary statistical KPIs for KnowledgeBaseArticle collection."""
    svc = KnowledgeBaseArticleService()
    return svc.calculate_aggregate_metrics()

# ==================== StandardOperatingProcedure Endpoints ====================
@router.get("/standardoperatingprocedures", response_model=List[Dict[str, Any]])
def list_standardoperatingprocedures(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StandardOperatingProcedure records with pagination and filtering."""
    svc = StandardOperatingProcedureService()
    items = svc.list_standardoperatingprocedures(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/standardoperatingprocedures/{item_id}", response_model=Dict[str, Any])
def get_standardoperatingprocedure_by_id(item_id: int):
    """Retrieve detailed record for StandardOperatingProcedure by ID."""
    svc = StandardOperatingProcedureService()
    item = svc.get_standardoperatingprocedure_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StandardOperatingProcedure with ID {item_id} not found")
    return item.to_dict()

@router.post("/standardoperatingprocedures", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_standardoperatingprocedure(payload: StandardOperatingProcedureCreateSchema):
    """Create new StandardOperatingProcedure instance in enterprise repository."""
    svc = StandardOperatingProcedureService()
    try:
        item = svc.create_standardoperatingprocedure(
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

@router.put("/standardoperatingprocedures/{item_id}", response_model=Dict[str, Any])
def update_standardoperatingprocedure(item_id: int, payload: StandardOperatingProcedureUpdateSchema):
    """Update existing StandardOperatingProcedure record fields."""
    svc = StandardOperatingProcedureService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_standardoperatingprocedure(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StandardOperatingProcedure with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/standardoperatingprocedures/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_standardoperatingprocedure(item_id: int, hard: bool = Query(False)):
    """Delete StandardOperatingProcedure record (soft-delete by default)."""
    svc = StandardOperatingProcedureService()
    ok = svc.delete_standardoperatingprocedure(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StandardOperatingProcedure with ID {item_id} not found")
    return None

@router.get("/standardoperatingprocedures/analytics/metrics", response_model=Dict[str, Any])
def get_standardoperatingprocedure_metrics():
    """Calculate summary statistical KPIs for StandardOperatingProcedure collection."""
    svc = StandardOperatingProcedureService()
    return svc.calculate_aggregate_metrics()

# ==================== KnowledgeCategoryTopic Endpoints ====================
@router.get("/knowledgecategorytopics", response_model=List[Dict[str, Any]])
def list_knowledgecategorytopics(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List KnowledgeCategoryTopic records with pagination and filtering."""
    svc = KnowledgeCategoryTopicService()
    items = svc.list_knowledgecategorytopics(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/knowledgecategorytopics/{item_id}", response_model=Dict[str, Any])
def get_knowledgecategorytopic_by_id(item_id: int):
    """Retrieve detailed record for KnowledgeCategoryTopic by ID."""
    svc = KnowledgeCategoryTopicService()
    item = svc.get_knowledgecategorytopic_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"KnowledgeCategoryTopic with ID {item_id} not found")
    return item.to_dict()

@router.post("/knowledgecategorytopics", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_knowledgecategorytopic(payload: KnowledgeCategoryTopicCreateSchema):
    """Create new KnowledgeCategoryTopic instance in enterprise repository."""
    svc = KnowledgeCategoryTopicService()
    try:
        item = svc.create_knowledgecategorytopic(
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

@router.put("/knowledgecategorytopics/{item_id}", response_model=Dict[str, Any])
def update_knowledgecategorytopic(item_id: int, payload: KnowledgeCategoryTopicUpdateSchema):
    """Update existing KnowledgeCategoryTopic record fields."""
    svc = KnowledgeCategoryTopicService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_knowledgecategorytopic(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"KnowledgeCategoryTopic with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/knowledgecategorytopics/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_knowledgecategorytopic(item_id: int, hard: bool = Query(False)):
    """Delete KnowledgeCategoryTopic record (soft-delete by default)."""
    svc = KnowledgeCategoryTopicService()
    ok = svc.delete_knowledgecategorytopic(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"KnowledgeCategoryTopic with ID {item_id} not found")
    return None

@router.get("/knowledgecategorytopics/analytics/metrics", response_model=Dict[str, Any])
def get_knowledgecategorytopic_metrics():
    """Calculate summary statistical KPIs for KnowledgeCategoryTopic collection."""
    svc = KnowledgeCategoryTopicService()
    return svc.calculate_aggregate_metrics()

# ==================== ContentReviewWorkflow Endpoints ====================
@router.get("/contentreviewworkflows", response_model=List[Dict[str, Any]])
def list_contentreviewworkflows(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ContentReviewWorkflow records with pagination and filtering."""
    svc = ContentReviewWorkflowService()
    items = svc.list_contentreviewworkflows(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/contentreviewworkflows/{item_id}", response_model=Dict[str, Any])
def get_contentreviewworkflow_by_id(item_id: int):
    """Retrieve detailed record for ContentReviewWorkflow by ID."""
    svc = ContentReviewWorkflowService()
    item = svc.get_contentreviewworkflow_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ContentReviewWorkflow with ID {item_id} not found")
    return item.to_dict()

@router.post("/contentreviewworkflows", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_contentreviewworkflow(payload: ContentReviewWorkflowCreateSchema):
    """Create new ContentReviewWorkflow instance in enterprise repository."""
    svc = ContentReviewWorkflowService()
    try:
        item = svc.create_contentreviewworkflow(
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

@router.put("/contentreviewworkflows/{item_id}", response_model=Dict[str, Any])
def update_contentreviewworkflow(item_id: int, payload: ContentReviewWorkflowUpdateSchema):
    """Update existing ContentReviewWorkflow record fields."""
    svc = ContentReviewWorkflowService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_contentreviewworkflow(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ContentReviewWorkflow with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/contentreviewworkflows/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contentreviewworkflow(item_id: int, hard: bool = Query(False)):
    """Delete ContentReviewWorkflow record (soft-delete by default)."""
    svc = ContentReviewWorkflowService()
    ok = svc.delete_contentreviewworkflow(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ContentReviewWorkflow with ID {item_id} not found")
    return None

@router.get("/contentreviewworkflows/analytics/metrics", response_model=Dict[str, Any])
def get_contentreviewworkflow_metrics():
    """Calculate summary statistical KPIs for ContentReviewWorkflow collection."""
    svc = ContentReviewWorkflowService()
    return svc.calculate_aggregate_metrics()

# ==================== ArticleFeedbackVote Endpoints ====================
@router.get("/articlefeedbackvotes", response_model=List[Dict[str, Any]])
def list_articlefeedbackvotes(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ArticleFeedbackVote records with pagination and filtering."""
    svc = ArticleFeedbackVoteService()
    items = svc.list_articlefeedbackvotes(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/articlefeedbackvotes/{item_id}", response_model=Dict[str, Any])
def get_articlefeedbackvote_by_id(item_id: int):
    """Retrieve detailed record for ArticleFeedbackVote by ID."""
    svc = ArticleFeedbackVoteService()
    item = svc.get_articlefeedbackvote_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ArticleFeedbackVote with ID {item_id} not found")
    return item.to_dict()

@router.post("/articlefeedbackvotes", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_articlefeedbackvote(payload: ArticleFeedbackVoteCreateSchema):
    """Create new ArticleFeedbackVote instance in enterprise repository."""
    svc = ArticleFeedbackVoteService()
    try:
        item = svc.create_articlefeedbackvote(
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

@router.put("/articlefeedbackvotes/{item_id}", response_model=Dict[str, Any])
def update_articlefeedbackvote(item_id: int, payload: ArticleFeedbackVoteUpdateSchema):
    """Update existing ArticleFeedbackVote record fields."""
    svc = ArticleFeedbackVoteService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_articlefeedbackvote(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ArticleFeedbackVote with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/articlefeedbackvotes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_articlefeedbackvote(item_id: int, hard: bool = Query(False)):
    """Delete ArticleFeedbackVote record (soft-delete by default)."""
    svc = ArticleFeedbackVoteService()
    ok = svc.delete_articlefeedbackvote(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ArticleFeedbackVote with ID {item_id} not found")
    return None

@router.get("/articlefeedbackvotes/analytics/metrics", response_model=Dict[str, Any])
def get_articlefeedbackvote_metrics():
    """Calculate summary statistical KPIs for ArticleFeedbackVote collection."""
    svc = ArticleFeedbackVoteService()
    return svc.calculate_aggregate_metrics()

# ==================== SearchQueryAnalytics Endpoints ====================
@router.get("/searchqueryanalyticss", response_model=List[Dict[str, Any]])
def list_searchqueryanalyticss(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SearchQueryAnalytics records with pagination and filtering."""
    svc = SearchQueryAnalyticsService()
    items = svc.list_searchqueryanalyticss(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/searchqueryanalyticss/{item_id}", response_model=Dict[str, Any])
def get_searchqueryanalytics_by_id(item_id: int):
    """Retrieve detailed record for SearchQueryAnalytics by ID."""
    svc = SearchQueryAnalyticsService()
    item = svc.get_searchqueryanalytics_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SearchQueryAnalytics with ID {item_id} not found")
    return item.to_dict()

@router.post("/searchqueryanalyticss", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_searchqueryanalytics(payload: SearchQueryAnalyticsCreateSchema):
    """Create new SearchQueryAnalytics instance in enterprise repository."""
    svc = SearchQueryAnalyticsService()
    try:
        item = svc.create_searchqueryanalytics(
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

@router.put("/searchqueryanalyticss/{item_id}", response_model=Dict[str, Any])
def update_searchqueryanalytics(item_id: int, payload: SearchQueryAnalyticsUpdateSchema):
    """Update existing SearchQueryAnalytics record fields."""
    svc = SearchQueryAnalyticsService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_searchqueryanalytics(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SearchQueryAnalytics with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/searchqueryanalyticss/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_searchqueryanalytics(item_id: int, hard: bool = Query(False)):
    """Delete SearchQueryAnalytics record (soft-delete by default)."""
    svc = SearchQueryAnalyticsService()
    ok = svc.delete_searchqueryanalytics(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SearchQueryAnalytics with ID {item_id} not found")
    return None

@router.get("/searchqueryanalyticss/analytics/metrics", response_model=Dict[str, Any])
def get_searchqueryanalytics_metrics():
    """Calculate summary statistical KPIs for SearchQueryAnalytics collection."""
    svc = SearchQueryAnalyticsService()
    return svc.calculate_aggregate_metrics()

# ==================== TechnicalFaqItem Endpoints ====================
@router.get("/technicalfaqitems", response_model=List[Dict[str, Any]])
def list_technicalfaqitems(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TechnicalFaqItem records with pagination and filtering."""
    svc = TechnicalFaqItemService()
    items = svc.list_technicalfaqitems(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/technicalfaqitems/{item_id}", response_model=Dict[str, Any])
def get_technicalfaqitem_by_id(item_id: int):
    """Retrieve detailed record for TechnicalFaqItem by ID."""
    svc = TechnicalFaqItemService()
    item = svc.get_technicalfaqitem_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TechnicalFaqItem with ID {item_id} not found")
    return item.to_dict()

@router.post("/technicalfaqitems", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_technicalfaqitem(payload: TechnicalFaqItemCreateSchema):
    """Create new TechnicalFaqItem instance in enterprise repository."""
    svc = TechnicalFaqItemService()
    try:
        item = svc.create_technicalfaqitem(
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

@router.put("/technicalfaqitems/{item_id}", response_model=Dict[str, Any])
def update_technicalfaqitem(item_id: int, payload: TechnicalFaqItemUpdateSchema):
    """Update existing TechnicalFaqItem record fields."""
    svc = TechnicalFaqItemService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_technicalfaqitem(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TechnicalFaqItem with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/technicalfaqitems/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_technicalfaqitem(item_id: int, hard: bool = Query(False)):
    """Delete TechnicalFaqItem record (soft-delete by default)."""
    svc = TechnicalFaqItemService()
    ok = svc.delete_technicalfaqitem(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TechnicalFaqItem with ID {item_id} not found")
    return None

@router.get("/technicalfaqitems/analytics/metrics", response_model=Dict[str, Any])
def get_technicalfaqitem_metrics():
    """Calculate summary statistical KPIs for TechnicalFaqItem collection."""
    svc = TechnicalFaqItemService()
    return svc.calculate_aggregate_metrics()

# ==================== TroubleshootingGuide Endpoints ====================
@router.get("/troubleshootingguides", response_model=List[Dict[str, Any]])
def list_troubleshootingguides(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TroubleshootingGuide records with pagination and filtering."""
    svc = TroubleshootingGuideService()
    items = svc.list_troubleshootingguides(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/troubleshootingguides/{item_id}", response_model=Dict[str, Any])
def get_troubleshootingguide_by_id(item_id: int):
    """Retrieve detailed record for TroubleshootingGuide by ID."""
    svc = TroubleshootingGuideService()
    item = svc.get_troubleshootingguide_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TroubleshootingGuide with ID {item_id} not found")
    return item.to_dict()

@router.post("/troubleshootingguides", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_troubleshootingguide(payload: TroubleshootingGuideCreateSchema):
    """Create new TroubleshootingGuide instance in enterprise repository."""
    svc = TroubleshootingGuideService()
    try:
        item = svc.create_troubleshootingguide(
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

@router.put("/troubleshootingguides/{item_id}", response_model=Dict[str, Any])
def update_troubleshootingguide(item_id: int, payload: TroubleshootingGuideUpdateSchema):
    """Update existing TroubleshootingGuide record fields."""
    svc = TroubleshootingGuideService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_troubleshootingguide(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TroubleshootingGuide with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/troubleshootingguides/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_troubleshootingguide(item_id: int, hard: bool = Query(False)):
    """Delete TroubleshootingGuide record (soft-delete by default)."""
    svc = TroubleshootingGuideService()
    ok = svc.delete_troubleshootingguide(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TroubleshootingGuide with ID {item_id} not found")
    return None

@router.get("/troubleshootingguides/analytics/metrics", response_model=Dict[str, Any])
def get_troubleshootingguide_metrics():
    """Calculate summary statistical KPIs for TroubleshootingGuide collection."""
    svc = TroubleshootingGuideService()
    return svc.calculate_aggregate_metrics()

# ==================== TranslationLocalization Endpoints ====================
@router.get("/translationlocalizations", response_model=List[Dict[str, Any]])
def list_translationlocalizations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TranslationLocalization records with pagination and filtering."""
    svc = TranslationLocalizationService()
    items = svc.list_translationlocalizations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/translationlocalizations/{item_id}", response_model=Dict[str, Any])
def get_translationlocalization_by_id(item_id: int):
    """Retrieve detailed record for TranslationLocalization by ID."""
    svc = TranslationLocalizationService()
    item = svc.get_translationlocalization_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TranslationLocalization with ID {item_id} not found")
    return item.to_dict()

@router.post("/translationlocalizations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_translationlocalization(payload: TranslationLocalizationCreateSchema):
    """Create new TranslationLocalization instance in enterprise repository."""
    svc = TranslationLocalizationService()
    try:
        item = svc.create_translationlocalization(
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

@router.put("/translationlocalizations/{item_id}", response_model=Dict[str, Any])
def update_translationlocalization(item_id: int, payload: TranslationLocalizationUpdateSchema):
    """Update existing TranslationLocalization record fields."""
    svc = TranslationLocalizationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_translationlocalization(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TranslationLocalization with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/translationlocalizations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_translationlocalization(item_id: int, hard: bool = Query(False)):
    """Delete TranslationLocalization record (soft-delete by default)."""
    svc = TranslationLocalizationService()
    ok = svc.delete_translationlocalization(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TranslationLocalization with ID {item_id} not found")
    return None

@router.get("/translationlocalizations/analytics/metrics", response_model=Dict[str, Any])
def get_translationlocalization_metrics():
    """Calculate summary statistical KPIs for TranslationLocalization collection."""
    svc = TranslationLocalizationService()
    return svc.calculate_aggregate_metrics()

# ==================== ArticleAttachmentFile Endpoints ====================
@router.get("/articleattachmentfiles", response_model=List[Dict[str, Any]])
def list_articleattachmentfiles(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ArticleAttachmentFile records with pagination and filtering."""
    svc = ArticleAttachmentFileService()
    items = svc.list_articleattachmentfiles(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/articleattachmentfiles/{item_id}", response_model=Dict[str, Any])
def get_articleattachmentfile_by_id(item_id: int):
    """Retrieve detailed record for ArticleAttachmentFile by ID."""
    svc = ArticleAttachmentFileService()
    item = svc.get_articleattachmentfile_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ArticleAttachmentFile with ID {item_id} not found")
    return item.to_dict()

@router.post("/articleattachmentfiles", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_articleattachmentfile(payload: ArticleAttachmentFileCreateSchema):
    """Create new ArticleAttachmentFile instance in enterprise repository."""
    svc = ArticleAttachmentFileService()
    try:
        item = svc.create_articleattachmentfile(
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

@router.put("/articleattachmentfiles/{item_id}", response_model=Dict[str, Any])
def update_articleattachmentfile(item_id: int, payload: ArticleAttachmentFileUpdateSchema):
    """Update existing ArticleAttachmentFile record fields."""
    svc = ArticleAttachmentFileService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_articleattachmentfile(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ArticleAttachmentFile with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/articleattachmentfiles/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_articleattachmentfile(item_id: int, hard: bool = Query(False)):
    """Delete ArticleAttachmentFile record (soft-delete by default)."""
    svc = ArticleAttachmentFileService()
    ok = svc.delete_articleattachmentfile(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ArticleAttachmentFile with ID {item_id} not found")
    return None

@router.get("/articleattachmentfiles/analytics/metrics", response_model=Dict[str, Any])
def get_articleattachmentfile_metrics():
    """Calculate summary statistical KPIs for ArticleAttachmentFile collection."""
    svc = ArticleAttachmentFileService()
    return svc.calculate_aggregate_metrics()

# ==================== InternalWikiPage Endpoints ====================
@router.get("/internalwikipages", response_model=List[Dict[str, Any]])
def list_internalwikipages(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List InternalWikiPage records with pagination and filtering."""
    svc = InternalWikiPageService()
    items = svc.list_internalwikipages(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/internalwikipages/{item_id}", response_model=Dict[str, Any])
def get_internalwikipage_by_id(item_id: int):
    """Retrieve detailed record for InternalWikiPage by ID."""
    svc = InternalWikiPageService()
    item = svc.get_internalwikipage_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"InternalWikiPage with ID {item_id} not found")
    return item.to_dict()

@router.post("/internalwikipages", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_internalwikipage(payload: InternalWikiPageCreateSchema):
    """Create new InternalWikiPage instance in enterprise repository."""
    svc = InternalWikiPageService()
    try:
        item = svc.create_internalwikipage(
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

@router.put("/internalwikipages/{item_id}", response_model=Dict[str, Any])
def update_internalwikipage(item_id: int, payload: InternalWikiPageUpdateSchema):
    """Update existing InternalWikiPage record fields."""
    svc = InternalWikiPageService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_internalwikipage(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"InternalWikiPage with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/internalwikipages/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_internalwikipage(item_id: int, hard: bool = Query(False)):
    """Delete InternalWikiPage record (soft-delete by default)."""
    svc = InternalWikiPageService()
    ok = svc.delete_internalwikipage(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"InternalWikiPage with ID {item_id} not found")
    return None

@router.get("/internalwikipages/analytics/metrics", response_model=Dict[str, Any])
def get_internalwikipage_metrics():
    """Calculate summary statistical KPIs for InternalWikiPage collection."""
    svc = InternalWikiPageService()
    return svc.calculate_aggregate_metrics()

# ==================== KnowledgeGraphNode Endpoints ====================
@router.get("/knowledgegraphnodes", response_model=List[Dict[str, Any]])
def list_knowledgegraphnodes(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List KnowledgeGraphNode records with pagination and filtering."""
    svc = KnowledgeGraphNodeService()
    items = svc.list_knowledgegraphnodes(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/knowledgegraphnodes/{item_id}", response_model=Dict[str, Any])
def get_knowledgegraphnode_by_id(item_id: int):
    """Retrieve detailed record for KnowledgeGraphNode by ID."""
    svc = KnowledgeGraphNodeService()
    item = svc.get_knowledgegraphnode_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"KnowledgeGraphNode with ID {item_id} not found")
    return item.to_dict()

@router.post("/knowledgegraphnodes", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_knowledgegraphnode(payload: KnowledgeGraphNodeCreateSchema):
    """Create new KnowledgeGraphNode instance in enterprise repository."""
    svc = KnowledgeGraphNodeService()
    try:
        item = svc.create_knowledgegraphnode(
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

@router.put("/knowledgegraphnodes/{item_id}", response_model=Dict[str, Any])
def update_knowledgegraphnode(item_id: int, payload: KnowledgeGraphNodeUpdateSchema):
    """Update existing KnowledgeGraphNode record fields."""
    svc = KnowledgeGraphNodeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_knowledgegraphnode(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"KnowledgeGraphNode with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/knowledgegraphnodes/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_knowledgegraphnode(item_id: int, hard: bool = Query(False)):
    """Delete KnowledgeGraphNode record (soft-delete by default)."""
    svc = KnowledgeGraphNodeService()
    ok = svc.delete_knowledgegraphnode(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"KnowledgeGraphNode with ID {item_id} not found")
    return None

@router.get("/knowledgegraphnodes/analytics/metrics", response_model=Dict[str, Any])
def get_knowledgegraphnode_metrics():
    """Calculate summary statistical KPIs for KnowledgeGraphNode collection."""
    svc = KnowledgeGraphNodeService()
    return svc.calculate_aggregate_metrics()

# ==================== RevisionHistoryLog Endpoints ====================
@router.get("/revisionhistorylogs", response_model=List[Dict[str, Any]])
def list_revisionhistorylogs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List RevisionHistoryLog records with pagination and filtering."""
    svc = RevisionHistoryLogService()
    items = svc.list_revisionhistorylogs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/revisionhistorylogs/{item_id}", response_model=Dict[str, Any])
def get_revisionhistorylog_by_id(item_id: int):
    """Retrieve detailed record for RevisionHistoryLog by ID."""
    svc = RevisionHistoryLogService()
    item = svc.get_revisionhistorylog_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"RevisionHistoryLog with ID {item_id} not found")
    return item.to_dict()

@router.post("/revisionhistorylogs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_revisionhistorylog(payload: RevisionHistoryLogCreateSchema):
    """Create new RevisionHistoryLog instance in enterprise repository."""
    svc = RevisionHistoryLogService()
    try:
        item = svc.create_revisionhistorylog(
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

@router.put("/revisionhistorylogs/{item_id}", response_model=Dict[str, Any])
def update_revisionhistorylog(item_id: int, payload: RevisionHistoryLogUpdateSchema):
    """Update existing RevisionHistoryLog record fields."""
    svc = RevisionHistoryLogService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_revisionhistorylog(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"RevisionHistoryLog with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/revisionhistorylogs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_revisionhistorylog(item_id: int, hard: bool = Query(False)):
    """Delete RevisionHistoryLog record (soft-delete by default)."""
    svc = RevisionHistoryLogService()
    ok = svc.delete_revisionhistorylog(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"RevisionHistoryLog with ID {item_id} not found")
    return None

@router.get("/revisionhistorylogs/analytics/metrics", response_model=Dict[str, Any])
def get_revisionhistorylog_metrics():
    """Calculate summary statistical KPIs for RevisionHistoryLog collection."""
    svc = RevisionHistoryLogService()
    return svc.calculate_aggregate_metrics()

# ==================== ExpertAuthorDirectory Endpoints ====================
@router.get("/expertauthordirectorys", response_model=List[Dict[str, Any]])
def list_expertauthordirectorys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ExpertAuthorDirectory records with pagination and filtering."""
    svc = ExpertAuthorDirectoryService()
    items = svc.list_expertauthordirectorys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/expertauthordirectorys/{item_id}", response_model=Dict[str, Any])
def get_expertauthordirectory_by_id(item_id: int):
    """Retrieve detailed record for ExpertAuthorDirectory by ID."""
    svc = ExpertAuthorDirectoryService()
    item = svc.get_expertauthordirectory_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ExpertAuthorDirectory with ID {item_id} not found")
    return item.to_dict()

@router.post("/expertauthordirectorys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_expertauthordirectory(payload: ExpertAuthorDirectoryCreateSchema):
    """Create new ExpertAuthorDirectory instance in enterprise repository."""
    svc = ExpertAuthorDirectoryService()
    try:
        item = svc.create_expertauthordirectory(
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

@router.put("/expertauthordirectorys/{item_id}", response_model=Dict[str, Any])
def update_expertauthordirectory(item_id: int, payload: ExpertAuthorDirectoryUpdateSchema):
    """Update existing ExpertAuthorDirectory record fields."""
    svc = ExpertAuthorDirectoryService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_expertauthordirectory(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ExpertAuthorDirectory with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/expertauthordirectorys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expertauthordirectory(item_id: int, hard: bool = Query(False)):
    """Delete ExpertAuthorDirectory record (soft-delete by default)."""
    svc = ExpertAuthorDirectoryService()
    ok = svc.delete_expertauthordirectory(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ExpertAuthorDirectory with ID {item_id} not found")
    return None

@router.get("/expertauthordirectorys/analytics/metrics", response_model=Dict[str, Any])
def get_expertauthordirectory_metrics():
    """Calculate summary statistical KPIs for ExpertAuthorDirectory collection."""
    svc = ExpertAuthorDirectoryService()
    return svc.calculate_aggregate_metrics()

# ==================== DeprecatedNotice Endpoints ====================
@router.get("/deprecatednotices", response_model=List[Dict[str, Any]])
def list_deprecatednotices(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DeprecatedNotice records with pagination and filtering."""
    svc = DeprecatedNoticeService()
    items = svc.list_deprecatednotices(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/deprecatednotices/{item_id}", response_model=Dict[str, Any])
def get_deprecatednotice_by_id(item_id: int):
    """Retrieve detailed record for DeprecatedNotice by ID."""
    svc = DeprecatedNoticeService()
    item = svc.get_deprecatednotice_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DeprecatedNotice with ID {item_id} not found")
    return item.to_dict()

@router.post("/deprecatednotices", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_deprecatednotice(payload: DeprecatedNoticeCreateSchema):
    """Create new DeprecatedNotice instance in enterprise repository."""
    svc = DeprecatedNoticeService()
    try:
        item = svc.create_deprecatednotice(
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

@router.put("/deprecatednotices/{item_id}", response_model=Dict[str, Any])
def update_deprecatednotice(item_id: int, payload: DeprecatedNoticeUpdateSchema):
    """Update existing DeprecatedNotice record fields."""
    svc = DeprecatedNoticeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_deprecatednotice(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DeprecatedNotice with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/deprecatednotices/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_deprecatednotice(item_id: int, hard: bool = Query(False)):
    """Delete DeprecatedNotice record (soft-delete by default)."""
    svc = DeprecatedNoticeService()
    ok = svc.delete_deprecatednotice(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DeprecatedNotice with ID {item_id} not found")
    return None

@router.get("/deprecatednotices/analytics/metrics", response_model=Dict[str, Any])
def get_deprecatednotice_metrics():
    """Calculate summary statistical KPIs for DeprecatedNotice collection."""
    svc = DeprecatedNoticeService()
    return svc.calculate_aggregate_metrics()

# ==================== AccessVisibilityTier Endpoints ====================
@router.get("/accessvisibilitytiers", response_model=List[Dict[str, Any]])
def list_accessvisibilitytiers(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List AccessVisibilityTier records with pagination and filtering."""
    svc = AccessVisibilityTierService()
    items = svc.list_accessvisibilitytiers(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/accessvisibilitytiers/{item_id}", response_model=Dict[str, Any])
def get_accessvisibilitytier_by_id(item_id: int):
    """Retrieve detailed record for AccessVisibilityTier by ID."""
    svc = AccessVisibilityTierService()
    item = svc.get_accessvisibilitytier_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"AccessVisibilityTier with ID {item_id} not found")
    return item.to_dict()

@router.post("/accessvisibilitytiers", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_accessvisibilitytier(payload: AccessVisibilityTierCreateSchema):
    """Create new AccessVisibilityTier instance in enterprise repository."""
    svc = AccessVisibilityTierService()
    try:
        item = svc.create_accessvisibilitytier(
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

@router.put("/accessvisibilitytiers/{item_id}", response_model=Dict[str, Any])
def update_accessvisibilitytier(item_id: int, payload: AccessVisibilityTierUpdateSchema):
    """Update existing AccessVisibilityTier record fields."""
    svc = AccessVisibilityTierService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_accessvisibilitytier(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"AccessVisibilityTier with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/accessvisibilitytiers/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_accessvisibilitytier(item_id: int, hard: bool = Query(False)):
    """Delete AccessVisibilityTier record (soft-delete by default)."""
    svc = AccessVisibilityTierService()
    ok = svc.delete_accessvisibilitytier(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"AccessVisibilityTier with ID {item_id} not found")
    return None

@router.get("/accessvisibilitytiers/analytics/metrics", response_model=Dict[str, Any])
def get_accessvisibilitytier_metrics():
    """Calculate summary statistical KPIs for AccessVisibilityTier collection."""
    svc = AccessVisibilityTierService()
    return svc.calculate_aggregate_metrics()

