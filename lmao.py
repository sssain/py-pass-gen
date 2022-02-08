import string
import random


## Tipe Huruf/Letters
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():

	## Seberapa Banyak Huruf

	huruf = int(input("Mau berapa karakter passwordnya? "))

	## shuffling the characters
	random.shuffle(characters)
	
	## mengambil karakter acak dan huruf
	password = []
	for i in range(huruf):
		password.append(random.choice(characters))

	random.shuffle(password)

	## Hasil
	print("".join(password))



## invoking the function
generate_random_password()