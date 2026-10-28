from datetime import datetime
from typing import Any, Optional
from uuid import UUID
from pydantic import BaseModel, Field

# Konfigurasi Skoring
class ScoringConfigCreate(BaseModel):
    version: str = Field(..., max_length=50)
    weights_json: dict[str, Any]
    threshold_json: dict[str, Any]
    traffic_mapping_json: dict[str, Any]
    confidence_threshold: float = Field(..., ge=0.0, le=1.0)
    area_parameters_json: dict[str, Any]
    is_active: bool = False

class ScoringConfigResponse(ScoringConfigCreate):
    id: UUID
    created_by: Optional[UUID] = None
    created_at: datetime

# Priority Label
class PriorityLabelCreate(BaseModel):
    segmentation_id: UUID
    config_id: Optional[UUID] = None
    area_score: Optional[float] = None
    depth_score: Optional[float] = None
    position_score: Optional[float] = None
    traffic_score: Optional[float] = None
    total_score: Optional[float] = None
    machine_category: Optional[str] = Field(None, pattern="^(Tinggi|Sedang|Rendah)$")

class PriorityLabelResponse(PriorityLabelCreate):
    id: UUID