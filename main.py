from ExtratorArgumentosURL import ExtratorArgumentoURL

"""
url = "www.bytebank.com.br/cambio?`valor=1500&moedaOrigem=real&moedaDestino=dolar"
indice = url.find("?")
print(url[indice + 1:])

"""

url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
cambio = ExtratorArgumentoURL(url)
moedaOrigem, moedaDestino = cambio.retornaMoedas()

valor = cambio.retornaValor()
print(moedaOrigem, moedaDestino, valor)
