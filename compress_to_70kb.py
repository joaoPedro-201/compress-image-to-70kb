from PIL import Image
import os

def resize_and_compress(input_path, output_path='compressed.jpg', max_size_kb=70, max_width=800, max_height=800):
    if not os.path.exists(input_path):
        print(f"❌ Arquivo '{input_path}' não encontrado.")
        return

    img = Image.open(input_path)

    img.thumbnail((max_width, max_height))

    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    for quality in range(95, 10, -5):
        img.save(output_path, format='JPEG', quality=quality, optimize=True)
        size_kb = os.path.getsize(output_path) / 1024
        print(f"Tentando qualidade={quality}: {size_kb:.2f} KB")
        if size_kb <= max_size_kb:
            print(f"✅ Sucesso: imagem salva com {size_kb:.2f} KB")
            return

    print("⚠️ Não foi possível atingir 70 KB sem perder muita qualidade.")

# Exemplo de uso
if __name__ == "__main__":
    caminho_imagem = "minha_imagem.jpeg"  # coloque o nome da imagem aqui
    resize_and_compress(caminho_imagem)
