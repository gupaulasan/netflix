# Netflix
Tratamento e análise de dados de utilização fornecidos pela Netflix

## Aquisição de dados
Por meio de solicitação no website da empresa, é possível obter um arquivo CSV com dados de utilização do serviço de streaming de filmes. As informações fornecidas consistem no data e hora do _play_, informações gerais do conteúdo sendo assistido, tais como nome do conteúdo, tipo, episódio, temporada, etc.

## Problematização
Minha intenção era avaliar os padrões de comportamento dos usuários da conta sendo analisada, havia duas questões principais
1. Os usuários da conta costumam utilizar mais o serviço durante a semana, como forma de descanso do dia do trabalho, ou durante o final de semana como lazer em seu tempo livre semanal?
2. Qual seria o melhor horário para enviar notificações de novos conteúdos aos usuários dessa conta?

## Proposta de solução
Utilizar das bibliotecas `Pandas` e `Matplotlib` para tratar os dados e plotá-los, na intenção de obter dois gráficos distintos
- Histograma das horas do dia em que são assistidos os episódios
- Histograma de dias da semana que os episódios são assistidos
