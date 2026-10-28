from datetime import date, datetime
from typing import Any, Optional
from uuid import UUID
from pydantic import BaseModel

# Penanganan Laporan
class HandlingCreate(BaseModel):
    report_id: UUID
    planned_date: Optional[date] = None
    team: Optional[str] = None
    internal_notes: Optional[str] = None

class HandlingUpdate(BaseModel):
    planned_date: Optional[date] = None
    team: Optional[str] = None
    internal_notes: Optional[str] = None
    completed_date: Optional[date] = None
    evidence_photo_path: Optional[str] = None
    actual_size_json: Optional[dict[str, Any]] = None

class HandlingResponse(HandlingCreate):
    completed_date: Optional[date] = None
    evidence_photo_path: Optional[str] = None
    actual_size_json: Optional[dict[str, Any]] = None

# Riwayat Status Laporan
class StatusHistoryCreate(BaseModel):
    report_id: UUID
    by_user_id: Optional[UUID] = None
    from_status: Optional[str] = None
    to_status: str
    reason: Optional[str] = None
    public_notes: Optional[str] = None

class StatusHistoryResponse(StatusHistoryCreate):
    id: UUID
    timestamp: datetime