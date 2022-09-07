#!/usr/bin/python

from consolemenu import *
from consolemenu.items import *

# Create the menu
menu = ConsoleMenu("Title", "Subtitle")

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected
menu_item = MenuItem("Gestion de Tournoi")
selection_menu = SelectionMenu(["Gérer", "Nouveau", "Modifier", "Supprimer"], menu_item)

# A FunctionItem runs a Python function when selected
#function_item = FunctionItem("Call a Python function", input, ["Enter an input"])

# A SelectionMenu constructs a menu from a list of strings
#selection_menu = SelectionMenu(["Tournoi", "Rounds", "Matchs", "Joueurs"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
#submenu_item = SubmenuItem("Joueurs", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(menu_item)
#menu.append_item(function_item)
#menu.append_item(submenu_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()