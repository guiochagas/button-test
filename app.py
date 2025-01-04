from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = "Clique no botão!"
    
    if request.method == 'POST':
        message = "Você clicou no botão!"

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
