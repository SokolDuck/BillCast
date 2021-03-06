from typing import Any, List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from bill_cast import schemas, crud, models
from bill_cast.api import deps


router = APIRouter()


@router.get("/", response_model=List[schemas.Unit])
def read_units(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    units = crud.unit.get_multi(db, skip=skip, limit=limit, user_id=current_user.id)
    return units


@router.post("/", response_model=schemas.Unit)
def create_unit(
    *,
    db: Session = Depends(deps.get_db),
    unit_create: schemas.UnitCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    """
    Create new unit.
    """
    unit = crud.unit.get_by_name(db, name=unit_create.name)

    if unit:
        raise HTTPException(
            status_code=400,
            detail="The unit with this name already exists in the system.",
        )
    else:
        unit = crud.unit.create(db, obj_in=unit_create, user_id=current_user.id)
    
    return unit
