import streamlit as st

def app():
    st.write('resources')
    
    resources = {
    "Government Initiatives and Helplines": {
        "National Commission for Women (NCW)": {
            "Helpline": "7827-170-170",
            "Website": "https://ncw.nic.in",
            "Description": "NCW provides support, counseling, and legal assistance to women in distress."
        },
        "Women's Helpline": {
            "Helpline Number": "181",
            "Description": "A 24-hour helpline for women in distress across India. This toll-free number provides immediate support and information about available resources and services."
        },
        "Police Emergency Services": {
            "Helpline Number": "100",
            "Description": "For immediate protection and assistance, women can contact the police, who have specially trained units to handle cases of domestic violence."
        },
        "Women Helpline": {
            "Phone": "1091",
            "Description": "This helpline is dedicated to providing assistance and support to women facing harassment and eve teasing. It's available nationwide."
        }
    },
    "Non-Governmental Organizations (NGOs)": {
        "Jagori": {
            "Website": "http://www.jagori.org/",
            "Phone": "8800996640",
            "Description": "Focuses on gender-based violence, including eve teasing, by conducting awareness programs and providing support to victims."
        }, 
        "SHEHA": {
            "Website": "https://www.snehamumbai.org/prevention-of-violence-against-women-and-children/",
            "Phone": "91675 35765",
            "Description": "Focuses on preventing violence against women and children in Mumbai through community-based interventions, crisis intervention, counseling, and empowering survivors to create safer environments."
        },
        "Aks":{
            "Website":"https://aksfoundation.org/",
            "Phone":"8793 088 814 ",
            "Description": "Dedicated to addressing sexual abuse and domestic violence by providing support, counseling, and education to survivors, promoting awareness, and working towards systemic change for safer communities."
            
        }    
    }
}
    for category, details in resources.items():
        st.subheader(category)
        for name, info in details.items():
            st.markdown(f"**{name}**")
            for key, value in info.items():
                st.write(f"{key}: {value}")
            st.write("---")
 