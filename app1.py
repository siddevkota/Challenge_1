import openai
import streamlit as st

openai.api_key = "YOUR_OPEN_AI_API_KEY"

def generate_social_media_post(combined_prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=combined_prompt,
        max_tokens=150,
        temperature=0.8
    )
    text = response.choices[0].text.strip()
    return text

def generate_image(combined_image_prompt):
    response = openai.Image.create(
        prompt=combined_image_prompt,
        n=1,
        size="1024x1024",
    )
    return response.data[0].url

st.title("Social Media Post Generator")

language = st.selectbox("Select Language", ["English", "Nepali", "Hindi", "Spanish", "French", "Japanese", "Korean", "Russian"])


static_prompt = f"""Act like a social media post generator. 
Include popular hashtags like #Travel, etc. and use emojis like 😃✈️❤️. 
Generate a short and sweet caption. If it is a list then include all the list but 
make it short. Generate according to the social media platform specified. Also keep
linebreakers after every 10-12 words. I want the post to be in this language: {language}.
""" 

prompt = st.text_area("Enter a prompt:")

image_prompt = "Should be images of objects. Do not add text to the image."

combined_image_prompt = f"{image_prompt} {prompt}"

combined_prompt = f"{static_prompt} {prompt}"

st.caption("_You can also specify the social media platform. For example: 'A post about travel on Instagram.'_")

if st.button("Generate"):    
    text = generate_social_media_post(combined_prompt)
    image_url = generate_image(combined_image_prompt)

    st.subheader("Generated Social Media Post:")
    st.code(text)

    st.image(image_url, caption='Generated Image', use_column_width=True)

st.markdown("<p style='text-align:center'>Created by: Team Corazon</p>", unsafe_allow_html=True)