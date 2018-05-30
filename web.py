from flask import Flask
from flask import render_template
from flask import g
from flask import request
from flask import jsonify
import aiml

app = Flask(__name__)
app.debug = True

def get_aiml_kernal():
    if not hasattr(g, 'aiml_kernal'):
        g.aiml_kernal = aiml.Kernel()
        g.aiml_kernal.learn("./aiml/botdata/arabic/*.aiml")
    return g.aiml_kernal

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/talk')
def talk():
    aiml_kernal = get_aiml_kernal()
    chat_input = request.args.get('chat_input', "", type=str)
    response = aiml_kernal.respond(chat_input)
    return jsonify(response=response)

if __name__ == '__main__':
    app.run()