[app]
title = EstimatePro
package.name = estimatepro
package.domain = org.estimatepro
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,txt
source.include_patterns = assests/*,screens/*,*.jpg,*.txt
version = 0.1.0

# Dependencies - Pin urllib3<2 for pyrebase4 compatibility
requirements = python3,kivy,pyrebase4,requests,urllib3<2,certifi,chardet,idna

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

# Entry point
log_level = 2
use_androidx = 1

[buildozer]
log_level = 2
warn_on_root = 0

[app:android]
# Keep python files bytecode compiled
android.keep_classes =


