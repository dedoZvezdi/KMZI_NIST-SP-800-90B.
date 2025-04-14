from itertools import cycle

class VigenereCipherAnalyzer:

    def __init__(self):
        self.results_file = "vigenere_results.txt"

    def vigenere_cipher(self, text: str, key: str, mode: str = 'encrypt') -> str:
        result = []
        key_chars = cycle(key.lower())
        
        for char, key_char in zip(text, key_chars):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key_offset = ord(key_char) - ord('a')
                
                if mode == 'decrypt':
                    new_char = chr((ord(char) - base - key_offset) % 26 + base)
                else:
                    new_char = chr((ord(char) - base + key_offset) % 26 + base)
                result.append(new_char)
            else:
                result.append(char)
        return ''.join(result)

    def interactive_mode(self):
        print("Vigenère Cipher Analyzer")
        print("Commands: 'encrypt', 'decrypt', or 'exit'")
        
        while True:
            choice = input("\nMode (encrypt/decrypt/exit): ").lower().strip()
            
            if choice == 'exit':
                break
                
            if choice not in ('encrypt', 'decrypt'):
                print("Invalid mode! Please try again.")
                continue
                
            try:
                message = input("Enter your message: ")
                key = input("Enter key: ")
                processed = self.vigenere_cipher(message, key, choice)
                print(f"\nResult: {processed}")
                    
            except ValueError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    analyzer = VigenereCipherAnalyzer()
    analyzer.interactive_mode()
