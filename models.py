from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

class Patient(db.Model):
  __tablename__ = 'APGAR'

  idx = db.Column(db.Integer, primary_key=True)
  CSEC_DISTRESS = db.Column(db.Integer, nullable=False)
  BABY_WEIGHT = db.Column(db.Integer, nullable=False)
  임신말기정밀_AC = db.Column(db.Integer, nullable=False)
  임신말기정밀_AFI = db.Column(db.Integer, nullable=False)
  Cs_Ix_malpresentation = db.Column(db.Integer, nullable=False)
  임신후기정밀_EBW = db.Column(db.Integer, nullable=False)
  HT_DEL = db.Column(db.Integer, nullable=False)
  SBP = db.Column(db.Integer, nullable=False)
  임신말기정밀_FL = db.Column(db.Integer, nullable=False)
  
