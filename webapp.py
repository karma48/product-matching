import streamlit as st
import requests
import json

# Web app URL from Google Apps Script deployment
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbxjix8ID4jMzkHQ6JYeLJUsY21GDqZtdZgRtof8ntPGnnSoPPo9Vada6Y3-T1GkSf52eA/exec"

def query_google_sheets(query):
    response = requests.post(WEB_APP_URL, json={"query": query})
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        return []

def main():
    st.title('Mobile Search Application')

    query = st.text_input("Enter your search query:")

    if st.button('Search'):
        if query:
            results = query_google_sheets(query)
            st.write("Results:")
            for result in results:
                st.write(result)
        else:
            st.write("Please enter a query.")

if __name__ == '__main__':
    main()
