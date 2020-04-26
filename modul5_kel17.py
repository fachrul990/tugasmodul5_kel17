from userService import userService #untuk menyertakan berkas userService


print("System Login Kelompok 17!\n")
email = input("Email: ")
password = input("Password: ")
get_class = userService(email,password) #pembuatan objek dari class userService
get_class.login()
