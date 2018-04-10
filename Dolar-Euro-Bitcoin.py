import requests
import json
import time
import datetime

while True:
    requisicao = requests.get('http://api.promasters.net.br/cotacao/v1/valores')
    cotacao = json.loads(requisicao.text)

    print('#### COTAÇÃO #### ', datetime.datetime.now())
    print('Dolar:', cotacao['valores']['USD']['valor'])
    print('Euro:', cotacao['valores']['EUR']['valor'])
    print('BTC:', cotacao['valores']['BTC']['valor'])
    time.sleep(2)