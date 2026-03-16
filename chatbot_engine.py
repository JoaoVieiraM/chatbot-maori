"""
Pousada Maori Chatbot Engine - Opção B (NLP com spaCy)
Motor inteligente de chatbot com processamento de linguagem natural
"""

import json
import spacy
from datetime import datetime
from unidecode import unidecode
from typing import Dict, List, Tuple, Optional


class MaoriChatbot:
    def __init__(self, knowledge_base_path: str = 'knowledge_base.json'):
        """Inicializa o chatbot com spaCy e base de conhecimento"""
        # Carrega modelo português do spaCy
        try:
            self.nlp = spacy.load('pt_core_news_md')
        except OSError:
            print("⚠️ Modelo spaCy não encontrado. Execute: python -m spacy download pt_core_news_md")
            raise

        # Carrega base de conhecimento
        with open(knowledge_base_path, 'r', encoding='utf-8') as f:
            self.knowledge = json.load(f)

        # Define intenções e seus padrões
        self.intents = {
            'saudacao': {
                'keywords': ['oi', 'olá', 'ola', 'bom dia', 'boa tarde', 'boa noite', 'hello', 'hi'],
                'response': self._resposta_saudacao
            },
            'despedida': {
                'keywords': ['tchau', 'adeus', 'até logo', 'ate logo', 'valeu', 'obrigado', 'obrigada', 'bye'],
                'response': self._resposta_despedida
            },
            'checkin': {
                'keywords': ['check-in', 'checkin', 'check in', 'entrada', 'chegar', 'chegada', 'horário de entrada'],
                'response': self._resposta_checkin
            },
            'checkout': {
                'keywords': ['check-out', 'checkout', 'check out', 'saída', 'saida', 'sair', 'horário de saída'],
                'response': self._resposta_checkout
            },
            'wifi': {
                'keywords': ['wifi', 'wi-fi', 'internet', 'senha', 'rede', 'conexão', 'conexao', 'wi fi'],
                'response': self._resposta_wifi
            },
            'cafe': {
                'keywords': ['café', 'cafe', 'café da manhã', 'cafe da manha', 'breakfast', 'almoço', 'almoco', 'comida'],
                'response': self._resposta_cafe
            },
            'quarto': {
                'keywords': ['quarto', 'comodidades', 'tv', 'frigobar', 'ar condicionado', 'ar-condicionado', 'banheiro'],
                'response': self._resposta_quarto
            },
            'tomadas': {
                'keywords': ['tomada', 'voltagem', 'energia', 'volt', '110', '220', 'adaptador'],
                'response': self._resposta_tomadas
            },
            'piscina': {
                'keywords': ['piscina', 'natação', 'natacao', 'nadar', 'pool'],
                'response': self._resposta_piscina
            },
            'pets': {
                'keywords': ['pet', 'cachorro', 'gato', 'animal', 'animais', 'estimação', 'estimacao', 'dog', 'cat'],
                'response': self._resposta_pets
            },
            'praias': {
                'keywords': ['praia', 'beach', 'mar', 'areia', 'boicucanga', 'brava', 'camburizinho', 'camburi', 'maresias'],
                'response': self._resposta_praias
            },
            'reserva': {
                'keywords': ['reserva', 'booking', 'reservar', 'próxima vez', 'proxima vez', 'voltar'],
                'response': self._resposta_reserva
            },
            'ajuda': {
                'keywords': ['ajuda', 'help', 'o que você faz', 'o que voce faz', 'como funciona'],
                'response': self._resposta_ajuda
            }
        }

    def normalize_text(self, text: str) -> str:
        """Normaliza texto removendo acentos e convertendo para minúsculas"""
        return unidecode(text.lower().strip())

    def detect_intent(self, user_input: str) -> Tuple[Optional[str], float]:
        """
        Detecta a intenção do usuário usando spaCy e similaridade semântica
        Retorna (intent_name, confidence_score)
        """
        # Processa texto com spaCy
        doc = self.nlp(user_input.lower())

        # Normaliza para busca por keywords
        normalized = self.normalize_text(user_input)

        # Primeiro: busca direta por keywords (alta confiança)
        for intent_name, intent_data in self.intents.items():
            for keyword in intent_data['keywords']:
                if self.normalize_text(keyword) in normalized:
                    return intent_name, 0.95

        # Segundo: similaridade semântica com spaCy
        best_match = None
        best_score = 0.0

        for intent_name, intent_data in self.intents.items():
            for keyword in intent_data['keywords']:
                keyword_doc = self.nlp(keyword)
                similarity = doc.similarity(keyword_doc)

                if similarity > best_score:
                    best_score = similarity
                    best_match = intent_name

        # Retorna melhor match se confiança > 0.6
        if best_score > 0.6:
            return best_match, best_score

        return None, 0.0

    def extract_beach_name(self, user_input: str) -> Optional[str]:
        """Extrai nome de praia da pergunta do usuário"""
        normalized = self.normalize_text(user_input)

        beach_names = {
            'boicucanga': 'Boicucanga Beach',
            'brava': 'Brava Beach',
            'camburizinho': 'Praia de Camburizinho',
            'camburi': 'Praia de Camburi',
            'maresias': 'Maresias Beach'
        }

        for key, full_name in beach_names.items():
            if key in normalized:
                return full_name

        return None

    def get_response(self, user_input: str) -> Dict[str, any]:
        """
        Processa entrada do usuário e retorna resposta
        """
        # Detecta intenção
        intent, confidence = self.detect_intent(user_input)

        # Se não detectou intenção, retorna mensagem padrão
        if not intent:
            return {
                'intent': 'desconhecido',
                'confidence': 0.0,
                'response': self._resposta_desconhecida()
            }

        # Executa função de resposta da intenção
        response_func = self.intents[intent]['response']
        response_text = response_func(user_input)

        return {
            'intent': intent,
            'confidence': confidence,
            'response': response_text
        }

    # ===== FUNÇÕES DE RESPOSTA =====

    def _resposta_saudacao(self, user_input: str) -> str:
        """Resposta para saudações"""
        hora = datetime.now().hour

        if 5 <= hora < 12:
            saudacao = "Bom dia"
        elif 12 <= hora < 18:
            saudacao = "Boa tarde"
        else:
            saudacao = "Boa noite"

        return f"{saudacao}! 🌺 Bem-vindo à Pousada Maori!\n\n" \
               f"Sou o assistente virtual e estou aqui para ajudar com qualquer dúvida sobre sua estadia.\n\n" \
               f"Você pode me perguntar sobre:\n" \
               f"• Check-in e check-out\n" \
               f"• Wi-Fi e senha\n" \
               f"• Café da manhã\n" \
               f"• Comodidades do quarto\n" \
               f"• Praias próximas\n" \
               f"• Piscina e outras facilidades\n\n" \
               f"Como posso ajudar? 😊"

    def _resposta_despedida(self, user_input: str) -> str:
        """Resposta para despedidas"""
        return "Foi um prazer ajudar! 🌺\n\n" \
               "Aproveite sua estadia na Pousada Maori!\n" \
               "Se precisar de algo, estou sempre por aqui. 😊\n\n" \
               "Até logo!"

    def _resposta_checkin(self, user_input: str) -> str:
        """Resposta sobre check-in"""
        data = self.knowledge['checkin']
        return f"📅 **Check-in - Pousada Maori**\n\n" \
               f"🕐 Horário: {data['horario']}\n\n" \
               f"⚠️ Importante: {data['observacao']}\n\n" \
               f"Ao chegar, dirija-se à recepção com seu documento de identidade.\n" \
               f"Será um prazer recebê-lo!"

    def _resposta_checkout(self, user_input: str) -> str:
        """Resposta sobre check-out"""
        data = self.knowledge['checkout']
        return f"📅 **Check-out - Pousada Maori**\n\n" \
               f"🕐 Horário: {data['horario']}\n\n" \
               f"📝 Instrução: {data['instrucao']}\n\n" \
               f"Esperamos que tenha aproveitado sua estadia! 🌺"

    def _resposta_wifi(self, user_input: str) -> str:
        """Resposta sobre Wi-Fi"""
        data = self.knowledge['wifi']
        return f"📶 **Wi-Fi - Pousada Maori**\n\n" \
               f"🌐 Nome da rede: **{data['rede']}**\n" \
               f"🔑 Senha: **{data['senha']}**\n\n" \
               f"✅ {data['disponibilidade']}\n\n" \
               f"Boa navegação! 💻"

    def _resposta_cafe(self, user_input: str) -> str:
        """Resposta sobre café da manhã"""
        data = self.knowledge['cafe_manha']
        return f"☕ **Café da Manhã - Pousada Maori**\n\n" \
               f"🕐 Horário: {data['horario']}\n" \
               f"📍 Local: {data['local']}\n\n" \
               f"⚠️ **Importante:** {data['importante']}\n\n" \
               f"Se o café da manhã não estiver incluído na sua reserva, " \
               f"você pode adicioná-lo na recepção.\n\n" \
               f"Bom apetite! 🥐🍳"

    def _resposta_quarto(self, user_input: str) -> str:
        """Resposta sobre comodidades do quarto"""
        comodidades = self.knowledge['quarto']['comodidades']
        lista = '\n'.join([f"✅ {item}" for item in comodidades])

        return f"🛏️ **Comodidades do Quarto**\n\n" \
               f"{lista}\n\n" \
               f"Tudo para garantir seu conforto durante a estadia! 🌺"

    def _resposta_tomadas(self, user_input: str) -> str:
        """Resposta sobre tomadas"""
        data = self.knowledge['tomadas']
        return f"⚡ **Tomadas - Pousada Maori**\n\n" \
               f"🔌 {data['aviso']}\n\n" \
               f"Caso seus aparelhos sejam 110V, certifique-se de trazer " \
               f"um adaptador ou transformador de voltagem."

    def _resposta_piscina(self, user_input: str) -> str:
        """Resposta sobre piscina"""
        data = self.knowledge['piscina']
        return f"🏊 **Piscina - Pousada Maori**\n\n" \
               f"🕐 Horário: {data['horario']}\n\n" \
               f"💡 {data['observacao']}\n\n" \
               f"Aproveite! 🌊"

    def _resposta_pets(self, user_input: str) -> str:
        """Resposta sobre pets"""
        data = self.knowledge['pets']
        return f"🐾 **Política de Pets**\n\n" \
               f"{data['mensagem']}"

    def _resposta_praias(self, user_input: str) -> str:
        """Resposta sobre praias"""
        # Tenta identificar praia específica
        beach_name = self.extract_beach_name(user_input)

        if beach_name:
            # Resposta sobre praia específica
            for praia in self.knowledge['praias']:
                if praia['nome'] == beach_name:
                    tempo = praia['tempo_pe'] if praia['tempo_pe'] else praia['tempo_carro']

                    return f"🏖️ **{praia['nome']}**\n\n" \
                           f"📍 Distância: {praia['distancia']}\n" \
                           f"⏱️ Tempo: {tempo}\n\n" \
                           f"**Perfil:** {praia['perfil']}\n\n" \
                           f"🌊 **Mar:** {praia['mar']}\n\n" \
                           f"⭐ **Destaque:** {praia['destaque']}\n\n" \
                           f"🎯 **Atividades:** {praia['atividades']}\n\n" \
                           f"🏪 **Infraestrutura:** {praia['infraestrutura']}"

        # Resposta geral sobre praias
        praias_texto = ""
        for i, praia in enumerate(self.knowledge['praias'], 1):
            tempo = praia['tempo_pe'] if praia['tempo_pe'] else praia['tempo_carro']
            praias_texto += f"\n{i}. **{praia['nome']}**\n   📍 {praia['distancia']} - {tempo}\n"

        return f"🏖️ **Praias Próximas à Pousada Maori**\n" \
               f"{praias_texto}\n" \
               f"💡 Pergunte sobre uma praia específica para mais detalhes!\n" \
               f"Exemplo: 'Me fale sobre Maresias'"

    def _resposta_reserva(self, user_input: str) -> str:
        """Resposta sobre reservas"""
        data = self.knowledge['reservas']
        return f"📅 **Reservas - Pousada Maori**\n\n" \
               f"{data['mensagem']}\n\n" \
               f"🔗 Link: {data['url']}\n\n" \
               f"Esperamos recebê-lo novamente! 🌺"

    def _resposta_ajuda(self, user_input: str) -> str:
        """Resposta sobre ajuda"""
        return f"❓ **Como posso ajudar?**\n\n" \
               f"Sou o assistente virtual da Pousada Maori! Posso responder sobre:\n\n" \
               f"🏨 **Hospedagem:**\n" \
               f"• Check-in e check-out\n" \
               f"• Comodidades do quarto\n" \
               f"• Tomadas e voltagem\n\n" \
               f"🌐 **Serviços:**\n" \
               f"• Wi-Fi (rede e senha)\n" \
               f"• Café da manhã\n" \
               f"• Piscina\n\n" \
               f"🏖️ **Turismo:**\n" \
               f"• Praias próximas\n" \
               f"• Distâncias e como chegar\n\n" \
               f"📋 **Políticas:**\n" \
               f"• Pets\n" \
               f"• Reservas\n\n" \
               f"Pode perguntar à vontade! 😊"

    def _resposta_desconhecida(self) -> str:
        """Resposta quando não entende a pergunta"""
        return f"🤔 Desculpe, não entendi sua pergunta.\n\n" \
               f"Tente perguntar sobre:\n" \
               f"• Check-in ou check-out\n" \
               f"• Wi-Fi e senha\n" \
               f"• Café da manhã\n" \
               f"• Praias próximas\n" \
               f"• Comodidades do quarto\n" \
               f"• Piscina\n\n" \
               f"Ou digite 'ajuda' para ver tudo que posso fazer! 😊"


# Teste do chatbot (executar diretamente este arquivo)
if __name__ == "__main__":
    print("🌺 Testando Chatbot Pousada Maori (Opção B - spaCy)\n")

    try:
        bot = MaoriChatbot()
        print("✅ Chatbot inicializado com sucesso!\n")
        print("=" * 60)

        # Testes
        test_questions = [
            "Olá!",
            "Qual o horário do check-in?",
            "Qual a senha do wifi?",
            "Aceita cachorro?",
            "Quais praias tem perto?",
            "Me fale sobre Maresias",
            "Que horas serve café da manhã?",
            "As tomadas são 110 ou 220?",
        ]

        for question in test_questions:
            print(f"\n👤 Usuário: {question}")
            response = bot.get_response(question)
            print(f"🤖 Bot (confiança: {response['confidence']:.2f}):\n{response['response']}")
            print("-" * 60)

    except Exception as e:
        print(f"❌ Erro: {e}")
        print("\n⚠️ Certifique-se de instalar o modelo spaCy:")
        print("   pip install -r requirements.txt")
        print("   python -m spacy download pt_core_news_md")
