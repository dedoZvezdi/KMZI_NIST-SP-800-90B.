import os
from collections import Counter

ENGLISH_FREQ = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702,
    'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153,
    'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507,
    'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056,
    'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074
}

BIGRAMS = {'th': 1.52, 'he': 1.28, 'in': 0.94, 'er': 0.94, 'an': 0.82}
TRIGRAMS = {'the': 1.81, 'and': 0.73, 'ing': 0.72, 'ent': 0.42, 'ion': 0.42}

COMMON_WORDS = {
    'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i',
    'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at',
    'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she',
    'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what',
    'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me',
    'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take',
    'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see',
    'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over',
    'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work',
    'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these',
    'give', 'day', 'most', 'us', 'hello', 'world'
}

def caesar_cipher(text: str, shift: int, mode: str) -> str:
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'decrypt':
                new_char = chr((ord(char) - base - shift) % 26 + base)
            else:
                new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

def calculate_score(text: str) -> float:
    text_lower = text.lower()
    
    letter_score = sum(ENGLISH_FREQ.get(char, 0) for char in text_lower if char in ENGLISH_FREQ)
    
    words = text_lower.split()
    word_score = sum(50 for word in words if word in COMMON_WORDS) 
    
    bigram_score = sum(20 for i in range(len(text_lower)-1) 
                   if text_lower[i:i+2] in BIGRAMS)
    trigram_score = sum(30 for i in range(len(text_lower)-2)
                    if text_lower[i:i+3] in TRIGRAMS)
    
    length_bonus = len(text) * 0.5 if any(word in COMMON_WORDS for word in words) else 0
    
    return letter_score + word_score + bigram_score + trigram_score + length_bonus

def brute_force_decrypt(ciphertext: str) -> tuple:
    candidates = []
    
    for shift in range(1, 26):
        decrypted = caesar_cipher(ciphertext, shift, 'decrypt')
        score = calculate_score(decrypted)
        candidates.append((score, shift, decrypted))
    
    candidates.sort(reverse=True, key=lambda x: x[0])
    
    with open("caesar_results.txt", "w") as f:
        for score, shift, text in candidates:
            f.write(f"Shift {shift:2d}: {text} (score: {score:.1f})\n")
    
    return candidates[0]  

def main():
    print("Advanced Caesar Cipher Breaker")
    print("Type 'encrypt', 'decrypt', 'bruteforce', or 'exit'")
    
    while True:
        choice = input("\nMode (encrypt/decrypt/bruteforce/exit): ").lower().strip()
        
        if choice == 'exit':
            print("Exiting the program. Goodbye!")
            break
            
        if choice not in ('encrypt', 'decrypt', 'bruteforce'):
            print("Invalid mode! Please try again.")
            continue
            
        try:
            message = input("Enter your message: ")
            
            if choice == 'bruteforce':
                score, shift, decrypted = brute_force_decrypt(message)
                print(f"\nDecryption Result:")
                print(f"Shift: {shift}")
                print(f"Text: {decrypted}")
                print(f"Confidence: {score:.1f}")
                print("All attempts saved to 'caesar_results.txt'")
                
                print("\nTop 3 Candidates:")
                with open("caesar_results.txt") as f:
                    for i, line in enumerate(f):
                        if i < 3:
                            print(line.strip())
                        else:
                            break
            else:
                shift = int(input("Enter shift value (integer): "))
                processed = caesar_cipher(message, shift, choice)
                print(f"\nResult: {processed}")
                
        except ValueError:
            print("Error: Shift must be an integer!")

if __name__ == "__main__":
    main()