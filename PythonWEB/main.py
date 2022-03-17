from flask import Flask
from flask import render_template, request

app= Flask(__name__)

#callback
@app.before_request
def before_request():
    print('Antes de la petición')

@app.after_request
def after_request(response):
    print('Despues de la petición')
    return response


@app.route('/')
def index():
    name = 'nombre'
    tipo = 'admin'
    cursos = ['Introducción a Materia','Biología','Química','Inglés']

    return render_template('index.html',username=name, tipo=tipo, cursos=cursos)

@app.route('/<area>/<username>/<int:tipo>') #parametros
def usuario(tipo,area,username):
    return area + ' Perfil de: ' + username + ' tipo:' + str(tipo)

@app.route('/datos')
def datos():
    nombre = request.args.get('nombre','') #Dic
    curso = request.args.get('curso','')
    return 'Listado de datos: ' + nombre + ', curso:' + curso

@app.route('/about')
def about():
    print('Estamos en el about')
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=9000)