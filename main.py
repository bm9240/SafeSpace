import streamlit as st 

from streamlit_option_menu import option_menu
import chatbot, forums, login , home, resources

st.set_page_config(
    page_title="SafeSpace",
)

def main():
    # Initialize session state for login
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    # If user is not logged in, show the login page
    if not st.session_state.logged_in:
        login.app()


    else:

        
        st.session_state.current_page = "Home"
        # Sidebar menu
        with st.sidebar:
            app = option_menu(
                menu_title='SafeSpace',
                options=['Home', 'ChatBot', 'Forums', 'Resources'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == "Home":
            home.app()
        elif app == "ChatBot":
            chatbot.app()    
        elif app == "Forums":
            forums.app()        
        elif app == 'Resources':
            resources.app()
        elif st.session_state.current_page == "Home":
            home.app()

if __name__ == "__main__":
    main()
