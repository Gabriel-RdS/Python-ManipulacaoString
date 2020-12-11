from ExtratorArgumentosURL import ExtratorArgumentosURL

"""
url = "www.bytebank.com.br/cambio?`valor=1500&moedaOrigem=real&moedaDestino=dolar"
indice = url.find("?")
print(url[indice + 1:])

"""

url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dólar"

argumentosUrl = ExtratorArgumentosURL(url)

moedaOrigem, MoedaDestino = argumentosUrl.retornaMoedas()
print(moedaOrigem, MoedaDestino)
