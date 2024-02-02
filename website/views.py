from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user 
from .models import Note
from . import db
import json


views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get('data')

        if len(note) < 1:
            flash("Note is too short.", category = 'error')
        else:
            new_note = Note(data = note, userID = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note successfully added!", category = "success")        

    return render_template("home.html", user = current_user)

@views.route("/delete-note", methods = ['POST'])
def delete_node():
    note = json.loads(request.data)
    noteID = note['noteID']
    note = Note.query.get(noteID)
    if note:
        if note.userID ==  current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
