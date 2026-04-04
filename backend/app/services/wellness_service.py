from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Session

from ..models.ayurveda_models import WellnessCenters


def list_centres(db: Session, center_type: Optional[str] = None) -> List[WellnessCenters]:
    q = db.query(WellnessCenters)
    if center_type:
        q = q.filter(WellnessCenters.center_type == center_type)
    return q.all()


def get_centre(db: Session, center_id: int) -> Optional[WellnessCenters]:
    return db.query(WellnessCenters).filter(WellnessCenters.center_id == center_id).first()


def create_centre(db: Session, **kwargs) -> WellnessCenters:
    centre = WellnessCenters(**kwargs)
    db.add(centre)
    db.commit()
    db.refresh(centre)
    return centre
