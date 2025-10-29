[app]

# Main Python file
source.dir = .
source.main = main.py

# App metadata
title = EstimatePro
package.name = estimatepro
package.domain = org.nithyashree
version = 1.0.0

# Include file types and folders
source.include_exts = py,png,jpg,kv,atlas
include_patterns = assests/*,screens/*,*.jpg,.github/*

# Exclude unnecessary folders
exclude_patterns = tests/*,__pycache__/*

# Permissions
android.permissions = INTERNET

# Orientation
orientation = portrait

# Dependencies
# Pin urllib3<2 to keep urllib3.contrib.appengine available for pyrebase4
requirements = python3,kivy,pyrebase4,requests,urllib3<2,certifi,chardet,idna

# Android API levels
android.minapi = 21
android.api = 33
android.ndk = 23b

# Accept Android SDK licenses automatically (useful for CI)
android.accept_sdk_license = True

# Python-for-Android (p4a) settings
p4a.bootstrap = sdl2

# Architecture
android.archs = arm64-v8a

# Entry settings
fullscreen = 1
log_level = 2

# Package format
package.format = apk

# Debug settings
android.debug = 1
android.allow_backup = 0
android.logcat_filters = *:S python:D

# OpenGL
android.opengl_version = 2

# AndroidX support
android.use_androidx = 1
android.enable_jetifier = 1
