[app]
title = EstimatePro
package.name = estimatepro
package.domain = org.estimatepro
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv
version = 0.1.0
requirements = python3,kivy,pyrebase4,requests,urllib3,certifi,idna,chardet,requests_toolbelt,sseclient,oauth2client,pycryptodome,google-auth,cachecontrol
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.release_artifact = bin/*.apk

# Entry point
requirements.hostpython =
presplash.filename =
icon.filename =
log_level = 2
use_androidx = 1

[buildozer]
log_level = 2
warn_on_root = 0

[app:android]
# Keep python files bytecode compiled
android.keep_classes =


