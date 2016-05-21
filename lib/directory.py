##
# Modulo per la gestione delle directory
# Data di inizio :: 12/05/2016
# Autore : TheSkymer
# Licenza Open Source
#

import sys
import os
from collections import UserDict

# Definisco una piccola doc per l'uso della classe
usage =
 """
    usage for Directory Library:
    - Use the prompt python directory.py directory_path
      for use only directory class for testing
    - Use python directory.py help for watch the doc
    - The out will be(if you are using the printDir method):
        directory : ...
                    ...
        file : ...
               ...
        path : directory_path
    - the Directory Library inizialize a dictionary with the all content of the sub-directorys or
      files

"""

# Crea una sub-class di userdict per inizializzare
# un dizionario contenete le informazioni riguardanti la directory
# nel formato {path : path_name, directory : directorys_list, file : files_list}
# tale classe è trattata come un dizionario che analizza soltanto una
# directory e ne salva il contenuto con i path dei file e directory
#
class Directory(UserDict):
    def __init__(self, file_path = None):
        UserDict.__init__(self)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        self["path"] = file_path
        self["file"] = []
        self["directory"] = []
        self.__parse(self["path"])

    # metodo privato per spezzettare la directory ed 
    # analizzarne il contenuto divendolo tra file e
    # directory
    # "La funzione potrebbe riscontrare problemi di riconoscimento"
    #
    def __parse(self, directory_path):
        for f in os.listdir(directory_path):
            obj_path = os.path.join(directory_path, f)
            try:
                c = os.listdir(obj_path)
                self["directory"].append(obj_path)
                if len(c) == 0:
                    return 0
                self.__parse(obj_path)
            except:
                self["file"].append(obj_path)


    # Analizza una directory distruggendo prima i dati del processo iniziale
    # e chiamando il metodo __parse per processare di nuovo la directory
    # e registarne così il suo contenuto attuale
    #
    def processDirectory(self):
        """ Call parse method """
        self["file"] = []
        self["directory"] = []
        self.__parse(self["path"])

    # Stampa il contenuto della directory in modo schematico :
    # path : path_name
    # file : file_name ...
    # directory : directory_name ...
    #
    def printDir(self):
        for (k, v) in self.items():
            if k != "path" :
                for e in v:
                    print(k, " : ", e)
            else:
                print(k, " : ", v)
	

# Unit Test
if __name__ == "__main__":
    directory_path = sys.argv[1]
    if directory_path == "help":
        print(usage)
    else:
        directory = Directory(directory_path)
        ## Some istruction
        #  ...



