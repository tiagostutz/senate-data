# Senate Data
Brazilian Senate OpenData downloader utilities

## Usage

* Create docker-compose.yml
```
version: '3.3'
services:
  senate-data:
    build: .
    image: flaviostutz/senate-data
    ports:
      - 6006:6006
      - 8888:8888
    volumes:
      - senate-input:/notebook/input
      - senate-output:/notebook/output
```

* under the **notebooks** folder, create a subfolder named **output**

* Run ```docker-compose up```

* On another terminal run `docker-compose exec senate-data jupyter notebook list`. It will show a URL like `http://0.0.0.0:8888/?token=5a16349cad2b6f8f438f51cf3c488a1bfb3f5216a27ede9c :: /notebooks`. Take note of this token because you will need it in the next step

* Open http://localhost:8888/ and It will ask for a token. Provide the one you copied from the previous step.

## Data downloads

* Speeches OK
  * http://legis.senado.leg.br/dadosabertos/plenario/lista/discursos/20130301/20130331
  * fields senador, partido, uf, sexo, data, indexacaoTexto, speechContents
  * output/speeches/speeches-201304.csv - yyyymm
  Materias
  * http://legis.senado.leg.br/dadosabertos/materia/pesquisa/lista?sigla=pls&ano=2013
  * fields codigoMateria, data, casa, tipoMateria, naturezaMateria, codigoAutor, nomeAutor, partidoAutor, ufAutor, sexoAutor, ementa, explicacaoEmenta, indexacaoMateria, assunto, situacao, relatores
  * relatores de http://legis.senado.leg.br/dadosabertos/materia/relatorias/131506
  * /output/materias/materias-list-2013.csv
* Votacoes
  * http://legis.senado.leg.br/dadosabertos/plenario/lista/votacao/20160401/20160430
  * fields descricaoVotacao, data, codigoMateria, ementa, explicacaoEmenta, indexacaoMateria, naturezaMateria, tipoMateria, codigoParlamentar, nomeParlamentar, partidoParlamentar, sexoParlamentar, ufParlamentar, votoSimNao
  * ementa, explicacaoEmenta, indexacaoMateria de http://legis.senado.leg.br/dadosabertos/materia/110428
  * /output/votes/votes-list-201301.csv - yyyymm
