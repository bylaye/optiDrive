import models, schemas, crud
from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

models.Base.metadata.create_all(bind=engine)
app = FastAPI(
        debug=True,
        title = "OptiDrive"
        )


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

version = "v1"

@app.post(f"/{version}/engins/add", response_model=schemas.Engin)
def create_engin(engin: schemas.EnginCreate, db: Session = Depends(get_db)):
    db_engin = crud.get_engin_by_immatricule(db, immatricule=engin.immatricule)
    if db_engin:
        raise HTTPException(status_code=400, detail="Immatricule already registered")
    return crud.create_engin(db=db, engin=engin)


@app.put("/"+version+"/engins/{immatricule}", response_model=schemas.Engin)
def update_engin(immatricule:str, engin_update: schemas.EnginUpdate, db: Session = Depends(get_db)):
    updated = crud.update_engin(db=db, immatricule=immatricule, update=engin_update)
    if updated:
        return updated
    else:
        raise HTTPException(status_code=404, detail="Engin not found")


@app.post(f"/{version}/chauffeurs/add", response_model=schemas.Chauffeur)
def create_chauffeur(chauffeur: schemas.ChauffeurCreate, db: Session = Depends(get_db)):
    db_chauffeur = crud.get_chauffeur_by_telephone(db, telephone=chauffeur.telephone)
    if db_chauffeur:
        raise HTTPException(status_code=400, detail=f"Telephone {db_chauffeur.telephone} already registered")
    return crud.create_chauffeur(db=db, chauffeur=chauffeur)


@app.post(f"/{version}/appareils/add", response_model=schemas.Appareil)
def create_appareil(appareil: schemas.AppareilCreate, db: Session = Depends(get_db)):
    db_appareil = crud.get_appareil_by_mac(db, adresse_mac=appareil.adresse_mac)
    if db_appareil:
        raise HTTPException(status_code=400, detail=f"{db_appareil.adresse_mac} already registered")
    return crud.create_appareil(db=db, appareil=appareil)



@app.post(f"/{version}/connecter/add", response_model=schemas.Connecter)
def connecter(conn: schemas.ConnecterCreate, db: Session = Depends(get_db)):
    return crud.connecter(db=db, new_conn=conn)


@app.post(f"/{version}/missions/add", response_model=schemas.Mission)
def create_mission(mission: schemas.MissionCreate, db: Session = Depends(get_db)):
    return crud.create_mission(db=db, mission=mission)


@app.put("/"+version+"/missions/{mission_id}", response_model=schemas.Mission)
def update_mission(mission_id:int, mission_update: schemas.MissionUpdate, db: Session = Depends(get_db)):
    updated = crud.update_mission(db=db, mission_id=mission_id, update=mission_update)
    if updated:
        return updated
    else:
        raise HTTPException(status_code=404, detail="Mission not found")


@app.post(f"/{version}/deplacements/add", response_model=schemas.Deplacement)
def create_deplacement(deplacement: schemas.DeplacementCreate, db: Session = Depends(get_db)):
    return crud.create_deplacement(db, deplacement)


@app.put("/"+version+"/deplacements/{deplacement_id}", response_model=schemas.Deplacement)
def update_deplacement(deplacement_id:int, deplacement_update: schemas.DeplacementUpdate, db: Session = Depends(get_db)):
    updated = crud.update_deplacement(db=db, deplacement_id=deplacement_id, update=deplacement_update)
    if updated:
        return updated
    else:
        raise HTTPException(status_code=404, detail="Deplacement not found")




@app.post(f"/{version}/affectations/add", response_model=List[schemas.Affecter])
def create_affecter(affecter: List[schemas.AffecterCreate], db: Session = Depends(get_db)):
    return crud.create_affectation(db, affecter)


@app.put("/"+version+"/affectations/{affecter_id}", response_model=schemas.Affecter)
def update_affecter(affecter_id:int, affecter_update: schemas.AffecterUpdate, db: Session = Depends(get_db)):
    updated = crud.update_affecter(db=db, affecter_id=affecter_id, update=affecter_update)
    if updated:
        return updated
    else:
        raise HTTPException(status_code=404, detail="Affectation not found")


