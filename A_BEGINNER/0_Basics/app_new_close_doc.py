'''
Thu Nov 14 04:44:48 PM +03 2024

author: gurkan
'''

### This code line provides a convenient scripting
## making shorter FreeCAD as an alias like 'App'.
# You can handily give as specific alias you like.
import FreeCAD as App # type: ignore

### To obtain readable names, it can use upper and lower letter cases.
##  Abbreviations are crucial and need to be evocatory.
# docName: The Document Name
docName = 'CreatingAndClosingDoc'

# Waiting for the creating approval from the user.
input('Press Enter to create a new FreeCAD Document!.. ')

### The code line below creates a new FreeCAD document
## The 'dot syntax' calls the object's method.
# Hey! FreeCAD make a new document with given name and handle it as 'doc'.
doc = App.newDocument(docName)

# Waiting for the closing approval from the user.
input('Press Enter to colse the document without saving!..')

# This code line closes the document named as 'docName'
App.closeDocument(docName)

