#File To Actually Create The Database 
from app import db, User, Pixel

db.create_all()
try:
  Pixel.__table__.create(db.session.bind)
  User.__table__.create(db.session.bind)
  
except Exception:
  print("Already Exist")
  

