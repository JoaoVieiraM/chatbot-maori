"""
Pousada Maori Chatbot - Flask API Server
Servidor web com API REST para o chatbot
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from chatbot_engine import MaoriChatbot
import os

# Inicializa Flask
app = Flask(__name__, static_folder='static')
CORS(app)  # Permite requisições do frontend React

# Inicializa chatbot
print("🌺 Inicializando Chatbot Pousada Maori...")
try:
    chatbot = MaoriChatbot()
    print("✅ Chatbot inicializado com sucesso!")
except Exception as e:
    print(f"❌ Erro ao inicializar chatbot: {e}")
    print("⚠️ Execute: python -m spacy download pt_core_news_md")
    chatbot = None


@app.route('/')
def index():
    """Página inicial com interface do chat"""
    return send_from_directory('static', 'index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Endpoint principal do chatbot
    POST /api/chat
    Body: {"message": "sua pergunta aqui"}
    Response: {"intent": "...", "confidence": 0.95, "response": "..."}
    """
    if not chatbot:
        return jsonify({
            'error': 'Chatbot não inicializado. Instale o modelo spaCy.',
            'install_command': 'python -m spacy download pt_core_news_md'
        }), 500

    try:
        data = request.get_json()

        if not data or 'message' not in data:
            return jsonify({
                'error': 'Campo "message" é obrigatório'
            }), 400

        user_message = data['message'].strip()

        if not user_message:
            return jsonify({
                'error': 'Mensagem não pode estar vazia'
            }), 400

        # Processa mensagem
        response = chatbot.get_response(user_message)

        return jsonify({
            'success': True,
            'user_message': user_message,
            **response
        })

    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'chatbot_ready': chatbot is not None,
        'service': 'Pousada Maori Chatbot'
    })


@app.route('/api/knowledge', methods=['GET'])
def knowledge():
    """Retorna toda a base de conhecimento (para debug)"""
    if not chatbot:
        return jsonify({'error': 'Chatbot não inicializado'}), 500

    return jsonify(chatbot.knowledge)


@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Endpoint não encontrado'}), 404


@app.errorhandler(500)
def internal_error(e):
    return jsonify({'error': 'Erro interno do servidor'}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'

    print(f"\n{'='*60}")
    print(f"🌺 Pousada Maori Chatbot Server")
    print(f"{'='*60}")
    print(f"🚀 Rodando em: http://localhost:{port}")
    print(f"📡 API endpoint: http://localhost:{port}/api/chat")
    print(f"🏥 Health check: http://localhost:{port}/api/health")
    print(f"{'='*60}\n")

    app.run(host='0.0.0.0', port=port, debug=debug)
