class Traductor():
    def __init__(self, *args, **kwargs):
        self.equivalencias = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "CH": "----",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "Ñ": "--.--",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----."}
    def morse_a_caracter_plano(self,morse):
        for caracter in self.equivalencias:
            if self.equivalencias[caracter] == morse:
                return caracter
        # Si no encontramos equivalencia, regresamos una cadena vacía
        return ""
    def decodificar_morse(self,morse):
        texto_plano = ""  # Aquí alojamos el resultado
        for caracter_morse in morse.split(" "):
            # Por cada carácter, buscamos su equivalencia
            caracter_plano = self.morse_a_caracter_plano(caracter_morse)
            # Lo concatenamos al resultado.
            texto_plano += caracter_plano
        return texto_plano
    def traducir(self,texto):
        divided= texto.split("//")
        divided2=[]
        decodificado=''
        for i in range(len(divided)):
            divided2.append(divided[i].split("/"))
        for i in range(len(divided2)):
            for j in range(len(divided2[i])):
                decodificado = decodificado+self.decodificar_morse(divided2[i][j])
            decodificado = decodificado+" "
        print(divided2)
        return decodificado
