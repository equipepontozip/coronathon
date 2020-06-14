# Combinatron

É um sistema que rastreia as demissões e conecta os candidatos para novas oportunidades de trabalho que melhor se adequam ao seu perfil. Utilizando fontes de dados públicas como o SINE o sistema consegue identificar as características do candidato e utilizando algoritmos de aprendizado de máquina faz o match do usuário com a vaga que melhor se encaixa ao seu perfil.

Resultado da Hackathon  [Coronathon](https://coronathon.enap.gov.br/) sediada pela [ENAP](https://www.enap.gov.br/pt/)

### Requisitos

Você precisa de ter [Docker](https://www.docker.com/) instalado na sua máquina.

## Fazendo Funcionar

Use o comando na raiz do projeto para fazer a API funcionar:
```
docker-compose up 
```

Depois você poderá fazer requisições na API pelo endereço  `localhost:8080`

## Rotas
GET - `/status`

## Principais Bibliotecas

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [numpy](https://numpy.org/) -  The fundamental package for scientific computing with Python 
* [surprise](http://surpriselib.com/) - Surprise is a Python scikit building and analyzing recommender systems that deal with explicit rating data.
* [cachetools](https://pypi.org/project/cachetools/) - Used to generate RSS Feeds


## Authors

* **Naiara Andrade Camelo** - [naiieandrade](https://github.com/naiieandrade)
* **Christian Moryah** - [chris-redfield](https://github.com/chris-redfield)
* **Nasser Boan** - [nasserboan](https://github.com/nasserboan)
* **Matheus Batista** - [matheusbsilva](https://github.com/matheusbsilva)
* **Lucian Lorens** - [lucianlorens](https://github.com/lucianlorens)

Veja também outros trabalhos da [Equipe.zip](https://github.com/your/project/contributors) 

## Agradecimentos

* A todos os profissionais da linha de frente que tem arriscado sua vida por nós.