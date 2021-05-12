import os
import os.path as op
from flask_admin import Admin
from carp import app, db
from flask import render_template, url_for, request, redirect, session, flash, redirect, Blueprint, abort
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin import form
from flask_admin.contrib import sqla
from carp.models import User, Busin, Booking, Turfs
from carp import file_path
from flask_admin.menu import MenuLink
from jinja2 import Markup

admin = Admin(app) 

class SecureModelView(ModelView):
    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            abort(403)





@app.route("/adminlogout")
def adminlogout():
    session.clear()
    return redirect("/adlogin")

@app.route("/adlogin", methods=['GET', 'POST'])
def adlogin():
    if request.method == "POST":
        if request.form.get("username") == "admin" and request.form.get("password") == "password":
            session['logged_in'] = True
            return redirect("/admin")
        else:
            return render_template("adlogin.html", failed=True)
    return render_template("adlogin.html")


class FileView(sqla.ModelView):
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
        }
class UserView(ModelView):
    column_exclude_list = ['password']

    def _list_thumbnail(view, context, model, name):
        if not model.image_file:
            return ''

        return Markup(
            '<img src="%s" style="height:50px; width:50px;">' %
            url_for('static',
                    filename='profile/' + model.image_file)
        )

    column_formatters = {
        'image_file': _list_thumbnail
    }

    form_extra_fields = {
        'image_file': form.ImageUploadField('Image', base_path=file_path, thumbnail_size=(100, 100, True))
    }


class FileView(ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.photo:
            return ''

        return Markup(
            '<img src="%s" style="height:50px; width:50px;">' %
            url_for('static',
                    filename='turfphotos/' + model.photo)
        )

    def _list_thumbnail2(view, context, model, name):
        if not model.photo1:
            return ''

        return Markup(
            '<img src="%s" style="height:50px; width:50px;">' %
            url_for('static',
                    filename='turfphotos/' + model.photo1)
        )

    def _list_thumbnail3(view, context, model, name):
        if not model.photo2:
            return ''

        return Markup(
            '<img src="%s" style="height:50px; width:50px;">' %
            url_for('static',
                    filename='turfphotos/' + model.photo2)
        )

    def _list_thumbnail4(view, context, model, name):
        if not model.photo3:
            return ''

        return Markup(
            '<img src="%s" style="height:50px; width:50px;">' %
            url_for('static',
                    filename='turfphotos/' + model.photo3)
        )

    column_formatters = {
        'photo': _list_thumbnail,
        'photo1': _list_thumbnail2,
        'photo2': _list_thumbnail3,
        'photo3': _list_thumbnail4,
    }

    form_extra_fields = {
        'photo': form.ImageUploadField('photo ', base_path=file_path, thumbnail_size=(100, 100, True)),
        'photo1': form.ImageUploadField('photo 1', base_path=file_path, thumbnail_size=(100, 100, True)),
        'photo2': form.ImageUploadField('photo 2', base_path=file_path, thumbnail_size=(100, 100, True)),
        'photo3': form.ImageUploadField('photo 3', base_path=file_path, thumbnail_size=(100, 100, True))

    }


admin.add_view(UserView(User, db.session ))
admin.add_view(ModelView(Busin, db.session ))
admin.add_view(ModelView(Booking, db.session ))
admin.add_view(FileView(Turfs, db.session ))

logout_link = MenuLink ('Logout','/adminlogout','adminlogout')
admin.add_link(logout_link)





