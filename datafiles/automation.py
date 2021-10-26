from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from sqlalchemy.sql import exists
import math

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI']   = 'sqlite:///appdatabase.db'
app.config['SECRET_KEY'] = 'eea013094d828aeb51a619aa'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)

class Laptops(db.Model):
    deviceid = db.Column(db.Integer(), db.ForeignKey('device.deviceid'), primary_key=True, nullable = False)
    laptopname = db.Column(db.Text(), nullable = False)
    processor = db.Column(db.Text(), nullable = False)
    laptopcolor = db.Column(db.Text(), nullable = False)
    ram = db.Column(db.Text(), nullable = False)
    storage = db.Column(db.Text(), nullable = False)
    gpu = db.Column(db.Text(), nullable = False)
    screensize = db.Column(db.Text(), nullable = False)
    contract_price = db.Column(db.Numeric(), nullable = False)
    cash_price = db.Column(db.Numeric(), nullable = False)

class Smartphones(db.Model):
    deviceid = db.Column(db.Integer(), db.ForeignKey('device.deviceid'), primary_key=True, nullable = False)
    smartphonename = db.Column(db.Text(), nullable = False)
    smartphonecolor = db.Column(db.Text(), nullable = False)
    smartphonestorage = db.Column(db.Text(), nullable = False)
    processor = db.Column(db.Text(), nullable = False)
    screensize = db.Column(db.Text(), nullable = False)
    contract_price = db.Column(db.Numeric(), nullable = False)
    cash_price = db.Column(db.Numeric(), nullable = False)

class Audio(db.Model):
    deviceid = db.Column(db.Integer(), db.ForeignKey('device.deviceid'), primary_key=True, nullable = False)
    audioname = db.Column(db.Text(), nullable = False)
    audiocolor = db.Column(db.Text(), nullable = False)
    contract_price = db.Column(db.Numeric(), nullable = False)
    cash_price = db.Column(db.Numeric(), nullable = False)

class Device(db.Model):
    deviceid = db.Column(db.Integer(), primary_key=True, nullable = False, autoincrement=True)

# storages = ['512gb','1Tb','2Tb',]
# rams = ['32gb','64gb']
# colors = ['mercury white','stealth black']
# name = 'Razer blade 15"'
# processors = ['Intel Core i7-10750H(6cores)','Intel Core i7-11800H(8cores)','Intel Core i9-11900H(8cores)']
# gpus = ['GeForce RTX 3070','GeForce RTX 3080','GeForce RTX 3090']
# size = '15 inch'
# cashprice = 170000
# for color in colors:
#     for storage in storages:
#         cashprice2 = cashprice
#         for ram in rams:
#             cashprice3 = cashprice
#             for processor in processors:
#                 cashprice4 = cashprice
#                 for gpu in gpus:
#                     dev = Device()
#                     db.session.add(dev)
#                     db.session.commit()
#                     contractprice = math.ceil(cashprice/12)
#                     lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
#                     laptop = Laptops(deviceid = lastid.deviceid, laptopname = name, 
#                                             laptopcolor = color, processor = processor, 
#                                             storage = storage, screensize = size, cash_price = cashprice,
#                                             contract_price = contractprice, gpu = gpu, ram=ram)
#                     db.session.add(laptop)
#                     db.session.commit()
#                     cashprice+=40000
#                 cashprice4 += 30000
#                 cashprice = cashprice4
#             cashprice3 += 20000
#             cashprice = cashprice3
#         cashprice2 += 20000
#         cashprice = cashprice2
#     cashprice = 170000

audiocolors = ['ivory','red','black']
cashprice = 10000
for i in range(5):
    for color in audiocolors:
        dev = Device()
        db.session.add(dev)
        db.session.commit()
        contractprice = math.ceil(cashprice/12)
        lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
        audio = Audio(deviceid = lastid.deviceid, audioname = 'Powerbeats pro', audiocolor = color,
                        cash_price = cashprice, contract_price = contractprice)
        db.session.add(audio)
        db.session.commit()