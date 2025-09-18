import time as t

while True:
    t.sleep(1)
    hora_atual = t.strftime("%H:%M:%S", t.localtime())
    print(hora_atual, end="\r")
