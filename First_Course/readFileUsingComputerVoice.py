import os, os.path
import pyttsx3

print("\n###############################################################")
print("##                      AUTHOR                               ##")
print("##                       Grey                                ##")
print("###############################################################\n")

# check if path or file exists
def checkIfExists(path):
	print("Analyse...\n")
	if os.path.exists(path):
		print(path +" existe")
		return checkIfFileOrDir(path)
	else:
		return path +" n'a pas été trouvé !"
		
# Check if path is a file or directory
def checkIfFileOrDir(path):
	if os.path.isfile(path):
		print(path +" est un fichier \n")
		print("Lecture du fichier... \n")
		openAndRead(path)
	elif os.path.isdir(path):
		print(path +" est un dossier et ne peut etre lu")
	else:
		return "Format inconnu"

# If file, open and read it
def openAndRead(path):
	f = open(path)
	line = f.readline()
	while line:
		print(line)
		pyttsx3.speak(line)
		line = f.readline()
	f.close()
	askIfAnotherFile()
	
# Ask if you want to read another file
def askIfAnotherFile():
	a = input("Voulez-vous lire un autre fichier ? (y/n) ")
	if a == "y":
		firstAction()
	elif a == "Y":
		firstAction()
	else:
		exit()

# First function called when script launched
def firstAction():
	print("Exemple: /home/grey/Documents \nExemple: /home/grey/Documents/test.txt\n")		
	f = input("Entrez le chemin ou le nom du fichier à lire: ")
	checkIfExists(f)

firstAction()
