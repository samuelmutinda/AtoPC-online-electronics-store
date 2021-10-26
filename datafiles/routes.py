import datetime
from datetime import date
from flask import Flask, render_template, request, session
from sqlalchemy.sql.expression import select
from datafiles import app
from flask import render_template, redirect, url_for, flash, request
from datafiles.models import (Bills, Contract, Contractcustomer, Customer, Debits, Deducted_from, 
                                Device, 
                                Employee, Instantpayment, Laptops, 
                                Package,  Paidby, Delivered_by,Delivered_to,Packaged_as,
                                Payment, Smartphones, Solddevices, 
                                Soldvia, Instantcustomer, Audio)
from datafiles.forms import (addsurface13form, deliveryform, registerform, 
                            loginform, purchaseform, addseform, addxrform, 
                            add11form,add12form,add12miniform,add12proform,
                            add12promaxform,addnote10form,adds20form,adds21form,
                            adds21plusform,adds21ultraform,addnote20form,
                            addnote20ultraform,addpixel4aform,addpixel4form,
                            addpixel5form,adminloginform,adminregisterform,
                            addmacbookairform,addmacbookpro13form,addmacbookpro16form,
                            addsurface13form,addsurface15form,addbladestealthform,addblade15form,
                            addairpodsform,addairpodsproform,addbudsliveform,addbudsplusform,
                            addbeatssoloproform,addgalaxybudsform,addpowerbeatsform,addpixelbudsform)
from datafiles import db
from flask_login import login_user, logout_user
from sqlalchemy.sql import exists
from flask_wtf import FlaskForm

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('index.html')

@app.route('/laptops')
def laptopspage():
    return render_template('laptops.html')

@app.route('/smartphoness')
def smartphonespage():
    return render_template('smartphones.html')

@app.route('/iphones')
def iphonespage():
    return render_template('iphones.html')

