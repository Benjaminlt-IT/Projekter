from cryptography.fernet import Fernet

def lavKey(keyPath):
    key = Fernet.generate_key()
    with open(keyPath, "wb") as keyFil:
        keyFil.write(key)
    print(key)



def læsKey(keyPath):
    with open(keyPath , "rb") as keyFil:
        key = keyFil.read()
    return key

def krypter(krypterPath):
    key = læsKey("C:/Users/benja/Desktop/key.txt")
    fernet = Fernet(key)
    with open(krypterPath, "rb") as f:
        data = f.read()
    krypteretData = fernet.encrypt(data)
    with open(krypterPath, "wb") as f:
        f.write(krypteretData)

def dekrypter(krypterPath):
    key = læsKey("C:/Users/benja/Desktop/key.txt")
    fernet = Fernet(key)
    with open(krypterPath, "rb") as f:
        krypteretData = f.read()
    data = fernet.decrypt(krypteretData)
    with open(krypterPath, "wb") as f:
        f.write(data)

#lavKey("C:/USers/benja/Desktop/key.txt")
dekrypter("C:/Users/benja/AppData/Local/Programs/Thonny/thonny.exe")