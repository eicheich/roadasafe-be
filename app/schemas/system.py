from datetime import datetime
from typing import Any, Optional
from uuid import UUID
from pydantic import BaseModel, Field

# Job Pemrosesan Asinkron
class ProcessingJobCreate(BaseModel):
    report_id: UUID
    status: str = Field(default="Antre", pattern="^(Antre|Diproses|Selesai|Gagal)$")

class ProcessingJobUpdate(BaseModel):
    status: str = Field(..., pattern="^(Antre|Diproses|Selesai|Gagal)$")
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    error_message: Optional[str] = None
    retry_count: Optional[int] = 0

class ProcessingJobResponse(BaseModel):
    id: UUID
    report_id: UUID
    status: str
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    error_message: Optional[str]
    retry_count: int

# Log Audit Admin/Petugas
class AuditLogCreate(BaseModel):
    user_id: Optional[UUID] = None
    action: str = Field(..., max_length=100)
    object: Optional[str] = Field(None, max_length=255)
    details_json: Optional[dict[str, Any]] = None

class AuditLogResponse(AuditLogCreate):
    id: UUID
    timestamp: datetime