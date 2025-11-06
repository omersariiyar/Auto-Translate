# Azerbaijani Auto-Correction Tool

A powerful system-wide keyboard automation tool for Azerbaijani Turkish typing that provides both manual character insertion and intelligent automatic word correction from Turkish/ASCII transliterations to proper Azerbaijani forms with ə character.

## 🚀 Features

- **🎯 Manual Hotkey**: Press `Ctrl + Left Shift` to instantly insert `ə` character anywhere
- **🔄 Smart Auto-Correction**: Automatically replaces Turkish/ASCII words with proper Azerbaijani equivalents when you finish typing (space/enter)
- **📚 Extensive Dictionary**: 626+ carefully curated word mappings from Turkish to Azerbaijani (loaded from JSON file)
- **🔤 Case Intelligence**: Preserves your original capitalization (UPPER, Title, lower)
- **📝 Multi-word Phrases**: Handles complete phrases like "eleştiriliyor" → "tənqid olunur"
- **🇹🇷 Turkish Character Support**: Full support for Turkish characters (ç, ğ, ı, ö, ş, ü)
- **🌐 Universal Compatibility**: Works seamlessly across ALL applications (Word, browsers, chat apps, IDEs, etc.)
- **⚡ Real-time Processing**: Instant replacements with no noticeable delay

## 📋 Prerequisites

- **Operating System**: Windows 10/11
- **Python**: Version 3.7 or higher
- **Privileges**: Standard user (no admin required)

## ⚙️ Installation

### Step 1: Download Files
```bash
# Download both files to the same folder:
# - auto_reverse_e.py (main program)
# - mapping.json (word dictionary)
# Example: C:\AutoReverse\
```

### Step 2: Install Dependencies
```bash
pip install pynput pyperclip
```

### Step 3: Run the Tool
```bash
python C:\auto_reverse_e.py
```

## 💡 Usage Guide

### Manual Character Input
- **Hotkey**: `Ctrl + Left Shift` → instantly types `ə`
- Works in any text field, anywhere on your system

### Automatic Word Correction
Simply type Turkish words naturally and press `Space` or `Enter`:

```
Type: "aziz" + Space → Result: "əziz "
Type: "eleştiriliyor" + Space → Result: "tənqid olunur "
Type: "meseleler" + Enter → Result: "məsələlər "
Type: "HASTA" + Space → Result: "XƏSTƏ "
Type: "Gazete" + Space → Result: "Qəzet "
```

### 📖 Popular Mappings

| Turkish/ASCII | Azerbaijani | Meaning |
|---------------|-------------|---------|
| aziz | əziz | dear |
| evvel | əvvəl | first/before |
| eleştiriliyor | tənqid olunur | being criticized |
| meseleler | məsələlər | issues |
| hasta | xəstə | patient/sick |
| gazete | qəzet | newspaper |
| öğretmen | müəllim | teacher |
| sabah | səhər | morning |
| bilgi | məlumat | information |
| değil | deyil | not |

## 🔧 How It Works

### Architecture
1. **📂 Dictionary Loading**: Loads word mappings from `mapping.json` file at startup
2. **🎧 Global Listener**: Monitors keyboard input system-wide using `pynput`
3. **📝 Word Buffering**: Intelligently accumulates characters until word boundaries
4. **🔍 Dictionary Lookup**: Checks typed words against mapping database loaded from JSON file
5. **✨ Smart Replacement**: When match found:
   - Precisely deletes original word with backspace simulation
   - Uses clipboard for reliable Unicode character insertion
   - Maintains original capitalization pattern
   - Adds proper spacing

### Technical Stack
- **JSON**: Stores word mappings in easily editable format
- **pynput**: Cross-platform keyboard event handling
- **pyperclip**: Reliable clipboard operations for Unicode support
- **threading**: Non-blocking replacement operations
- **Unicode**: Full support for Azerbaijani character set

## 🛠️ Advanced Configuration

### Adding Custom Mappings
You can add new word mappings by editing the `mapping.json` file:

```json
{
    "your_turkish_word": "azerbaijani_equivalent",
    "merhaba": "salam",
    "teşekkürler": "təşəkkürlər",
    "new_word": "new_mapping"
}
```

**Note**: You need to restart the program after editing the JSON file.

### Performance Tuning
- **Memory usage**: ~10-20 MB (very lightweight)
- **CPU impact**: Negligible background processing
- **Response time**: < 50ms for most replacements
- **Dictionary size**: 626+ word mappings (automatically loaded from JSON file)

## ❗ Troubleshooting

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Script not responding | Run with elevated privileges if needed |
| Characters appearing incorrectly | Ensure target app supports Unicode |
| Import errors | `pip install pynput pyperclip` |
| JSON file not found | Ensure mapping.json is in the same folder as auto_reverse_e.py |
| JSON syntax errors | Validate JSON format using online JSON validator |
| Replacement not working | Check if word exists in mapping.json dictionary |
| Performance issues | Close unnecessary background apps |

### Stopping the Tool
- **Graceful exit**: Press `ESC` key
- **Force quit**: `Ctrl+C` in terminal
- **Task Manager**: End python.exe process if frozen

## 🤝 Contributing

We welcome contributions! You can help by:
- 📝 Adding new Turkish → Azerbaijani word mappings
- 🐛 Reporting bugs and issues
- ⚡ Performance optimizations
- 🌐 Adding support for other languages
- 📚 Improving documentation

## 📄 License

This project is open source and available under the **MIT License**.

## 🖥️ System Requirements

| Component | Requirement |
|-----------|-------------|
| **OS** | Windows 10/11 (64-bit recommended) |
| **Python** | 3.7+ |
| **RAM** | 50MB available memory |
| **Storage** | 5MB disk space |
| **Network** | Not required (works offline) |

## 🔥 Pro Tips

- **Startup**: Add to Windows startup for automatic launching
- **Efficiency**: Learn common mappings for faster typing
- **Backup**: Keep your custom mappings backed up (especially mapping.json file)
- **Updates**: Regularly update the word dictionary by adding new entries to mapping.json
- **Integration**: Works perfectly with autocomplete and spell checkers

## 🏷️ Version Info

- **Current Version**: 2.0
- **Last Updated**: November 2024
- **Compatibility**: Windows 10/11, Python 3.7+
- **Status**: Actively maintained

---

*Transform your Turkish typing into perfect Azerbaijani effortlessly!*
