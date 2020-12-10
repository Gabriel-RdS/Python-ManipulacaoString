
url = "www.bytebank.com.br/cambio?`valor=1500&moedaOrigem=real&moedaDestino=dolar"
indice = url.find("?")
print(url[indice + 1:])
