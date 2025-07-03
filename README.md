# Proyecto Flask API RESTful con Peewee y MySQL/PostgreSQL

Este proyecto es una API RESTful construida con **Flask** y **Peewee ORM**, compatible tanto con **MySQL** como con **PostgreSQL**, para la gestión de productos.

## Tecnologías utilizadas

- Python 3.10+
- Flask
- Peewee ORM
- MySQL o PostgreSQL (según configuración)
- Bruno (para pruebas)

## 📁 Estructura del proyecto

flask_4/

├── app.py

├── .env

├── .gitignore

├── requirements.txt

├── models/

│ └── Producto.py

├── controllers/

│ └── ProductoController.py

├── routes/

│ └── api.py

r
Copiar
Editar

## Configuración

1. Crea y activa un entorno virtual:

```bash
python -m venv .venv
.venv\Scripts\activate  # En Windows
Instala las dependencias:
```
```bash
Copiar
Editar
pip install -r requirements.txt
Crea un archivo .env con el tipo de base de datos que deseas usar:
```
ini
Copiar
Editar
DB_TYPE=postgres
Puedes cambiar a mysql si usas MySQL.

Asegúrate de tener creada la base de datos correspondiente (flask_4) en tu gestor (MySQL o PostgreSQL).

## Endpoints disponibles

Método	Endpoint	Descripción

GET	/api/productos	Listar todos los productos

GET	/api/productos/<id>	Obtener producto por ID

POST	/api/productos	Crear nuevo producto

PATCH	/api/productos/<id>	Actualizar total o parcialmente un producto

DELETE	/api/productos/<id>	Eliminar un producto

Todos los endpoints devuelven y reciben datos en formato JSON.

## Ejemplo de cuerpo JSON para crear producto (POST)
json
Copiar
Editar
{
  "nombre": "Teclado",
  "costo": 50.00,
  "precio": 75.00,
  "stock": 10
}
 
## Variables del modelo Producto

Campo	Descripción

id	Identificador único (autogenerado)

nombre	Nombre del producto

costo	Costo del producto

precio	Precio de venta

stock	Cantidad en inventario

creado_en	Fecha de creación

actualizado_en	Fecha de última actualización

eliminado	Booleano (si fue eliminado lógicamente)

## Enlace git hub
```bash
https://github.com/cristiancb10/flask_4.git
```
Cristian Coca Bejarano
