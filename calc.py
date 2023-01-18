# Importer les modules requis
from tkinter import *
import tkinter.font as font
import \
    json  # Un fichier JSON est un fichier qui stocke des structures de données simples et des objets,Il est principalement utilisé pour transmettre des données entre un serveur et une application Web, comme alternative à XML

#  ╔═══════════════════════════════════════╗
#  ║          Calculatrice Python          ║
#  ║               Crée par                ║
#  ║          Ahmed Malik Ben elkadi       ║
#  ╚═══════════════════════════════════════╝

# Tous les commentaires seront en français et les noms de variables seront en anglais


# Création de la fenêtre principale
Interface = Tk()
Interface.configure(background="#708090")
# Liste pour stocker l'historique des calculs
history = []
# Variable permettant de stocker le chemin d'accès au fichier d'historique
history_file = 'Historique.json'

Interface.geometry("550x430")
Interface.title("Calcultrice ")
Interface.resizable(0, 0)

# Création d'une StringVar pour prendre le texte saisi dans le widget Entry
inp = StringVar()
myFont = font.Font(size=15, slant="italic")

# Création d'un widget Entry pour obtenir l'expression mathématique,
# Et aussi pour afficher les résultats
screen = Entry(Interface, text=inp, width=30,
               justify='right', font=(29), bd=4, background="white")

# Nous  utilisons une structure de type grille
screen.grid(row=0, columnspan=4, padx=15,
            pady=15, ipady=5, )

# La matrice des clés contient toutes les clés nécessaires de c jusqu'a puissance 2
key_matrix = [["c", u"\u221A", "/", "<-"],
              ["7", "8", "9", "*", ],
              ["4", "5", "6", "-", ],
              ["1", "2", "3", "+", ],
              ["!", "%", ".", "="],
              ["(", ")", "^2"]]

history_list = Listbox(Interface)
history_list.grid(row=0, column=8, rowspan=5, padx=1, pady=15, ipadx=5, ipady=5, )

# un dict pour les bouttons
btn_dict = {}

# ici on met une variable pour stocké les resultats obtenues
result = 0


def Calculate(event):
    # obtenir le nom du bouton cliqué
    button = event.widget.cget("text")

    # global sur python nous permet d'appeller les variable
    # qui sont dans le programme mais en dehros de la fonction utilisé
    global key_matrix, inp, result

    try:
        # la condition pour utilisé la Racine carrée
        if button == u"\u221A":
            ans = float(inp.get()) ** (0.5)
            result = str(ans)
            inp.set(str(ans))
        elif button == "^2":  # la puissance 2
            ans = float(inp.get()) ** 2
            result = str(ans)
            inp.set(str(ans))

        elif button == "c":  # pour le bouton effacé
            inp.set("")

        elif button == "!":  # pour le factorial
            def fact(n):
                return 1 if n == 0 else n * fact(n - 1)

            inp.set(str(fact(int(inp.get()))))

        elif button == "%":
            ans = float(inp.get()) / 100
            result = float(ans)
            inp.set(float(set))

        elif button == "<-":  # pour supprimé une entrée
            inp.set(inp.get()[:len(inp.get()) - 1])

        elif button == "=":  # Montrer les résultats
            result = str(eval(inp.get()))
            inp.set(result)

            # Sauvegarder le calcul actuel dans l'historique
            history.append(inp.get())
            with open(history_file, 'w') as file:
                file.write(json.dumps(history))


        else:
            # Affichage sur l'écran du chiffre appuyé
            inp.set(inp.get() + str(button))

    except:  # En cas de syntaxe invalide dans l'expression
        inp.set("Mauvaise opération")


def display_history():
    global history, history_list
    # chargement de l'historique depuis le fichier
    try:
        with open(history_file, 'r') as file:

            history = json.loads(file.read())

    except json.decoder.JSONDecodeError:  # S'il y a une erreur de décodage JSON, un message d'erreur est affiché.
        print('Erreur ')
    # effacer l'historique
    history_list.delete(0, END)

    index = 0
    while index < len(
            history):  # La boucle while parcours chaque élément de l'historique et les insère dans la liste widget à chaque itération.
        history_list.insert(index, history[index])
        index += 1


history_button = Button(Interface, text="Historique", command=display_history, background="#708090")
history_button.grid(row=6, column=3)

percentage_button = Button(Interface, text="%", command=Calculate)
percentage_button.grid(row=5, column=2)


def clear_history():
    with open(history_file, 'w') as file:
        file.write('')
    history_list.delete(0, END)


clear_history_button = Button(Interface, text="Effacer l'historique", command=clear_history, background="#708090")
clear_history_button.grid(row=6, column=4)

# creation des bouton avec des boucles


i = 0
j = 0
while i < len(key_matrix):
    while j < len(key_matrix[i]):
        # Créer et ajouter les boutons au dictionnaire
        btn_dict["btn_" + str(key_matrix[i][j])] = Button(
            Interface, bd=1, text=str(key_matrix[i][j]), font=myFont)

        # position des bouton
        btn_dict["btn_" + str(key_matrix[i][j])].grid(
            row=i + 1, column=j, padx=5, pady=5, ipadx=5, ipady=5)

        # Attribution d'une action aux boutons
        btn_dict["btn_" + str(key_matrix[i][j])].bind('<Button-1>', Calculate)

        j += 1
    i += 1
    j = 0

Interface.mainloop()

