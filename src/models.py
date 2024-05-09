from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base


class Engins(Base):
    __tablename__ = 'Engins'
    idEngin = Column(Integer, primary_key=True)
    immatricule = Column(String(10), unique=True, index=True)
    marque = Column(String(20), index=True)
    capacite = Column(Float)
    connecter = relationship("Connecter", back_populates="engin")
    affecterEngin = relationship("Affecter", back_populates="engin")


class Chauffeurs(Base):
    __tablename__ = 'Chauffeurs'
    idChauffeur = Column(Integer, primary_key=True)
    telephone = Column(String(10), unique=True, index=True)
    prenom = Column(String(20))
    nom = Column(String(20))
    connecter1 = relationship("Connecter", back_populates="chauffeur")


class Appareils(Base):
    __tablename__ = 'Appareils'
    idAppareil = Column(Integer, primary_key=True)
    adresse_mac = Column(String(20), unique=True, index=True)
    connecter2 = relationship("Connecter", back_populates="appareil")
    location = relationship("Localisations", back_populates="appareil")
    deplacement = relationship("Deplacements", back_populates="appareil")


class Connecter(Base):
    __tablename__ = 'Connecter'
    idConnecter = Column(Integer, primary_key=True)
    idAppareil = Column(Integer, ForeignKey('Appareils.idAppareil'))
    idEngin = Column(Integer, ForeignKey('Engins.idEngin'))
    idChauffeur = Column(Integer, ForeignKey('Chauffeurs.idChauffeur'))
    dateheure = Column(DateTime)
    engin = relationship("Engins", back_populates="connecter")
    chauffeur = relationship("Chauffeurs", back_populates="connecter1")
    appareil = relationship("Appareils", back_populates="connecter2")


class Deplacements(Base):
    __tablename__ = 'Deplacements'
    idDeplacement = Column(Integer, primary_key=True)
    depart = Column(DateTime, index=True )
    arrivee = Column(DateTime)
    typeCharge = Column(String(25), index=True )
    quantiteCharge = Column(Float)
    statusDeplacement = Column(String(20))
    idAppareil = Column(Integer, ForeignKey('Appareils.idAppareil'))
    appareil = relationship("Appareils", back_populates="deplacement")
    idMission = Column(Integer, ForeignKey('Missions.idMission'))
    mission = relationship("Missions", back_populates="deplacement")


class Missions(Base):
    __tablename__ = 'Missions'
    idMission = Column(Integer, primary_key=True)
    entite = Column(String(30), index=True)
    typeMission = Column(String(30), index=True)
    description = Column(String(255))
    debutMission = Column(DateTime)
    finMission = Column(DateTime)
    quantite = Column(Float)
    statusMission = Column(String(20))
    deplacement = relationship("Deplacements", back_populates="mission")
    affecterMission = relationship("Affecter", back_populates="mission")


class Affecter(Base):
    __tablename__ ='Affecter'
    idAffecter = Column(Integer, primary_key=True)
    idEngin = Column(Integer, ForeignKey('Engins.idEngin'))
    idMission = Column(Integer, ForeignKey('Missions.idMission'))
    engin = relationship("Engins", back_populates="affecterEngin")
    mission = relationship("Missions", back_populates="affecterMission")
    debutAffectation = Column(DateTime)
    finAffectation = Column(DateTime)
    statusAffectation = Column(String(20))


class Localisations(Base):
    __tablename__ = 'Localisations'
    idLocalisation = Column(Integer, primary_key=True)
    longitude = Column(String(50), index=True )
    lattitude = Column(String(50), index=True )
    idAppareil = Column(Integer, ForeignKey('Appareils.idAppareil'))
    appareil = relationship("Appareils", back_populates="location")
