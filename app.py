from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Variável para registrar o clique do botão
button_clicked = False

@app.route('/')
def home():
    message = "Clique no botão!"  # Mensagem inicial
    return render_template('index.html', message=message)

@app.route('/click', methods=['POST'])
def button_click():
    global button_clicked
    button_clicked = True  # Registra que o botão foi clicado
    print("O botão foi clicado no servidor!")  # Imprime a mensagem no servidor
    return jsonify(status="success", message="Botão clicado!")

if __name__ == '__main__':
    app.run(debug=True)
