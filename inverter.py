def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

string_teste = input("Digite uma palavra ou frase para inverter: ")
print(f"Resultado original: {string_teste}")
print(f"Resultado invertido: {inverter_string(string_teste)}")