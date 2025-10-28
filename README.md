# EstimatePro - Construction Cost Estimator App

A comprehensive Android application for calculating construction material costs including concrete, steel, bricks, plaster, paint, tiles, excavation, anti-termite treatment, and more.

## Features

- 🔐 **Firebase Authentication** - Secure sign up and sign in
- 📊 **11 Different Calculators**:
  - Concrete Volume
  - Steel Weight
  - Bricks
  - Blocks
  - Plaster
  - Paint
  - Tiles
  - Excavation
  - Slope Filling
  - Anti-Termite Treatment
  - Water Tank
- 🎨 **Modern UI** - Clean interface with icons for each category
- 📱 **Android Compatible** - Works on Android 5.0+ (API 21+)

## Building the APK

Since Buildozer requires Linux, you need to build on a Linux environment. Choose one of these methods:

### Method 1: WSL (Windows Subsystem for Linux) - Easiest for Windows

1. Open PowerShell as Administrator and run:
   ```
   wsl --install
   ```

2. Restart your computer

3. Open Ubuntu from Start Menu

4. Run the build script:
   ```bash
   cd /mnt/c/Users/Hp/Desktop/myproject
   bash build_apk.sh
   ```

5. Find your APK in the `bin/` folder

### Method 2: GitHub Actions (Cloud Build)

1. Create a GitHub repository

2. Push your code to GitHub

3. The workflow (`.github/workflows/build_apk.yml`) will automatically build the APK

4. Download the APK from GitHub Actions artifacts

### Method 3: Linux VM or Machine

Follow standard buildozer instructions on any Linux system.

## Dependencies

- Python 3.10+
- Kivy
- Pyrebase4 (Firebase integration)
- Requests, urllib3, certifi (Network libraries)

All dependencies are configured in `buildozer.spec`.

## Project Structure

```
myproject/
├── main.py                    # App entry point
├── firebase_config.py         # Firebase configuration
├── buildozer.spec            # Build configuration
├── screens/                   # All screen modules
│   ├── auth.py               # Authentication
│   ├── dashboard.py          # Main dashboard
│   ├── concrete.py           # Concrete calculator
│   └── ...                   # Other calculators
├── assests/                   # Assets folder
│   ├── logo.jpg
│   ├── concrete.jpg
│   └── ...                   # Other icons
└── *.jpg                      # Root level images
```

## Configuration

The app is configured in `buildozer.spec`:
- **App Name**: EstimatePro
- **Package**: org.nithyashree.estimatepro
- **Version**: 1.0.0
- **Min Android**: API 21 (Android 5.0)
- **Target Android**: API 33 (Android 13)
- **Architecture**: arm64-v8a

## Firebase Setup

The app uses Firebase for authentication. Configuration is in `firebase_config.py`.

## Installation on Android Device

1. Enable "Install from unknown sources" on your Android device
2. Transfer the APK to your device
3. Open the APK file to install
4. Launch "EstimatePro" from your app drawer

## Troubleshooting

- **Build fails**: Make sure all dependencies are installed
- **Images not showing**: Check that all .jpg files are included in build
- **Firebase not working**: Verify internet connection and Firebase config

## License

All rights reserved.

## Support

For issues or questions, please refer to the build instructions in `build_instructions.txt`.

