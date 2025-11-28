import streamlit as st
import string
from typing import Dict
import plotly.graph_objects as go

# Page config
st.set_page_config(
    page_title="🔐 Classical Ciphers Lab",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CIPHER IMPLEMENTATIONS
# ============================================================

class CaesarCipher:
    """Caesar cipher implementation."""
    
    def __init__(self, shift=3):
        self.shift = shift % 26
    
    def encrypt(self, text):
        result = []
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result.append(chr((ord(char) - ord('A') + self.shift) % 26 + ord('A')))
                else:
                    result.append(chr((ord(char) - ord('a') + self.shift) % 26 + ord('a')))
            else:
                result.append(char)
        return ''.join(result)
    
    def decrypt(self, text):
        result = []
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result.append(chr((ord(char) - ord('A') - self.shift) % 26 + ord('A')))
                else:
                    result.append(chr((ord(char) - ord('a') - self.shift) % 26 + ord('a')))
            else:
                result.append(char)
        return ''.join(result)
    
    def brute_force(self, text):
        results = {}
        for shift in range(26):
            self.shift = shift
            results[shift] = self.decrypt(text)
        return results


class VigenereCipher:
    """Vigenere cipher implementation."""
    
    def __init__(self, key="SECRET"):
        self.key = key.upper()
    
    def _extend_key(self, text):
        key_index = 0
        extended_key = []
        for char in text:
            if char.isalpha():
                extended_key.append(self.key[key_index % len(self.key)])
                key_index += 1
            else:
                extended_key.append('0')
        return extended_key
    
    def encrypt(self, text):
        extended_key = self._extend_key(text)
        result = []
        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(extended_key[i]) - ord('A')
                if char.isupper():
                    result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
                else:
                    result.append(chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A')).lower())
            else:
                result.append(char)
        return ''.join(result)
    
    def decrypt(self, text):
        extended_key = self._extend_key(text)
        result = []
        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(extended_key[i]) - ord('A')
                if char.isupper():
                    result.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
                else:
                    result.append(chr((ord(char.upper()) - ord('A') - shift) % 26 + ord('A')).lower())
            else:
                result.append(char)
        return ''.join(result)


# ============================================================
# STREAMLIT UI
# ============================================================

st.markdown("# 🔐 Classical Ciphers Lab")
st.markdown("### An Interactive Cryptology Application")
st.markdown("---")

with st.sidebar:
    st.markdown("## ⚙️ Configuration")
    cipher_type = st.radio(
        "🔑 Select Cipher:",
        ["Caesar Cipher", "Vigenere Cipher"]
    )

tab1, tab2, tab3, tab4 = st.tabs(["Encrypt/Decrypt", "Brute Force", "Analysis", "Guide"])

# TAB 1
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Input Section")
        if cipher_type == "Caesar Cipher":
            shift = st.slider("Shift Value:", 0, 25, 3)
            plaintext = st.text_area("Plaintext:", "Hello World", height=150)
            col_enc, col_dec = st.columns(2)
            with col_enc:
                if st.button("Encrypt", use_container_width=True, key="caesar_enc"):
                    cipher = CaesarCipher(shift)
                    result = cipher.encrypt(plaintext)
                    st.session_state.result = result
            with col_dec:
                if st.button("Decrypt", use_container_width=True, key="caesar_dec"):
                    cipher = CaesarCipher(shift)
                    result = cipher.decrypt(plaintext)
                    st.session_state.result = result
        else:
            key = st.text_input("Key:", "SECRET")
            plaintext = st.text_area("Plaintext:", "Send supplies", height=150)
            col_enc, col_dec = st.columns(2)
            with col_enc:
                if st.button("Encrypt", use_container_width=True, key="vig_enc"):
                    cipher = VigenereCipher(key)
                    result = cipher.encrypt(plaintext)
                    st.session_state.result = result
            with col_dec:
                if st.button("Decrypt", use_container_width=True, key="vig_dec"):
                    cipher = VigenereCipher(key)
                    result = cipher.decrypt(plaintext)
                    st.session_state.result = result
    
    with col2:
        st.markdown("### Result")
        if "result" in st.session_state:
            st.code(st.session_state.result, language="text")
            st.metric("Length", len(st.session_state.result))
        else:
            st.info("Click Encrypt/Decrypt to see results")

# TAB 2
with tab2:
    st.markdown("### Caesar Brute Force Attack")
    encrypted = st.text_area("Encrypted Text:", "Khoor Zruog")
    if st.button("Attack"):
        caesar = CaesarCipher(0)
        results = caesar.brute_force(encrypted)
        for shift, plaintext in sorted(results.items()):
            col_s, col_t = st.columns([0.3, 0.7])
            with col_s:
                st.write(f"**Shift {shift}:**")
            with col_t:
                st.code(plaintext)

# TAB 3
with tab3:
    st.markdown("### Frequency Analysis")
    text = st.text_area("Text:", "The quick brown fox")
    if st.button("Analyze"):
        freq = {}
        for c in text.upper():
            if c.isalpha():
                freq[c] = freq.get(c, 0) + 1
        fig = go.Figure([go.Bar(x=list(freq.keys()), y=list(freq.values()))])
        st.plotly_chart(fig, use_container_width=True)

# TAB 4
with tab4:
    st.markdown("""
    ### Caesar Cipher
    Shifts each letter by fixed amount.
    - Shift 3: A→D, B→E, etc.
    - Only 26 possible keys
    
    ### Vigenere Cipher
    Uses keyword for encryption.
    - More secure than Caesar
    - Hard to break without key
    """)
