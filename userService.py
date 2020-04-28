class userService(object):
    """description of class"""
    def __init__(self, email, password): #pembuatan constructor
        self.email = email
        self.password = password
        self.data = {
            "fachrulkelompok17@gmail.com" : {
                "email"     : "fachrulkelompok17@gmail.com",
                "password"  : "12345",
                "role"      : "superadmin"
            },
            "taufikkelompok17@gmail.com" : {
                "email"     : "taufikkelompok17@gmail.com",
                "password"  : "12345",
                "role"      : "user"
            }
        }
        self.history = {
            "fachrulkelompok17@gmail.com" : {
                "peminjaman_buku" : {'Fisika Dasar','Dasar Komputer dan Pemrograman'},
                "tanggal_pinjam"  : "26-04-2020"
            },
            "taufikkelompok17@gmail.com" :{
                "peminjaman_buku" : {'Kalkulus','Dasar Komputer dan Pemrograman','Konsep Jaringan Komputer'},
                "tanggal_pinjam"  : "26-04-2020",
                }
            }
        
    def login(self): #pembuatan method login
        get_data = self.checkCredentials() #pembuatan variabel baru untuk pengecekan data inputan user
        get_history = self.checkCredentials2()
        if get_history:
           hist_buku = get_history['peminjaman_buku']
           hist_date = get_history['tanggal_pinjam'] 
        if get_data: #pengkondisian boolean untuk login user
            print("\nWelcome ",get_data['role'])
            print("Logged it as user email: ",get_data['email'], "\n")
            print(get_data['email'], "meminjam buku :\n")
            for buku in hist_buku:
                print(buku)
                print()
            print("Tanggal Peminjaman : ", hist_date)
        else:
            print("\nInvalid Login!\n")

    def checkCredentials(self): #method untuk mengecek data inputan user
        for value in self.data:
            if value == self.email:
                get_data_user = self.data[value]
                if self.password == get_data_user['password']:
                     return get_data_user 
                else:
                     return False

    def checkCredentials2(self): #method untuk mengecek data inputan user
        for value in self.history:
            if value == self.email:
                return self.history[value]
            else:
                return False
                

