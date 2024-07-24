import random
karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sf = int(input("lütfen giriş yaparken kullancağiniz şifrenin uzunluğunu girin:"))
parola = ""
for i in range(sf):
    parola = parola + random.choice(karakter)
print(parola)
