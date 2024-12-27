#------------------------------------------------------------
### IMPORTS --------------------------------------------
import importlib
import os
import draft

# Dynamically import all Python files in the current directory
current_dir = os.path.dirname(__file__)
for file in os.listdir(current_dir):
    if file.endswith('.py') and file != '_ml.py':
        module_name = file[:-3] # Remove .py extension
        globals()[module_name] = importlib.import_module(module_name)



#------------------------------------------------------------