# 🔗 Como Integrar o Chatbot ao Site React da Pousada Maori

## 🎯 3 Opções de Integração

### Opção 1: Botão Flutuante (Recomendado) ⭐

Adiciona um botão fixo no canto inferior direito que abre o chat em nova aba.

#### Passo 1: Adicione ao `src/App.tsx`

```tsx
function App() {
  // ... código existente ...

  return (
    <div className="min-h-screen bg-gradient-to-br from-maori-beige via-white to-maori-turquoise/10">
      <Hero />

      {/* ... resto do código ... */}

      <Footer />

      {/* ADICIONE AQUI - Botão flutuante do chatbot */}
      <a
        href="https://SEU-CHATBOT.onrender.com"
        target="_blank"
        rel="noopener noreferrer"
        className="fixed bottom-6 right-6 bg-maori-turquoise hover:bg-maori-coral text-white font-bold px-6 py-4 rounded-full shadow-2xl hover:shadow-3xl transition-all duration-300 flex items-center gap-2 z-50 group"
      >
        <span className="text-2xl">💬</span>
        <span className="hidden sm:inline">Assistente Virtual</span>
        <motion.div
          animate={{ scale: [1, 1.2, 1] }}
          transition={{ repeat: Infinity, duration: 2 }}
          className="absolute -top-1 -right-1 w-3 h-3 bg-green-400 rounded-full"
        />
      </a>
    </div>
  );
}
```

**Resultado:** Botão flutuante sempre visível! 🎈

---

### Opção 2: Widget Incorporado (iframe)

Incorpora o chatbot diretamente na página.

#### Passo 1: Crie componente `src/components/ChatWidget.tsx`

```tsx
import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { FaTimes, FaComments } from 'react-icons/fa';

const ChatWidget = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      {/* Botão para abrir */}
      {!isOpen && (
        <motion.button
          onClick={() => setIsOpen(true)}
          className="fixed bottom-6 right-6 bg-maori-turquoise hover:bg-maori-coral text-white p-4 rounded-full shadow-2xl z-50"
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.9 }}
        >
          <FaComments className="text-3xl" />
        </motion.button>
      )}

      {/* Widget do chat */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, y: 100, scale: 0.8 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 100, scale: 0.8 }}
            className="fixed bottom-6 right-6 w-[400px] h-[600px] bg-white rounded-2xl shadow-2xl z-50 overflow-hidden"
          >
            {/* Header do widget */}
            <div className="bg-maori-turquoise text-white p-4 flex items-center justify-between">
              <div className="flex items-center gap-3">
                <FaComments className="text-2xl" />
                <div>
                  <h3 className="font-bold">Assistente Virtual</h3>
                  <p className="text-xs opacity-90">Pousada Maori</p>
                </div>
              </div>
              <button
                onClick={() => setIsOpen(false)}
                className="hover:bg-white/20 p-2 rounded-lg transition-colors"
              >
                <FaTimes />
              </button>
            </div>

            {/* iframe do chatbot */}
            <iframe
              src="https://SEU-CHATBOT.onrender.com"
              className="w-full h-[calc(100%-64px)] border-none"
              title="Chatbot Pousada Maori"
            />
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
};

export default ChatWidget;
```

#### Passo 2: Adicione ao `src/App.tsx`

```tsx
import ChatWidget from './components/ChatWidget';

function App() {
  return (
    <div className="...">
      {/* ... código existente ... */}

      {/* Adicione antes do </div> final */}
      <ChatWidget />
    </div>
  );
}
```

**Resultado:** Widget que abre/fecha com animação! ✨

---

### Opção 3: Seção Dedicada na Página

Adiciona uma seção completa no guia com o chatbot incorporado.

#### Adicione ao `src/App.tsx` (antes do Footer)

