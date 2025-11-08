# redstains.com
from pynput import keyboard
from pynput.keyboard import Key, Controller
import time
import threading
import pyperclip
import json
import os

# Load mapping from JSON file
def load_mapping():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mapping_file = os.path.join(script_dir, 'mapping.json')
    
    try:
        with open(mapping_file, 'r', encoding='utf-8') as f:
            mapping = json.load(f)
        print(f"Loaded {len(mapping)} word mappings from mapping.json")
        return mapping
    except FileNotFoundError:
        print(f"Error: mapping.json file not found at {mapping_file}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in mapping.json: {e}")
        return {}
    except Exception as e:
        print(f"Error loading mapping.json: {e}")
        return {}

# Load mapping from JSON file
MAPPING = load_mapping()

# Normalize mapping keys to lower-case
MAPPING = {k.lower(): v for k, v in MAPPING.items()}

controller = Controller()
pressed_buffer = []  # list of characters of current word
word_history = []  # stores previous words for multi-word matching
is_replacing = threading.Event()  # flag: set when we are performing replacement
pressed_keys = set()  # for hotkey combinations

def adjust_case(original_typed: str, replacement: str) -> str:
    if original_typed.isupper():
        return replacement.upper()
    if len(original_typed) > 0 and original_typed[0].isupper() and original_typed[1:].islower():
        return replacement[0].upper() + replacement[1:]
    return replacement


def replace_last_word_select_all(replacement: str, length: int):
    is_replacing.set()
    try:
        # Select exactly the number of characters we typed + 1 extra for safety
        for i in range(length + 1):
            controller.press(Key.shift)
            controller.press(Key.left)
            controller.release(Key.left)
            controller.release(Key.shift)
        
        # Wait then type replacement (this will overwrite selection)
        time.sleep(0.1)
        controller.type(replacement + ' ')
        
    finally:
        time.sleep(0.025)
        is_replacing.clear()


def replace_last_word(replacement: str, length: int):
    is_replacing.set()
    try:
        # Save current clipboard
        try:
            old_clipboard = pyperclip.paste()
        except:
            old_clipboard = ""
        
        # Wait a bit before starting deletion
        time.sleep(0.035)
        
        # Delete the typed word + 1 extra character for safety
        for i in range(length + 1):
            controller.press(Key.backspace)
            controller.release(Key.backspace)
            time.sleep(0.01)
        
        # Wait before typing replacement
        time.sleep(0.05)
        
        # Copy replacement to clipboard
        final_text = replacement
        if not replacement.endswith(' '):
            final_text += ' '
            
        pyperclip.copy(final_text)
        time.sleep(0.02)
        
        # Paste from clipboard (Ctrl+V)
        controller.press(Key.ctrl)
        controller.press('v')
        controller.release('v')
        controller.release(Key.ctrl)
        
        time.sleep(0.02)
        
        # Restore old clipboard
        try:
            pyperclip.copy(old_clipboard)
        except:
            pass
        
    finally:
        time.sleep(0.035)
        is_replacing.clear()


def flush_buffer_check_and_maybe_replace():
    if not pressed_buffer:
        return
    
    current_word = ''.join(pressed_buffer)
    current_word_lower = current_word.lower()
    
    # First, try two-word combination with previous word (if exists)
    if word_history:
        # Only check the last TYPED word (not replaced words from mapping)
        # We need to track which words in history are original vs replacements
        previous_word = word_history[-1]
        two_word_phrase = f"{previous_word} {current_word}"
        two_word_phrase_lower = two_word_phrase.lower()
        
        if two_word_phrase_lower in MAPPING:
            replacement_text = MAPPING[two_word_phrase_lower]
            replacement_text = adjust_case(two_word_phrase, replacement_text)
            
            # Total length = previous word + space + current word
            total_length = len(previous_word) + 1 + len(current_word)
            
            print(f"Match found (2 words): '{two_word_phrase}' → '{replacement_text}'")
            
            threading.Thread(target=replace_last_word, args=(replacement_text, total_length), daemon=True).start()
            
            # Remove the previous word from history since we replaced it
            word_history.pop()
            # Don't add replacement to history (it shouldn't be part of next match)
            
            pressed_buffer.clear()
            return
    
    # If no two-word match, try single word match
    if current_word_lower in MAPPING:
        replacement_text = MAPPING[current_word_lower]
        replacement_text = adjust_case(current_word, replacement_text)
        total_length = len(current_word)
        
        print(f"Match found (1 word): '{current_word}' → '{replacement_text}'")
        
        threading.Thread(target=replace_last_word, args=(replacement_text, total_length), daemon=True).start()
        
        # Don't store replaced word in history
        pressed_buffer.clear()
        return
    
    # No match found, store current word in history for potential two-word match next time
    word_history.append(current_word)
    if len(word_history) > 5:  # Keep only last 5 words
        word_history.pop(0)
    
    pressed_buffer.clear()


def on_press(key):
    if is_replacing.is_set():
        return
    
    # Add key to pressed_keys for hotkey detection
    pressed_keys.add(key)
    
    # Check for Ctrl + Left Shift hotkey
    if ((Key.ctrl in pressed_keys or Key.ctrl_l in pressed_keys or Key.ctrl_r in pressed_keys) and 
        Key.shift_l in pressed_keys):
        controller.type('ə')
        pressed_keys.clear()
        return
    
    try:
        if hasattr(key, 'char') and key.char is not None:
            ch = key.char
            # Accept alphanumeric and Turkish characters
            if ch.isalnum() or ch == '_' or ch in 'çğıöşüÇĞIİÖŞÜ':
                pressed_buffer.append(ch)
                return
            else:
                # Check and replace on space or enter, not on other punctuation
                if ch == ' ':
                    flush_buffer_check_and_maybe_replace()
                else:
                    # Clear buffer on other punctuation but don't replace
                    pressed_buffer.clear()
                return
        else:
            # Handle special keys
            if key in (Key.space, Key.enter):
                # Trigger replacement on space key or enter key
                flush_buffer_check_and_maybe_replace()
                return
            elif key == Key.backspace:
                # Remove last character from buffer instead of clearing it completely
                if pressed_buffer:
                    pressed_buffer.pop()
                return
            elif key == Key.tab:
                # Clear buffer but don't replace on tab
                pressed_buffer.clear()
                return
            elif key == Key.esc:
                print("\nExiting...")
                return False
            else:
                # For other special keys (arrows, function keys, etc.), clear buffer
                pressed_buffer.clear()
                return
    except Exception:
        pressed_buffer.clear()
        return


def on_release(key):
    # Remove key from pressed_keys when released
    pressed_keys.discard(key)


def main():
    print("Auto reverse-e listener started.")
    print("Features:")
    print("  • Auto-replace: aziz + SPACE/ENTER → əziz")
    print("  • Hotkey: Ctrl + Left Shift → ə")
    print(f"  • Dictionary: {len(MAPPING)} word mappings loaded")
    print("Press ESC to quit.")
    
    if not MAPPING:
        print("Warning: No word mappings loaded. Please check mapping.json file.")
        
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            return


if __name__ == '__main__':
    main()

# omre - RedStains
# redstains.com