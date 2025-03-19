from scraper import WebScraper

tags_dict = {
    'nombre_producto': "//h1[@class='ui-pdp-title']",
    'precio_actual': "//span[@class='andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact']",
    'precio_antes': "//s[@class='andes-money-amount ui-pdp-price__part ui-pdp-price__original-value andes-money-amount--previous andes-money-amount--cents-superscript andes-money-amount--compact']",
    'porcentaje_descuento': "",
    'cuotas': "",
    'envio': "",
}

search = "televisor"
url_ficha = "//a[@class='poly-component__title']"
url = f"https://listado.mercadolibre.com.ar/{search}#D[A:{search}]"

scraper = WebScraper(url)
titulos = scraper.extraer_urls(url_ficha, tags_dict)

