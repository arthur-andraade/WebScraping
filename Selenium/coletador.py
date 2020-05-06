from selenium import webdriver
import time


class Coletador:
    def __init__(self,url):
        self.browser = webdriver.Firefox() #Inicializando browser
        self.browser.get(url) #Entrando na page do estabelecimento no Ifood
        time.sleep(3)
        self.listaProdutosNovosExtraidos = []
        self.listaDosProdutos = []
        self.scroll = 0

    # Buscando dados chaves de acordo com sua organização na DOM
    def buscandoDados(self):
        self.titulos = self.browser.find_elements_by_class_name("dish-card__description")
        self.detalhes = self.browser.find_elements_by_class_name("dish-card__details")
        self.precos = self.browser.find_elements_by_class_name("dish-card__price")
        time.sleep(1)

    # Extraindo o "valor" dos dados
    def extraiDados(self):
        for index in range(0, len(self.titulos)):
            novoProduto = [self.titulos[index].text, self.precos[index].text, self.detalhes[index].text]
            self.listaProdutosNovosExtraidos.append(novoProduto)
            novoProduto = []

    # Compara se os produtos capitados são repetidos
    def comparaSeProdutoEstaNaLista(self):
        for produto in self.listaProdutosNovosExtraidos:
            novo = True
            
            for produtoAnalisado in self.listaDosProdutos:
                if(produto[0] in produtoAnalisado):
                    novo = False
                    break

            if(novo):
                self.listaDosProdutos.append(produto)
        
        self.listaProdutosNovosExtraidos = []

    # Função responsável por arrastar o scroll para percorrer página abaixo
    def percorrePaginaAbaixo (self):
        self.scroll = self.scroll + 1200
        self.browser.execute_script("window.scrollTo(0,{0});".format(self.scroll))
        time.sleep(1)
    
    # Start para começar a análisa da pagina web e coletar os dados
    def analisaPaginaWeb(self,iteracao):
        contador = 1
        while(contador != iteracao):
            self.percorrePaginaAbaixo()
            self.buscandoDados()
            self.extraiDados()
            self.comparaSeProdutoEstaNaLista()
            contador = contador + 1
            print(contador)
        self.browser.close()


# DANDO START NO ALGORITMO
algoritmo = Coletador("https://www.ifood.com.br/delivery/botucatu-sp/nunos-jardim-paraiso/e0b7e466-044f-479f-9b5d-e43c24302736?utm_medium=share")
algoritmo.analisaPaginaWeb(21)

#Verificando lista de produtos
for produto in algoritmo.listaDosProdutos:
    print("PRODUTO -> | {0} | {1} | {2} |\n".format(produto[0],produto[1],produto[2]))