```tsx
{/* Seção do Chatbot */}
<motion.div
  className="max-w-6xl mx-auto px-4 py-16 sm:px-6 lg:px-8"
  initial={{ opacity: 0, y: 30 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true }}
  transition={{ duration: 0.6 }}
>
  <div className="text-center mb-10">
    <div className="text-6xl mb-4">💬</div>
    <h2 className="text-4xl font-display font-bold text-maori-dark mb-4">
      Assistente Virtual 24/7
    </h2>
    <p className="text-lg text-gray-600 max-w-2xl mx-auto">
      Tire suas dúvidas em tempo real! Nosso assistente está sempre disponível para ajudar.
    </p>
  </div>

  <div className="bg-white rounded-2xl shadow-2xl overflow-hidden border-2 border-maori-turquoise">
    <iframe
      src="https://SEU-CHATBOT.onrender.com"
      className="w-full h-[700px] border-none"
      title="Chatbot Pousada Maori"
    />
  </div>
</motion.div>
```

**Resultado:** Seção completa dedicada ao chatbot! 📱

---

## 📱 Card de "Fale Conosco" com Link

Adicione um card ao grid de informações:

```tsx
<InfoCard
  icon={<FaComments />}
  title="Assistente Virtual"
  color="turquoise"
  highlight={true}
  items={[
    "Disponível 24 horas por dia",
    "Respostas instantâneas",
    "Informações sobre praias, check-in, Wi-Fi e muito mais!"
  ]}
  link="https://SEU-CHATBOT.onrender.com"
/>
```

---

## 🎨 Estilos Adicionais

Se usar o botão flutuante, adicione ao `src/App.css`:

```css
/* Botão flutuante do chatbot */
.chatbot-fab {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 9999;
  box-shadow: 0 8px 16px rgba(27, 184, 206, 0.3);
}

.chatbot-fab:hover {
  box-shadow: 0 12px 24px rgba(27, 184, 206, 0.4);
  transform: translateY(-2px);
}

/* Responsivo */
@media (max-width: 640px) {
  .chatbot-fab {
    bottom: 16px;
    right: 16px;
  }
}
```

---

## 🔄 Substituir URL do Chatbot

**IMPORTANTE:** Substitua `https://SEU-CHATBOT.onrender.com` pela URL real do seu chatbot após o deploy!

Exemplo:
- Deploy no Render: `https://pousada-maori-chatbot.onrender.com`
- Deploy no Railway: `https://pousada-maori-chatbot.up.railway.app`
- Deploy no Fly.io: `https://pousada-maori-chatbot.fly.dev`

---

## 📊 Comparação das Opções

| Opção | Vantagens | Desvantagens | Recomendado Para |
|-------|-----------|--------------|------------------|
| **Botão Flutuante** | Sempre visível, não invasivo | Abre nova aba | Acesso rápido |
| **Widget Incorporado** | Experiência integrada | Mais complexo | UX premium |
| **Seção Dedicada** | Destaque total | Usuário precisa rolar | Chatbot como feature principal |
| **Card no Grid** | Simples e consistente | Menos destaque | Integração sutil |

---

## 🚀 Recomendação Final

**Para a Pousada Maori, recomendo:**

1. **Opção 1 (Botão Flutuante)** - Principal
   - Sempre acessível
   - Não atrapalha navegação
   - Fácil de implementar

2. **+ Opção 4 (Card no Grid)** - Complementar
   - Adiciona card "Assistente Virtual" nas informações
   - Reforça a presença do chatbot

**Resultado:** Usuários veem o chatbot em dois lugares - no card de informações E no botão flutuante! 🎯

---

## ✅ Checklist de Integração

- [ ] Chatbot deployado e funcionando
- [ ] URL do chatbot anotada
- [ ] Escolhida opção de integração
- [ ] Código adicionado ao App.tsx
- [ ] URL substituída no código
- [ ] Testado em desktop
- [ ] Testado em mobile
- [ ] Build do React funciona
- [ ] Deploy do site atualizado

---

## 🎉 Pronto!

Seu guia digital agora tem um **assistente virtual inteligente** integrado! 🤖

Os hóspedes podem tirar dúvidas sobre:
- ✅ Check-in/Check-out
- ✅ Wi-Fi e senha
- ✅ Praias próximas
- ✅ Café da manhã
- ✅ E muito mais!

**Tudo isso 24/7, sem custo adicional!** 🌺
