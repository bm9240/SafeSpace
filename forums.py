import streamlit as st
    
def app():

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    
    if 'username' in st.session_state:
        username = st.session_state.username
    else:
        username = "Guest"

    if 'messages' not in st.session_state:
        st.session_state['messages'] = {
            'Domestic Violence': [],
            'Sexual Harassment': [],
            'Eve Teasing': [],
            'Mental Health': []
        }
    
    # Sidebar for topic selection and message input
    st.sidebar.title("Chat Forum")
    topic = st.sidebar.selectbox("Select Topic", list(st.session_state['messages'].keys()))
    new_message = st.sidebar.text_area("Enter your message")
    
    if st.sidebar.button("Post Message"):
        if username and new_message:
            st.session_state['messages'][topic].append(f"{username}: {new_message}")
            st.sidebar.success("Message posted!")
        else:
            st.sidebar.error("Please enter both username and message")

    # Main area to display messages
    st.title("SafeSpace Chat Forum")
    st.write("Select a topic from the sidebar to view and post messages.")
    
    def display_messages(topic):
        st.write(f"### {topic} Messages")
        for message in st.session_state['messages'][topic]:
            st.write(f"- {message}")
    
    # Display messages for the selected topic
    display_messages(topic)

if __name__ == '__main__':
    app()
