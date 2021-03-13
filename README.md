# Site do LiveDivulgador

O bot [LiveDivulgador](https://github.com/LiveDivulgador/Live-Divulgador) tem um site onde mostra todos os streamers divulgados.

## Disclaimer
Foi utilizada a template [One Page Wonder](https://startbootstrap.com/template-overviews/one-page-wonder) da [Start Bootstrap](https://startbootstrap.com). A mesma foi modificada para ser mais minimalista.


## Pré Requesitos
- Python3.x
- Flask
- Pandas
- Python-dotenv (opcional, apenas se estiver em um ambiente de desenvolvimento)
- Gunicorn (opcional, apenas no caso de subir o site no heroku)


## Ficheiros
- Colunas dentro do ficheiro `ex_streamers_new.csv`:

	- Id: O Twitch ID do(a) streamer
	- Nome: O nome do canal do(a) streamer
	- Descr: Descrição presente no sobre do(a) streamer
	- Avatar: URL para o avatar do canal do(a) streamer

- Procfile - Este ficheiro é específico para o Heroku saber qual é o ficheiro `.py` principal que o gunicorn deve executar


## Utilização
Caso esteja em um ambiente de desenvolvimento, renomeie o ficheiro `.env_example` para `.env`.

Também deve renomear o ficheiro `ex_streamers_new.csv` para apenas `streamers_new.csv`.

Após isso basta então populacionar o .csv com as informações de alguns streamers.

Por fim deve abrir um terminal na pasta raiz do repositório e executar o comando: `flask run`


## Colaboração
Se gostou do projeto e tem interesse em ajudar, pode sempre seguir as contas do bot no Twitter: [@LiveDivulgador](https://twitter.com/LiveDivulgador) e [@LiveDivulgador2](https://twitter.com/LiveDivulgador2)

Dessa forma estará a ajudar o projeto e os streamers divulgados por ele!

Também pode contribuir com código ou mesmo reportando falhas e dando palpites de novas funcionalidades.

Opiniões são sempre bem vindas!