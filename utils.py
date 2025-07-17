import bcrypt
def generate_password(password:str):
    return bcrypt.hashpw(password.encode(),bcrypt.gensalt((13))).decode()
def verify_password(password:str,hash_password:str):
    return bcrypt.checkpw(password.encode(),hash_password.encode())