# 🌺 Chatbot Pousada Maori - Opção B (NLP com spaCy)

Chatbot inteligente com processamento de linguagem natural para responder todas as dúvidas dos hóspedes da Pousada Maori.

## 🎯 Características

✅ **100% Gratuito** - Sem custos de API ou mensalidades
✅ **Inteligente** - Processamento de linguagem natural com spaCy
✅ **Em Português** - Compreende variações e sinônimos em PT-BR
✅ **Responsivo** - Interface bonita em desktop e mobile
✅ **Fácil Deploy** - Funciona em hospedagem gratuita

## 🧠 Capacidades do Chatbot

O chatbot responde sobre:
- ✅ Check-in e check-out (horários, políticas)
- ✅ Wi-Fi (rede e senha)
- ✅ Café da manhã (horários, inclusão)
- ✅ Comodidades do quarto
- ✅ Tomadas e voltagem
- ✅ Piscina (horários, manutenção)
- ✅ Política de pets
- ✅ **5 praias próximas** com detalhes completos
- ✅ Reservas e Booking.com

### 🏖️ Praias Cobertas
1. **Boicucanga Beach** (450m - 6min a pé)
2. **Brava Beach** (850m - 11min a pé)
3. **Praia de Camburizinho** (2.7km - 8min de carro)
4. **Praia de Camburi** (3.4km - 10min de carro)
5. **Maresias Beach** (6km - 15min de carro)

## 🚀 Instalação e Uso

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### 1. Instalar Dependências

```bash
# Navegue até a pasta do chatbot
cd chatbot

# Instale as dependências
pip install -r requirements.txt

# Baixe o modelo de português do spaCy (IMPORTANTE!)
python -m spacy download pt_core_news_md
```

### 2. Testar o Motor do Chatbot

```bash
# Teste o chatbot diretamente
python chatbot_engine.py
```

Você verá o chatbot respondendo perguntas de teste!

### 3. Rodar o Servidor

```bash
# Inicie o servidor Flask
python app.py
```

Acesse: **http://localhost:5000**

## 📁 Estrutura do Projeto

```
chatbot/
├── knowledge_base.json      # Base de conhecimento completa
├── chatbot_engine.py         # Motor inteligente com spaCy
├── app.py                    # Servidor Flask API
├── requirements.txt          # Dependências Python
├── static/
│   ├── index.html           # Interface do chat
│   ├── style.css            # Estilos (cores da Pousada Maori)
│   └── script.js            # Lógica do frontend
├── README.md                 # Este arquivo
├── .gitignore               # Arquivos a ignorar no Git
├── Procfile                 # Config para Heroku/Render
└── render.yaml              # Config para Render

```

## 🎨 Interface

