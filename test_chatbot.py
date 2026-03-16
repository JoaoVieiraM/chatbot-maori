"""
Script de teste para o Chatbot Pousada Maori
Testa todas as funcionalidades principais
"""

import sys
from chatbot_engine import MaoriChatbot

def print_separator():
    print("\n" + "="*80 + "\n")

def print_response(question, response_data):
    print(f"👤 Usuário: {question}")
    print(f"🤖 Intenção detectada: {response_data['intent']} (confiança: {response_data['confidence']:.2%})")
    print(f"💬 Resposta:\n{response_data['response']}")
    print_separator()

def main():
    print("🌺 TESTE DO CHATBOT POUSADA MAORI 🌺")
    print_separator()

    # Inicializa chatbot
    try:
        print("⏳ Inicializando chatbot com spaCy...")
        bot = MaoriChatbot()
        print("✅ Chatbot inicializado com sucesso!\n")
    except Exception as e:
        print(f"❌ Erro ao inicializar: {e}")
        print("\n⚠️ Execute antes:")
        print("   pip install -r requirements.txt")
        print("   python -m spacy download pt_core_news_md")
        sys.exit(1)

    print_separator()
    print("🧪 EXECUTANDO TESTES AUTOMÁTICOS")
    print_separator()

    # Testes organizados por categoria
    test_cases = {
        "Saudações": [
            "Olá!",
            "Bom dia",
            "Oi, tudo bem?"
        ],
        "Check-in/Check-out": [
            "Qual o horário do check-in?",
            "Até que horas posso fazer checkout?",
            "Posso chegar depois das 21h?"
        ],
        "Wi-Fi": [
            "Qual a senha do wifi?",
            "Como me conecto na internet?",
            "Tem wi-fi?"
        ],
        "Café da Manhã": [
            "Que horas serve café da manhã?",
            "O café está incluído?",
            "Horário do breakfast"
        ],
        "Quarto": [
            "O quarto tem ar condicionado?",
            "Quais as comodidades do quarto?",
            "Tem TV no quarto?"
        ],
        "Tomadas": [
            "As tomadas são 110 ou 220?",
            "Preciso de adaptador?",
            "Qual a voltagem?"
        ],
        "Piscina": [
            "Qual o horário da piscina?",
            "A piscina está aberta?",
            "Posso usar a piscina?"
        ],
        "Pets": [
            "Aceita cachorro?",
            "Posso trazer meu pet?",
            "Animais são permitidos?"
        ],
        "Praias - Geral": [
            "Quais praias tem perto?",
            "Tem praia próxima?",
            "Onde fica a praia?"
        ],
        "Praias - Específicas": [
            "Me fale sobre Maresias",
            "Como é a praia de Boicucanga?",
            "Qual a distância para Camburi?"
        ],
        "Reservas": [
            "Como faço para reservar novamente?",
            "Onde posso fazer outra reserva?",
            "Quero voltar, como reservo?"
        ],
        "Ajuda": [
            "Ajuda",
            "O que você pode fazer?",
            "Como funciona?"
        ],
        "Despedida": [
            "Obrigado!",
            "Valeu pela ajuda",
            "Tchau"
        ]
    }

    # Estatísticas
    total_tests = sum(len(questions) for questions in test_cases.values())
    successful_tests = 0
    failed_tests = 0

    # Executa testes por categoria
    for category, questions in test_cases.items():
        print(f"📂 Categoria: {category}")
        print("-" * 80)

        for question in questions:
            try:
                response = bot.get_response(question)
                print_response(question, response)

                # Verifica se detectou alguma intenção
                if response['intent'] != 'desconhecido':
                    successful_tests += 1
                else:
                    failed_tests += 1
                    print("⚠️ Não detectou intenção específica")

            except Exception as e:
                print(f"❌ Erro ao processar '{question}': {e}")
                failed_tests += 1
                print_separator()

    # Relatório final
    print("\n")
    print("="*80)
    print("📊 RELATÓRIO DE TESTES")
    print("="*80)
    print(f"Total de testes: {total_tests}")
    print(f"✅ Sucessos: {successful_tests} ({successful_tests/total_tests*100:.1f}%)")
    print(f"❌ Falhas: {failed_tests} ({failed_tests/total_tests*100:.1f}%)")
    print("="*80)

    # Avaliação
    success_rate = successful_tests / total_tests * 100
    if success_rate >= 90:
        print("\n🎉 EXCELENTE! O chatbot está funcionando perfeitamente!")
    elif success_rate >= 70:
        print("\n✅ BOM! O chatbot está funcionando bem, mas pode melhorar.")
    else:
        print("\n⚠️ ATENÇÃO! O chatbot precisa de ajustes.")

    print("\n💡 Dicas:")
    print("   • Chatbot entende variações de perguntas graças ao spaCy")
    print("   • Pode adicionar mais keywords em chatbot_engine.py")
    print("   • Base de conhecimento em knowledge_base.json")

    print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    main()
