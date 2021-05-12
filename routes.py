import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from carp import app, db, bcrypt
from carp.forms import RegistrationForm, LoginForm, BusinForm, UpdateAccountForm, BookingForm
from carp.models import User, Busin, Booking, Turfs
from flask_login import login_user, current_user, logout_user, login_required
from flask import send_from_directory


@app.route("/")
def index():
    return render_template('index.html', title='home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')
@app.route("/admintable")
def admintable():
    return render_template('tables.html', title='Admin')

@app.route("/profile/<int:turfid>")
def profile(turfid):
    prof = Turfs.query.filter_by(id=turfid).first()
    return render_template('profile.html', title='profile', prof=prof)

@app.route("/turf")
def turf():
    turf = Turfs.query.all()
    return render_template('turfs.html', title='turf', turf=turf)

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')

@app.route("/Bdetails")
def Bdetails():
    booking = Booking.query.filter_by(username=current_user.username).all()
    return render_template('Bdetails.html', title='details', booking=booking)


'''@app.route("/search", method=['POST'])
def search():
    if request.method=='POST':
        search=User.query.all filter()'''

@app.route('/booking/<int:book_id>/delete',  methods=['POST'])
@login_required
def delete_book(book_id):
    book = Booking.query.filter_by(id=book_id).first()
    db.session.delete(book)
    db.session.commit()
    flash('Your Booking has been Canceled', 'success')
    return redirect(url_for('Bdetails'))





#@app.route("/pay")
#def pay():
  #  return render_template('pay.html', title='Pay')


@app.route("/test")
def test():
    return render_template('test.html', title='Test')




@app.route("/business", methods=['GET', 'POST'])
def business():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = BusinForm()
    if form.validate_on_submit():

        user = Busin(companyname=form.companyname.data, email=form.email.data, place=form.place.data, phone=form.phone.data,)
        db.session.add(user)
        db.session.commit()
        flash('Registered successfully, We will contact you as soon as possible  ', 'success')
        return redirect(url_for('business'))
    return render_template('business.html', title='Business', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))




def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn



@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data

        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)





@app.route("/booking/<int:turf_id>", methods=['GET', 'POST'])
@login_required
def booking(turf_id):

    form = BookingForm()
    tu = Turfs.query.filter_by(id=turf_id).first()
    if form.validate_on_submit():
        user = Booking(username=form.username.data, email=form.email.data, date=form.date.data, time=form.time.data,
                    companyname=form.companyname.data, players=form.players.data, category=form.category.data,
                       phone=form.phone.data, location=form.location.data, time1=form.time1.data,)


        db.session.add(user)
        db.session.commit()
        flash('Your turf has been Booked', 'success')
        return redirect(url_for('turf'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.category.data = tu.category
        form.location.data = tu.location
        form.companyname.data = tu.companyname

    return render_template('booking.html', title='Booking', form=form)


@app.route("/search", methods=['POST'])
def search():
     category = request.form['category']
     location = request.form['location']
     search = Turfs.query.filter_by(category=category,location=location).all()
     return render_template('search.html', title='truf', search=search)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)



