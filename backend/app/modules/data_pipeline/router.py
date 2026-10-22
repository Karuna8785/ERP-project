"""
Data Pipeline, ETL & Data Lake Federation - REST API Endpoints Router
"""
from fastapi import APIRouter, HTTPException, Query, status, Depends
from typing import List, Dict, Any, Optional
from .services import (
    DataPipelineDefinitionService,
    ETLJobExecutionRunService,
    DataSourceConnectionService,
    DataSinkDestinationService,
    SchemaRegistryContractService,
    PartitioningStrategyRuleService,
    DataQualityCheckRuleService,
    TransformationDataflowService,
    IncrementalSyncWatermarkService,
    PipelineAlertNotificationService,
    DataLakeStorageBucketService,
    ColumnMaskingPolicyService,
    DataLineageEdgeService,
    BackfillExecutionJobService,
    PipelineThroughputMetricService,
    StreamingTopicOffsetService,
)
from .schemas import (
    DataPipelineDefinitionCreateSchema, DataPipelineDefinitionUpdateSchema, DataPipelineDefinitionResponseSchema,
    ETLJobExecutionRunCreateSchema, ETLJobExecutionRunUpdateSchema, ETLJobExecutionRunResponseSchema,
    DataSourceConnectionCreateSchema, DataSourceConnectionUpdateSchema, DataSourceConnectionResponseSchema,
    DataSinkDestinationCreateSchema, DataSinkDestinationUpdateSchema, DataSinkDestinationResponseSchema,
    SchemaRegistryContractCreateSchema, SchemaRegistryContractUpdateSchema, SchemaRegistryContractResponseSchema,
    PartitioningStrategyRuleCreateSchema, PartitioningStrategyRuleUpdateSchema, PartitioningStrategyRuleResponseSchema,
    DataQualityCheckRuleCreateSchema, DataQualityCheckRuleUpdateSchema, DataQualityCheckRuleResponseSchema,
    TransformationDataflowCreateSchema, TransformationDataflowUpdateSchema, TransformationDataflowResponseSchema,
    IncrementalSyncWatermarkCreateSchema, IncrementalSyncWatermarkUpdateSchema, IncrementalSyncWatermarkResponseSchema,
    PipelineAlertNotificationCreateSchema, PipelineAlertNotificationUpdateSchema, PipelineAlertNotificationResponseSchema,
    DataLakeStorageBucketCreateSchema, DataLakeStorageBucketUpdateSchema, DataLakeStorageBucketResponseSchema,
    ColumnMaskingPolicyCreateSchema, ColumnMaskingPolicyUpdateSchema, ColumnMaskingPolicyResponseSchema,
    DataLineageEdgeCreateSchema, DataLineageEdgeUpdateSchema, DataLineageEdgeResponseSchema,
    BackfillExecutionJobCreateSchema, BackfillExecutionJobUpdateSchema, BackfillExecutionJobResponseSchema,
    PipelineThroughputMetricCreateSchema, PipelineThroughputMetricUpdateSchema, PipelineThroughputMetricResponseSchema,
    StreamingTopicOffsetCreateSchema, StreamingTopicOffsetUpdateSchema, StreamingTopicOffsetResponseSchema,
)

router = APIRouter(prefix="/data_pipeline", tags=["Data Pipeline, ETL & Data Lake Federation"])

