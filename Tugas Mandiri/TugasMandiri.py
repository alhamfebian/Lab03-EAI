from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os

# Mengambil nilai username dan password SSO UI dari environtment
# Variabel di sistem operasi yang sedang berjalan. Jika environtmen variabel tidak ditemukan atau kosong, maka Python aka mengisi dengan string default
USERNAME = os.getenv('UI_SSO_USERNAME', 'alhamfebian68')
PASSWORD = os.getenv('UI_SSO_PASSWORD', 'Alhamfbn25')

if __name__ == '__main__':
  # Membuat driver/'jembatan' ke Firefox
  driver = webdriver.Firefox()
  driver.get('https://www.gmail.com/')

  # Mencari tag HTML yang digunakan untuk memasukkan username, lalu nilainya akan diisi dengan string dari variable USERNAME
  username_input = driver.find_element_by_name('identifier')
  username_input.send_keys(USERNAME)
  
  form_username_next = driver.find_element_by_id('identifierNext')
  form_username_next.click()
  time.sleep(5)

  # Serupa dengan isian username di atas tapi untuk password
  password_input = driver.find_element_by_name('password')
  password_input.send_keys(PASSWORD)

  # Melakukan submit form
  login_form = driver.find_element_by_id('passwordNext')
  login_form.click()
  time.sleep(5)

  # Tunggu paling lama 5 detik hingga browser mengembalikan halaman baru
  driver.implicity_wait(5)

  try:
    # Jika gagal login, cetak pesan error dari halaman web ke shell
    status_message = drive.find_element_by_id('status')
    print(status_message.text)
  except NoSuchElementException:
    pass
  finally:
    drive.close()