import tweepy, time, sys, requests

def escreverEmArquivo(text, file):
    nomeDoArquivo = file+".txt"
    arquivo = open(nomeDoArquivo, "a")
    arquivo = open(nomeDoArquivo, "r")
    linhas = arquivo.readlines()
    linhas.append(text + "\n")
    arquivo = open(nomeDoArquivo, "w")
    arquivo.writelines(linhas)
    arquivo.close()

def verificarConexao():
    try:
        response = requests.get("http://www.google.com")
        if(response.status_code == 200):
            return True
        else:
            return False
    except:
        return False
    

consumer_keys = ['XvboRjR2hR46xOdtszALnO6x9',
                 's1KSP6Vm6i3Y8LcSxiOm2NNRG',
                 '5om5GoAhQPrscLFUHoHduFrIq',
                 'uygazRzTBUWnLKreqreTTZUU4']

consumer_secrets = ['XPrDtZqa26LGYbHKy3oHFx9S28KnGCgf7t1YYCLg0ffCTB008Q',
                    '24dWKJXmPgT6Ylwcu9DQ0QCvHUS9m66w7M2cuVrluC9cTZopSR',
                    'mitUyswANwwu2frthDvsbpKkFZIbfQhxZEcRI5ns0VYhT3U5Lq',
                    'S7wDD3xD3m29LC9krtDwBQLOMjdg74LwOiufzynVB0rCwp9J5V']

token_keys = ['2488355484-rh8Nl9DfkZa1OQKSmjf04MKs4u9wDDhy96YpKHh',
              '2488355484-NdyEb5c6FXS8HmRr0OWGeRCcmYxEdocTnqj7e9V',
              '2488355484-s9i5qFgYJwZvxmTcQasg1MvHoJdUgmwCbSJ7OuX',
              '2488355484-xxYFzpgF3Wv6HThYYkdYd7uo5uGL8O7Z3bv6P9v']

token_secrets = ['bMTr9xWpnrFBXEj96YPCJHo6GCw6JSlHzjR3G1nt1TZcj',
                 'Z8p0Newb5QvhLhijApZC7MitQcOW8gyCD9XXVoYFoDNHM',
                 'uKwQcTE81FZ1aER9oGqsfjzivhK2ZJhVVe3koAQqFgx5s',
                 'ffPBvMtX1NqWM4bmuhKTzy1Svih1tZeehVf5pUpmUeiYE']
alerta = True
quantPos = 0
quantNeg = 0
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

auth = tweepy.OAuthHandler(consumer_keys[0], consumer_secrets[0])
auth.set_access_token(token_keys[0], token_secrets[0])
api = tweepy.API(auth)

arquivos = ["positivos.txt", "negativos.txt"]

print("escrevendo em arquivos...")
for arquivo in arquivos:
    arquivo = open(arquivo, "r")
    linhas = arquivo.readlines()
    polaridade = 0
    for tweetId in linhas:
        try:
            tweet = api.get_status(tweetId)
            texto = tweet.text.translate(non_bmp_map)
            if(polaridade == 0):
                escreverEmArquivo(" ".join(texto.split()), "tweets positivos")
                quantPos +=1
            else:
                escreverEmArquivo(" ".join(texto.split()), "tweets negativos")
                quantNeg +=1
        except:
            print("tweet com id: ", tweetId, " não está disponível")
            
    polaridade += 1

print("capturados ", str(quantPos), " tweets positivos")
print("capturados ", str(quantNeg), " tweets negativos")
