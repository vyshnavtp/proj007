from carp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"



class Busin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    companyname = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    place = db.Column(db.String(20),  nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"Busin('{self.companyname}', '{self.email}', '{self.phone}', '{self.place}')"



class Turfs(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    companyname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120),  nullable=False)
    location = db.Column(db.String(20),  nullable=False)
    category = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    photo = db.Column(db.String(20), nullable=False, default='default.jpg')
    photo1 = db.Column(db.String(20),  default='default.jpg')
    photo2 = db.Column(db.String(20), default='default.jpg')
    photo3 = db.Column(db.String(20), default='default.jpg')
    address  = db.Column(db.Text(2000), nullable=False)
    price = db.Column(db.Text(20), nullable=False)


    def __repr__(self):
        return f"Turfs('{self.companyname}', '{self.email}', '{self.uid}','{self.phone}', '{self.location}',  '{self.category}'," \
               f" '{self.photo}', '{self.photo1}', '{self.photo2}', '{self.photo3}')"


'''class FileView(sqla.ModelView):
    form_overrides = {
        'photo': form.FileUploadField,
        'photo1': form.FileUploadField,
        'photo2': form.FileUploadField,
        'photo3': form.FileUploadField,
    }
    form_args = {
        'photo': {
            'label': "Photo",
            'base_path': file_path,
            'allow_overwrite': False,
        },

        'photo1': {
            'label': "Photo1",
            'base_path': file_path,
            'allow_overwrite': False,
        },

        'photo2': {
            'label': "Photo2",
            'base_path': file_path,
            'allow_overwrite': False,
        },

        'photo3': {
            'label': "Photo3",
            'base_path': file_path,
            'allow_overwrite': False,
        }
        }'''





class Booking(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    date = db.Column(db.Date())
    time = db.Column(db.Time())
    time1 = db.Column(db.Time())
    #date = db.Column(db.String(120), nullable=False)
    #time = db.Column(db.String(120), nullable=False)
    #time1 = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    companyname = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(20),  nullable=False)
    category = db.Column(db.String(20), nullable=False)
    players = db.Column(db.String())
    def __repr__(self):
        return f" Booking('{self.companyname}', '{self.email}', '{self.phone}', '{self.location}','{self.category}', " \
               f"'{self.time}', '{self.date}', '{self.players}', '{self.username}')"



