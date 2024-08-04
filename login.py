import os
import json
import base64
import streamlit as st
from faker import Faker
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import time

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_email' not in st.session_state:
    st.session_state.user_email = None
if 'username' not in st.session_state:
    st.session_state.username = None
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Login"
if 'login_attempted' not in st.session_state:
    st.session_state['login_attempted'] = False

# Initialize Firebase
if not firebase_admin._apps:
    firebase_credentials = os.getenv('FIREBASE_CREDENTIALS')
    if firebase_credentials is None:
        st.error("Firebase credentials not set in environment variables.")
    else:
        try:
            firebase_credentials = base64.b64decode(firebase_credentials).decode('utf-8')
            cred = credentials.Certificate(json.loads(firebase_credentials))
            firebase_admin.initialize_app(cred)
        except Exception as e:
            st.error(f"Error initializing Firebase: {e}")

fake = Faker()

def generate_fake_username():
    return fake.user_name()

def app():
    st.title("Welcome To: SafeSpace")

    choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
    
    if choice == 'Login':
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        login_button = st.button('Login')
        
        if login_button and not st.session_state['logged_in']:
            try:
                user = auth.get_user_by_email(email)
                st.session_state['logged_in'] = True
                st.session_state['user_email'] = email
                st.session_state['current_page'] = "Home"
                st.session_state['username'] = user.uid
                time.sleep(0.5)  # Add a small delay
            except Exception as e:
                st.session_state['login_attempted'] = False
                st.error(f'Invalid email or password: {e}')

    else:
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        signup_button = st.button('Create My Account')
        
        if signup_button:
            username = generate_fake_username()
            try:
                user = auth.create_user(email=email, password=password, uid=username)
                st.session_state['username'] = username
                st.success('Account created successfully!')
                st.markdown(f'Your generated username is: {username}')
                st.markdown('You can now login with your email and password.')
            except Exception as e:
                st.error(f'Error creating account: {e}')
