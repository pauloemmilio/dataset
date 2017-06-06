# Tweets para Análise de Sentimentos em Português (TAS-PT)

O TAS-PT é um dataset para análise de sentimentos na língua portuguesa com dados coletados do Twitter.

O dataset é composto por dois arquivos:
 
  - *positivo.txt* contém IDs de 38119 tweets com sentimento positivo
  - *negativo.txt* contém IDs de 38119 tweets com sentimento negativo

Os tweets foram capturados e rotulados automaticamente. Tweets com emoticons ':)' ou ':-)'
foram rotulados como positivos e tweets com emoticons ':(' ou ':-(' foram rotulados como negativos.

O dataset não possui o conteúdo textual dos tweets, pois tal disponibilização fere
as regras de privacidade do Twitter. Por isso, é necessário utilizar a API do Twitter
para recuperar o conteúdo das mensagens através dos IDs nos arquivos.

Executando o arquivo *script.py* os tweets correspondentes aos IDs dos arquivos *positivos.txt* e *negativos.txt* são baixados e gravados num banco de dados SQLite (arquivo *tweets.sqlite*).

Por causa dos limites de acesso à API do Twitter, o processo de download dos tweets
pode demorar muitas horas. Por isso, é possível cancelar e reiniciar o script de
download quantas vezes for necessário. Os tweets já armazenados não serão baixados
novamente.

O banco de dados contém uma tabela que armazena os tweets. Ela possui três colunas:
tweet_id, text e sentiment. A primeira armazena o ID do tweet, a segunda o conteúdo textual e a última o sentimento (0 = negativo e 1 = positivo).

Para acessar os tweets no banco de dados, importe o arquivo db.py e chame a função `get_tweets()`.
