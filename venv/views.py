from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_user, login_required, current_user
from models import Note, User
from __init__ import db
import json
 

views = Blueprint('views', __name__)



#------------------------------------view/home page------------------------------
@views.route('/', methods=['GET', 'POST'])
@login_required # decorator / flask_login / log in to acess home page
def home ():
    if request.method == 'POST':
        note = request.form.get('note') #from home.py
        if len(note) < 1:
            flash('Note is too short', category ='error')
        else:
            new_note = Note(data=note, user_id=current_user.id ) #from models.py
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category ='success')


    return render_template("home.html", user=current_user)   #nav bar sections access #passes user to template
#------------------------------------view/home page------------------------------


#------------------------------------note delete via json func-------------------
# #------------------------------------looks for a note id sent by  index.js------
@views.route('/delete-note', methods = ['POST'])
def delete_note(): 
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id: 
            db.session.delete(note)
            db.session.commit()
    return jsonify({})






