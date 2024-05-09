from sqlalchemy.orm import Session
import models, schemas
from typing import List

def get_engin_by_immatricule(db: Session, immatricule:str):
    return db.query(models.Engins).filter(models.Engins.immatricule==immatricule).first()


def create_engin(db: Session, engin=schemas.EnginCreate):
    db_engin = models.Engins(
            immatricule = engin.immatricule,
            marque = engin.marque,
            capacite = engin.capacite
        )
    db.add(db_engin)
    db.commit()
    db.refresh(db_engin)
    return db_engin


def update_engin(db:Session, immatricule:str, update:schemas.EnginUpdate):
    db_update = get_engin_by_immatricule(db, immatricule)
    if db_update:
        for k, v in update.dict().items():
            setattr(db_update, k, v)
        db.commit()
        db.refresh(db_update)
        return db_update
    else:
        return None




def get_chauffeur_by_telephone(db: Session, telephone:str):
    return db.query(models.Chauffeurs).filter(models.Chauffeurs.telephone==telephone).first()


def create_chauffeur(db:Session, chauffeur=schemas.ChauffeurCreate):
    db_chauffeur = models.Chauffeurs(**chauffeur.dict())
    db.add(db_chauffeur)
    db.commit()
    return db_chauffeur


def get_appareil_by_mac(db: Session, adresse_mac:str):
    return db.query(models.Appareils).filter(models.Appareils.adresse_mac==adresse_mac).first()


def create_appareil(db:Session, appareil=schemas.AppareilCreate):
    db_appareil = models.Appareils(
            adresse_mac = appareil.adresse_mac
        )
    db.add(db_appareil)
    db.commit()
    db.refresh(db_appareil)
    return db_appareil


def connecter(db:Session, new_conn=schemas.ConnecterCreate):
    conn = models.Connecter(**new_conn.dict())
    db.add(conn)
    db.commit()
    db.refresh(conn)
    return conn


def create_mission(db:Session, mission=schemas.MissionCreate):
    db_mission = models.Missions(**mission.dict())
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission


def update_mission(db:Session, mission_id:int, update:schemas.MissionUpdate):
    db_update = db.query(models.Missions).filter(models.Missions.idMission == mission_id).first()
    if db_update:
        if db_update.statusMission != "FINISH":
            for k, v in update.dict().items():
                setattr(db_update, k, v)
            db.commit()
            db.refresh(db_update)
        return db_update
    else:
        return None


def create_deplacement(db:Session, deplacement=schemas.DeplacementCreate):
    db_deplacement = models.Deplacements(**deplacement.dict())
    db.add(db_deplacement)
    db.commit()
    db.refresh(db_deplacement)
    return db_deplacement


def update_deplacement(db:Session, deplacement_id:int, update:schemas.DeplacementUpdate):
    db_update = db.query(models.Deplacements).filter(models.Deplacements.idDeplacement == deplacement_id).first()
    if db_update:
        if db_update.statusDeplacement != "FINISH":
            for k, v in update.dict().items():
                setattr(db_update, k, v)
            db.commit()
            db.refresh(db_update)
        return db_update
    else:
        return None




def create_affectation(db:Session, affecter:List[schemas.AffecterCreate]):
    db_affectations = []
    for aff in affecter:
        db_aff = models.Affecter(**aff.dict())
        db.add(db_aff)
        db_affectations.append(db_aff)
    db.commit()
    return db_affectations


def update_affecter(db:Session, affecter_id:int, update:schemas.AffecterUpdate):
    db_update = db.query(models.Affecter).filter(models.Affecter.idAffecter == affecter_id).first()
    if db_update:
        if db_update.statusAffectation != "FINISH":
            for k, v in update.dict().items():
                setattr(db_update, k, v)
            db.commit()
            db.refresh(db_update)
        return db_update
    else:
        return None


