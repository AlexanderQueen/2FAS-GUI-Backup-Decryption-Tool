# 🔐 2FAS GUI Backup Decryption Tool

<div align="center">

![2FAS Logo](https://img.shields.io/badge/2FAS-Backup%20Decryption-28a745?style=for-the-badge&logo=security&logoColor=white)

**A modern, secure GUI application for decrypting 2FAS app backup files**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![PyQt6](https://img.shields.io/badge/PyQt6-GUI-green?style=flat-square&logo=qt&logoColor=white)](https://pypi.org/project/PyQt6/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-red?style=flat-square)](https://github.com/AlexanderQueen/2fas-gui-backup-decryption-tool/releases)

[🚀 Quick Start](#-quick-start) • [📥 Download](#-download) • [🛠️ Installation](#️-installation) • [📖 Documentation](#-documentation)

</div>

---

## ✨ Features

<div align="center">

| 🎨 **Modern UI** | 🔒 **Secure Decryption** | 📁 **Easy File Handling** |      
|:---:|:---:|:---:|
| Beautiful Qt6 interface with dark theme | Industry-standard AES-GCM encryption | Drag & drop + file browser support |

| 🧵 **Multithreading** | 💾 **Export Options** | 🔄 **Cross-Platform** |
|:---:|:---:|:---:|
| Non-blocking UI during decryption | Save results as JSON files | Windows, macOS, Linux support |

</div>

## 🎯 What is this?

The **2FAS GUI Backup Decryption Tool** is a user-friendly desktop application that allows you to decrypt and view your 2FAS authenticator app backup files. Whether you need to migrate to a new device, audit your 2FA tokens, or simply access your backup data, this tool provides a secure and intuitive solution.

## 🖼️ Screenshots

<div align="center">
<table>
<tr>
<td align="center">
<img src="https://github.com/user-attachments/assets/2f34c337-2b98-4840-896a-97a6a4a15ebc" alt="Main Interface" width="400"/>
<br><em>Clean, modern interface</em>
</td>
<td align="center">
<img src="https://via.placeholder.com/400x300/495057/28a745?text=Drag+%26+Drop" alt="Drag & Drop" width="400"/>
<br><em>Intuitive file handling</em>
</td>
</tr>
</table>
</div>

## 🚀 Quick Start

### Option 1: Download Pre-built Executable (Recommended)

1. **Download** the latest release from the [Releases page](https://github.com/AlexanderQueen/2fas-gui-backup-decryption-tool/releases)
2. **Run** the executable directly - no installation required!
3. **Load** your `.2fas` backup file
4. **Enter** your backup password
5. **Decrypt** and view your data

### Option 2: Run from Source

```bash
# Clone the repository![2fas](https://github.com/user-attachments/assets/a1890452-f2d4-48f1-9061-785f0b507b29)

git clone https://github.com/AlexanderQueen/2fas-gui-backup-decryption-tool.git
cd 2fas-gui-backup-decryption-tool

# Install dependencies
pip install -r requirements.txt

# Run the application
python 2fas.py
```

## 📥 Download

<div align="center">

### 🎯 Latest Release: v1.0.0

| Platform | Download | Size |
|:--------:|:--------:|:----:|
| 🪟 **Windows** | [2FAS-GUI-Backup-Decryption-Tool.exe](https://github.com/AlexanderQueen/2fas-gui-backup-decryption-tool/releases/latest/download/2FAS-Decryption-Tool.exe) | ~35MB |
| 🍎 **macOS** | [2FAS-GUI-Backup-Decryption-Tool.dmg](https://github.com/AlexanderQueen/2fas-gui-backup-decryption-tool/releases/latest/download/2FAS-Decryption-Tool.dmg) | TBD |
| 🐧 **Linux** | [2FAS-GUI-Backup-Decryption-Tool](https://github.com/AlexanderQueen/2fas-gui-backup-decryption-tool/releases/latest/download/2FAS-Decryption-Tool) | TBD |

</div>

## 🛠️ Installation

### Prerequisites

- **Python 3.8+** (for running from source)
- **2FAS backup file** (`.2fas` extension)
- **Backup password** (the one you set when creating the backup)

### Dependencies

```bash
PyQt6>=6.0.0
cryptography>=3.4.0
```

### Building from Source

```bash
# Install build dependencies
pip install pyinstaller

# Build executable
python build.py
```

The built executable will be available in the `dist/` folder.

## 📖 How to Use

### Step-by-Step Guide

1. **📂 Load Your Backup**
   - Drag and drop your `.2fas` file onto the application
   - OR click the file area to browse and select your backup

2. **🔑 Enter Password**
   - Type your backup password in the password field
   - This is the password you set when creating the backup in 2FAS

3. **🔓 Decrypt**
   - Click the "🔓 Decrypt Backup" button
   - Wait for the progress bar to complete

4. **📄 View Results**
   - Your decrypted data will appear in JSON format
   - Review your 2FA tokens and associated data

5. **💾 Save (Optional)**
   - Click "💾 Save Results" to export the data
   - Choose your preferred location and filename

### Supported File Format

- **Input**: `.2fas` backup files from 2FAS Authenticator app
- **Output**: JSON format with all your 2FA token data

## 🔒 Security Features

- **🛡️ Local Processing**: All decryption happens locally on your device
- **🔐 Industry Standard**: Uses AES-GCM encryption with PBKDF2 key derivation
- **🚫 No Data Collection**: No data is sent to external servers
- **🧵 Secure Memory**: Passwords are handled securely in memory

## 🏗️ Technical Details

### Encryption Specification

- **Algorithm**: AES-GCM (Galois/Counter Mode)
- **Key Derivation**: PBKDF2-HMAC-SHA256
- **Iterations**: 10,000
- **Key Length**: 256-bit

### Architecture

```
📁 Project Structure
├── 2fas.py              # Main application file
├── build.py             # Build script for executables
├── requirements.txt     # Python dependencies
├── icons/               # Application icons
└── dist/               # Built executables (after build)
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **🍴 Fork** the repository
2. **🌿 Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **💫 Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **🚀 Push** to the branch (`git push origin feature/amazing-feature`)
5. **📝 Open** a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/2fas-gui-backup-decryption-tool.git
cd 2fas-gui-backup-decryption-tool

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run in development mode
python 2fas.py
```

## 🐛 Bug Reports & Feature Requests

Found a bug or have a feature request? Please [open an issue](https://github.com/AlexanderQueen/2fas-gui-backup-decryption-tool/issues) with:

- **🐛 Bug Reports**: Steps to reproduce, expected vs actual behavior, system info
- **💡 Feature Requests**: Clear description of the feature and its use case

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **2FAS Team** - For creating the excellent 2FAS Authenticator app
- **PyQt6** - For the fantastic GUI framework
- **Cryptography Library** - For secure encryption implementation

## ⭐ Support

If this tool helped you, please consider:

- ⭐ **Starring** this repository
- 🐛 **Reporting** any bugs you find
- 💬 **Sharing** with others who might need it
- 🤝 **Contributing** to make it even better

---

<div align="center">

**Made with ❤️ by [@AlexanderQueen](https://github.com/AlexanderQueen)**

[🏠 Home](https://github.com/AlexanderQueen/2fas-gui-backup-decryption-tool) • [📝 Issues](https://github.com/AlexanderQueen/2fas-gui-backup-decryption-tool/issues) • [🚀 Releases](https://github.com/AlexanderQueen/2fas-gui-backup-decryption-tool/releases)

</div>
