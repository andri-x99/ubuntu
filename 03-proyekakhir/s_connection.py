import requests
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

class Conn():
    def __init__(self, url='localhost', port=27017):
        self.koneksi = MongoClient(url,port)
        self.db = self.koneksi.dionaea
        # self.co1 = self.db.connections
        # self.co2 = self.db.logins
        try:
            self.koneksi.server_info()
            # print("Status : Terhubung ke MongoDB")
            # print("IP Address : {}, Port : {}".format(url,port)) 
        except ServerSelectionTimeoutError:
            print("Status : Gagal untuk terhubung ke MongoDB")
            print("Silahkan menyalakan service MongoDB dengan benar")
            
         
# Atha' bin Abi Rabah
# Urwah Bin Zubair
# https://www.programcreek.com/python/example/82177/pymongo.errors.ServerSelectionTimeoutError
