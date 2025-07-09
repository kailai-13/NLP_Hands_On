# Install googletrans
# pip install googletrans==4.0.0-rc1

from googletrans import Translator

# Initialize the Translator
translator = Translator()

# Text to translate
text = "Hello, how are you?"

# Translate to Tamil
translated = translator.translate(text, dest='ta')
print(f"Original: {text}")
print(f"Translated (Tamil): {translated.text}")

# Translate to Hindi
translated_hi = translator.translate(text, dest='hi')
print(f"Translated (Hindi): {translated_hi.text}")
