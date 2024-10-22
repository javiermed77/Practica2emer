from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/inscripcion', methods=['GET', 'POST'])
def inscripcion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        curso = request.form['curso']
        return f'Inscrito: {nombre} {apellidos} en el curso {curso}'
    return render_template('inscripcion.html')


@app.route('/registro_usuarios', methods=['GET', 'POST'])
def registro_usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        return f'Usuario registrado: {nombre} {apellidos}, Correo: {correo}'
    return render_template('registro_usuarios.html')


@app.route('/registro_productos', methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        return f'Producto registrado: {producto}, Categoría: {categoria}, Existencia: {existencia}, Precio: {precio}'
    return render_template('registro_productos.html')

@app.route('/registro_libros', methods=['GET', 'POST'])
def registro_libros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        tipo = request.form['tipo']
        return f'Libro registrado: {titulo}, Autor: {autor}, Tipo: {tipo}'
    return render_template('registro_libros.html')

if __name__ == '__main__':
    app.run(debug=True)