@app.route('/iphonexr', methods = ['GET', 'POST'])
def iphonexrpage():
    getcolor = request.form.getlist('xrcolor')
    getstorage = request.form.getlist('xrstorage')
    if request.method == 'POST':
        selecteddevice = Smartphones.query.filter_by(smartphonename = 'iPhone XR', smartphonecolor = getcolor[0], smartphonestorage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            session['phone'] = selecteddevice
            return redirect(url_for('checkout'))
    return render_template('iphonexr.html')

@app.route('/iphonese', methods = ['GET', 'POST'])
def iphonesepage():
    getcolor = request.form.getlist('secolor')
    getstorage = request.form.getlist('sestorage')
    if request.method == 'POST':
        selecteddevice = Smartphones.query.filter_by(smartphonename = 'iPhone SE', smartphonecolor = getcolor[0], smartphonestorage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['phone'] = selecteddevice
            return redirect(url_for('checkout'))
    return render_template('iphonese.html')


@app.route('/iphone12')
def iphone12page():
    return render_template('iphone12.html')

@app.route('/baseiphone12', methods = ['GET', 'POST'])
def baseiphone12page():
    getcolor = request.form.getlist('12phonecolor')
    getstorage = request.form.getlist('12phonestorage')
    if request.method == 'POST':
        selecteddevice = Smartphones.query.filter_by(smartphonename = 'iPhone12', smartphonecolor = getcolor[0], smartphonestorage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            return redirect(url_for('checkout'))
            session['phone'] = selecteddevice
    return render_template('baseiphone12.html')

@app.route('/iphone12promax', methods = ['GET', 'POST'])
def iphone12promaxpage():
    getcolor = request.form.getlist('12promaxcolor')
    getstorage = request.form.getlist('12promaxstorage')
    if request.method == 'POST':
        getcolor = getcolor[0]
        getstorage = getstorage[0]
        selecteddevice = Smartphones.query.filter_by(smartphonename = 'iPhone12 pro max', smartphonecolor = getcolor, smartphonestorage = getstorage).first()
        if selecteddevice == None:
            flash('Configuration out of stock. Try a different one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['phone'] = selecteddevice
            return redirect(url_for('checkout'))
    return render_template('12promax.html')

@app.route('/samsungphones')
def samsungpage():
    return render_template('samsungs.html')

@app.route('/note20')
def note20page():
    return render_template('note20.html')

@app.route('/basenote20', methods = ['GET', 'POST'])
def basenote20page():
    getcolor = request.form.getlist('20notecolor')
    getstorage = request.form.getlist('20notestorage')
    if request.method == 'POST':
        selecteddevice = Smartphones.query.filter_by(smartphonename = 'Galaxy Note 20', smartphonecolor = getcolor[0], smartphonestorage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['phone'] = selecteddevice
            return redirect(url_for('checkout'))
    return render_template('basenote20.html')

@app.route('/note20ultra', methods = ['GET', 'POST'])
def note20ultrapage():
    getcolor = request.form.getlist('20ultracolor')
    getstorage = request.form.getlist('20ultrastorage')
    if request.method == 'POST':
        selecteddevice = Smartphones.query.filter_by(smartphonename = 'Galaxy Note 20 ultra', smartphonecolor = getcolor[0], smartphonestorage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['phone'] = selecteddevice
            return redirect(url_for('checkout'))
    return render_template('note20ultra.html')

@app.route('/s21')
def s21page():
    return render_template('s21.html')

@app.route('/s21ultra', methods = ['GET', 'POST'])
def s21ultrapage():
    getcolor = request.form.getlist('s21ultracolor')
    getstorage = request.form.getlist('s21ultrastorage')
    if request.method == 'POST':
        selecteddevice = Smartphones.query.filter_by(smartphonename = 'Galaxy S21 ultra', smartphonecolor = getcolor[0], smartphonestorage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['phone'] = selecteddevice
            return redirect(url_for('checkout'))
    return render_template('s21ultra.html')

@app.route('/s21plus', methods = ['GET', 'POST'])
def s21pluspage():
    getcolor = request.form.getlist('s21+color')
    getstorage = request.form.getlist('s21+storage')
    if request.method == 'POST':
        selecteddevice = Smartphones.query.filter_by(smartphonename = 'Galaxy S21 plus', smartphonecolor = getcolor[0], smartphonestorage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['phone'] = selecteddevice
            return redirect(url_for('checkout'))
    return render_template('s21plus.html')

@app.route('/bases21', methods = ['GET', 'POST'])
def bases21page():
    getcolor = request.form.getlist('s21color')
    getstorage = request.form.getlist('s21storage')
    if request.method == 'POST':
        selecteddevice = Smartphones.query.filter_by(smartphonename = 'Galaxy S21', smartphonecolor = getcolor[0], smartphonestorage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['phone'] = selecteddevice
            return redirect(url_for('checkout'))
    return render_template('bases21.html')

@app.route('/s20ultra', methods = ['GET', 'POST'])
def s20ultrapage():
    getcolor = request.form.getlist('s20ultracolor')
    getstorage = request.form.getlist('s20ultrastorage')
    if request.method == 'POST':
        selecteddevice = Smartphones.query.filter_by(smartphonename = 'Galaxy S20 ultra', smartphonecolor = getcolor[0], smartphonestorage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['phone'] = selecteddevice
            return redirect(url_for('checkout'))
    return render_template('s20ultra.html')

@app.route('/note10+', methods = ['GET', 'POST'])
def note10pluspage():
    getcolor = request.form.getlist('note10color')
    getstorage = request.form.getlist('note10storage')
    if request.method == 'POST':
        selecteddevice = Smartphones.query.filter_by(smartphonename = 'Galaxy Note 10+', smartphonecolor = getcolor[0], smartphonestorage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['phone'] = selecteddevice
            return redirect(url_for('checkout'))
    return render_template('note10+.html')

@app.route('/pixel')
def pixelpage():
    return render_template('pixel.html')

@app.route('/pixel5', methods=['GET', 'POST'])
def pixel5page():
    getcolor = request.form.getlist('pixel5color')
    getstorage = request.form.getlist('pixel5storage')
    if request.method == 'POST':
        selecteddevice = Smartphones.query.filter_by(smartphonename = 'pixel 5', smartphonecolor = getcolor[0], smartphonestorage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['phone'] = selecteddevice
            return redirect(url_for('checkout'))
    return render_template('pixel5.html')

@app.route('/pixel4a', methods=['GET', 'POST'])
def pixel4apage():
    getcolor = request.form.getlist('pixel4acolor')
    getstorage = request.form.getlist('pixel4astorage')
    if request.method == 'POST':
        selecteddevice = Smartphones.query.filter_by(smartphonename = 'pixel 4a', smartphonecolor = getcolor[0], smartphonestorage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['phone'] = selecteddevice
            return redirect(url_for('checkout'))
    return render_template('pixel4a.html')

@app.route('/pixel4', methods=['GET', 'POST'])
def pixel4page():
    getcolor = request.form.getlist('pixel4color')
    getstorage = request.form.getlist('pixel4storage')
    if request.method == 'POST':
        selecteddevice = Smartphones.query.filter_by(smartphonename = 'pixel 4', smartphonecolor = getcolor[0], smartphonestorage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['phone'] = selecteddevice
            return redirect(url_for('checkout'))
    return render_template('pixel4.html')

@app.route('/iphone11', methods=['GET', 'POST'])
def iphone11page():
    getcolor = request.form.getlist('11phonecolor')
    getstorage = request.form.getlist('11phonestorage')
    if request.method == 'POST':
        selecteddevice = Smartphones.query.filter_by(smartphonename='iPhone11', smartphonecolor = getcolor[0], smartphonestorage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['phone'] = selecteddevice
            return redirect(url_for('checkout'))
    return render_template('iphone11.html')

@app.route('/iphone12mini', methods=['GET', 'POST'])
def iphone12minipage():
    getcolor = request.form.getlist('12phonecolor')
    getstorage = request.form.getlist('12phonestorage')
    if request.method == 'POST':
        selecteddevice = Smartphones.query.filter_by(smartphonename='iPhone12 mini', smartphonecolor = getcolor[0], smartphonestorage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selectedid = int(selecteddevice.deviceid)
            session['phone'] = selectedid
            return redirect(url_for('checkout'))
    return render_template('iphone12mini.html')

@app.route('/iphone12pro', methods = ['GET', 'POST'])
def iphone12propage():
    getcolor = request.form.getlist('12procolor')
    getstorage = request.form.getlist('12prostorage')
    if request.method == 'POST':
        getcolor = getcolor[0]
        getstorage = getstorage[0]
        selecteddevice = Smartphones.query.filter_by(smartphonename = 'iPhone12 pro', smartphonecolor=getcolor, smartphonestorage=getstorage).first()
        if selecteddevice == None:
            flash('Configuration out of stock. Try a different one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['phone'] = selecteddevice
            return redirect(url_for('checkout'))
    return render_template('iphone12pro.html')

@app.route('/macbooks')
def macbookpage():
    return render_template('macbooks.html')

@app.route('/16inchmacbook', methods=['GET', 'POST'])
def macbookpro16():
    getcpu = request.form.getlist('16inchprocessor')
    getram = request.form.getlist('16inchram')
    getgpu = request.form.getlist('16inchgpu')
    getstorage = request.form.getlist('16inchstorage')
    getcolor = request.form.getlist('16inchcolor')
    if request.method == 'POST':
        selecteddevice = Laptops.query.filter_by(laptopname = 'MacBook Pro 16"', processor = getcpu[0], ram = getram[0], gpu = getgpu[0], storage = getstorage[0], laptopcolor = getcolor[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['laptop'] = selecteddevice
            return redirect(url_for('checkoutlaptop'))
    return render_template('16inch.html')

@app.route('/13inchmacbook', methods=['GET', 'POST'])
def macbookpro13():
    getram = request.form.getlist('13inchram')
    getstorage = request.form.getlist('13inchstorage')
    getcolor = request.form.getlist('13inchcolor')
    if request.method == 'POST':
        selecteddevice = Laptops.query.filter_by(laptopname = 'MacBook Pro 13(M1)', laptopcolor = getcolor[0], ram = getram[0], storage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['laptop'] = selecteddevice
            return redirect(url_for('checkoutlaptop'))
    return render_template('macbookpro13.html')

@app.route('/macbookair', methods=['GET', 'POST'])
def macbookairpage():
    getram = request.form.getlist('airram')
    getstorage = request.form.getlist('airstorage')
    getcolor = request.form.getlist('aircolor')
    if request.method == 'POST':
        selecteddevice = Laptops.query.filter_by(laptopname = 'MacBook Air(M1)', laptopcolor = getcolor[0], ram = getram[0], storage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['laptop'] = selecteddevice
            return redirect(url_for('checkoutlaptop'))
    return render_template('macbookair.html')

@app.route('/surface')
def surfacepage():
    return render_template('surface.html')

@app.route('/surface13.5', methods=['GET', 'POST'])
def surface13page():
    getcpu = request.form.getlist('13.5inchprocessor')
    getram = request.form.getlist('13.5inchram')
    getstorage = request.form.getlist('13.5inchstorage')
    getcolor = request.form.getlist('13.5inchcolor')
    if request.method == 'POST':
        selecteddevice = Laptops.query.filter_by(laptopname = 'Surface Laptop 4(13.5")', processor = getcpu[0], laptopcolor = getcolor[0], ram = getram[0], storage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['laptop'] = selecteddevice
            return redirect(url_for('checkoutlaptop'))
    return render_template('surface13.html')

@app.route('/surface15', methods=['GET', 'POST'])
def surface15page():
    getcpu = request.form.getlist('15inchprocessor')
    getram = request.form.getlist('15inchram')
    getstorage = request.form.getlist('15inchstorage')
    getcolor = request.form.getlist('15inchcolor')
    if request.method == 'POST':
        selecteddevice = Laptops.query.filter_by(laptopname = 'Surface Laptop 4(15")', processor = getcpu[0], laptopcolor = getcolor[0], ram = getram[0], storage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['laptop'] = selecteddevice
            return redirect(url_for('checkoutlaptop'))
    return render_template('surface15.html')

@app.route('/razer', methods=['GET', 'POST'])
def razerpage():
    return render_template('razer.html')

@app.route('/bladestealth', methods=['GET', 'POST'])
def bladestealth():
    getram = request.form.getlist('bladeram')
    getstorage = request.form.getlist('bladestorage')
    getcolor = request.form.getlist('bladecolor')
    if request.method == 'POST':
        selecteddevice = Laptops.query.filter_by(laptopname = 'Razer blade stealth', laptopcolor = getcolor[0], ram = getram[0], storage = getstorage[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['laptop'] = selecteddevice
            return redirect(url_for('checkoutlaptop'))
    return render_template('blade13.html')

@app.route('/blade15', methods=['GET', 'POST'])
def blade15():
    getcpu = request.form.getlist('blade15processor')
    getram = request.form.getlist('blade15ram')
    getgpu = request.form.getlist('blade15gpu')
    getstorage = request.form.getlist('blade15storage')
    getcolor = request.form.getlist('blade15color')
    if request.method == 'POST':
        selecteddevice = Laptops.query.filter_by(laptopname = 'Razer blade 15"', processor = getcpu[0], ram = getram[0], gpu = getgpu[0], storage = getstorage[0], laptopcolor = getcolor[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['laptop'] = selecteddevice
            return redirect(url_for('checkoutlaptop'))
    return render_template('blade15.html')

@app.route('/checkoutlaptop', methods=['GET', 'POST'])
def checkoutlaptop():
    selecteddevice = session.get('laptop', None)
    laptoptobuy = Laptops.query.filter_by(deviceid = selecteddevice).first()
    form = purchaseform()
    if form.validate_on_submit():
        attempted_user = Customer.query.filter_by(username=form.username.data).first()
        delivery_company = form.deliverycompany.data
        creditcard = form.creditcard.data
        session['creditcard'] = creditcard
        payment_method = form.paymentmethod.data
        session['payment_method'] = payment_method
        session['selected_company'] = delivery_company
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            session['current_user'] = attempted_user.id
            login_user(attempted_user)
            return redirect(url_for('laptopdeliverypage'))
        else:
            flash('Username and password mismatch')
    return render_template('buylaptop.html', form=form, item=laptoptobuy)

@app.route('/audio')
def audiopage():
    return render_template('audio.html')

@app.route('/airpods')
def airpods():
    return render_template('appleaudio.html')

@app.route('/beats')
def beats():
    return render_template('beats.html')

@app.route('/galaxybuds')
def galaxybuds():
    return render_template('galaxyaudio.html')

@app.route('/pixelbuds')
def pixelbuds():
    return render_template('pixelbuds.html')

@app.route('/budslive', methods=['GET', 'POST'])
def budslive():
    getcolor = request.form.getlist('budslivecolor')
    if request.method == 'POST':
        selecteddevice = Audio.query.filter_by(audioname = 'Galaxy buds live', 
                                                audiocolor = getcolor[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['audio'] = selecteddevice
            return redirect(url_for('checkoutaudio'))
    return render_template('buybudslive.html')

@app.route('/buds+', methods=['GET', 'POST'])
def budsplus():
    getcolor = request.form.getlist('budspluscolor')
    if request.method == 'POST':
        selecteddevice = Audio.query.filter_by(audioname = 'Galaxy buds plus', 
                                                audiocolor = getcolor[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['audio'] = selecteddevice
            return redirect(url_for('checkoutaudio'))
    return render_template('buybudsplus.html')

@app.route('/airpodspro', methods=['GET', 'POST'])
def airpodspro():
    getcolor = 'white'
    if request.method == 'POST':
        selecteddevice = Audio.query.filter_by(audioname = 'Airpods pro', 
                                                audiocolor = getcolor).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['audio'] = selecteddevice
            return redirect(url_for('checkoutaudio'))
    return render_template('airpodspro.html')

@app.route('/buyairpods', methods=['GET', 'POST'])
def buyairpods():
    getcolor = 'white'
    if request.method == 'POST':
        selecteddevice = Audio.query.filter_by(audioname = 'Airpods', 
                                                audiocolor = getcolor).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['audio'] = selecteddevice
            return redirect(url_for('checkoutaudio'))
    return render_template('airpods.html')

@app.route('/buypixelbuds', methods=['GET', 'POST'])
def buypixelbuds():
    getcolor = 'clearly white'
    if request.method == 'POST':
        selecteddevice = Audio.query.filter_by(audioname = 'Pixel buds', 
                                                audiocolor = getcolor).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['audio'] = selecteddevice
            return redirect(url_for('checkoutaudio'))
    return render_template('buypixelbuds.html')

@app.route('/powerbeats', methods=['GET', 'POST'])
def powerbeats():
    getcolor = request.form.getlist('powerbeatscolor')
    if request.method == 'POST':
        selecteddevice = Audio.query.filter_by(audioname = 'Powerbeats pro', 
                                                audiocolor = getcolor[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['audio'] = selecteddevice
            return redirect(url_for('checkoutaudio'))
    return render_template('powerbeats.html')

@app.route('/beatssolopro', methods=['GET', 'POST'])
def beatssolopro():
    getcolor = request.form.getlist('soloprocolor')
    if request.method == 'POST':
        selecteddevice = Audio.query.filter_by(audioname = 'Beats solo pro', 
                                                audiocolor = getcolor[0]).first()
        if selecteddevice is None:
            flash('Your configuration is out of stock. Try another one')
        else:
            selecteddevice = selecteddevice.deviceid
            selecteddevice = str(selecteddevice)
            session['audio'] = selecteddevice
            return redirect(url_for('checkoutaudio'))
    return render_template('solopro.html')

@app.route('/checkoutaudio', methods=['GET', 'POST'])
def checkoutaudio():
    selecteddevice = session.get('audio', None)
    audiotobuy = Audio.query.get(selecteddevice)
    form = purchaseform()
    if form.validate_on_submit():
        attempted_user = Customer.query.filter_by(username=form.username.data).first()
        delivery_company = form.deliverycompany.data
        creditcard = form.creditcard.data
        session['creditcard'] = creditcard
        payment_method = form.paymentmethod.data
        session['payment_method'] = payment_method
        session['selected_company'] = delivery_company
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            session['current_user'] = attempted_user.id
            login_user(attempted_user)
            return redirect(url_for('audiodeliverypage'))
        else:
            flash('Username and password mismatch')
    return render_template('audiocheckout.html', form=form, audio=audiotobuy)


@app.route('/delivery', methods=['GET', 'POST'])
def audiodeliverypage():
    selecteddevice = session.get('audio', None)
    companyname = session.get('selected_company', None)
    user = session.get('current_user', None)
    payment_method = session.get('payment_method', None)
    today = date.today()
    today += datetime.timedelta(days=1)
    tomorrow = today
    today -= datetime.timedelta(days=1)
    nextyear = today.replace(year = today.year + 1)
    audiotobuy = Audio.query.filter_by(deviceid = selecteddevice).first()
    cashprice = int(audiotobuy.cash_price)
    contractprice = int(audiotobuy.contract_price)
    form = deliveryform()
    if form.validate_on_submit():
        package_to_create = Package(county = form.county.data, 
                                    delivery_address=form.deliveryaddress.data, 
                                    postal_address = form.postaladdress.data,
                                    delivery_date = tomorrow, order_date = today)
        db.session.add(package_to_create)
        db.session.commit()

        trackingno = package_to_create.trackingid

        packagedas = Packaged_as(deviceid = selecteddevice, trackingid = trackingno)
        db.session.add(packagedas)
        db.session.commit()

        companyandno = Delivered_by(trackingid = trackingno, companyname = companyname)
        db.session.add(companyandno)
        db.session.commit()

        deliver_to = Delivered_to(trackingid = trackingno, customerid = user)
        db.session.add(deliver_to)
        db.session.commit()

        selectedaudio = Audio.query.filter_by(deviceid=selecteddevice).first()
        sale = Solddevices(deviceid = selecteddevice, devicename = selectedaudio.audioname, 
                            devicecolor = selectedaudio.audiocolor, cash_price = selectedaudio.cash_price, 
                            contract_price = selectedaudio.contract_price
                            )
        db.session.add(sale)
        db.session.commit()

        sdev = Device.query.filter_by(deviceid = selectedaudio.deviceid).first()
        db.session.delete(sdev)
        db.session.commit()

        if payment_method == 'Contract':
            cc = session.get('creditcard', None)
            paymentmade = Payment(paymentamount = contractprice, credit_card = cc)
            db.session.add(paymentmade)
            db.session.commit()

            signedcontract = Contract(contractamount = contractprice, startingdate = today, endingdate = nextyear)
            db.session.add(signedcontract)
            db.session.commit()

            check = Contractcustomer.query.filter_by(id = user).first()
            if check == None:
                contract_customer = Contractcustomer(id = user)
                db.session.add(contract_customer)
                db.session.commit()

                bill = Bills(contractid = signedcontract.contractid, customerid = user)
                db.session.add(bill)
                db.session.commit()

            else:
                bill = Bills(contractid = signedcontract.contractid, customerid = user)
                db.session.add(bill)
                db.session.commit()

            deviceandpayment = Soldvia(deviceid = selecteddevice, paymentid = paymentmade.paymentid)
            db.session.add(deviceandpayment)
            db.session.commit()

            deductedfrom = Deducted_from(paymentid = paymentmade.paymentid, contractid = signedcontract.contractid)
            db.session.add(deductedfrom)
            db.session.commit()

            paid_by = Paidby(paymentid = paymentmade.paymentid, customerid = user)
            db.session.add(paid_by)
            db.session.commit()

        else:
            cc = session.get('creditcard', None)
            paymentmade = Payment(paymentamount = cashprice, credit_card = cc)
            db.session.add(paymentmade)
            db.session.commit()

            transaction = Instantpayment(transactionamount = cashprice, transactiondate = today)
            db.session.add(transaction)
            db.session.commit()
            
            check = Instantcustomer.query.filter_by(id = user).first()
            if check is None:
                instant_c = Instantcustomer(id = user)
                db.session.add(instant_c)
                db.session.commit()

                debit = Debits(customerid = user, transactionid = transaction.transactionid)
                db.session.add(debit)
                db.session.commit()
            else:
                debit = Debits(customerid = user, transactionid = transaction.transactionid)
                db.session.add(debit)
                db.session.commit()

            deviceandpayment = Soldvia(deviceid = selecteddevice, paymentid = paymentmade.paymentid)
            db.session.add(deviceandpayment)
            db.session.commit()

            deductedfrom = Deducted_from(paymentid = paymentmade.paymentid, transactionid = transaction.transactionid)
            db.session.add(deductedfrom)
            db.session.commit()

            paid_by = Paidby(paymentid = paymentmade.paymentid, customerid = user)
            db.session.add(paid_by)
        db.session.commit()
        flash('success. Your tracking id is '+str(trackingno))
        return redirect(url_for('homepage'))
        
        
    elif form.validate_on_submit is False:
        flash('Please fill in all required boxes')
    return render_template('delivery.html', form=form, phoneid=audiotobuy, payment_method = payment_method)

@app.route('/checkoutphone', methods=['GET', 'POST'])
def checkout():
    selecteddevice = session.get('phone', None)
    phonetobuy = Smartphones.query.get(selecteddevice)
    form = purchaseform()
    if form.validate_on_submit():
        attempted_user = Customer.query.filter_by(username=form.username.data).first()
        delivery_company = form.deliverycompany.data
        creditcard = form.creditcard.data
        session['creditcard'] = creditcard
        payment_method = form.paymentmethod.data
        session['payment_method'] = payment_method
        session['selected_company'] = delivery_company
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            session['current_user'] = attempted_user.id
            login_user(attempted_user)
            return redirect(url_for('deliverypage'))
        else:
            flash('Username and password mismatch')
    return render_template('buyphone.html', form=form, phoneid=phonetobuy)

@app.route('/phonedelivery', methods=['GET', 'POST'])
def deliverypage():
    selecteddevice = session.get('phone', None)
    companyname = session.get('selected_company', None)
    user = session.get('current_user', None)
    payment_method = session.get('payment_method', None)
    today = date.today()
    today += datetime.timedelta(days=1)
    tomorrow = today
    today -= datetime.timedelta(days=1)
    nextyear = today.replace(year = today.year + 1)
    phonetobuy = Smartphones.query.filter_by(deviceid = selecteddevice).first()
    cashprice = int(phonetobuy.cash_price)
    contractprice = int(phonetobuy.contract_price)
    form = deliveryform()
    if form.validate_on_submit():
        package_to_create = Package(county = form.county.data, 
                                    delivery_address=form.deliveryaddress.data, 
                                    postal_address = form.postaladdress.data,
                                    delivery_date = tomorrow, order_date = today)
        db.session.add(package_to_create)
        db.session.commit()

        trackingno = package_to_create.trackingid

        packagedas = Packaged_as(deviceid = selecteddevice, trackingid = trackingno)
        db.session.add(packagedas)
        db.session.commit()

        companyandno = Delivered_by(trackingid = trackingno, companyname = companyname)
        db.session.add(companyandno)
        db.session.commit()

        deliver_to = Delivered_to(trackingid = trackingno, customerid = user)
        db.session.add(deliver_to)
        db.session.commit()

        selectedphone = Smartphones.query.filter_by(deviceid=selecteddevice).first()
        sale = Solddevices(deviceid = selecteddevice, devicename = selectedphone.smartphonename, 
                            devicecolor = selectedphone.smartphonecolor, devicestorage = selectedphone.smartphonestorage,
                            screensize = selectedphone.screensize,
                            processor = selectedphone.processor,
                            cash_price = selectedphone.cash_price, contract_price = selectedphone.contract_price
                            )
        db.session.add(sale)
        db.session.commit()

        sdev = Device.query.filter_by(deviceid = selectedphone.deviceid).first()
        db.session.delete(sdev)
        db.session.commit()

        if payment_method == 'Contract':
            cc = session.get('creditcard', None)
            paymentmade = Payment(paymentamount = contractprice, credit_card = cc)
            db.session.add(paymentmade)
            db.session.commit()

            signedcontract = Contract(contractamount = contractprice, startingdate = today, endingdate = nextyear)
            db.session.add(signedcontract)
            db.session.commit()

            check = Contractcustomer.query.filter_by(id = user).first()
            if check == None:
                contract_customer = Contractcustomer(id = user)
                db.session.add(contract_customer)
                db.session.commit()

                bill = Bills(contractid = signedcontract.contractid, customerid = user)
                db.session.add(bill)
                db.session.commit()

            else:
                bill = Bills(contractid = signedcontract.contractid, customerid = user)
                db.session.add(bill)
                db.session.commit()

            deviceandpayment = Soldvia(deviceid = selecteddevice, paymentid = paymentmade.paymentid)
            db.session.add(deviceandpayment)
            db.session.commit()

            deductedfrom = Deducted_from(paymentid = paymentmade.paymentid, contractid = signedcontract.contractid)
            db.session.add(deductedfrom)
            db.session.commit()

            paid_by = Paidby(paymentid = paymentmade.paymentid, customerid = user)
            db.session.add(paid_by)
            db.session.commit()

        else:
            cc = session.get('creditcard', None)
            paymentmade = Payment(paymentamount = cashprice, credit_card = cc)
            db.session.add(paymentmade)
            db.session.commit()

            transaction = Instantpayment(transactionamount = cashprice, transactiondate = today)
            db.session.add(transaction)
            db.session.commit()
            
            check = Instantcustomer.query.filter_by(id = user).first()
            if check is None:
                instant_c = Instantcustomer(id = user)
                db.session.add(instant_c)
                db.session.commit()

                debit = Debits(customerid = user, transactionid = transaction.transactionid)
                db.session.add(debit)
                db.session.commit()
            else:
                debit = Debits(customerid = user, transactionid = transaction.transactionid)
                db.session.add(debit)
                db.session.commit()

            deviceandpayment = Soldvia(deviceid = selecteddevice, paymentid = paymentmade.paymentid)
            db.session.add(deviceandpayment)
            db.session.commit()

            deductedfrom = Deducted_from(paymentid = paymentmade.paymentid, transactionid = transaction.transactionid)
            db.session.add(deductedfrom)
            db.session.commit()

            paid_by = Paidby(paymentid = paymentmade.paymentid, customerid = user)
            db.session.add(paid_by)
        db.session.commit()
        flash('success. Your tracking id is '+str(trackingno))
        return redirect(url_for('dashboard'))
        
    elif form.validate_on_submit is False:
        flash('Please fill in all required boxes')
    return render_template('audiodelivery.html', form=form, audio=phonetobuy, payment_method = payment_method)

@app.route('/laptopdelivery', methods=['GET', 'POST'])
def laptopdeliverypage():
    selecteddevice = session.get('laptop', None)
    companyname = session.get('selected_company', None)
    user = session.get('current_user', None)
    payment_method = session.get('payment_method', None)
    today = date.today()
    today += datetime.timedelta(days=1)
    tomorrow = today
    today -= datetime.timedelta(days=1)
    nextyear = today.replace(year = today.year + 1)
    laptoptobuy = Laptops.query.filter_by(deviceid = selecteddevice).first()
    cashprice = int(laptoptobuy.cash_price)
    contractprice = int(laptoptobuy.contract_price)
    form = deliveryform()
    if form.validate_on_submit():
        package_to_create = Package(county = form.county.data, 
                                    delivery_address=form.deliveryaddress.data, 
                                    postal_address = form.postaladdress.data,
                                    delivery_date = tomorrow, order_date = today)
        db.session.add(package_to_create)
        db.session.commit()

        trackingno = package_to_create.trackingid

        packagedas = Packaged_as(deviceid = selecteddevice, trackingid = trackingno)
        db.session.add(packagedas)
        db.session.commit()

        companyandno = Delivered_by(trackingid = trackingno, companyname = companyname)
        db.session.add(companyandno)
        db.session.commit()

        deliver_to = Delivered_to(trackingid = trackingno, customerid = user)
        db.session.add(deliver_to)
        db.session.commit()

        selectedlaptop = Laptops.query.filter_by(deviceid=selecteddevice).first()
        sale = Solddevices(deviceid = selecteddevice, devicename = selectedlaptop.laptopname, 
                            devicecolor = selectedlaptop.laptopcolor, devicestorage = selectedlaptop.storage,
                            screensize = selectedlaptop.screensize, ram = selectedlaptop.ram,
                            processor = selectedlaptop.processor, gpu = selectedlaptop.gpu,
                            cash_price = selectedlaptop.cash_price, contract_price = selectedlaptop.contract_price
                            )
        db.session.add(sale)
        db.session.commit()

        sdev = Device.query.filter_by(deviceid = selectedlaptop.deviceid).first()
        db.session.delete(sdev)

        if payment_method == 'Contract':
            cc = session.get('creditcard', None)
            paymentmade = Payment(paymentamount = cashprice, credit_card = cc)
            db.session.add(paymentmade)
            db.session.commit()

            signedcontract = Contract(contractamount = contractprice, startingdate = today, endingdate = nextyear)
            db.session.add(signedcontract)
            db.session.commit()

            check = Contractcustomer.query.filter_by(id = user).first()
            if check == None:
                flash('check is none')
                contract_customer = Contractcustomer(id = user)
                db.session.add(contract_customer)
                db.session.commit()

                bill = Bills(contractid = signedcontract.contractid, customerid = user)
                db.session.add(bill)
                db.session.commit()

            else:
                bill = Bills(contractid = signedcontract.contractid, customerid = user)
                db.session.add(bill)
                db.session.commit()

            deviceandpayment = Soldvia(deviceid = selecteddevice, paymentid = paymentmade.paymentid)
            db.session.add(deviceandpayment)
            db.session.commit()

            deductedfrom = Deducted_from(paymentid = paymentmade.paymentid, contractid = signedcontract.contractid)
            db.session.add(deductedfrom)
            db.session.commit()

            paid_by = Paidby(paymentid = paymentmade.paymentid, customerid = user)
            db.session.add(paid_by)
            db.session.commit()

        else:
            cc = session.get('creditcard', None)
            paymentmade = Payment(paymentamount = contractprice, credit_card = cc)
            db.session.add(paymentmade)
            db.session.commit()

            transaction = Instantpayment(transactionamount = cashprice, transactiondate = today)
            db.session.add(transaction)
            db.session.commit()
            
            check = Instantcustomer.query.filter_by(id = user).first()
            if check is None:
                instant_c = Instantcustomer(id = user)
                db.session.add(instant_c)
                db.session.commit()

                debit = Debits(customerid = user, transactionid = transaction.transactionid)
                db.session.add(debit)
                db.session.commit()
            else:
                debit = Debits(customerid = user, transactionid = transaction.transactionid)
                db.session.add(debit)
                db.session.commit()

            deviceandpayment = Soldvia(deviceid = selecteddevice, paymentid = paymentmade.paymentid)
            db.session.add(deviceandpayment)
            db.session.commit()

            deductedfrom = Deducted_from(paymentid = paymentmade.paymentid, transactionid = transaction.transactionid)
            db.session.add(deductedfrom)
            db.session.commit()

            paid_by = Paidby(paymentid = paymentmade.paymentid, customerid = user)
            db.session.add(paid_by)
        db.session.commit()
        flash('success. Your tracking id is '+str(trackingno))
        return redirect(url_for('dashboard'))
        
    elif form.validate_on_submit is False:
        flash('Please fill in all required boxes')
    return render_template('laptopdelivery.html', form=form, laptopid=laptoptobuy, payment_method = payment_method)

@app.route('/signup', methods=['GET', 'POST'])
def signuppage():
    form = registerform()
    if form.validate_on_submit():
        user_to_create = Customer(email=form.email.data, username=form.username.data, password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('loginpage'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Err: {err_msg}', category='danger')
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def loginpage():
    form=loginform()
    if form.validate_on_submit():
        attempted_user = Customer.query.filter_by(username=form.username.data).first()
        attempted_user = attempted_user
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            session['logged_user'] = attempted_user.id
            return redirect(url_for('dashboard'))
        else:
            flash('Username and passord mismatch')
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    user = session.get('logged_user', None)
    ordered = Delivered_to.query.filter_by(customerid = user).all()
    cont = Bills.query.filter_by(customerid = user).all()
    contracts = []
    for c in cont:
        contracts.append(c.contractid)
    contracts2 = []
    for c in contracts:
        contractquery = Contract.query.filter_by(contractid = c).first()
        contracts2.append(contractquery)

    contracts3 = contracts2
    paymentids1 = []
    for c2 in contracts3:
        c2 = c2.contractid
        pid1 = Deducted_from.query.filter_by(contractid = c2).first()
        paymentids1.append(pid1.paymentid)

    soldvias1 = []
    for p1 in paymentids1:
        svia1 = Soldvia.query.filter_by(paymentid = p1).first()
        soldvias1.append(svia1)
    contractdevices = []
    for s in soldvias1:
        did = Solddevices.query.filter_by(deviceid = s.deviceid).first()
        contractdevices.append(did)

    trans = Debits.query.filter_by(customerid = user).all()
    transactions = []
    for t in trans:
        transactions.append(t.transactionid)
    transactions2 = []
    for t in transactions:
        transactionquery = Instantpayment.query.filter_by(transactionid = t).first()
        transactions2.append(transactionquery)
    itemids = []
    devices = []
    transactions3 = transactions2
    paymentids2 = []
    for t2 in transactions3:
        t2 = t2.transactionid
        pid2 = Deducted_from.query.filter_by(transactionid = t2).first()
        paymentids2.append(pid2.paymentid)

    soldvias2 = []
    for p2 in paymentids2:
        svia2 = Soldvia.query.filter_by(paymentid = p2).first()
        soldvias2.append(svia2)
    transactiondevices = []
    for s in soldvias2:
        did = Solddevices.query.filter_by(deviceid = s.deviceid).first()
        transactiondevices.append(did)
    for i in ordered:
        trackingno = i.trackingid
        itemid = Package.query.filter_by(trackingid = trackingno).first()
        itemid2 = Packaged_as.query.filter_by(trackingid = trackingno).first()
        device_id = itemid2.deviceid
        device = Solddevices.query.filter_by(deviceid = device_id).first()
        devices.append(device)
        itemids.append(itemid)
    return render_template('dashboard.html', items = itemids, ordernos = ordered, devices = devices,
                            contracts = contracts2, transactions = transactions2,
                            transactiondevices = transactiondevices, contractdevices = contractdevices)

@app.route('/logout')
def logoutpage():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('homepage'))

@app.route('/admin')
def adminpage():
    sales = Solddevices.query.all()
    packages = []
    for sale in sales:
        s = Packaged_as.query.filter_by(deviceid = sale.deviceid).first()
        s2 = Package.query.filter_by(trackingid = s.trackingid).first()
        packages.append(s2)
    dcustomers = []
    for package in packages:
        p = Delivered_to.query.filter_by(trackingid = package.trackingid).first()
        dcustomer = p.customerid
        dcustomers.append(dcustomer)
    users = []
    for c in dcustomers:
        user = Customer.query.filter_by(id = c).first()
        users.append(user)
    companies = []
    for p in packages:
        dby = Delivered_by.query.filter_by(trackingid = p.trackingid).first()
        companies.append(dby)
    return render_template('admin.html', devices = sales, packages = packages, users = users, companies = companies)

@app.route('/managesmartphones')
def adminsmartphones():
    smartphones = Smartphones.query.all()
    return render_template('managesmartphones.html', smartphones = smartphones)

@app.route('/manageaudio')
def adminaudio():
    audio = Audio.query.all()
    return render_template('manageaudio.html', audio = audio)

@app.route('/addairpods', methods=['GET', 'POST'])
def addairpods():
    form = addairpodsform()
    if form.validate_on_submit():
        name = 'Airpods'
        color = 'white'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            audio = Audio(deviceid = lastid.deviceid, audioname = name, 
                                audiocolor = color, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(audio)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminaudio'))
    return render_template('addairpods.html', form = form)

@app.route('/addairpodspro', methods=['GET', 'POST'])
def addairpodspro():
    form = addairpodsproform()
    if form.validate_on_submit():
        name = 'Airpods pro'
        color = 'white'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            audio = Audio(deviceid = lastid.deviceid, audioname = name, 
                                audiocolor = color, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(audio)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminaudio'))
    return render_template('addairpodspro.html', form = form)

@app.route('/addpixelbuds', methods=['GET', 'POST'])
def addpixelbuds():
    form = addpixelbudsform()
    if form.validate_on_submit():
        name = 'Pixel buds'
        color = 'clearly white'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            audio = Audio(deviceid = lastid.deviceid, audioname = name, 
                                audiocolor = color, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(audio)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminaudio'))
    return render_template('addpixelbuds.html', form = form)

@app.route('/addbudsplus', methods=['GET', 'POST'])
def addbudsplus():
    form = addbudsplusform()
    if form.validate_on_submit():
        name = 'Galaxy buds plus'
        color = form.color.data
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            audio = Audio(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color,cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(audio)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminaudio'))
    return render_template('addbudsplus.html', form = form)

@app.route('/addbudslive', methods=['GET', 'POST'])
def addbudslive():
    form = addbudsliveform()
    if form.validate_on_submit():
        name = 'Galaxy buds live'
        color = form.color.data
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            audio = Audio(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color,cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(audio)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminaudio'))
    return render_template('addbudslive.html', form = form)

@app.route('/addpowerbeats', methods=['GET', 'POST'])
def addpowerbeats():
    form = addpowerbeatsform()
    if form.validate_on_submit():
        name = 'Powerbeats pro'
        color = form.color.data
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            audio = Audio(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color,cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(audio)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminaudio'))
    return render_template('addpowerbeats.html', form = form)

@app.route('/addbeatssolo', methods=['GET', 'POST'])
def addbeatssolo():
    form = addbeatssoloproform()
    if form.validate_on_submit():
        name = 'Beats solo pro'
        color = form.color.data
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            audio = Audio(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color,cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(audio)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminaudio'))
    return render_template('addbeatssolo.html', form = form)

@app.route('/addiPhoneSE', methods=['GET', 'POST'])
def addiphonese():
    form = addseform()
    if form.validate_on_submit():
        name = 'iPhone SE'
        color = form.color.data
        processor = 'apple A13'
        storage = form.storage.data
        screensize = '4.7 inch'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            phone = Smartphones(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color, processor = processor, 
                                smartphonestorage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(phone)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminsmartphones'))
    return render_template('addiphonese.html', form = form)

@app.route('/addiPhoneXr', methods=['GET', 'POST'])
def addiphonexr():
    form = addxrform()
    if form.validate_on_submit():
        name = 'iPhone XR'
        color = form.color.data
        processor = 'apple A12'
        storage = form.storage.data
        screensize = '6.1 inch'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            phone = Smartphones(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color, processor = processor, 
                                smartphonestorage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(phone)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminsmartphones'))
    return render_template('addiphonexr.html', form = form)

@app.route('/addiPhone11', methods=['GET', 'POST'])
def addiphone11():
    form = add11form()
    if form.validate_on_submit():
        name = 'iPhone11'
        color = form.color.data
        processor = 'apple A13'
        storage = form.storage.data
        screensize = '6.1 inch'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            phone = Smartphones(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color, processor = processor, 
                                smartphonestorage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(phone)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminsmartphones'))
    return render_template('addiphone11.html', form = form)

@app.route('/addiPhone12mini', methods=['GET', 'POST'])
def addiphone12mini():
    form = add12miniform()
    if form.validate_on_submit():
        name = 'iPhone12 mini'
        color = form.color.data
        processor = 'apple A14'
        storage = form.storage.data
        screensize = '5.4 inch'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            phone = Smartphones(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color, processor = processor, 
                                smartphonestorage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(phone)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminsmartphones'))
    return render_template('addiphone12mini.html', form = form)

@app.route('/addiPhone12', methods=['GET', 'POST'])
def addiphone12():
    form = add12form()
    if form.validate_on_submit():
        name = 'iPhone12'
        color = form.color.data
        processor = 'apple A14'
        storage = form.storage.data
        screensize = '6.1 inch'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            phone = Smartphones(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color, processor = processor, 
                                smartphonestorage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(phone)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminsmartphones'))
    return render_template('addiphone12.html', form = form)

@app.route('/addiPhone12pro', methods=['GET', 'POST'])
def addiphone12pro():
    form = add12proform()
    if form.validate_on_submit():
        name = 'iPhone12 pro'
        color = form.color.data
        processor = 'apple A14'
        storage = form.storage.data
        screensize = '6.1 inch'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            phone = Smartphones(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color, processor = processor, 
                                smartphonestorage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(phone)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminsmartphones'))
    return render_template('addiphone12pro.html', form = form)

@app.route('/addiPhone12promax', methods=['GET', 'POST'])
def addiphone12promax():
    form = add12promaxform()
    if form.validate_on_submit():
        name = 'iPhone12 pro max'
        color = form.color.data
        processor = 'apple A14'
        storage = form.storage.data
        screensize = '6.7 inch'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            phone = Smartphones(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color, processor = processor, 
                                smartphonestorage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(phone)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminsmartphones'))
    return render_template('addiphone12promax.html', form = form)

@app.route('/addnote10+', methods=['GET', 'POST'])
def addnote10plus():
    form = addnote10form()
    if form.validate_on_submit():
        name = 'Galaxy Note 10+'
        color = form.color.data
        processor = 'snapdragon 855'
        storage = form.storage.data
        screensize = '6.8 inch'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            phone = Smartphones(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color, processor = processor, 
                                smartphonestorage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(phone)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminsmartphones'))
    return render_template('addnote10+.html', form = form)

@app.route('/adds20ultra', methods=['GET', 'POST'])
def adds20ultra():
    form = adds20form()
    if form.validate_on_submit():
        name = 'Galaxy S20 ultra'
        color = form.color.data
        processor = 'snapdragon 865 5G'
        storage = form.storage.data
        screensize = '6.8 inch'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            phone = Smartphones(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color, processor = processor, 
                                smartphonestorage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(phone)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminsmartphones'))
    return render_template('adds20ultra.html', form = form)

@app.route('/adds21', methods=['GET', 'POST'])
def adds21():
    form = adds21form()
    if form.validate_on_submit():
        name = 'Galaxy S21'
        color = form.color.data
        processor = 'snapdragon 888'
        storage = form.storage.data
        screensize = '6.2 inch'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            phone = Smartphones(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color, processor = processor, 
                                smartphonestorage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(phone)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminsmartphones'))
    return render_template('adds21.html', form = form)

@app.route('/adds21+', methods=['GET', 'POST'])
def adds21plus():
    form = adds21plusform()
    if form.validate_on_submit():
        name = 'Galaxy S21 plus'
        color = form.color.data
        processor = 'snapdragon 888'
        storage = form.storage.data
        screensize = '6.7 inch'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            phone = Smartphones(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color, processor = processor, 
                                smartphonestorage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(phone)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminsmartphones'))
    return render_template('adds21+.html', form = form)

@app.route('/adds21ultra', methods=['GET', 'POST'])
def adds21ultra():
    form = adds21ultraform()
    if form.validate_on_submit():
        name = 'Galaxy S21 ultra'
        color = form.color.data
        processor = 'snapdragon 888'
        storage = form.storage.data
        screensize = '6.8 inch'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            phone = Smartphones(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color, processor = processor, 
                                smartphonestorage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(phone)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminsmartphones'))
    return render_template('adds21ultra.html', form = form)

@app.route('/addnote20', methods=['GET', 'POST'])
def addnote20():
    form = addnote20form()
    if form.validate_on_submit():
        name = 'Galaxy Note 20'
        color = form.color.data
        processor = 'snapdragon 865 5G+'
        storage = form.storage.data
        screensize = '6.7 inch'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            phone = Smartphones(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color, processor = processor, 
                                smartphonestorage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(phone)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminsmartphones'))
    return render_template('addnote20.html', form = form)

@app.route('/addnote20ultra', methods=['GET', 'POST'])
def addnote20ultra():
    form = addnote20ultraform()
    if form.validate_on_submit():
        name = 'Galaxy Note 20 ultra'
        color = form.color.data
        processor = 'snapdragon 865 5G+'
        storage = form.storage.data
        screensize = '6.8 inch'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            phone = Smartphones(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color, processor = processor, 
                                smartphonestorage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(phone)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminsmartphones'))
    return render_template('addnote20ultra.html', form = form)

@app.route('/addpixel4', methods=['GET', 'POST'])
def addpixel4():
    form = addpixel4form()
    if form.validate_on_submit():
        name = 'pixel 4'
        color = form.color.data
        processor = 'snapdragon 855'
        storage = form.storage.data
        screensize = '5.4 inch'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            phone = Smartphones(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color, processor = processor, 
                                smartphonestorage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(phone)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminsmartphones'))
    return render_template('addpixel4.html', form = form)

@app.route('/addpixel4a', methods=['GET', 'POST'])
def addpixel4a():
    form = addpixel4aform()
    if form.validate_on_submit():
        name = 'pixel 4a'
        color = form.color.data
        processor = 'snapdragon 765G'
        storage = form.storage.data
        screensize = '6.2 inch'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            phone = Smartphones(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color, processor = processor, 
                                smartphonestorage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(phone)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminsmartphones'))
    return render_template('addpixel4a.html', form = form)

@app.route('/addpixel5', methods=['GET', 'POST'])
def addpixel5():
    form = addpixel5form()
    if form.validate_on_submit():
        name = 'pixel 5'
        color = form.color.data
        processor = 'snapdragon 765G'
        storage = form.storage.data
        screensize = '6.0 inch'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            phone = Smartphones(deviceid = lastid.deviceid, smartphonename = name, 
                                smartphonecolor = color, processor = processor, 
                                smartphonestorage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice)
            db.session.add(phone)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminsmartphones'))
    return render_template('addpixel5.html', form = form)

@app.route('/adminlogin', methods=['GET', 'POST'])
def adminloginpage():
    form=adminloginform()
    if form.validate_on_submit():
        attempted_admin = Employee.query.filter_by(username=form.username.data).first()
        attempted_admin = attempted_admin
        if attempted_admin and attempted_admin.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_admin)
            return redirect(url_for('adminpage'))
        else:
            flash('Username and passord mismatch')
    return render_template('adminlogin.html', form=form)

@app.route('/adminregister', methods=['GET', 'POST'])
def adminregister():
    form = adminregisterform()
    if form.validate_on_submit():
        if form.secretkey.data == 'secret':
            user_to_create = Employee(email=form.email.data, username=form.username.data, password=form.password1.data)
            db.session.add(user_to_create)
            db.session.commit()
            return redirect(url_for('adminloginpage'))
        else:
            flash('Wrong secret key. Please try again')
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Err: {err_msg}', category='danger')
    return render_template('adminregister.html', form=form)

@app.route('/managelaptops')
def adminlaptops():
    laptops = Laptops.query.all()
    return render_template('managelaptops.html', laptops = laptops)

@app.route('/addmacbookair', methods=['GET', 'POST'])
def addmacbookair():
    form = addmacbookairform()
    if form.validate_on_submit():
        name = 'MacBook Air(M1)'
        color = form.color.data
        processor = 'Apple M1(8 Cores)'
        storage = form.storage.data
        screensize = '13 inch'
        gpu = 'Apple M1 graphics'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        ram = form.ram.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            laptop = Laptops(deviceid = lastid.deviceid, laptopname = name, 
                                laptopcolor = color, processor = processor, 
                                storage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice, gpu = gpu, ram=ram)
            db.session.add(laptop)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminlaptops'))
    return render_template('addmacbookair.html', form = form)

@app.route('/addmacbookpro13', methods=['GET', 'POST'])
def addmacbookpro13():
    form = addmacbookpro13form()
    if form.validate_on_submit():
        name = 'MacBook Pro 13"(M1)'
        color = form.color.data
        processor = 'Apple M1(8 Cores)'
        storage = form.storage.data
        screensize = '13 inch'
        gpu = 'Apple M1 graphics'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        ram = form.ram.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            laptop = Laptops(deviceid = lastid.deviceid, laptopname = name, 
                                laptopcolor = color, processor = processor, 
                                storage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice, gpu = gpu, ram=ram)
            db.session.add(laptop)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminlaptops'))
    return render_template('addmacbookpro13.html', form = form)

@app.route('/addmacbookpro16', methods=['GET', 'POST'])
def addmacbookpro16():
    form = addmacbookpro16form()
    if form.validate_on_submit():
        name = 'MacBook Pro 16"'
        color = form.color.data
        processor = form.processor.data
        storage = form.storage.data
        screensize = '16 inch'
        gpu = form.gpu.data
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        ram = form.ram.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            laptop = Laptops(deviceid = lastid.deviceid, laptopname = name, 
                                laptopcolor = color, processor = processor, 
                                storage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice, gpu = gpu, ram=ram)
            db.session.add(laptop)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminlaptops'))
    return render_template('addmacbookpro16.html', form = form)

@app.route('/addsurface13', methods=['GET', 'POST'])
def addsurface13():
    form = addsurface13form()
    if form.validate_on_submit():
        name = 'Surface Laptop 4(13.5")'
        color = form.color.data
        processor = form.processor.data
        storage = form.storage.data
        screensize = '13.5 inch'
        if processor == 'Intel Core i5-1135G7(4cores)' or processor=='Intel Core i7-1185G7(4cores)':
            gpu = 'Iris® Xe  Graphics'
        else:
            gpu = 'Radeon™ Graphics'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        ram = form.ram.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            laptop = Laptops(deviceid = lastid.deviceid, laptopname = name, 
                                laptopcolor = color, processor = processor, 
                                storage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice, gpu = gpu, ram=ram)
            db.session.add(laptop)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminlaptops'))
    return render_template('addsurface13.html', form = form)

@app.route('/addsurface15', methods=['GET', 'POST'])
def addsurface15():
    form = addsurface15form()
    if form.validate_on_submit():
        name = 'Surface Laptop 4(15")'
        color = form.color.data
        processor = form.processor.data
        storage = form.storage.data
        screensize = '13.3 inch'
        if processor == 'Intel Core i7-1185G7(4cores)':
            gpu = 'Iris® Xe  Graphics'
        else:
            gpu = 'Radeon™ Graphics'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        ram = form.ram.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            laptop = Laptops(deviceid = lastid.deviceid, laptopname = name, 
                                laptopcolor = color, processor = processor, 
                                storage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice, gpu = gpu, ram=ram)
            db.session.add(laptop)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminlaptops'))
    return render_template('addsurface15.html', form = form)

@app.route('/addbladestealth', methods=['GET', 'POST'])
def addbladestealth():
    form = addbladestealthform()
    if form.validate_on_submit():
        name = 'Razer blade stealth'
        color = form.color.data
        processor = 'Intel® Core™ i7-1165G7(4cores)'
        storage = form.storage.data
        screensize = '13 inch'
        gpu = 'NVIDIA® GeForce GTX 1650 Ti Max-Q'
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        ram = form.ram.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            laptop = Laptops(deviceid = lastid.deviceid, laptopname = name, 
                                laptopcolor = color, processor = processor, 
                                storage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice, gpu = gpu, ram=ram)
            db.session.add(laptop)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminlaptops'))
    return render_template('addbladestealth.html', form = form)

@app.route('/addblade15', methods=['GET', 'POST'])
def addblade15():
    form = addblade15form()
    if form.validate_on_submit():
        name = 'Razer blade 15"'
        color = form.color.data
        processor = form.processor.data
        storage = form.storage.data
        screensize = '15 inch'
        gpu = form.gpu.data
        cashprice = form.cashprice.data
        contractprice = form.contractprice.data
        ram = form.ram.data
        units = form.units.data
        for i in range(units):
            dev = Device()
            db.session.add(dev)
            db.session.commit()
            lastid = Device.query.filter_by(deviceid = dev.deviceid).first()
            laptop = Laptops(deviceid = lastid.deviceid, laptopname = name, 
                                laptopcolor = color, processor = processor, 
                                storage = storage, screensize = screensize, cash_price = cashprice,
                                contract_price = contractprice, gpu = gpu, ram=ram)
            db.session.add(laptop)
            db.session.commit()
        flash('added')
        return redirect(url_for('adminlaptops'))
    return render_template('addblade15.html', form = form)

if __name__=="__main__":
    app.run(debug=True)