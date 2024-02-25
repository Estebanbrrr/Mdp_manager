from flask import Blueprint
from flask import Flask, request, render_template, redirect, abort, flash, session
from datetime import datetime
from connexion_db import get_db


client_manager = Blueprint('client_manager', __name__,
                        template_folder='templates')

@client_manager.route('/client/manage/show')
def client_casque_show():
    mycursor = get_db().cursor()
    id_client = session.get('id_user')

    print(" [show] id client : " + str(id_client))

    sql = "SELECT * FROM mots_de_passe WHERE id_utilisateur = %s;"

    mycursor.execute(sql, (id_client,))
    mot_de_passe = mycursor.fetchall()


    return render_template('client/manage.html',
                           mot_de_passe = mot_de_passe)



@client_manager.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    mycursor = get_db().cursor()
    id_client = session.get('id_user')

    nom = request.form.get('nom', '')
    motdepasse = request.form.get('motdepasse', '')

    print(" [add] id client : " + str(id_client))

    sql = "INSERT INTO mots_de_passe (nom_site, mot_de_passe, date_ajout, id_utilisateur) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql, (nom, motdepasse, datetime.now(), id_client))
    get_db().commit()

    message = u'casque ajouté , nom:' + nom
    flash(message, 'alert-success')

    return redirect('/client/manage/show')


@client_manager.route('/client/manage/supprimer', methods=['GET'])
def supprimer():
    mycursor = get_db().cursor()

    id_client = session.get('id_user')
    id_mot_de_passe = request.args.get('id_mot_de_passe')


    sql = "DELETE FROM mots_de_passe WHERE id_mot_de_passe = %s AND id_utilisateur = %s"
    mycursor.execute(sql, (id_mot_de_passe, id_client))
    get_db().commit()

    flash('Le mot de passe a été supprimé avec succès.', 'alert-success')

    return redirect('/client/manage/show')
