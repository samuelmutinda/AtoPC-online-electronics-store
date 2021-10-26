import sqlalchemy
from datafiles import db, login_manager
from datafiles import bcrypt
from flask_login import UserMixin
from sqlalchemy.sql import exists
from sqlalchemy.ext.automap import automap_base

@login_manager.user_loader
def load_user(user_id):
    try:
        return Customer.query.get(int(user_id))
    except:
        return Employee.query.get(int(user_id))

class Customer(db.Model, UserMixin):
    id=db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username=db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

class Employee(db.Model, UserMixin):
    id=db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username=db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

Base = automap_base()
Base.prepare(db.engine, reflect = True)
Manufacturer = Base.classes.manufacturer

class Payment(db.Model):
    paymentid = db.Column(db.Integer(), primary_key=True, nullable = False, autoincrement=True)
    paymentamount = db.Column(db.Numeric(), nullable = False)
    credit_card = db.Column(db.Text(), nullable = False)

class Soldvia(db.Model):
    deviceid = db.Column(db.Integer(), db.ForeignKey('device.deviceid'), primary_key=True, nullable = False)
    paymentid = db.Column(db.Integer(), db.ForeignKey('payment.paymentid'), primary_key=True, nullable = False)

class Paidby(db.Model):
    paymentid = db.Column(db.Integer(), db.ForeignKey('payment.paymentid'), primary_key=True, nullable = False)
    customerid = db.Column(db.Integer(), db.ForeignKey('customer.id'), primary_key=True, nullable = False)

class Contract(db.Model):
    contractid = db.Column(db.Integer(), primary_key=True, nullable = False, autoincrement=True)
    contractamount = db.Column(db.Integer(), nullable = False)
    startingdate = db.Column(db.Date(), nullable = False)
    endingdate = db.Column(db.Date(), nullable = False)

class Instantpayment(db.Model):
    transactionid = db.Column(db.Integer(), primary_key=True, nullable = False, autoincrement=True)
    transactionamount = db.Column(db.Integer(), nullable = False)
    transactiondate = db.Column(db.Date(), nullable = False)

class Deducted_from(db.Model):
    paymentid = db.Column(db.Integer(), db.ForeignKey('payment.paymentid'), primary_key=True, nullable = False)
    contractid = db.Column(db.Integer(), db.ForeignKey('contract.contractid'), primary_key=True, nullable = True)
    transactionid = db.Column(db.Integer(), db.ForeignKey('instantpayment.transactionid'), primary_key=True, nullable = True)

class Contractcustomer(db.Model):
    id=db.Column(db.Integer(), db.ForeignKey('customer.id'), primary_key=True)

class Instantcustomer(db.Model):
    id=db.Column(db.Integer(), db.ForeignKey('customer.id'), primary_key=True)

class Bills(db.Model):
    customerid = db.Column(db.Integer(), db.ForeignKey('contractcustomer.id'), primary_key=True, nullable = False)
    contractid = db.Column(db.Integer(), db.ForeignKey('contract.contractid'), primary_key=True, nullable = False)

class Debits(db.Model):
    customerid = db.Column(db.Integer(), db.ForeignKey('instantcustomer.id'), primary_key=True, nullable = False)
    transactionid = db.Column(db.Integer(), db.ForeignKey('instantpayment.transactionid'), primary_key=True, nullable = False)

class Smartphones(db.Model):
    deviceid = db.Column(db.Integer(), db.ForeignKey('device.deviceid'), primary_key=True, nullable = False)
    smartphonename = db.Column(db.Text(), nullable = False)
    smartphonecolor = db.Column(db.Text(), nullable = False)
    smartphonestorage = db.Column(db.Text(), nullable = False)
    processor = db.Column(db.Text(), nullable = False)
    screensize = db.Column(db.Text(), nullable = False)
    contract_price = db.Column(db.Numeric(), nullable = False)
    cash_price = db.Column(db.Numeric(), nullable = False)

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

class Audio(db.Model):
    deviceid = db.Column(db.Integer(), db.ForeignKey('device.deviceid'), primary_key=True, nullable = False)
    audioname = db.Column(db.Text(), nullable = False)
    audiocolor = db.Column(db.Text(), nullable = False)
    contract_price = db.Column(db.Numeric(), nullable = False)
    cash_price = db.Column(db.Numeric(), nullable = False)

class Device(db.Model):
    deviceid = db.Column(db.Integer(), primary_key=True, nullable = False, autoincrement=True)

class Package(db.Model):
    trackingid = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    county = db.Column(db.Text(), nullable = False)
    delivery_address = db.Column(db.Text(), nullable = True)
    postal_address = db.Column(db.Text(), nullable = True)
    delivery_date = db.Column(db.Date(), nullable = False)
    order_date = db.Column(db.Date(), nullable = False)

class Packaged_as(db.Model):
    deviceid = db.Column(db.Integer(), db.ForeignKey('device.deviceid'), primary_key=True, nullable = False)
    trackingid = db.Column(db.Integer(), db.ForeignKey('package.trackingid'), primary_key=True, nullable = False)

class Delivery_company(db.Model):
    companyname = db.Column(db.Text(), primary_key=True, nullable = False)

class Delivered_by(db.Model):
    trackingid = db.Column(db.Integer(), db.ForeignKey('device.deviceid'), primary_key=True, nullable = False)
    companyname = db.Column(db.Text(), db.ForeignKey('delivery_company.companyname'), primary_key=True, nullable = False)

class Delivered_to(db.Model):
    customerid = db.Column(db.Integer(), db.ForeignKey('customer.id'), primary_key=True, nullable = False)
    trackingid = db.Column(db.Integer(), db.ForeignKey('device.deviceid'), primary_key=True, nullable = False)

class Solddevices(db.Model):
    saleid = db.Column(db.Integer(), primary_key=True, nullable = False, autoincrement = True)
    deviceid = db.Column(db.Integer(), nullable = False)
    devicename = db.Column(db.Text(), nullable = False)
    devicecolor = db.Column(db.Text(), nullable = False)
    devicestorage = db.Column(db.Text(), nullable = True)
    screensize = db.Column(db.Text(), nullable = True)
    ram = db.Column(db.Text(), nullable = True)
    processor = db.Column(db.Text(), nullable = True)
    gpu = db.Column(db.Text(), nullable = True)
    cash_price = db.Column(db.Numeric(), nullable = False)
    contract_price = db.Column(db.Numeric(), nullable = False)

# class Contractcustomer(db.Model):
#     id=db.Column(db.Integer(), db.ForeignKey('customer.id'), primary_key=True)
#     subscribedcontract=db.Column(db.Integer(), db.ForeignKey('contract.id'))
# class Instantcustomer(db.Model):
#     id=db.Column(db.Integer(), db.ForeignKey('customer.id'), primary_key=True)
#     madepayment=db.Column(db.Integer(), db.ForeignKey('instantpayment.id'))

    # def __repr__(self):
    #     return f'Item {self.mname}'