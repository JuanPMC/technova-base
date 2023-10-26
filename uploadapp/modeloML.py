import hashlib
import os
import cadquery as cq

class modeloML(object):

    def __init__(self, file):
        # init variables
        self.file = file
        self.preddiccion = 0

        # algoritmo de preddicion
        self.file = self.preProcesar()
        self.predeccir()
        self.eliminarFichero()

    def predeccir(self):
        with open(self.file,"rb") as f:
            bytes = f.read() # read file as bytes
            readable_hash = hashlib.md5(bytes).hexdigest();
            print(readable_hash)
        self.preddiccion = 1

    def eliminarFichero(self):
        os.remove(self.file)

    def preProcesar(self):
        input_file  = "media/{}".format(self.file)
        output_file = input_file +'.stl'

        afile = cq.importers.importStep(input_file)
        cq.exporters.export(afile,output_file)
        os.remove(input_file)

        os.system("admesh {} --write-off={}.off".format(output_file,output_file))
        return output_file + ".off"
