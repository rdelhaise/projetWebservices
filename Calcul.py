# coding:utf-8 #

class Calcul(object):

    def __init__(self):
        self.results = {}

        self.numbers = []

    @staticmethod
    def formatResponse(result):
        resultStr = ""
        for key in result:
            # Formate le résultat pour en faire un str qui sera la réponse du webservice
            resultStr += 'Operation n°' + str(key) + ' : ' + str(result[key]) + '\n'

        return resultStr

    def doOperation(self, ope):
        result = None
        numberA = None
        numberB = None
        i = -1
        if self.numbers:
            for number in self.numbers:
                # Permet de savoir combien d'opération on été faite
                i += 1
                if not numberA:
                    numberA = number
                # Le nombre B ne peut avoir de nombre au à la première boucle
                if not numberB and i > 0:
                    numberB = number
                if numberA and numberB:

                    try:
                        # Python n'accepte que des . et nom des ,
                        numberA = numberA.replace(",", ".")
                        numberB = numberB.replace(",", ".")
                        # Passage des nombres en Float
                        numberA = float(numberA)
                        numberB = float(numberB)
                        if ope == '+':
                            result = numberA + numberB
                        elif ope == '-':
                            result = numberA - numberB
                        elif ope == '*':
                            result = numberA * numberB
                        elif ope == '/':
                            if numberA != 0.0 and numberB != 0.0:
                                result = numberA / numberB
                            else:
                                result = "Il n'est pas possible de diviser par 0"
                        # Ajout du resultat dans un dictionnaire qui sera renvoyé
                        self.results[i] = result
                        # la variable numbreA devient result, permettant de faire plusieurs opérations
                        numberA = str(result)
                        numberB = None
                        result = True
                    except:
                        self.results['error'] = "Veuillez revoir ce que vous envoyez, les variables sont a et b et ce doit être des chiffres"

    def getResults(self):
        return self.formatResponse(self.results)

    def setNumbers(self, newNumbers):

        self.numbers = newNumbers

    def getNumbers(self):

        return self.numbers
