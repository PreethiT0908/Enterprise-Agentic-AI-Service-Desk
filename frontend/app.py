import streamlit as st
import requests

st.title("Enterprise Agentic AI Service Desk")

issue = st.text_area("Describe your issue")

if st.button("Submit Incident"):

    response = requests.post(
        "http://127.0.0.1:8000/api/v1/incidents",
        json={"message": issue}
    )

    if response.status_code == 200:
        result = response.json()

        st.subheader("Incident Analysis")
        st.json(result["incident"])

        st.subheader("Knowledge Base")
        st.json(result["knowledge"])

        st.subheader("Troubleshooting")
        st.json(result["troubleshooting"])

        st.subheader("Automation")
        st.json(result["automation"])

        st.subheader("Decision")
        st.json(result["decision"])

        if "ticket" in result:
            st.subheader("Ticket")
            st.json(result["ticket"])

            st.subheader("Routing")
            st.json(result["routing"])

            st.subheader("Notification")
            st.json(result["notification"])