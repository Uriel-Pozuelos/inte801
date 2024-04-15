# from lib import d
# from lib.jwt import hash_password
from lib.security import safe
import os

# d = d.D()
# json_data = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# # d.error("Esto es un mensaje de error")
# # d.info("Esto es un mensaje de información")
# # d.success("Esto es un mensaje de éxito")
# # d.warning("Esto es un mensaje de advertencia")
# # d.json(json_data)

# # # Ejemplo de log con color personalizado
# # d.log("Este es un mensaje con color personalizado", color='\033[95m')


text = "<script>alert('hola')</script> Como estas?"
text2 = "Holña"
sql = "SELECT * FROM users WHERE id = 1"

print(safe(text))
print(safe(text2))
print(safe(sql))


# password = "rush2112"
# with open("password.txt", "r") as f:
#     if password + "\n" in f.readlines():
#         print("La contraseña está en el archivo")
#     else:
#         print("La contraseña no está en el archivo")




