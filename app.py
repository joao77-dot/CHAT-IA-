from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

# Configuração da API do Gemini
genai.configure(api_key="AIzaSyDTJxcpKjTrVp_a_oKCxLUmyZDGu7Z6URY")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

app = Flask(__name__)

# Página inicial
@app.route('/')
def index():
    return render_template('chat.html')  # A página HTML que você já tem

# Endpoint para mensagens do chatbot
@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message')
    
    # Verifica se a mensagem corresponde a um comando específico
    if user_message.lower() in ["quem te criou?", "quem te programou?", "quem é você", "quem e voce", "quem te programou", "quem te criou"]:
        bot_response = "Eu fui criado e programado por João!"
    else:
        # Envia a mensagem para o chatbot
        response = chat.send_message(user_message)
        bot_response = response.text
    
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
