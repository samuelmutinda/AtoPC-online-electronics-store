from flask_wtf import FlaskForm
from flask import request
from wtforms import StringField, PasswordField, SubmitField, RadioField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from datafiles.models import Customer, Employee, Payment

class registerform(FlaskForm):
    def validate_username(self, username_to_check):
        user = Customer.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists')
    def validate_email(self, email_to_check):
        email = Customer.query.filter_by(username=email_to_check.data).first()
        if email:
            raise ValidationError('Email already exists')

    email = StringField(label='Enter your email', validators=[Email(), DataRequired()])
    username = StringField(label='Create username', validators=[Length(min=2, max=30), DataRequired()])
    password1 = PasswordField(label='Create password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create account')

class adminregisterform(FlaskForm):
    def validate_username(self, username_to_check):
        user = Employee.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists')
    def validate_email(self, email_to_check):
        email = Employee.query.filter_by(username=email_to_check.data).first()
        if email:
            raise ValidationError('Email already exists')

    email = StringField(label='Enter your email', validators=[Email(), DataRequired()])
    username = StringField(label='Create username', validators=[Length(min=2, max=30), DataRequired()])
    secretkey = StringField(label='Enter secret key', validators=[DataRequired()])
    password1 = PasswordField(label='Create password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create account')