A interface usa as cores oficiais da Pousada Maori:
- 🔵 Turquesa (#1BB8CE) - Cor principal
- 🔴 Coral (#FF6B6B)
- 🟠 Laranja (#FF9800)
- 🟡 Amarelo (#FFD54F)
- ⚪ Bege (#F5F1E8)

## 🌐 Deploy Gratuito

### Opção 1: Render (Recomendado)

1. Crie conta em [render.com](https://render.com)
2. Clique em "New" → "Web Service"
3. Conecte seu repositório GitHub
4. Configure:
   - **Build Command:** `pip install -r requirements.txt && python -m spacy download pt_core_news_md`
   - **Start Command:** `gunicorn app:app`
   - **Environment:** Python 3
5. Clique em "Create Web Service"

**URL do chatbot:** `https://seu-app.onrender.com`

### Opção 2: Railway

1. Crie conta em [railway.app](https://railway.app)
2. Clique em "New Project" → "Deploy from GitHub"
3. Selecione o repositório
4. Railway detecta automaticamente Python
5. Deploy automático!

**500 horas/mês gratuitas**

### Opção 3: Fly.io

```bash
# Instale Fly CLI
curl -L https://fly.io/install.sh | sh

# Navegue até a pasta
cd chatbot

# Faça login
fly auth login

# Lance o app
fly launch

# Deploy
fly deploy
```

### Opção 4: Heroku

```bash
# Instale Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Crie app
heroku create pousada-maori-chatbot

# Deploy
git push heroku main
```

## 🔗 Integração com o Site React

### Opção A: Widget Flutuante

Adicione ao `src/App.tsx`:

```tsx
// No final do componente App, antes do </div> final
<div className="chatbot-widget">
  <iframe
    src="https://seu-chatbot.onrender.com"
    style={{
      position: 'fixed',
      bottom: '20px',
      right: '20px',
      width: '400px',
      height: '600px',
      border: 'none',
      borderRadius: '20px',
      boxShadow: '0 10px 25px rgba(0,0,0,0.15)',
      zIndex: 9999
    }}
  />
</div>
```

### Opção B: Botão de Chat

Crie um botão que abre o chat em nova aba:

```tsx
<a
  href="https://seu-chatbot.onrender.com"
  target="_blank"
  rel="noopener noreferrer"
  className="chat-button"
>
  💬 Tire suas dúvidas
</a>
```

### Opção C: Seção Dedicada

Adicione uma seção no guia:

```tsx
<section className="chatbot-section">
  <h2>💬 Assistente Virtual</h2>
  <p>Tire suas dúvidas em tempo real!</p>
  <iframe
    src="https://seu-chatbot.onrender.com"
    width="100%"
    height="700px"
    style={{ border: 'none', borderRadius: '20px' }}
  />
</section>
```

## 📱 QR Code para Hóspedes

1. Acesse [qr-code-generator.com](https://www.qr-code-generator.com/)
2. Cole a URL do chatbot: `https://seu-chatbot.onrender.com`
3. Customize:
   - Cor: #1BB8CE (turquesa Maori)
   - Adicione logo da pousada ao centro
   - Texto: "Assistente Virtual Pousada Maori"
4. Baixe em alta resolução
5. Imprima e distribua:
   - Porta de cada quarto
   - Recepção
   - Área da piscina
   - Mesa do café da manhã

## 🧪 Testes

### Testar Localmente

```bash
# Terminal 1: Rode o servidor
python app.py

# Terminal 2: Teste a API
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Qual a senha do wifi?"}'
```

### Testar Health Check

```bash
curl http://localhost:5000/api/health
```

### Perguntas de Teste

Experimente perguntar:
- "Olá!"
- "Qual o horário do check-in?"
- "Qual a senha do Wi-Fi?"
- "Aceita cachorro?"
- "Quais praias tem perto?"
- "Me fale sobre Maresias"
- "Que horas serve café da manhã?"
- "As tomadas são 110 ou 220?"
- "Qual o horário da piscina?"
- "Como faço uma nova reserva?"

## 🛠️ Personalização

### Adicionar Novas Informações

Edite `knowledge_base.json`:

```json
{
  "nova_secao": {
    "titulo": "Informação Nova",
    "detalhes": "Conteúdo aqui"
  }
}
```

### Adicionar Nova Intenção

Edite `chatbot_engine.py`:

```python
'nova_intencao': {
    'keywords': ['palavra1', 'palavra2'],
    'response': self._resposta_nova_intencao
}

def _resposta_nova_intencao(self, user_input: str) -> str:
    return "Sua resposta aqui"
```

## 📊 Monitoramento

### Ver Logs (Render)
```bash
# Acesse o dashboard Render
# Clique no seu serviço → Aba "Logs"
```

### Ver Logs (Railway)
```bash
railway logs
```

### Ver Logs (Heroku)
```bash
heroku logs --tail
```

## ⚙️ Variáveis de Ambiente

Configure no seu provedor de hospedagem:

```bash
DEBUG=False          # Desativa debug em produção
PORT=5000            # Porta do servidor
```

## 🔒 Segurança

- ✅ CORS configurado
- ✅ Validação de entrada
- ✅ Rate limiting (adicionar se necessário)
- ✅ Sem armazenamento de dados pessoais
- ✅ Sem dependência de APIs externas

## 📈 Melhorias Futuras

Possíveis upgrades:
- [ ] Adicionar analytics (quantas perguntas por dia)
- [ ] Suporte a múltiplos idiomas (inglês, espanhol)
- [ ] Histórico de conversas (opcional)
- [ ] Integração com WhatsApp Business
- [ ] Feedback de satisfação após cada resposta
- [ ] Dashboard de admin com estatísticas

## 🐛 Solução de Problemas

### Erro: "Modelo spaCy não encontrado"
```bash
python -m spacy download pt_core_news_md
```

### Erro: "ModuleNotFoundError: No module named 'flask'"
```bash
pip install -r requirements.txt
```

### Chatbot não responde corretamente
- Verifique `knowledge_base.json` está correto
- Teste com `python chatbot_engine.py`
- Veja os logs do servidor

### Deploy falha no Render/Railway
- Verifique se `requirements.txt` está completo
- Confirme comando de build inclui download do spaCy
- Veja logs de build para erros específicos

## 💰 Custos

**R$ 0,00/mês** em todos os cenários:
- ✅ Render: Gratuito para sempre (com algumas limitações)
- ✅ Railway: 500 horas/mês grátis
- ✅ Fly.io: Tier gratuito disponível
- ✅ Sem custos de API

Uso estimado para pousada pequena/média:
- ~100-500 mensagens/dia
- Funciona perfeitamente no plano gratuito

## 📞 Suporte

Problemas? Verifique:
1. `python chatbot_engine.py` funciona?
2. `python app.py` inicia sem erros?
3. Modelo spaCy está instalado?
4. `knowledge_base.json` está válido?

## 🎉 Resultado Final

Um chatbot completo que:
- ✅ Responde 100% das dúvidas dos hóspedes
- ✅ Funciona 24/7 sem intervenção
- ✅ Interface linda e profissional
- ✅ Inteligente com NLP
- ✅ Gratuito para sempre
- ✅ Fácil de manter e atualizar

---

**Desenvolvido com ❤️ para a Pousada Maori**
**Versão:** 1.0.0 (Opção B - spaCy)
**Data:** Março 2026
