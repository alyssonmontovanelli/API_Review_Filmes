# <center>Sistema de Filmes e Avaliações

## <font color="green">Descrição</font>
<p>Este projeto implementa um sistema de cadastro de filmes e avaliações de usuários, permitindo que os filmes sejam avaliados com uma nota de 1 a 10 e acompanhados de um comentário. O sistema foi desenvolvido com FastAPI para a API e SQLAlchemy para a interação com o banco de dados relacional. O banco de dados armazena informações sobre filmes e avaliações. </p>
<br>

## <font color="green">Tecnologias Utilizadas</font>
- FastAPI: Framework Python para criação da API.
- SQLAlchemy: ORM para integração com banco de dados relacional.
- MySQL: Banco de dados utilizado.
- Pydantic: Validação e serialização de dados.
- Uvicorn: Servidor ASGI para rodar a aplicação.

<br>


## Estrutura do Banco de Dados

![Exemplo de Diagrama](img/relacao_db.png)

- ### Tabelas Criadas:
  - <strong>tb_filmes</strong>: Contém informações a respeito dos filmes, como título (nome), ano de lançamento, gênero (ação, aventura, etc) e diretor;
  - <strong>tb_avaliacoes</strong>: Informações sobre avaliações de cada filme, como nome do avaliador, nota, comentário e código ID do filme.

- ### Relacionamentos:
  - A tabela tb_avaliacoes está relacionada à tabela tb_filmes por intermédio da chave estrangeira "filme_id", através de uma relação muitos para um, ou seja, um filme pode ter diversas avaliações conectadas a ele.

- ### Modelagem do Banco de Dados:
  - Optei pela construção/modelagem das tabelas utilizando o SQLAlchemy (pastas config e models deste projeto), abaixo estão recortes dos scripts com os parâmetros e regras utilizadas.
  
![Exemplo de Diagrama](img/modelagem_tb_filmes.png)
![Exemplo de Diagrama](img/modelagem_tb_avaliacoes.png)



