# 🖼️ Compress Image to 70KB (Python)

Este script em Python permite **redimensionar e comprimir imagens** até que o arquivo tenha no máximo **70 KB**, preservando ao máximo a qualidade.

---

## 🔧 Como funciona

- Reduz a **resolução da imagem** mantendo a proporção.
- Converte imagens `PNG`, `RGBA`, `P` para `JPEG`.
- Ajusta automaticamente a **qualidade de compressão** para atingir o tamanho-alvo.

---

## 📥 Requisitos

- Python 3.7 ou superior
- Pillow

Instale o Pillow com:

bash
pip install pillow

---

## 📌 Modo de uso
1. 📁 Coloque a imagem que deseja comprimir na mesma pasta do arquivo compress_to_70kb.py.

2. ✏️ Abra o arquivo compress_to_70kb.py e edite a seguinte linha no final:
   caminho_imagem = "sua_imagem.jpg"
3. ▶️ Execute o script no terminal (VS Code ou outro terminal Python):
    python compress_to_70kb.py

