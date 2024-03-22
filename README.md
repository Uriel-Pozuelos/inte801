# Proyecto integrador 🚀

## Correr el proyecto

Para correr el proyecto es necesario tener instalado [Node.js](https://nodejs.org/es/).
o [Bun](https://bun.sh/).

Lo ocupamos para poder compilar los estilos de la página usando [Tailwind CSS](https://tailwindcss.com/) y [DaisyUI](https://daisyui.com/).

Una vez que tengas instalado Node.js, puedes correr el siguiente comando para instalar las dependencias del proyecto:

```bash
npm install -D tailwindcss daisyui@latest
o
bun add tailwindcss daisyui
```

Una vez que hayas instalado las dependencias, puedes correr el siguiente comando para compilar los estilos:

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch
o
bunx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch
```

Listo, ahora ya puedes correr el proyecto con el siguiente comando:

nota:cada vez que corras el proyecto, debes correr el comando de tailwindcss o bunx tailwindcss

```bash
python3 main.py
```
