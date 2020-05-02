import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.espn.com.br/nfl/classificacao")
soup = BeautifulSoup(page.content, 'html.parser')

divs = soup.body.div
tabelas = divs.find_all("table")

timesDados = []
times = []

for tabela in tabelas:
    tabelaComNomesTimes = tabela.find_all("tr")
    for linha in tabelaComNomesTimes:
        dadosNome = linha.find_all("span", class_="hide-mobile")
        for nome in dadosNome:
            stringNome = nome.find("a")
            try:
                times.append(stringNome.get_text())
            except:
                continue
    

    for linha in tabelaComNomesTimes:
        dadosCompeticao = linha.find_all("td")
        dados = ""
        for dado in dadosCompeticao:
            outDados = dado.find("span", class_="stat-cell")
            try: 
                dados = dados + " |" + outDados.get_text() +"|"
            except:
                continue
        if(dados != ''):
            timesDados.append(dados)


for time in range(0, len(times)):
    print(
        times[time] + "---> >> " + timesDados[time] + " <<\n"
    )