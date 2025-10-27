
import streamlit as st

st.title("🔮 Jeu de déduction magique")


def repond_oui_non(question):
    while True:
        reponse = input(question + " (oui/non) ").strip().lower()
        if reponse in ["oui", "non"]:
            return reponse
        else:
            print("Veuillez répondre par 'oui' ou 'non'.")


print("bonjour Mr/Mn " + "." + "heureux de vous rencontrer ")

nom = input("Quel est votre nom ? ")
print("bonjour " + nom )

print("Imaginez que vous avez choisi un nombre entier non nul.")

print("ne me le dite pas garder ce nombre secret")

if repond_oui_non("Avez-vous choisi un nombre dans votre tête ?") == "non":
    print("Prenez le temps de choisir un nombre, puis relancez le programme.")
    exit()


print("Additionnez ce nombre avec lui-même.")
if repond_oui_non("Avez-vous effectué l'addition ?") == "non":
    print("Faites l'addition mentalement, puis relancez.")
    exit()

print("Multipliez maintenant le resultat de l'addittion par un nombre entier compris entre 0 et 10.")
while True:
    try:
        n = int(input("entre le nombre  que vous avez choisi ? "))
        if 1 <= n <= 10:
            break
        else:
            print("Le nombre doit être entre 1 et 10.")
    except ValueError:
        print("Ce n'est pas un nombre entier valide.")

if repond_oui_non("Avez-vous effectué la multiplication ?") == "non":
    print("Faites la multiplication mentalement, puis relancez.")
    exit()


print("Divisez maintenant le résultat obtenu par le nombre que vous aviez choisi au début.")
if repond_oui_non("Avez-vous effectué la division ?") == "non":
    print("Faites la division mentalement, puis relancez.")
    exit()
nombre_devine = (n * 2)
print("Je devine que le resultat est :" + str(nombre_devine))
