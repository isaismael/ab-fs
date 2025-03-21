from flask import Flask, Blueprint, render_template, request
from app.scraper import WebScraper

bp = Blueprint('scraper-meli', __name__, url_prefix='/scraper-meli' )

tags_dict = {
    'nombre_producto': "//h1[@class='ui-pdp-title']",
    'precio_actual': "//span[@class='andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact']",
    'precio_antes': "//s[@class='andes-money-amount ui-pdp-price__part ui-pdp-price__original-value andes-money-amount--previous andes-money-amount--cents-superscript andes-money-amount--compact']",
    'porcentaje_descuento': "//span[@class='andes-money-amount__discount ui-pdp-family--REGULAR']",
    'cuotas': "//p[@id='pricing_price_subtitle']",
    'envio': "//div[@class='ui-pdp-buy-box-offers__offer-list-children']",
}

@bp.route('/')
def index_meli():
    return render_template('sc_meli.html')

@bp.route('/buscar', methods=['GET'])
def buscar():
    search = request.args.get('q', '')
    print(search)
    
    url = f"https://listado.mercadolibre.com.ar/{search}#D[A:{search}]"
    
    print(url)
    
    return render_template('resultados.html')    
        


'''
info=info , search=search
scraper = WebScraper(url)
titulos = scraper.extraer_urls(url_ficha, tags_dict)
'''

