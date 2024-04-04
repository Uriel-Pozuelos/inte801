# Ejecutar main.py en segundo plano
Start-Job -ScriptBlock { py main.py }

# Activar el compilador de TailwindCSS con watch
npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch
