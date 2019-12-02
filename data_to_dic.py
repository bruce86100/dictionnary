import json

data = json.load(open("data.json"))


def definition(w):
    w = w.lower()
    for i in data:
        if i['M']['mot'] == w:
            return format_answer(i)
    else:
        return "le mot n'a pas été trouvé, veuillez relancer la recherche."


def format_answer(i):
    return "Contexte : " + i['CONT'] + "\n"+"Définition : " + i['SENS'] + "\n" + "Champ lexical :" + i['DOM']['nom'] + "\n" + "Catégorie : " +  i['CA']['categorie'] + "\n" + "Type : " + i['CA']['type'] + "\n" + "Genre :" + i['CA']['genre']


word = input("Entrez un mot :")

print(definition(word))
