import urllib
import urllib.request


try:
    site = urllib.request.urlopen('https://web.whatsapp.com')
except urllib.error.URLError:
    print('\033[31mERRO. Problema de conexão, tente novamente mais tarde.\033[0m')
else:
    print(f'\033[34mO site está funcionando e está acessível.\033[0m')

