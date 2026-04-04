from __future__ import annotations

from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.ayurveda_models import WellnessCenters
from ..schemas.wellness import WellnessResponse
from ..services.wellness_service import get_centre, list_centres

router = APIRouter(prefix="/wellness", tags=["wellness"])


@router.get("", response_model=List[WellnessResponse])
def get_all_centres(
    center_type: Optional[str] = Query(None, description="Filter: yoga or wellness"),
    db: Session = Depends(get_db),
) -> List[WellnessCenters]:
    return list_centres(db, center_type)


@router.get("/{center_id}", response_model=WellnessResponse)
def get_centre_by_id(center_id: int, db: Session = Depends(get_db)) -> WellnessCenters:
    centre = get_centre(db, center_id)
    if not centre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Centre not found.")
    return centre
