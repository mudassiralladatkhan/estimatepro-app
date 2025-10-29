[app]
title = EstimatePro
package.name = estimatepro
package.domain = org.estimatepro
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,txt
source.include_patterns = assests/*,screens/*,*.jpg,*.txt,*.py
version = 0.1.1

# Dependencies - Complete list for pyrebase4 and Firebase
# Don't pin python3 and kivy versions - let p4a choose compatible versions
requirements = python3,kivy,pillow,openssl,pyrebase4,requests,urllib3<2,certifi,chardet,idna,pycryptodome,python-jwt,gcloud,sseclient,requests-toolbelt

# Android settings
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.gradle_dependencies = 

# Python-for-Android settings
p4a.bootstrap = sdl2
p4a.branch = master

# Entry point
log_level = 2
use_androidx = 1

[buildozer]
log_level = 2
warn_on_root = 0

[app:android]
# Keep python files bytecode compiled
android.keep_classes =


