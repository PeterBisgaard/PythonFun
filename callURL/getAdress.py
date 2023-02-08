import urllib.request
import urllib.parse
import json

def getAdress(adress):
    urlAdress = urllib.parse.quote(adress)
    #https://api.dataforsyningen.dk/autocomplete?q=K%C3%B8&type=adresse&caretpos=2&supplerendebynavn=true&stormodtagerpostnumre=true&multilinje=true&fuzzy=true
    url = "https://api.dataforsyningen.dk/autocomplete?q={}&type=adresse&caretpos=2&supplerendebynavn=true&stormodtagerpostnumre=true&multilinje=true&fuzzy=true".format(urlAdress)
    response = urllib.request.urlopen(url)
    data = response.read()
    jsonText = data.decode('utf-8')
    text = json.loads(jsonText)
    return text[0]['forslagstekst']

print(getAdress('I P Hansens vej 22'))



