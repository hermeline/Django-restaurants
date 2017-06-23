#-*- coding: utf-8 -*-
# Nous importons la classeHttpResponse du module django.http ,  permet d'encapsuler votre réponse dans un objet plus générique
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.  Une fonction home, avec comme argument une instance de HttpRequest avecl 'argument request'
def home(request):

    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
# la fonction déclare une chaîne de caractères nomméetextet crée une nouvelle instance deHttpResponseà partir de cette chaîne
    text = """<h1>Nos menus :</h1>

              <p>Pour tous les goûts :</p>"""

    return HttpResponse(text)

def view_menu(request, id_menu):
    """
    Vue qui affiche un menu selon son  ID
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    return HttpResponse(
        "Vous avez demandé le menu #{0} !".format(id_menu)
    )




# Simuler une page non trouvée - renvoyer une page 404
from django.http import HttpResponse, Http404


def view_article(request, id_menu):

    # Si l'ID est supérieur à 100, nous considérons que le menu n'existe pas

    if int(id_menu) > 100:

        raise Http404


    return HttpResponse('<h1>Ce menu n\'existe pas</h1>')




# Vue qui renvoie la date actuelle  +  vue "calculette" avec render

from datetime import datetime
from django.shortcuts import render

def date_actuelle(request):
    return render(request, 'menus/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'menus/addition.html', locals())
