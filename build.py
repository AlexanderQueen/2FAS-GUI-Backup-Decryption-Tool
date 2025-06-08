import PyInstaller.__main__
import os

# Create dist directory if it doesn't exist
if not os.path.exists('dist'):
    os.makedirs('dist')

# Define icon path (optional)
icon_path = 'icons/2fas.png'

# Check if icon exists
if os.path.exists(icon_path):
    print(f"Using icon: {icon_path}")
    icon_arg = f'--icon={icon_path}'
else:
    print("No icon found - using fallback icon from code")
    icon_arg = ''

# Run PyInstaller
args = [
    '2fas.py',  # Your main script file
    '--name=2FAS-Decryption-Tool',
    '--onefile',
    '--windowed',
    '--noconsole',
    '--clean',
    '--hidden-import=PyQt6.QtCore',
    '--hidden-import=PyQt6.QtWidgets', 
    '--hidden-import=PyQt6.QtGui',
    '--hidden-import=cryptography.hazmat.primitives.ciphers.aead',
    '--hidden-import=cryptography.hazmat.primitives.hashes',
    '--hidden-import=cryptography.hazmat.primitives.kdf.pbkdf2',
    f'--add-data={icon_path};icons',  # Include the icon file in the assets folder
    f'--icon={icon_path}',  # Use PNG format for the exe icon
]

# Add icon if it exists
if icon_arg:
    args.append(icon_arg)

PyInstaller.__main__.run(args)

print("\n✅ Build complete!")
print("📁 Check the 'dist' folder for your executable")