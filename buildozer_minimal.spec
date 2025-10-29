[app]
title = EstimatePro Test
package.name = estimateprotest
package.domain = org.estimateprotest
source.dir = .
source.include_exts = py
version = 0.1.0

# Minimal dependencies - JUST Kivy, NO Firebase
requirements = python3,kivy

# Android settings
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

# Python-for-Android settings
p4a.bootstrap = sdl2

# Entry point - USE MINIMAL VERSION
entrypoint = main_minimal.py
log_level = 2
use_androidx = 1

[buildozer]
log_level = 2
warn_on_root = 0
