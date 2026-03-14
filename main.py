from client import Client
from conta import Conta

print("testando o projeto...")

c1 = Client("João", "114444-2222")

conta = Conta(c1.name, 6565, 0)

print(f"Name: {c1.name} | Telephone: {c1.telephone}")
print(f"Titular: {conta.titular} | Number: {conta.number} | Saldo: {conta.saldo}")