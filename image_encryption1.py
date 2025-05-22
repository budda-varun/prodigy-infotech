from PIL import Image
import os
def encrypt_decrypt_image(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            img = img.convert('RGB') 
            pixels = img.load()
            width, height = img.size
            for x in range(width):
                for y in range(height):
                    r, g, b = pixels[x, y]
                    # Invert each color channel (simple reversible operation)
                    pixels[x, y] = (255 - r, 255 - g, 255 - b)
            img.save(output_path)
            print(f"Image saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")
def main():
    print(" Simple Image Encryption Tool")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice.")
        return
    input_path = input("Enter the path to the image file: ").strip()
    if not os.path.isfile(input_path):
        print("File does not exist.")
        return
    if choice == 'e':
        output_path = "encrypted_image.png"
    else:
        output_path = "decrypted_image.png"
    encrypt_decrypt_image(input_path, output_path)
if __name__ == "__main__":
    main()
