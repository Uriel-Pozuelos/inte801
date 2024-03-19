from lib import d

d = d.D()
json_data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

d.error("Esto es un mensaje de error")
d.info("Esto es un mensaje de información")
d.success("Esto es un mensaje de éxito")
d.warning("Esto es un mensaje de advertencia")
d.json(json_data)

# Ejemplo de log con color personalizado
d.log("Este es un mensaje con color personalizado", color='\033[95m')
