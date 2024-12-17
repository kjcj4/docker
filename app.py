from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Configuración de la aplicación Flask y base de datos
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.db'  # Archivo de base de datos SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactivar la notificación de modificaciones
db = SQLAlchemy(app)

# Definir el modelo de Producto
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID único para cada producto
    nombre = db.Column(db.String(100), nullable=False)  # Nombre del producto
    completo = db.Column(db.Boolean, default=False)  # Estado si está completo o no

    def __repr__(self):
        return f'<Producto {self.nombre}>'

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

# Ruta principal para mostrar y agregar productos
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener el nombre del producto desde el formulario
        nombre = request.form['nombre']
        # Crear un nuevo producto
        nuevo_producto = Producto(nombre=nombre)
        db.session.add(nuevo_producto)
        db.session.commit()
        return redirect(url_for('index'))  # Redirigir a la página principal para ver el producto agregado

    # Obtener todos los productos de la base de datos
    productos = Producto.query.all()
    return render_template('index.html', productos=productos)

# Marcar un producto como completo
@app.route('/completar/<int:id>', methods=['POST'])
def completar(id):
    producto = Producto.query.get(id)  # Obtener el producto por ID
    if producto:
        producto.completo = True  # Marcar como completo
        db.session.commit()
    return redirect(url_for('index'))

# Eliminar un producto de la lista
@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    producto = Producto.query.get(id)  # Obtener el producto por ID
    if producto:
        db.session.delete(producto)  # Eliminar el producto de la base de datos
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
