from typing import Any, Optional
from uuid import UUID
from pydantic import BaseModel, Field

# Citra Jalan
class RoadImageCreate(BaseModel):
    report_id: UUID
    file_path: str
    phash: Optional[str] = None
    exif_lat: Optional[float] = None
    exif_lng: Optional[float] = None
    quality_score: Optional[float] = None

class RoadImageResponse(RoadImageCreate):
    id: UUID

# Deteksi Kerusakan
class DamageDetectionCreate(BaseModel):
    image_id: UUID
    model_version_id: Optional[UUID] = None
    bbox: dict[str, Any]  # e.g., {"x": 100, "y": 150, "w": 50, "h": 60}
    confidence: float = Field(..., ge=0.0, le=1.0)

class DamageDetectionResponse(DamageDetectionCreate):
    id: UUID

# Segmentasi Kerusakan
class DamageSegmentationCreate(BaseModel):
    detection_id: UUID
    mask_path: str
    pixel_area: Optional[int] = None
    estimated_m2_area: Optional[float] = None
    core_dark_ratio: Optional[float] = None
    lane_position: Optional[str] = None

class DamageSegmentationResponse(DamageSegmentationCreate):
    id: UUID