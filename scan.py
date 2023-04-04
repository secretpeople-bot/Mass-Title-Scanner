import threading
import requests
import colorama
import os
from colorama import init, Fore, Back, Style, init
from concurrent.futures import ThreadPoolExecutor

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

gr = Fore.GREEN
rd = Fore.RED
yl = Fore.YELLOW
rs = Style.RESET_ALL

# fungsi untuk melakukan pengecekan title website
def check_title(url):
    try:
        # tambahkan http:// jika belum ada di URL
        if not url.startswith('http') and not url.startswith("https://"):
            url = 'http://' + url

        # ambil response dari website
        response = requests.get(url, timeout=5)

        # ambil title dari response
        title = response.text.split('<title>')[1].split('</title>')[0]

        # tampilkan verbosenya
        print(f"{gr}[SUCCESS]{rs} {url} - {title}")

        # simpan result ke file
        with open('results.txt', 'a') as f:
            f.write(f"{url} - {title}\n")
    except Exception as e:
        # tampilkan verbosenya jika terjadi error
        print(f"{rd}[ERROR]{rs} {url}")

# fungsi untuk membaca list website dari file
def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

clear_screen()

init()

if __name__ == '__main__':
    # minta input nama file dari pengguna
    print(f"{gr}[ MASS TITLE CHECKER ] {gr}[ Vexelvox ]{rs}")
    filename = input(f"{gr}Give Me Site List Bitch{rd}/Vexelvox> {gr}$ {rs}")

    # baca list website dari file
    urls = read_file(filename)

    # buat thread pool dengan jumlah thread sebanyak 10
    with ThreadPoolExecutor(max_workers=10) as executor:
        # submit setiap website ke thread pool untuk dicek
        for url in urls:
            executor.submit(check_title, url)

    # tampilkan pesan ketika selesai
    print(f"{gr}Done!{rs} Check Your Results.txt")

    # tutup program
    exit()
