# 🚀 Guia Rápido - Chatbot Pousada Maori

## ⚡ Instalação Rápida (5 minutos)

### 1. Instale as dependências
```bash
cd chatbot
pip install -r requirements.txt
python -m spacy download pt_core_news_md
```

### 2. Rode o chatbot
```bash
python app.py
```

### 3. Abra no navegador
```
http://localhost:5000
```

**Pronto! O chatbot está funcionando! 🎉**

---

## 🌐 Deploy Rápido em Render (10 minutos)

### 1. Crie conta gratuita
- Acesse: https://render.com
- Clique em "Get Started"
- Faça login com GitHub

### 2. Suba seu código para GitHub
```bash
cd chatbot
git init
git add .
git commit -m "Chatbot Pousada Maori"
git remote add origin https://github.com/SEU-USUARIO/chatbot-maori.git
git push -u origin main
```

### 3. Deploy no Render
1. No Render, clique em "New" → "Web Service"
2. Conecte seu repositório GitHub
3. Preencha:
   - **Name:** `pousada-maori-chatbot`
   - **Build Command:** `pip install -r requirements.txt && python -m spacy download pt_core_news_md`
   - **Start Command:** `gunicorn app:app`
4. Clique em "Create Web Service"

**Aguarde 5-10 minutos...**

### 4. Acesse seu chatbot!
```
https://pousada-maori-chatbot.onrender.com
```

---

## 💬 Teste Rápido

Pergunte ao chatbot:
- "Qual a senha do Wi-Fi?"
- "Quais praias tem perto?"
- "Aceita pets?"
- "Que horas serve café?"

---

## 📱 Criar QR Code

1. Acesse: https://www.qr-code-generator.com/
2. Cole a URL do seu chatbot
3. Baixe o QR Code
4. Imprima e coloque nos quartos!

---

## 🎨 Integrar ao Site React

Adicione ao seu `src/App.tsx`:

```tsx
{/* Botão flutuante do chatbot */}
<a
  href="https://pousada-maori-chatbot.onrender.com"
  target="_blank"
  className="fixed bottom-6 right-6 bg-maori-turquoise text-white px-6 py-4 rounded-full shadow-lg hover:shadow-xl transition-all"
>
  💬 Assistente Virtual
</a>
```

---

## ❓ Problemas?

**Erro ao instalar spaCy:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download pt_core_news_md
```

**Chatbot não responde:**
- Verifique se o servidor está rodando
- Abra o console do navegador (F12) para ver erros
- Teste a API: `curl http://localhost:5000/api/health`

**Deploy falhou:**
- Veja os logs no dashboard do Render
- Verifique se todos os arquivos foram commitados
- Confirme que `requirements.txt` está presente

---

## ✅ Checklist de Sucesso

- [ ] Chatbot funciona localmente
- [ ] Testa pelo menos 5 perguntas diferentes
- [ ] Deploy feito com sucesso
- [ ] URL do chatbot funciona
- [ ] QR Code criado
- [ ] QR Code impresso e distribuído
- [ ] (Opcional) Integrado ao site React

---

**Parabéns! Seu chatbot está no ar! 🎉**

Se tiver dúvidas, consulte o `README.md` completo.
