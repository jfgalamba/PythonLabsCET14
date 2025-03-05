# try:
#     idade = int(input("Idade: "))
#     print(f"Dobro da idade: {2 * idade}")
# except ValueError:
#     print("Idade inválida")
# print("FIM")

try:
    idade = int(input("Idade: "))
except ValueError:
    print("Idade inválida")
else:   # noexception:
    print(f"Dobro da idade: {2 * idade}")

while True:
    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Idade inválida")
    else:   # noexception:
        print(f"Dobro da idade: {2 * idade}")
        break

print("FIM")


