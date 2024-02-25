from flask import Blueprint
from flask import Flask, request, render_template, redirect, abort, flash, session

from connexion_db import get_db


client_manager = Blueprint('client_manager', __name__,
                        template_folder='templates')

@client_manager.route('/client/manage/show')
def client_casque_show():
    mycursor = get_db().cursor()
    id_client = session.get('id_user')

    print("id client : " + str(id_client))

    sql = "SELECT * FROM mots_de_passe;"

    mycursor.execute(sql)
    mot_de_passe = mycursor.fetchall()


    return render_template('client/manage.html',
                           mot_de_passe = mot_de_passe)



@client_manager.route('/ajouter', methods=['GET', 'POST'])
def ajouter():

    return render_template('client/ajouter.html')