from _des import _DES
import time
message = "ItoMarik"
key = "Nogizaka"
num = int.from_bytes(key.encode("utf-8"),     byteorder='big')
mes = int.from_bytes(message.encode("utf-8"), byteorder='big')
print("mes was", mes)
des_instance = _DES()
start = time.time()
des_instance.set_key(num)
fin = des_instance.encrypt(mes)
res = des_instance.decrypt(fin)
print(res.to_bytes(8, byteorder="big"))
end = time.time()
print("time for key set and encrypt:", end-start)
print(hex(fin))
