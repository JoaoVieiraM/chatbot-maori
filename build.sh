#!/bin/bash
# Build script para Render

echo "📦 Instalando dependências..."
pip install --upgrade pip
pip install wheel

echo "🔧 Instalando spaCy e dependências..."
pip install -r requirements.txt

echo "📥 Baixando modelo português do spaCy..."
python -m spacy download pt_core_news_sm

echo "✅ Build concluído!"
