# C216-Projeto Final
# Gestão de Álbuns Musicais

## Integrantes
- **Nome Completo:** Luiza Kinsky Mendes
- **Matrícula:** 32
- **E-mail:** luizamendes@ges.inatel.br

## Descrição do Projeto
Este projeto foi desenvolvido como parte do curso de engenharia de software no INATEL. O sistema permite a gestão de álbuns musicais, incluindo operações como adicionar, listar, atualizar e remover álbuns musicais, além de registrar vendas.

## Objetivos
O objetivo principal deste projeto é proporcionar uma ferramenta de gestão de álbuns musicais que seja simples de usar, mas eficiente e capaz de gerenciar dados de vendas de forma integrada. O sistema é desenvolvido utilizando FastAPI para o backend, PostgreSQL como banco de dados e Docker para facilitar o deployment e a execução em diferentes ambientes.

## Como Rodar o Projeto
Para rodar o projeto, você precisará ter o Docker e o Docker Compose instalados em sua máquina. Com essas ferramentas instaladas, siga os passos abaixo:

1. Clone o repositório:
   git clone [URL do repositório]
2. Navegue até o diretório do projeto:
   cd [Nome do Diretório do Projeto]
3. Execute o comando para construir e iniciar os contêineres:
   docker-compose up --build

Esse comando vai construir os contêineres necessários para o backend, frontend e banco de dados, e vai iniciar todos eles. Após a execução do comando, a API estará disponível em Backend: `http://localhost:8000/`
Frontend: `http://127.0.0.1:3000/`

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.
