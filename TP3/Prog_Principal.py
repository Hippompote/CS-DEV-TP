'''

Créé par H. Salmon

Jeu du pendu en version console et graphique.
Version TKinter non finalisée, version console fonctionnelle.
Version TKinter en partie réalisée à l'aide de la version de Axel François, actuellement en césure
lien : https://github.com/AxFrancois/CSDEV-Pendu/
'''

import penducons as pc
mots = open('./TP3/Mots.txt','r')

pc.pendu(pc.randWord(mots))
