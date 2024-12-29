import requests

# Função para receber o objeto JSON que recebe da requisição
# Função com objetivo de retornar um dict conforme schema do banco de dados
def criaDictFilmeAPI(req):
   
   titulo_request = req['Title']
   ano_lancamento_request = int(req['Year'])
   genero_request = req['Genre']
   diretor_request = req['Director']

   filme = {
      "titulo": titulo_request,
      "ano_lancamento": ano_lancamento_request,
      "genero": genero_request,
      "diretor": diretor_request
   }

   return filme

def requestFilmeAPI(nome_filme):
   try:
      key = "d71b7b36"
      filme = nome_filme.replace(" ", "+") #Formato que é aceito pela API
      url = f"http://www.omdbapi.com/?t={filme}&plot=full&apikey={key}"

      # Requisição
      response = requests.get(url)
      resposta = response.json()

      # função para retornar os dicionarios conforme Schema do banco de dados
      return criaDictFilmeAPI(resposta)
   
   except Exception as e:
      raise Exception(f"erro {str(e)}")

      

