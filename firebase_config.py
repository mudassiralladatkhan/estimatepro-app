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

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
