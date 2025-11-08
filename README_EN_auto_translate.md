# Auto Translate - Real-Time Translation Tool

## 📋 Overview

**Auto Translate** is a powerful Python-based tool that automatically translates your text as you type, anywhere on your computer. Simply type a sentence, end it with punctuation (`.`, `!`, `?`, etc.), and watch it instantly translate to your target language!

## ✨ Features

- 🌍 **Universal Translation**: Works in any application - browsers, text editors, chat apps, etc.
- 🚀 **Real-Time Processing**: Instant translation as you finish typing
- 🎯 **Smart Detection**: Automatically detects source language
- 📝 **Multiple Punctuation Support**: Recognizes `.`, `!`, `?`, `:`, `;` as sentence endings
- 💾 **Clipboard Safety**: Preserves your original clipboard content
- 🔤 **Auto-Capitalization**: Ensures first letter of translation is capitalized
- 📏 **Smart Spacing**: Automatically adds space between sentences
- 🐛 **Debug Mode**: Built-in debugging for troubleshooting

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Required Libraries

Install all dependencies with a single command:

```bash
pip install deep-translator pynput pyperclip
```

Or install individually:

```bash
pip install deep-translator
pip install pynput
pip install pyperclip
```

### Library Details

- **deep-translator**: Handles translation via Google Translate API (no API key required!)
- **pynput**: Captures keyboard input globally
- **pyperclip**: Manages clipboard operations

> **Note**: `deep-translator` provides free access to Google Translate without requiring an API key. It uses the unofficial web interface.

## 🚀 Usage

### Starting the Application

#### Method 1: Using Command Line

1. Open terminal/command prompt
2. Navigate to the script directory:
   ```bash
   cd "C:\Program Files\Auto_Translate"
   ```
3. Run the script:
   ```bash
   python auto_translate.py
   ```

#### Method 2: Using Batch File (Quick Start)

For faster access, use the included `auto_translate.bat` file:

1. Open `auto_translate.bat` in a text editor
2. Update the path to your script location:
   ```batch
   @echo off
   cd C:\Program Files\Auto_Translate
   python auto_translate.py
   pause
   ```
3. Save the file
4. Double-click `auto_translate.bat` to run

> **Tip**: Create a shortcut to `auto_translate.bat` on your desktop for instant access!

### Configuration

When you start the application, you'll see:

```
============================================================
Auto Translate Listener
============================================================
Target language: EN
Usage:
  • Type anywhere
  • End your sentence with a period (.), exclamation (!), question mark (?), etc.
  • It will automatically translate and replace
  • Press ESC to exit
============================================================

Would you like to change the target language? (en/tr/de/fr/es/az etc.)
Default: en (English)
Target language code (Enter = default):
```

**Supported Language Codes:**
- `en` - English
- `tr` - Turkish
- `de` - German
- `fr` - French
- `es` - Spanish
- `az` - Azerbaijani
- `ru` - Russian
- `ja` - Japanese
- `zh` - Chinese
- And many more...

### How It Works

1. **Type Your Sentence**: Start typing in any application
2. **End With Punctuation**: Finish with `.`, `!`, `?`, `:`, or `;`
3. **Watch the Magic**: Your sentence is automatically translated and replaced
4. **Continue Typing**: The next sentence will have proper spacing

### Example

**Input:** `Hello world.`  
**Output:** `Merhaba dünya.`

**Input:** `Merhaba dünya. How are you?`  
**Output:** `Merhaba dünya. Nasılsın?`

## ⚙️ Technical Details

### Architecture

The application uses a multi-threaded architecture:

1. **Main Thread**: Runs the keyboard listener
2. **Translation Thread**: Handles API calls without blocking input
3. **Replacement Thread**: Manages text replacement operations

### Key Components

#### 1. Keyboard Listener (`on_press`)
- Captures all keystrokes globally
- Buffers characters until punctuation is detected
- Handles special keys (Space, Enter, Backspace, ESC)

#### 2. Translation Engine (`translate_text`)
- Uses Google Translate via `deep-translator`
- Automatic source language detection
- Error handling with fallback to original text

#### 3. Text Replacement (`replace_sentence_with_translation`)
- Selects typed text using Shift+Left Arrow
- Deletes original sentence
- Pastes translated text with proper formatting
- Preserves clipboard content

#### 4. Sentence Processing (`process_sentence`)
- Determines if space is needed before translation
- Manages buffer lifecycle
- Coordinates translation and replacement

### Features in Detail

#### Smart Spacing
The tool detects if your sentence starts with a space:
- **First sentence**: No leading space
- **Subsequent sentences**: Adds space automatically

#### Capitalization
Every translated sentence begins with a capital letter, ensuring proper grammar.

#### Punctuation Preservation
Original punctuation marks are preserved:
- Input: `Hello!` → Output: `Merhaba!`
- Input: `How are you?` → Output: `Nasılsın?`

## 🐛 Debug Mode

The application includes debug output for troubleshooting:

```
Debug: Buffer length=5, Punctuation='.', Total to delete=6, Space needed=False
✓ 'hello' → 'Hello.'
```

This shows:
- Characters in buffer
- Punctuation mark used
- Number of characters to delete
- Whether spacing is needed
- Original and translated text

## ⚠️ Limitations

1. **Rate Limiting**: Google Translate may throttle requests if you translate too frequently
2. **Character Limit**: ~5000 characters per translation
3. **Internet Required**: Needs active internet connection
4. **API Dependency**: Relies on unofficial Google Translate access

## 🔧 Troubleshooting

### Translation Not Working
- Check internet connection
- Verify `deep-translator` is installed correctly
- Try reducing translation frequency

### Text Selection Issues
- Increase timing delays in code (adjust `time.sleep()` values)
- Check if your application supports clipboard operations

### Keyboard Input Not Detected
- Run script with administrator privileges
- Ensure `pynput` has necessary permissions

## 📝 Configuration Options

### Adjusting Timing

If translations are too fast/slow, modify these values in the code:

```python
time.sleep(0.003)  # Selection speed
time.sleep(0.05)   # Delete operation
time.sleep(0.1)    # Replacement operation
```

### Adding Sentence Endings

Edit the `sentence_end_chars` list:

```python
sentence_end_chars = ['.', '!', '?', ':', ';', '…']  # Add more
```

## 🔒 Privacy & Security

- All translations are processed via Google Translate servers
- No data is stored locally by this application
- Clipboard content is restored after each operation
- Keyboard input is only monitored, not logged

## 👨‍💻 Developer Information

- **Author**: omre (RedStains)
- **Website**: redstains.com
- **License**: Check repository for license details

## 🆘 Support

For issues, questions, or contributions:
1. Check the debug output for errors
2. Verify all dependencies are installed
3. Ensure you have the latest version

## 📜 Version History

- **v1.0**: Initial release with basic translation
- **v1.1**: Added smart spacing and capitalization
- **v1.2**: Improved clipboard management
- **v1.3**: Debug mode and error handling

---

**Made with ❤️ by RedStains**  
*Translate as you type, anywhere!*