from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os

# Mengambil nilai username dan password SSO UI dari environtment
# Variabel di sistem operasi yang sedang berjalan. Jika environtmen variabel tidak ditemukan atau kosong, maka Python aka mengisi dengan string default
KEYWORD = os.getenv('UI_SSO_USERNAME', 'Harga IHSG hari ini')

if __name__ == '__main__':
  # Membuat driver/'jembatan' ke Firefox
  driver = webdriver.Firefox()
  driver.get('https://www.google.com')

  # Mencari tag HTML yang digunakan untuk memasukkan username, lalu nilainya akan diisi dengan string dari variable USERNAME
  keyword_input = driver.find_element_by_name('q')
  keyword_input.send_keys(KEYWORD)
  
  keyword_submit = driver.find_element_by_name('btnK')
  keyword_submit.submit()
  time.sleep(5)

  try:
    # Jika gagal login, cetak pesan error dari halaman web ke shell
    status_message = drive.find_element_by_id('status')
    print(status_message.text)
  except NoSuchElementException:
    pass
  finally:
    drive.close()