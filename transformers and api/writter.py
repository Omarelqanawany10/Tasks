import streamlit as st
from api_key import api_key_medical
import google.generativeai as model 
import mimetypes    
from api_key import api_writter

model.configure(api_key=api_writter)
generation_config = {
    "temperature": 02.0,
     "top_p": 0.95,
    "top_k": 50,
    "max_output_tokens": 1000,
    "response_mime_type": "text/plain"
}
model = model.GenerativeModel(model_name="gemini-3-flash-preview", generation_config=generation_config)  
st.set_page_config(layout="wide")
st.title("YOUR AI WRITTER IS HERE ... just give me a topic and i will write you a full article about it in seconds") 
st.image(r"C:\Users\omare\Downloads\download (1).jpg",width=1500)
with st.sidebar:
    title = st.text_input("Enter the title of the article you want to write")
    submit_button = st.button("write")
   
     
    keywords = st.text_area("Enter keywords for the article (you can enter multiple keywords separated by commas)")
    number_of_words = st.slider("Select the number of words for the article", min_value=250, max_value=1000, step=250)  
    prompet = [f"write a detailed article about {title} in {number_of_words} words and make sure to include the following keywords : {keywords} "]
    response = model.generate_content(prompet)
if  submit_button:
    st.write(response.text)