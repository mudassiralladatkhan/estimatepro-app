import pyrebase

firebase_config = {
    "apiKey": "AIzaSyAtOfxnIb4EDyjGtz16j69i2zxh6BNlOmk",
    "authDomain": "estimatepro-f4576.firebaseapp.com",
    "databaseURL": "https://estimatepro.firebaseio.com",
    "projectId": "estimatepro-f4576",
    "storageBucket": "estimatepro-f4576.firebasestorage.app",
    "messagingSenderId": "49386723953",
    "appId": "1:49386723953:web:52d603c294d88873ce59d0"
}

# Lazy initialization to prevent crashes on app startup
_firebase = None
_auth = None

def get_firebase():
    global _firebase
    if _firebase is None:
        try:
            _firebase = pyrebase.initialize_app(firebase_config)
        except Exception as e:
            print(f"Firebase init error: {e}")
            _firebase = None
    return _firebase

def get_auth():
    global _auth
    if _auth is None:
        fb = get_firebase()
        if fb:
            try:
                _auth = fb.auth()
            except Exception as e:
                print(f"Firebase auth error: {e}")
                _auth = None
    return _auth

# For backward compatibility
auth = get_auth()
