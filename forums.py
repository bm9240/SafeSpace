import streamlit as st
from database import add_message, get_messages


def app():
    # Initialize session state for login and username
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if 'username' not in st.session_state:
        st.session_state['username'] = "Guest"

    # Sidebar for topic selection and message input
    st.sidebar.title("Chat Forum")
    topic = st.sidebar.selectbox("Select Topic", ['Domestic Violence', 'Sexual Harassment', 'Eve Teasing', 'Mental Health'])
    new_message = st.sidebar.text_area("Enter your message")

    # Handle message posting
    if st.sidebar.button("Post Message"):
        if st.session_state.username and new_message:
            add_message(topic, st.session_state.username, new_message)
            st.sidebar.success("Message posted!")
        else:
            st.sidebar.error("Please enter both username and message")

    # Main area to display messages
    st.title("SafeSpace Chat Forum")
    st.write("Select a topic from the sidebar to view and post messages.")

    # Function to display messages based on selected topic
    def display_messages(selected_topic):
        messages = get_messages(selected_topic)
        st.write("### Messages")
        for message in messages:
            st.write(f"*Topic:* {message[1]} | *User:* {message[2]}")
            st.write(f"{message[3]}")
            st.write("---")  # Divider for messages

    # Display messages for the selected topic
    display_messages(topic)