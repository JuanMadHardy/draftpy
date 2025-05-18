url = "https://www.dittcasa.com"
tupla = url.partition('www.')
protocolo, separador, dominio = tupla
print("Protocolo: {0}\nDominio: {1}".format(protocolo, dominio))