class loginform(FlaskForm):
    username = StringField(label='Enter your username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class adminloginform(FlaskForm):
    username = StringField(label='Enter your username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class purchaseform(FlaskForm):
    username = StringField(label='Enter your username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    creditcard = StringField(label='Enter your credit card number', validators=[DataRequired()])
    deliverycompany = RadioField('Delivery company', choices=[('Posta','Posta'),('DHL','DHL'),('G4S','G4S')], validators=[DataRequired()])
    paymentmethod = RadioField('Payment method', choices=[('Contract','Contract'),('Cash','Cash')], validators=[DataRequired()])
    submit = SubmitField(label='Proceed')

class deliveryform(FlaskForm):
    postaladdress = StringField(label='Enter your postal address', validators=[DataRequired()])
    deliveryaddress = StringField(label='Enter your delivery address', validators=[DataRequired()])
    county = StringField(label='Enter your county of residence', validators=[DataRequired()])
    submit = SubmitField(label='Finish')

class addseform(FlaskForm):
    color = RadioField('Color', choices=[('red','PRODUCT(RED)'),('silver','Silver'),('black','Black')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('64gb','64gb'),('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addxrform(FlaskForm):
    color = RadioField('Color', choices=[('red','PRODUCT(RED)'),('white','white'),('black','Black'),
                        ('blue','Blue'),('coral','Coral'),('yellow','Yellow')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('64gb','64gb'),('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class add11form(FlaskForm):
    color = RadioField('Color', choices=[('red','PRODUCT(RED)'),('white','white'),('black','Black'),
                        ('yellow','Yellow'),('green','Green'),('purple','Purple')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('64gb','64gb'),('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class add12form(FlaskForm):
    color = RadioField('Color', choices=[('red','PRODUCT(RED)'),('white','white'),('black','Black'),
                        ('blue','Blue'),('green','Green'),('purple','Purple')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('64gb','64gb'),('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class add12miniform(FlaskForm):
    color = RadioField('Color', choices=[('red','PRODUCT(RED)'),('white','white'),('black','Black'),
                        ('blue','Blue'),('green','Green'),('purple','Purple')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('64gb','64gb'),('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class add12proform(FlaskForm):
    color = RadioField('Color', choices=[('graphite','Graphite'),('silver','Silver'),('gold','Gold'),('pacific blue','Pacific blue')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('64gb','64gb'),('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class add12promaxform(FlaskForm):
    color = RadioField('Color', choices=[('graphite','Graphite'),('silver','Silver'),('gold','Gold'),('pacific blue','Pacific blue')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('64gb','64gb'),('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addnote10form(FlaskForm):
    color = RadioField('Color', choices=[('aura glow','Aura glow'),('aura white','Aura white'),
                                        ('aura blue','Aura blue'),('aura black','Aura black')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class adds20form(FlaskForm):
    color = RadioField('Color', choices=[('cosmic black','Cosmic black'),('cosmic white','Cosmic white')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class adds21form(FlaskForm):
    color = RadioField('Color', choices=[('phantom violet','Phantom violet'),('phantom pink','Phantom pink'),
                                        ('phantom white','Phantom white'),('phantom gray','Phantom gray')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class adds21plusform(FlaskForm):
    color = RadioField('Color', choices=[('phantom violet','Phantom violet'),
                                        ('phantom silver','Phantom silver'),('phantom black','Phantom black')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class adds21ultraform(FlaskForm):
    color = RadioField('Color', choices=[('phantom silver','Phantom silver'),('phantom black','Phantom black')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class adds21ultraform(FlaskForm):
    color = RadioField('Color', choices=[('phantom silver','Phantom silver'),('phantom black','Phantom black')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addnote20form(FlaskForm):
    color = RadioField('Color', choices=[('mystic bronze','Mystic bronze'),
                        ('mystic gray','Mystic gray'),('mystic green','Mystic green')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addnote20ultraform(FlaskForm):
    color = RadioField('Color', choices=[('mystic bronze','Mystic bronze'),
                        ('mystic black','Mystic black'),('mystic white','Mystic white')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addpixel4form(FlaskForm):
    color = RadioField('Color', choices=[('just black','Just black'),('oh so orange','Oh So Orange'),('clearly white','Clearly White')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addpixel4aform(FlaskForm):
    color = RadioField('Color', choices=[('just black','Just black'),('clearly white','Clearly White')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addpixel5form(FlaskForm):
    color = RadioField('Color', choices=[('just black','Just black'),('sorta sage','Sorta sage')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('128gb','128gb'),('256gb','256gb'),('512gb','512gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addmacbookairform(FlaskForm):
    color = RadioField('Color', choices=[('space gray','space gray'),('silver','Silver')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('256gb','256gb'),('512gb','512gb'),('1Tb','1TB'),('2Tb','2TB')], validators=[DataRequired()])
    ram = RadioField('RAM', choices=[('8gb','8gb'),('16gb','16gb'),('32gb','32gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addmacbookpro13form(FlaskForm):
    color = RadioField('Color', choices=[('space gray','space gray'),('silver','Silver')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('256gb','256gb'),('512gb','512gb'),('1Tb','1TB'),('2Tb','2TB')], validators=[DataRequired()])
    ram = RadioField('RAM', choices=[('8gb','8gb'),('16gb','16gb'),('32gb','32gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addmacbookpro16form(FlaskForm):
    color = RadioField('Color', choices=[('space gray','space gray'),('silver','Silver')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('256gb','256gb'),('512gb','512gb'),('1Tb','1TB'),('2Tb','2TB')], validators=[DataRequired()])
    ram = RadioField('RAM', choices=[('16gb','16gb'),('32gb','32gb'),('64gb','64gb')], validators=[DataRequired()])
    processor = RadioField('Processor', choices=[('9th-gen Intel Core i7-9750H(6 Cores)',
                            '2.6GHz 6-core 9th-generation Intel® Core™ i7-9750H'),
                            ('9th-gen Core i9-9880H(8 Cores)',
                            '2.3GHz 8-core 9th-generation Intel® Core™ i9-9880H')], validators=[DataRequired()])
    gpu = RadioField('Graphics Card', choices=[('Intel UHD Graphics 630','Intel UHD Graphics 630'),
                    ('AMD Radeon Pro 5300M','AMD Radeon Pro 5300M with 4GB of GDDR6 memory'),
                    ('AMD Radeon Pro 5500M','AMD Radeon Pro 5500M with 8GB of GDDR6 memory'),
                    ('AMD Radeon Pro 5600M','AMD Radeon Pro 5600M with 8GB of HBM2 memory')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addsurface13form(FlaskForm):
    color = RadioField('Color', choices=[('ice blue','Ice blue'),('sandstone','Sandstone'),
                      ('platinum','Platinum'),('matte black','Matte black')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('256gb','256gb'),('512gb','512gb'),
                        ('1Tb','1TB')], validators=[DataRequired()])
    ram = RadioField('RAM', choices=[('16gb','16gb'),('32gb','32gb')], validators=[DataRequired()])
    processor = RadioField('Processor', choices=[('Intel Core i5-1135G7(4cores)',
                            'Quad Core 11th Gen Intel® Core™ i5-1135G7 (Iris® Xe  Graphics)'),
                            ('Intel Core i7-1185G7(4cores)',
                            'Quad Core 11th Intel® Core™ i7-1185G7 (Iris® Xe  Graphics)'),
                            ('AMD Ryzen 5 4680U(4cores)',
                            'AMD Ryzen™ 5 4680U (Radeon™ Graphics)')],
                             validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addsurface15form(FlaskForm):
    color = RadioField('Color', choices=[('platinum','Platinum'),('matte black','Matte black')], 
                        validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('256gb','256gb'),('512gb','512gb'),
                        ('1Tb','1TB')], validators=[DataRequired()])
    ram = RadioField('RAM', choices=[('16gb','16gb'),('32gb','32gb')], validators=[DataRequired()])
    processor = RadioField('Processor', choices=[('Intel Core i7-1185G7(4cores)',
                            'Quad Core 11th Intel® Core™ i7-1185G7 (Iris® Xe  Graphics)'),
                            ('AMD Ryzen 7 4980U(8cores)',
                            '8 Core AMD Ryzen™ 7 4980U (Radeon™ Graphics)')],
                             validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addbladestealthform(FlaskForm):
    color = RadioField('Color', choices=[('mercury white','Mercury white'),('stealth black','Stealth black')], validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('512gb','512gb'),('1Tb','1TB'),('2Tb','2TB')], validators=[DataRequired()])
    ram = RadioField('RAM', choices=[('16gb','16gb'),('32gb','32gb')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addblade15form(FlaskForm):
    color = RadioField('Color', choices=[('mercury white','Mercury white'),('stealth black','Stealth black')], 
                        validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('512gb','512gb'),
                        ('1Tb','1TB'),('2Tb','2TB')], validators=[DataRequired()])
    ram = RadioField('RAM', choices=[('16gb','16gb'),('32gb','32gb')], validators=[DataRequired()])
    processor = RadioField('Processor', choices=[('Intel Core i7-10750H(6cores)',
                            '2.60 GHz Intel Core i7-10750H(6cores)'),
                            ('Intel Core i7-11800H(8cores)',
                            '2.30 GHz Intel Core i7-11800H(8cores)'),
                            ('Intel Core i9-11900H(8cores)',
                            '2.50 GHz Intel Core i9-11900H(8cores)')],
                             validators=[DataRequired()])
    gpu = RadioField('Graphics Card', choices=[('GeForce RTX 3070','NVIDIA® GeForce RTX™ 3070'),
                    ('GeForce RTX 3080','NVIDIA® GeForce RTX™ 3080'),
                    ('GeForce RTX 3090','NVIDIA® GeForce RTX™ 3090')], validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addairpodsform(FlaskForm):
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addairpodsproform(FlaskForm):
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addpixelbudsform(FlaskForm):
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addbudsliveform(FlaskForm):
    color = RadioField('Color', choices=[('mystic white','Mystic white'),('mystic bronze','Mystic bronze'),
                        ('mystic black','mystic black')], 
                        validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addbudsplusform(FlaskForm):
    color = RadioField('Color', choices=[('white','White'),('blue','Blue'),
                        ('black','Black')], 
                        validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addgalaxybudsform(FlaskForm):
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addpowerbeatsform(FlaskForm):
    color = RadioField('Color', choices=[('ivory','Ivory'),('red','Red'),
                        ('black','Black')], 
                        validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')

class addbeatssoloproform(FlaskForm):
    color = RadioField('Color', choices=[('ivory','Ivory'),('gray','Gray'),
                        ('black','Black')], 
                        validators=[DataRequired()])
    cashprice = IntegerField('Cash price', validators=[DataRequired()])
    contractprice = IntegerField('Cash price', validators=[DataRequired()])
    units = IntegerField('Units', validators=[DataRequired()])
    submit = SubmitField(label='Add')