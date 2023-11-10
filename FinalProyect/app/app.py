from flask import Flask, render_template

app = Flask(__name__)

#Se indica que es la ruta raíz
@app.route('/')
#Se crea una vista llamada index que se expresa en forma de una función
def index():
    cursos = ['PHP', 'Python', 'JAVA']
    #Diccionario
    data = {
        'titulo': 'Index',
        'bienvenida': 'Saludos',
        'cursos': cursos, 
        'numero_cursos': len(cursos)
    }
    return render_template('index.html', data=data)
    #mensaje = "<h1>¡Hola mundo desde Flask!</h1>"

#Si está en la página principal, llama a la función
if __name__=='__main__':
    app.run(debug=True, port=5000)