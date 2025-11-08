# redstains.com
from deep_translator import GoogleTranslator
from pynput import keyboard
from pynput.keyboard import Key, Controller
import time
import threading
import pyperclip

controller = Controller()
sentence_buffer = []  # Holds the characters of the sentence
is_replacing = threading.Event()  # True during replacement operation
target_language = 'en'  # Default target language (English)
sentence_end_chars = ['.', '!', '?', ':', ';']  # Sentence ending characters

def translate_text(text, dest_language='en'):
    """Translates the text"""
    try:
        translator = GoogleTranslator(source='auto', target=dest_language)
        translated = translator.translate(text)
        return translated
    except Exception as e:
        print(f"\rTranslation error: {e}")
        return text  # Return original text on error

def replace_sentence_with_translation(original_sentence: str, translated: str, length: int, end_char: str, needs_space_before: bool):
    """Deletes the written sentence and pastes the translated version"""
    is_replacing.set()
    try:
        # Save old clipboard
        try:
            old_clipboard = pyperclip.paste()
        except:
            old_clipboard = ""
        
        time.sleep(0.1)
        
        total_chars = length + 1
        
        print(f"\nDebug: Buffer length={length}, Punctuation='{end_char}', Total to delete={total_chars}, Space needed={needs_space_before}")
        
        # STEP 1: Delete original sentence + punctuation mark
        # Select characters with Shift+Left Arrow
        for i in range(total_chars):
            with controller.pressed(Key.shift):
                controller.tap(Key.left)
            time.sleep(0.003)
        
        time.sleep(0.05)
        
        # Delete selected text
        controller.tap(Key.delete)
        time.sleep(0.1)
        
        # STEP 2: Remove punctuation mark from end of translation if present
        translated_clean = translated.rstrip('.!?:;,')
        
        # Capitalize first letter of translation
        if translated_clean:
            translated_clean = translated_clean[0].upper() + translated_clean[1:] if len(translated_clean) > 1 else translated_clean.upper()
        
        # If there's a previous sentence (needs_space_before=True), add space at the beginning
        if needs_space_before:
            final_text = ' ' + translated_clean + end_char
        else:
            final_text = translated_clean + end_char
        
        # Copy translated text to clipboard and paste
        pyperclip.copy(final_text)
        time.sleep(0.05)
        
        # Paste with Ctrl+V
        with controller.pressed(Key.ctrl):
            controller.tap('v')
        
        time.sleep(0.05)
        
        # Restore old clipboard
        try:
            pyperclip.copy(old_clipboard)
        except:
            pass
        
        print(f"✓ '{original_sentence}' → '{final_text}'")
        
    finally:
        time.sleep(0.1)
        is_replacing.clear()

def process_sentence(end_char='.'):
    """Translates the sentence in the buffer and replaces it"""
    if not sentence_buffer:
        return
    
    # Join all characters in buffer
    full_text = ''.join(sentence_buffer)
    # Use cleaned version for translation
    sentence = full_text.strip()
    
    if len(sentence) > 0:
        # Check if buffer starts with space (means there's text before)
        needs_space_before = len(full_text) > 0 and full_text[0] == ' '
        
        # Translate (in background)
        translated = translate_text(sentence, target_language)
        
        total_length = len(full_text)
        
        threading.Thread(
            target=replace_sentence_with_translation, 
            args=(sentence, translated, total_length, end_char, needs_space_before), 
            daemon=True
        ).start()
    
    sentence_buffer.clear()

def on_press(key):
    """Called when a key is pressed"""
    if is_replacing.is_set():
        return
    
    try:
        if hasattr(key, 'char') and key.char is not None:
            ch = key.char
            
            # Sentence ended with punctuation mark, translate
            if ch in sentence_end_chars:
                if sentence_buffer:
                    process_sentence(end_char=ch)
                return
            else:
                # Add other characters to buffer
                sentence_buffer.append(ch)
                return
        else:
            # Special keys
            if key == Key.space:
                # Add space character
                sentence_buffer.append(' ')
                return
            elif key == Key.enter:
                # Can also translate sentence with Enter
                if sentence_buffer:
                    process_sentence(end_char='.')
                return
            elif key == Key.backspace:
                # Delete last character with Backspace
                if sentence_buffer:
                    sentence_buffer.pop()
                return
            elif key == Key.esc:
                print("\nExiting...")
                return False
            
    except Exception as e:
        print(f"Error: {e}")
        return

def on_release(key):
    """Called when a key is released"""
    pass

def main():
    global target_language
    
    print("=" * 60)
    print("Auto Translate Listener")
    print("=" * 60)
    print(f"Target language: {target_language.upper()}")
    print("Usage:")
    print("  • Type anywhere")
    print("  • End your sentence with a period (.), exclamation (!), question mark (?), etc.")
    print("  • It will automatically translate and replace")
    print("  • Press ESC to exit")
    print("=" * 60)
    
    # Language selection
    print("\nWould you like to change the target language? (en/tr/de/fr/es/az etc.)")
    print("Default: en (English)")
    lang_input = input("Target language code (Enter = default): ").strip().lower()
    
    if lang_input:
        target_language = lang_input
        print(f"Target language set to {target_language.upper()}.")
    
    print("\nListener started... Start typing!")
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            return

if __name__ == '__main__':
    main()

# omre - RedStains
# redstains.com