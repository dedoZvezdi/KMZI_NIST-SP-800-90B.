import math
from collections import Counter
import zlib
import numpy as np

def calculate_min_entropy(text: str) -> float:

    filtered_text = [c.lower() for c in text if c.isalpha()]
    if not filtered_text:
        return 0.0
    
    counts = Counter(filtered_text)
    total_chars = len(filtered_text)
    max_prob = max(counts.values()) / total_chars
    return -math.log2(max_prob) if max_prob > 0 else 0.0

def calculate_shannon_entropy(text: str) -> float:

    filtered_text = [c.lower() for c in text if c.isalpha()]
    if not filtered_text:
        return 0.0
    
    counts = Counter(filtered_text)
    total_chars = len(filtered_text)
    entropy = 0.0
    
    for count in counts.values():
        p = count / total_chars
        if p > 0:  
            entropy -= p * math.log2(p)
        
    return entropy

def markov_test(text: str) -> float:

    filtered_text = [c.lower() for c in text if c.isalpha()]
    if len(filtered_text) < 2:
        return 0.0
    
    transitions = 0
    for i in range(len(filtered_text) - 1):
        if filtered_text[i] != filtered_text[i+1]:
            transitions += 1
            
    return transitions / (len(filtered_text) - 1)

def compression_test(text: str) -> float:

    text_bytes = text.encode('utf-8')
    if not text_bytes:
        return 0.0
    compressed = zlib.compress(text_bytes)
    return len(compressed) / len(text_bytes)

def analyze_entropy(text: str, label: str = "Text"):

    filtered_text = [c.lower() for c in text if c.isalpha()]
    unique_chars = set(filtered_text)
    
    print(f"\n{label} Entropy Analysis:")
    print("-" * 40)
    print(f"Min-Entropy: {calculate_min_entropy(text):.4f} bits")
    print(f"Shannon Entropy: {calculate_shannon_entropy(text):.4f} bits")
    print(f"Markov Test Score: {markov_test(text):.4f} (1.0 = perfect)")
    print(f"Compression Ratio: {compression_test(text):.4f} (the smaller the better)")
    print(f"Unique Chars: {len(unique_chars)}")
    print(f"Total Chars: {len(filtered_text)}")
    
    if filtered_text:
        counts = Counter(filtered_text)
        print("\nMost common letters")
        for char, count in counts.most_common(5):
            freq = count / len(filtered_text) * 100
            print(f"'{char}': {count} ({freq:.1f}%)")

def main():
    plaintext = "The quick brown fox jumps over the lazy dog"
    caesar_cipher = "Wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj"
    vigenere_cipher = "Tik qwecm fhrzq ioc jxmpw ohrn tik lasb doj"
    random_text = "Xqjwkv yfphz bldgs mci rntao vxue xqj hzwy nkt"

    repetitive = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    alternating = "ABABABABABABABABABABABABABABABABABABABAB"
    long_english = """
    This is a much longer sample of English text. It contains many different words
    and should therefore have a character frequency distribution similar to regular
    English. The longer the text, the more reliable the statistical analysis will be
    for comparisons between different encryption methods and texts.
    """

    analyze_entropy(plaintext, "plaintext")
    analyze_entropy(caesar_cipher, "caesar_cipher")
    analyze_entropy(vigenere_cipher, "vigenere_cipher")
    analyze_entropy(random_text, "random_text")
    analyze_entropy(repetitive, "repetitive")
    analyze_entropy(alternating, "alternating")
    analyze_entropy(long_english, "long_english")

if __name__ == "__main__":
    main()