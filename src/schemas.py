from pydantic import BaseModel
from typing import Union, Literal, Optional, List
from datetime import datetime

# Engins
class EnginCapacite(BaseModel):
    capacite: Union[float, int] = 0


class EnginBase(EnginCapacite):
    immatricule: str
    marque: str = None


class EnginCreate(EnginBase):
    pass


class EnginUpdate(EnginCapacite):
    pass


class Engin(EnginBase):
    idEngin: int
    
    class Config:
        #orm_mode = True
        from_attributes = True


# Chauffeurs
class ChauffeurBase(BaseModel):
    prenom: str
    nom: str
    telephone: str


class ChauffeurCreate(ChauffeurBase):
    pass


class Chauffeur(ChauffeurBase):
    idChauffeur: int

    class Config:
        #orm_mode = True
        from_attributes = True


#Appareils
class AppareilBase(BaseModel):
    adresse_mac: str


class AppareilCreate(AppareilBase):
    pass


class Appareil(AppareilBase):
    idAppareil: int
    
    class Config:
        from_attributes = True


# Connecter
class ConnecterBase(BaseModel):
    idAppareil: int
    idEngin: int
    idChauffeur: int


class ConnecterCreate(ConnecterBase):
    dateheure: datetime = datetime.now()


class Connecter(ConnecterBase):
    idConnecter: int
    
    class Config:
        from_attributes = True


# Missions
class MissionStatus(BaseModel):
    statusMission: Literal["RUN", "FINISH", "CANCEL"] = "RUN"


class MissionFin(MissionStatus):
    finMission: Optional[datetime] = None


class MissionBase(MissionStatus):
    entite: str = None
    typeMission: Literal["Trans", "Dep", "Loc"] = "Trans"
    description: str = None
    debutMission: datetime = datetime.now()
    quantite: float = 0


class MissionCreate(MissionBase):
    pass


class MissionUpdate(MissionFin):
    pass


class Mission(MissionBase, MissionFin):
    idMission: int
    
    class Config:
        from_attributes = True
        exclude = ("statusMission")


# Deplacements
class DeplacementStatus(BaseModel):
    statusDeplacement: Literal["RUN","CANCEL", "FINISH"] = "RUN"
    quantiteCharge: float = 0


class DeplacementArrivee(DeplacementStatus):
    arrivee: Optional[datetime] = None


class DeplacementBase(DeplacementStatus):
    idMission: int
    idAppareil: int
    depart: datetime = datetime.now()
    typeCharge: str


class DeplacementCreate(DeplacementBase):
    pass


class DeplacementUpdate(DeplacementArrivee):
    pass


class Deplacement(DeplacementBase):
    idDeplacement: int
    
    class Config:
        from_attributes = True



# Affecter
class AffecterStatus(BaseModel):
    statusAffectation: Literal["RUN", "FINISH", "CANCEL"] = "RUN"
    

class AffecterFin(AffecterStatus):
    finAffectation: Optional[datetime] = None


class AffecterBase(AffecterStatus):
    debutAffectation: datetime = datetime.now()


class AffecterCreate(AffecterBase):
    idMission: int
    idEngin: int


class AffecterUpdate(AffecterFin):
    pass


class Affecter(AffecterBase):
    idAffecter: int
    idEngin: int
    idMission: int
    
    class Config:
        from_attributes = True


