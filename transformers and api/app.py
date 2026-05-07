import mimetypes
import streamlit as st
from api_key import api_key_medical 
import google.generativeai as genai
api_key = api_key_medical
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 0.2,
     "top_p": 0.95,
    "top_k": 50,
    "max_output_tokens": 1000,
    "response_mime_type": "text/plain"
}
     
model = genai.GenerativeModel(model_name="gemini-3-flash-preview", generation_config=generation_config)   
     
system_prompt= """

you are ai assistant specialized in liver imaging analysis and detremine if there signs of liver cancer or no

examine image carfully for abnormalities such as tumers,lesions and irrigular shapes

classify the image to only 2 categories :

1- cancer

2- normal

 

output requirments :

prediction  (cancer,normal)

confidence score (0:100 %)

explanation why you choose this category    """ 





st.set_page_config(layout="wide")
st.title("YOUR AI DOCTOR IS HERE")
st.image(r"C:\Users\omare\Downloads\download.jpg",width=1500)
upload_file = st.file_uploader("Upload your liver image ", type=["jpg", "jpeg", "png"])
if upload_file is not None:
    st.image(upload_file, caption="Uploaded Image", use_column_width=True)
    st.write("Processing the image...")
    
submit_button = st.button("analyze")    

if submit_button and upload_file is not None:
    image_data = upload_file.getvalue()
    mime_type= mimetypes.guess_type(upload_file.name)[0]
    image_parts=[{
        "data":image_data,
        "mime_type":mime_type
    }]
    prompt_parts=[
        image_parts[0],
        system_prompt
    ]
    response = model.generate_content(prompt_parts)
    st.write(response.text)
    
    