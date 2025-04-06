# web-scrapping


## Selenoid configuration
> Selenoid é um servidor de testes de automação que permite executar testes em paralelo em diferentes navegadores e versões. Ele é uma alternativa ao Selenium Grid e é mais leve e fácil de configurar.

Para instalar o Selenoid, siga os passos abaixo:
1. Instale o Docker em sua máquina. Você pode encontrar instruções de instalação no site oficial do Docker: https://docs.docker.com/get-docker/
2. Instale o Selenoid usando o seguinte comando:
```bash
# instalar o navegador Chrome
docker pull selenoid/chrome:latest

# para os containers internos acessarem a rede
docker network create selenoid
```

3. Inicie o Selenoid usando o seguinte comando:
```bash
docker compose up -d
```
4. Verifique se o Selenoid está em execução acessando o seguinte URL em seu navegador: http://localhost:8080/status. Você deve ver uma página com informações sobre os navegadores disponíveis e suas versões.

## linkedin API params


> API link:
> https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?


* location $\rightarrow$ Lugar para procurar a vaga. Ex: "São Paulo, SP"
* keywords $\rightarrow$ Palavra chave para procurar a vaga. Ex: "Desenvolvedor Python"
* geoid $\rightarrow$ ID do lugar. Ex: "103644278" para São Paulo, SP
* f_TRP $\rightarrow$ Tempo máximo para a vaga. Ex: "r86400" para 24 horas (86400 segundos)
* distance $\rightarrow$ Distância em milhas. Ex: "25" para 25 milhas. **MAXIMO 50 milhas**
* f_C $\rightarrow$ Companhia. Ex.: 3065723 para "Smartfit"
* f_JT $\rightarrow$ Tipo de trabalho. Ex: "F" para "Full Time"
  * F = Tempo integral
  * P = Meio período
  * C = Contrato
  * T = Temporario
  * V = Voluntário
* f_E $\rightarrow$ Level de experiência. Ex: "1" para "Estagio"
  * 1 = Estagio
  * 2 = Assistente
  * 3 = Júnior
  * 4 = Pleno-sênior
  * 5 = Diretor
* f_WT $\rightarrow$ Tipo de trabalho remoto. Ex: "2" para "Remote"
  * 1 = Presencial
  * 2 = Remoto
  * 3 = Híbrido

> job link:
> https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/415825954
> 
> 4158259546 - data-entity-urn="urn:li:jobPosting:4158259546"

