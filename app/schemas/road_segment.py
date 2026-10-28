from typing import Any, Optional
from uuid import UUID
from pydantic import BaseModel, Field

class RoadSegmentBase(BaseModel):
    name: str = Field(..., max_length=255)
    classification: Optional[str] = Field(None, pattern="^(arteri|kolektor|lokal)$")
    authority: Optional[str] = Field(None, pattern="^(nasional|provinsi|kota)$")

class RoadSegmentCreate(RoadSegmentBase):
    # Format GeoJSON geometry (LineString)
    geometry: dict[str, Any]

class RoadSegmentResponse(RoadSegmentBase):
    id: UUID
    geometry: dict[str, Any]