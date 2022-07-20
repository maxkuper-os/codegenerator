import hashlib
import math
import random
class Generator:
    def generate_pass(lengthPass):
        try:
            if lengthPass < 4:
                lengthPass = 4
            if lengthPass == 5 or lengthPass == 7:
                lengthPass = 6
            if lengthPass > 8:
                lengthPass = 8
        except TypeError:
            print("Неправильный тип данных")
        password = ""
        abc = "1234567890"
        while len(password) < lengthPass:
            password += abc[math.floor(random.random() * len(abc))]	
        return password
    def generate_salt(lengthSalt):
        salt = ""
        abc = "abcdefghijklmnopqrstuvwxyz1234567890"
        while len(salt) < lengthSalt:
            salt += abc[math.floor(random.random() * len(abc))]	
        return salt
    def generate_hash(salt,password):
        password = salt + password
        encrypted = hashlib.sha1(password.encode()).hexdigest()
        return encrypted


encrypted = hashlib.sha1(b'code').hexdigest()