# ==================== DataPipelineDefinition Endpoints ====================
@router.get("/datapipelinedefinitions", response_model=List[Dict[str, Any]])
def list_datapipelinedefinitions(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DataPipelineDefinition records with pagination and filtering."""
    svc = DataPipelineDefinitionService()
    items = svc.list_datapipelinedefinitions(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/datapipelinedefinitions/{item_id}", response_model=Dict[str, Any])
def get_datapipelinedefinition_by_id(item_id: int):
    """Retrieve detailed record for DataPipelineDefinition by ID."""
    svc = DataPipelineDefinitionService()
    item = svc.get_datapipelinedefinition_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DataPipelineDefinition with ID {item_id} not found")
    return item.to_dict()

@router.post("/datapipelinedefinitions", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_datapipelinedefinition(payload: DataPipelineDefinitionCreateSchema):
    """Create new DataPipelineDefinition instance in enterprise repository."""
    svc = DataPipelineDefinitionService()
    try:
        item = svc.create_datapipelinedefinition(
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

@router.put("/datapipelinedefinitions/{item_id}", response_model=Dict[str, Any])
def update_datapipelinedefinition(item_id: int, payload: DataPipelineDefinitionUpdateSchema):
    """Update existing DataPipelineDefinition record fields."""
    svc = DataPipelineDefinitionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_datapipelinedefinition(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DataPipelineDefinition with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/datapipelinedefinitions/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_datapipelinedefinition(item_id: int, hard: bool = Query(False)):
    """Delete DataPipelineDefinition record (soft-delete by default)."""
    svc = DataPipelineDefinitionService()
    ok = svc.delete_datapipelinedefinition(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DataPipelineDefinition with ID {item_id} not found")
    return None

@router.get("/datapipelinedefinitions/analytics/metrics", response_model=Dict[str, Any])
def get_datapipelinedefinition_metrics():
    """Calculate summary statistical KPIs for DataPipelineDefinition collection."""
    svc = DataPipelineDefinitionService()
    return svc.calculate_aggregate_metrics()

# ==================== ETLJobExecutionRun Endpoints ====================
@router.get("/etljobexecutionruns", response_model=List[Dict[str, Any]])
def list_etljobexecutionruns(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ETLJobExecutionRun records with pagination and filtering."""
    svc = ETLJobExecutionRunService()
    items = svc.list_etljobexecutionruns(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/etljobexecutionruns/{item_id}", response_model=Dict[str, Any])
def get_etljobexecutionrun_by_id(item_id: int):
    """Retrieve detailed record for ETLJobExecutionRun by ID."""
    svc = ETLJobExecutionRunService()
    item = svc.get_etljobexecutionrun_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ETLJobExecutionRun with ID {item_id} not found")
    return item.to_dict()

@router.post("/etljobexecutionruns", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_etljobexecutionrun(payload: ETLJobExecutionRunCreateSchema):
    """Create new ETLJobExecutionRun instance in enterprise repository."""
    svc = ETLJobExecutionRunService()
    try:
        item = svc.create_etljobexecutionrun(
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

@router.put("/etljobexecutionruns/{item_id}", response_model=Dict[str, Any])
def update_etljobexecutionrun(item_id: int, payload: ETLJobExecutionRunUpdateSchema):
    """Update existing ETLJobExecutionRun record fields."""
    svc = ETLJobExecutionRunService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_etljobexecutionrun(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ETLJobExecutionRun with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/etljobexecutionruns/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_etljobexecutionrun(item_id: int, hard: bool = Query(False)):
    """Delete ETLJobExecutionRun record (soft-delete by default)."""
    svc = ETLJobExecutionRunService()
    ok = svc.delete_etljobexecutionrun(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ETLJobExecutionRun with ID {item_id} not found")
    return None

@router.get("/etljobexecutionruns/analytics/metrics", response_model=Dict[str, Any])
def get_etljobexecutionrun_metrics():
    """Calculate summary statistical KPIs for ETLJobExecutionRun collection."""
    svc = ETLJobExecutionRunService()
    return svc.calculate_aggregate_metrics()

# ==================== DataSourceConnection Endpoints ====================
@router.get("/datasourceconnections", response_model=List[Dict[str, Any]])
def list_datasourceconnections(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DataSourceConnection records with pagination and filtering."""
    svc = DataSourceConnectionService()
    items = svc.list_datasourceconnections(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/datasourceconnections/{item_id}", response_model=Dict[str, Any])
def get_datasourceconnection_by_id(item_id: int):
    """Retrieve detailed record for DataSourceConnection by ID."""
    svc = DataSourceConnectionService()
    item = svc.get_datasourceconnection_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DataSourceConnection with ID {item_id} not found")
    return item.to_dict()

@router.post("/datasourceconnections", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_datasourceconnection(payload: DataSourceConnectionCreateSchema):
    """Create new DataSourceConnection instance in enterprise repository."""
    svc = DataSourceConnectionService()
    try:
        item = svc.create_datasourceconnection(
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

@router.put("/datasourceconnections/{item_id}", response_model=Dict[str, Any])
def update_datasourceconnection(item_id: int, payload: DataSourceConnectionUpdateSchema):
    """Update existing DataSourceConnection record fields."""
    svc = DataSourceConnectionService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_datasourceconnection(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DataSourceConnection with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/datasourceconnections/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_datasourceconnection(item_id: int, hard: bool = Query(False)):
    """Delete DataSourceConnection record (soft-delete by default)."""
    svc = DataSourceConnectionService()
    ok = svc.delete_datasourceconnection(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DataSourceConnection with ID {item_id} not found")
    return None

@router.get("/datasourceconnections/analytics/metrics", response_model=Dict[str, Any])
def get_datasourceconnection_metrics():
    """Calculate summary statistical KPIs for DataSourceConnection collection."""
    svc = DataSourceConnectionService()
    return svc.calculate_aggregate_metrics()

# ==================== DataSinkDestination Endpoints ====================
@router.get("/datasinkdestinations", response_model=List[Dict[str, Any]])
def list_datasinkdestinations(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DataSinkDestination records with pagination and filtering."""
    svc = DataSinkDestinationService()
    items = svc.list_datasinkdestinations(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/datasinkdestinations/{item_id}", response_model=Dict[str, Any])
def get_datasinkdestination_by_id(item_id: int):
    """Retrieve detailed record for DataSinkDestination by ID."""
    svc = DataSinkDestinationService()
    item = svc.get_datasinkdestination_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DataSinkDestination with ID {item_id} not found")
    return item.to_dict()

@router.post("/datasinkdestinations", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_datasinkdestination(payload: DataSinkDestinationCreateSchema):
    """Create new DataSinkDestination instance in enterprise repository."""
    svc = DataSinkDestinationService()
    try:
        item = svc.create_datasinkdestination(
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

@router.put("/datasinkdestinations/{item_id}", response_model=Dict[str, Any])
def update_datasinkdestination(item_id: int, payload: DataSinkDestinationUpdateSchema):
    """Update existing DataSinkDestination record fields."""
    svc = DataSinkDestinationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_datasinkdestination(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DataSinkDestination with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/datasinkdestinations/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_datasinkdestination(item_id: int, hard: bool = Query(False)):
    """Delete DataSinkDestination record (soft-delete by default)."""
    svc = DataSinkDestinationService()
    ok = svc.delete_datasinkdestination(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DataSinkDestination with ID {item_id} not found")
    return None

@router.get("/datasinkdestinations/analytics/metrics", response_model=Dict[str, Any])
def get_datasinkdestination_metrics():
    """Calculate summary statistical KPIs for DataSinkDestination collection."""
    svc = DataSinkDestinationService()
    return svc.calculate_aggregate_metrics()

# ==================== SchemaRegistryContract Endpoints ====================
@router.get("/schemaregistrycontracts", response_model=List[Dict[str, Any]])
def list_schemaregistrycontracts(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List SchemaRegistryContract records with pagination and filtering."""
    svc = SchemaRegistryContractService()
    items = svc.list_schemaregistrycontracts(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/schemaregistrycontracts/{item_id}", response_model=Dict[str, Any])
def get_schemaregistrycontract_by_id(item_id: int):
    """Retrieve detailed record for SchemaRegistryContract by ID."""
    svc = SchemaRegistryContractService()
    item = svc.get_schemaregistrycontract_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"SchemaRegistryContract with ID {item_id} not found")
    return item.to_dict()

@router.post("/schemaregistrycontracts", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_schemaregistrycontract(payload: SchemaRegistryContractCreateSchema):
    """Create new SchemaRegistryContract instance in enterprise repository."""
    svc = SchemaRegistryContractService()
    try:
        item = svc.create_schemaregistrycontract(
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

@router.put("/schemaregistrycontracts/{item_id}", response_model=Dict[str, Any])
def update_schemaregistrycontract(item_id: int, payload: SchemaRegistryContractUpdateSchema):
    """Update existing SchemaRegistryContract record fields."""
    svc = SchemaRegistryContractService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_schemaregistrycontract(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"SchemaRegistryContract with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/schemaregistrycontracts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_schemaregistrycontract(item_id: int, hard: bool = Query(False)):
    """Delete SchemaRegistryContract record (soft-delete by default)."""
    svc = SchemaRegistryContractService()
    ok = svc.delete_schemaregistrycontract(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"SchemaRegistryContract with ID {item_id} not found")
    return None

@router.get("/schemaregistrycontracts/analytics/metrics", response_model=Dict[str, Any])
def get_schemaregistrycontract_metrics():
    """Calculate summary statistical KPIs for SchemaRegistryContract collection."""
    svc = SchemaRegistryContractService()
    return svc.calculate_aggregate_metrics()

# ==================== PartitioningStrategyRule Endpoints ====================
@router.get("/partitioningstrategyrules", response_model=List[Dict[str, Any]])
def list_partitioningstrategyrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PartitioningStrategyRule records with pagination and filtering."""
    svc = PartitioningStrategyRuleService()
    items = svc.list_partitioningstrategyrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/partitioningstrategyrules/{item_id}", response_model=Dict[str, Any])
def get_partitioningstrategyrule_by_id(item_id: int):
    """Retrieve detailed record for PartitioningStrategyRule by ID."""
    svc = PartitioningStrategyRuleService()
    item = svc.get_partitioningstrategyrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PartitioningStrategyRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/partitioningstrategyrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_partitioningstrategyrule(payload: PartitioningStrategyRuleCreateSchema):
    """Create new PartitioningStrategyRule instance in enterprise repository."""
    svc = PartitioningStrategyRuleService()
    try:
        item = svc.create_partitioningstrategyrule(
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

@router.put("/partitioningstrategyrules/{item_id}", response_model=Dict[str, Any])
def update_partitioningstrategyrule(item_id: int, payload: PartitioningStrategyRuleUpdateSchema):
    """Update existing PartitioningStrategyRule record fields."""
    svc = PartitioningStrategyRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_partitioningstrategyrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PartitioningStrategyRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/partitioningstrategyrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_partitioningstrategyrule(item_id: int, hard: bool = Query(False)):
    """Delete PartitioningStrategyRule record (soft-delete by default)."""
    svc = PartitioningStrategyRuleService()
    ok = svc.delete_partitioningstrategyrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PartitioningStrategyRule with ID {item_id} not found")
    return None

@router.get("/partitioningstrategyrules/analytics/metrics", response_model=Dict[str, Any])
def get_partitioningstrategyrule_metrics():
    """Calculate summary statistical KPIs for PartitioningStrategyRule collection."""
    svc = PartitioningStrategyRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== DataQualityCheckRule Endpoints ====================
@router.get("/dataqualitycheckrules", response_model=List[Dict[str, Any]])
def list_dataqualitycheckrules(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DataQualityCheckRule records with pagination and filtering."""
    svc = DataQualityCheckRuleService()
    items = svc.list_dataqualitycheckrules(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/dataqualitycheckrules/{item_id}", response_model=Dict[str, Any])
def get_dataqualitycheckrule_by_id(item_id: int):
    """Retrieve detailed record for DataQualityCheckRule by ID."""
    svc = DataQualityCheckRuleService()
    item = svc.get_dataqualitycheckrule_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DataQualityCheckRule with ID {item_id} not found")
    return item.to_dict()

@router.post("/dataqualitycheckrules", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_dataqualitycheckrule(payload: DataQualityCheckRuleCreateSchema):
    """Create new DataQualityCheckRule instance in enterprise repository."""
    svc = DataQualityCheckRuleService()
    try:
        item = svc.create_dataqualitycheckrule(
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

@router.put("/dataqualitycheckrules/{item_id}", response_model=Dict[str, Any])
def update_dataqualitycheckrule(item_id: int, payload: DataQualityCheckRuleUpdateSchema):
    """Update existing DataQualityCheckRule record fields."""
    svc = DataQualityCheckRuleService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_dataqualitycheckrule(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DataQualityCheckRule with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/dataqualitycheckrules/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dataqualitycheckrule(item_id: int, hard: bool = Query(False)):
    """Delete DataQualityCheckRule record (soft-delete by default)."""
    svc = DataQualityCheckRuleService()
    ok = svc.delete_dataqualitycheckrule(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DataQualityCheckRule with ID {item_id} not found")
    return None

@router.get("/dataqualitycheckrules/analytics/metrics", response_model=Dict[str, Any])
def get_dataqualitycheckrule_metrics():
    """Calculate summary statistical KPIs for DataQualityCheckRule collection."""
    svc = DataQualityCheckRuleService()
    return svc.calculate_aggregate_metrics()

# ==================== TransformationDataflow Endpoints ====================
@router.get("/transformationdataflows", response_model=List[Dict[str, Any]])
def list_transformationdataflows(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List TransformationDataflow records with pagination and filtering."""
    svc = TransformationDataflowService()
    items = svc.list_transformationdataflows(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/transformationdataflows/{item_id}", response_model=Dict[str, Any])
def get_transformationdataflow_by_id(item_id: int):
    """Retrieve detailed record for TransformationDataflow by ID."""
    svc = TransformationDataflowService()
    item = svc.get_transformationdataflow_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"TransformationDataflow with ID {item_id} not found")
    return item.to_dict()

@router.post("/transformationdataflows", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_transformationdataflow(payload: TransformationDataflowCreateSchema):
    """Create new TransformationDataflow instance in enterprise repository."""
    svc = TransformationDataflowService()
    try:
        item = svc.create_transformationdataflow(
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

@router.put("/transformationdataflows/{item_id}", response_model=Dict[str, Any])
def update_transformationdataflow(item_id: int, payload: TransformationDataflowUpdateSchema):
    """Update existing TransformationDataflow record fields."""
    svc = TransformationDataflowService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_transformationdataflow(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"TransformationDataflow with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/transformationdataflows/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_transformationdataflow(item_id: int, hard: bool = Query(False)):
    """Delete TransformationDataflow record (soft-delete by default)."""
    svc = TransformationDataflowService()
    ok = svc.delete_transformationdataflow(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"TransformationDataflow with ID {item_id} not found")
    return None

@router.get("/transformationdataflows/analytics/metrics", response_model=Dict[str, Any])
def get_transformationdataflow_metrics():
    """Calculate summary statistical KPIs for TransformationDataflow collection."""
    svc = TransformationDataflowService()
    return svc.calculate_aggregate_metrics()

# ==================== IncrementalSyncWatermark Endpoints ====================
@router.get("/incrementalsyncwatermarks", response_model=List[Dict[str, Any]])
def list_incrementalsyncwatermarks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List IncrementalSyncWatermark records with pagination and filtering."""
    svc = IncrementalSyncWatermarkService()
    items = svc.list_incrementalsyncwatermarks(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/incrementalsyncwatermarks/{item_id}", response_model=Dict[str, Any])
def get_incrementalsyncwatermark_by_id(item_id: int):
    """Retrieve detailed record for IncrementalSyncWatermark by ID."""
    svc = IncrementalSyncWatermarkService()
    item = svc.get_incrementalsyncwatermark_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"IncrementalSyncWatermark with ID {item_id} not found")
    return item.to_dict()

@router.post("/incrementalsyncwatermarks", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_incrementalsyncwatermark(payload: IncrementalSyncWatermarkCreateSchema):
    """Create new IncrementalSyncWatermark instance in enterprise repository."""
    svc = IncrementalSyncWatermarkService()
    try:
        item = svc.create_incrementalsyncwatermark(
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

@router.put("/incrementalsyncwatermarks/{item_id}", response_model=Dict[str, Any])
def update_incrementalsyncwatermark(item_id: int, payload: IncrementalSyncWatermarkUpdateSchema):
    """Update existing IncrementalSyncWatermark record fields."""
    svc = IncrementalSyncWatermarkService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_incrementalsyncwatermark(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"IncrementalSyncWatermark with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/incrementalsyncwatermarks/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_incrementalsyncwatermark(item_id: int, hard: bool = Query(False)):
    """Delete IncrementalSyncWatermark record (soft-delete by default)."""
    svc = IncrementalSyncWatermarkService()
    ok = svc.delete_incrementalsyncwatermark(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"IncrementalSyncWatermark with ID {item_id} not found")
    return None

@router.get("/incrementalsyncwatermarks/analytics/metrics", response_model=Dict[str, Any])
def get_incrementalsyncwatermark_metrics():
    """Calculate summary statistical KPIs for IncrementalSyncWatermark collection."""
    svc = IncrementalSyncWatermarkService()
    return svc.calculate_aggregate_metrics()

# ==================== PipelineAlertNotification Endpoints ====================
@router.get("/pipelinealertnotifications", response_model=List[Dict[str, Any]])
def list_pipelinealertnotifications(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PipelineAlertNotification records with pagination and filtering."""
    svc = PipelineAlertNotificationService()
    items = svc.list_pipelinealertnotifications(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/pipelinealertnotifications/{item_id}", response_model=Dict[str, Any])
def get_pipelinealertnotification_by_id(item_id: int):
    """Retrieve detailed record for PipelineAlertNotification by ID."""
    svc = PipelineAlertNotificationService()
    item = svc.get_pipelinealertnotification_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PipelineAlertNotification with ID {item_id} not found")
    return item.to_dict()

@router.post("/pipelinealertnotifications", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_pipelinealertnotification(payload: PipelineAlertNotificationCreateSchema):
    """Create new PipelineAlertNotification instance in enterprise repository."""
    svc = PipelineAlertNotificationService()
    try:
        item = svc.create_pipelinealertnotification(
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

@router.put("/pipelinealertnotifications/{item_id}", response_model=Dict[str, Any])
def update_pipelinealertnotification(item_id: int, payload: PipelineAlertNotificationUpdateSchema):
    """Update existing PipelineAlertNotification record fields."""
    svc = PipelineAlertNotificationService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_pipelinealertnotification(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PipelineAlertNotification with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/pipelinealertnotifications/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pipelinealertnotification(item_id: int, hard: bool = Query(False)):
    """Delete PipelineAlertNotification record (soft-delete by default)."""
    svc = PipelineAlertNotificationService()
    ok = svc.delete_pipelinealertnotification(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PipelineAlertNotification with ID {item_id} not found")
    return None

@router.get("/pipelinealertnotifications/analytics/metrics", response_model=Dict[str, Any])
def get_pipelinealertnotification_metrics():
    """Calculate summary statistical KPIs for PipelineAlertNotification collection."""
    svc = PipelineAlertNotificationService()
    return svc.calculate_aggregate_metrics()

# ==================== DataLakeStorageBucket Endpoints ====================
@router.get("/datalakestoragebuckets", response_model=List[Dict[str, Any]])
def list_datalakestoragebuckets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DataLakeStorageBucket records with pagination and filtering."""
    svc = DataLakeStorageBucketService()
    items = svc.list_datalakestoragebuckets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/datalakestoragebuckets/{item_id}", response_model=Dict[str, Any])
def get_datalakestoragebucket_by_id(item_id: int):
    """Retrieve detailed record for DataLakeStorageBucket by ID."""
    svc = DataLakeStorageBucketService()
    item = svc.get_datalakestoragebucket_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DataLakeStorageBucket with ID {item_id} not found")
    return item.to_dict()

@router.post("/datalakestoragebuckets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_datalakestoragebucket(payload: DataLakeStorageBucketCreateSchema):
    """Create new DataLakeStorageBucket instance in enterprise repository."""
    svc = DataLakeStorageBucketService()
    try:
        item = svc.create_datalakestoragebucket(
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

@router.put("/datalakestoragebuckets/{item_id}", response_model=Dict[str, Any])
def update_datalakestoragebucket(item_id: int, payload: DataLakeStorageBucketUpdateSchema):
    """Update existing DataLakeStorageBucket record fields."""
    svc = DataLakeStorageBucketService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_datalakestoragebucket(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DataLakeStorageBucket with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/datalakestoragebuckets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_datalakestoragebucket(item_id: int, hard: bool = Query(False)):
    """Delete DataLakeStorageBucket record (soft-delete by default)."""
    svc = DataLakeStorageBucketService()
    ok = svc.delete_datalakestoragebucket(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DataLakeStorageBucket with ID {item_id} not found")
    return None

@router.get("/datalakestoragebuckets/analytics/metrics", response_model=Dict[str, Any])
def get_datalakestoragebucket_metrics():
    """Calculate summary statistical KPIs for DataLakeStorageBucket collection."""
    svc = DataLakeStorageBucketService()
    return svc.calculate_aggregate_metrics()

# ==================== ColumnMaskingPolicy Endpoints ====================
@router.get("/columnmaskingpolicys", response_model=List[Dict[str, Any]])
def list_columnmaskingpolicys(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List ColumnMaskingPolicy records with pagination and filtering."""
    svc = ColumnMaskingPolicyService()
    items = svc.list_columnmaskingpolicys(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/columnmaskingpolicys/{item_id}", response_model=Dict[str, Any])
def get_columnmaskingpolicy_by_id(item_id: int):
    """Retrieve detailed record for ColumnMaskingPolicy by ID."""
    svc = ColumnMaskingPolicyService()
    item = svc.get_columnmaskingpolicy_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"ColumnMaskingPolicy with ID {item_id} not found")
    return item.to_dict()

@router.post("/columnmaskingpolicys", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_columnmaskingpolicy(payload: ColumnMaskingPolicyCreateSchema):
    """Create new ColumnMaskingPolicy instance in enterprise repository."""
    svc = ColumnMaskingPolicyService()
    try:
        item = svc.create_columnmaskingpolicy(
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

@router.put("/columnmaskingpolicys/{item_id}", response_model=Dict[str, Any])
def update_columnmaskingpolicy(item_id: int, payload: ColumnMaskingPolicyUpdateSchema):
    """Update existing ColumnMaskingPolicy record fields."""
    svc = ColumnMaskingPolicyService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_columnmaskingpolicy(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"ColumnMaskingPolicy with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/columnmaskingpolicys/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_columnmaskingpolicy(item_id: int, hard: bool = Query(False)):
    """Delete ColumnMaskingPolicy record (soft-delete by default)."""
    svc = ColumnMaskingPolicyService()
    ok = svc.delete_columnmaskingpolicy(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"ColumnMaskingPolicy with ID {item_id} not found")
    return None

@router.get("/columnmaskingpolicys/analytics/metrics", response_model=Dict[str, Any])
def get_columnmaskingpolicy_metrics():
    """Calculate summary statistical KPIs for ColumnMaskingPolicy collection."""
    svc = ColumnMaskingPolicyService()
    return svc.calculate_aggregate_metrics()

# ==================== DataLineageEdge Endpoints ====================
@router.get("/datalineageedges", response_model=List[Dict[str, Any]])
def list_datalineageedges(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List DataLineageEdge records with pagination and filtering."""
    svc = DataLineageEdgeService()
    items = svc.list_datalineageedges(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/datalineageedges/{item_id}", response_model=Dict[str, Any])
def get_datalineageedge_by_id(item_id: int):
    """Retrieve detailed record for DataLineageEdge by ID."""
    svc = DataLineageEdgeService()
    item = svc.get_datalineageedge_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"DataLineageEdge with ID {item_id} not found")
    return item.to_dict()

@router.post("/datalineageedges", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_datalineageedge(payload: DataLineageEdgeCreateSchema):
    """Create new DataLineageEdge instance in enterprise repository."""
    svc = DataLineageEdgeService()
    try:
        item = svc.create_datalineageedge(
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

@router.put("/datalineageedges/{item_id}", response_model=Dict[str, Any])
def update_datalineageedge(item_id: int, payload: DataLineageEdgeUpdateSchema):
    """Update existing DataLineageEdge record fields."""
    svc = DataLineageEdgeService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_datalineageedge(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"DataLineageEdge with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/datalineageedges/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_datalineageedge(item_id: int, hard: bool = Query(False)):
    """Delete DataLineageEdge record (soft-delete by default)."""
    svc = DataLineageEdgeService()
    ok = svc.delete_datalineageedge(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"DataLineageEdge with ID {item_id} not found")
    return None

@router.get("/datalineageedges/analytics/metrics", response_model=Dict[str, Any])
def get_datalineageedge_metrics():
    """Calculate summary statistical KPIs for DataLineageEdge collection."""
    svc = DataLineageEdgeService()
    return svc.calculate_aggregate_metrics()

# ==================== BackfillExecutionJob Endpoints ====================
@router.get("/backfillexecutionjobs", response_model=List[Dict[str, Any]])
def list_backfillexecutionjobs(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List BackfillExecutionJob records with pagination and filtering."""
    svc = BackfillExecutionJobService()
    items = svc.list_backfillexecutionjobs(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/backfillexecutionjobs/{item_id}", response_model=Dict[str, Any])
def get_backfillexecutionjob_by_id(item_id: int):
    """Retrieve detailed record for BackfillExecutionJob by ID."""
    svc = BackfillExecutionJobService()
    item = svc.get_backfillexecutionjob_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"BackfillExecutionJob with ID {item_id} not found")
    return item.to_dict()

@router.post("/backfillexecutionjobs", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_backfillexecutionjob(payload: BackfillExecutionJobCreateSchema):
    """Create new BackfillExecutionJob instance in enterprise repository."""
    svc = BackfillExecutionJobService()
    try:
        item = svc.create_backfillexecutionjob(
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

@router.put("/backfillexecutionjobs/{item_id}", response_model=Dict[str, Any])
def update_backfillexecutionjob(item_id: int, payload: BackfillExecutionJobUpdateSchema):
    """Update existing BackfillExecutionJob record fields."""
    svc = BackfillExecutionJobService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_backfillexecutionjob(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"BackfillExecutionJob with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/backfillexecutionjobs/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_backfillexecutionjob(item_id: int, hard: bool = Query(False)):
    """Delete BackfillExecutionJob record (soft-delete by default)."""
    svc = BackfillExecutionJobService()
    ok = svc.delete_backfillexecutionjob(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"BackfillExecutionJob with ID {item_id} not found")
    return None

@router.get("/backfillexecutionjobs/analytics/metrics", response_model=Dict[str, Any])
def get_backfillexecutionjob_metrics():
    """Calculate summary statistical KPIs for BackfillExecutionJob collection."""
    svc = BackfillExecutionJobService()
    return svc.calculate_aggregate_metrics()

# ==================== PipelineThroughputMetric Endpoints ====================
@router.get("/pipelinethroughputmetrics", response_model=List[Dict[str, Any]])
def list_pipelinethroughputmetrics(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List PipelineThroughputMetric records with pagination and filtering."""
    svc = PipelineThroughputMetricService()
    items = svc.list_pipelinethroughputmetrics(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/pipelinethroughputmetrics/{item_id}", response_model=Dict[str, Any])
def get_pipelinethroughputmetric_by_id(item_id: int):
    """Retrieve detailed record for PipelineThroughputMetric by ID."""
    svc = PipelineThroughputMetricService()
    item = svc.get_pipelinethroughputmetric_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"PipelineThroughputMetric with ID {item_id} not found")
    return item.to_dict()

@router.post("/pipelinethroughputmetrics", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_pipelinethroughputmetric(payload: PipelineThroughputMetricCreateSchema):
    """Create new PipelineThroughputMetric instance in enterprise repository."""
    svc = PipelineThroughputMetricService()
    try:
        item = svc.create_pipelinethroughputmetric(
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

@router.put("/pipelinethroughputmetrics/{item_id}", response_model=Dict[str, Any])
def update_pipelinethroughputmetric(item_id: int, payload: PipelineThroughputMetricUpdateSchema):
    """Update existing PipelineThroughputMetric record fields."""
    svc = PipelineThroughputMetricService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_pipelinethroughputmetric(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"PipelineThroughputMetric with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/pipelinethroughputmetrics/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pipelinethroughputmetric(item_id: int, hard: bool = Query(False)):
    """Delete PipelineThroughputMetric record (soft-delete by default)."""
    svc = PipelineThroughputMetricService()
    ok = svc.delete_pipelinethroughputmetric(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"PipelineThroughputMetric with ID {item_id} not found")
    return None

@router.get("/pipelinethroughputmetrics/analytics/metrics", response_model=Dict[str, Any])
def get_pipelinethroughputmetric_metrics():
    """Calculate summary statistical KPIs for PipelineThroughputMetric collection."""
    svc = PipelineThroughputMetricService()
    return svc.calculate_aggregate_metrics()

# ==================== StreamingTopicOffset Endpoints ====================
@router.get("/streamingtopicoffsets", response_model=List[Dict[str, Any]])
def list_streamingtopicoffsets(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
):
    """List StreamingTopicOffset records with pagination and filtering."""
    svc = StreamingTopicOffsetService()
    items = svc.list_streamingtopicoffsets(status=status, priority=priority, limit=limit, offset=offset)
    return [x.to_dict() for x in items]

@router.get("/streamingtopicoffsets/{item_id}", response_model=Dict[str, Any])
def get_streamingtopicoffset_by_id(item_id: int):
    """Retrieve detailed record for StreamingTopicOffset by ID."""
    svc = StreamingTopicOffsetService()
    item = svc.get_streamingtopicoffset_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"StreamingTopicOffset with ID {item_id} not found")
    return item.to_dict()

@router.post("/streamingtopicoffsets", status_code=status.HTTP_201_CREATED, response_model=Dict[str, Any])
def create_streamingtopicoffset(payload: StreamingTopicOffsetCreateSchema):
    """Create new StreamingTopicOffset instance in enterprise repository."""
    svc = StreamingTopicOffsetService()
    try:
        item = svc.create_streamingtopicoffset(
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

@router.put("/streamingtopicoffsets/{item_id}", response_model=Dict[str, Any])
def update_streamingtopicoffset(item_id: int, payload: StreamingTopicOffsetUpdateSchema):
    """Update existing StreamingTopicOffset record fields."""
    svc = StreamingTopicOffsetService()
    updates = payload.dict(exclude_unset=True)
    updated = svc.update_streamingtopicoffset(item_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail=f"StreamingTopicOffset with ID {item_id} not found")
    return updated.to_dict()

@router.delete("/streamingtopicoffsets/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_streamingtopicoffset(item_id: int, hard: bool = Query(False)):
    """Delete StreamingTopicOffset record (soft-delete by default)."""
    svc = StreamingTopicOffsetService()
    ok = svc.delete_streamingtopicoffset(item_id, hard_delete=hard)
    if not ok:
        raise HTTPException(status_code=404, detail=f"StreamingTopicOffset with ID {item_id} not found")
    return None

@router.get("/streamingtopicoffsets/analytics/metrics", response_model=Dict[str, Any])
def get_streamingtopicoffset_metrics():
    """Calculate summary statistical KPIs for StreamingTopicOffset collection."""
    svc = StreamingTopicOffsetService()
    return svc.calculate_aggregate_metrics()

