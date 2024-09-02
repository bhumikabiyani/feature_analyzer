import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)
version = 'models/gemini-1.5-flash'  
model = genai.GenerativeModel(version)

def generate_response(prompt, images):
    response = model.generate_content([prompt] + images)
    return response.text

def main():
    red_black_theme = """
    <style>
        body, .stApp {
            background-color: #000000;  /* Black background for the app */
            color: #ffffff;             /* White text */
        }
        .stTextInput > div > div > input {
            background-color: #000000;  /* Black background for input field */
            color: #ffffff;             /* White text in input field */
            border: 1px solid #f44336;  /* Red border for input fields */
        }
        .stButton > button {
            background-color: #f44336;  /* Red buttons */
            color: #ffffff;             /* White text on buttons */
            border: none;
        }
        .stButton > button:hover {
            background-color: #b71c1c;  /* Darker red on hover */
        }
        .stFileUploader > div > div {
            background-color: #000000;  /* Black background for file uploader */
            color: #ffffff;             /* White text in file uploader */
            border: 1px solid #f44336;  /* Red border for file uploader */
        }
        .stMarkdown {
            color: #ffffff;             /* White text for markdown content */
        }
        .css-1aumxhk {
            color: #ffffff;             /* Ensuring all other text is white */
        }
    </style>
    """
    st.markdown(red_black_theme, unsafe_allow_html=True)

    st.title("Red Bus User Assistance Web App")
    
    user_prompt = st.text_input("Enter your prompt:", "")

    uploaded_files = st.file_uploader("Upload Images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    col1, col2 = st.columns(2)

    with col1:
        describe_features = st.button("Describe Features")

    with col2:
        solve_query = st.button("Solve Query")

    left_col, right_col = st.columns([1, 2])  

    if uploaded_files:
        with left_col:
            images = [Image.open(file) for file in uploaded_files]

            for image, file in zip(images, uploaded_files):
                st.image(image, caption=file.name, width=200)  

        if describe_features:
            with right_col:
                st.write("Describing features from the screenshots...")
                feature_prompt = """Provide description of the features visible in the screenshots, focusing on bus amenities, layout, and any relevant visual information. If there is details of bus then along with description output a table with bus details in it."""
                response_text = generate_response(feature_prompt, images)
                st.markdown(response_text)

        if solve_query:
            if user_prompt:
                with right_col:
                    prompt="""Be assistive, easy to understand, and engaging in nature. Provide relevant information based on the screenshots and user query."""
                    st.write("Processing your query...")
                    if "details" in user_prompt.lower() and "bus" in user_prompt.lower():
                        prompt += """Provide the details of the bus in a table format. Include columns for Bus Name, Departure Time, Arrival Time, Price, and Available Seats. Also, give a short description of the bus features based on the screenshot."""
                    elif "offers" in user_prompt.lower():
                        prompt += """Check if there are any offers in the provided screenshots. If offers are found, list them. If no offers are found, respond with a message asking the user to check each bus manually or send more screenshots for analysis."""
                    elif "departure" in user_prompt.lower() or "arrival" in user_prompt.lower():
                        prompt += """Filter the bus list based on the specified departure or arrival times. Provide details such as bus name, departure time, and arrival time in a table format."""
                    elif "sort" in user_prompt.lower() and "price" in user_prompt.lower():
                        prompt += """Sort the buses based on price from low to high or high to low as requested. Include bus name, price, and other relevant details in a table format."""
                    elif "sort" in user_prompt.lower() and "rating" in user_prompt.lower():
                        prompt += """Sort the buses based on customer ratings from high to low. Provide bus name, rating, and other relevant details in a table format."""
                    elif "route" in user_prompt.lower() or "destination" in user_prompt.lower():
                        prompt += """Identify buses that travel to the specified destination. Include details like bus name, route, departure time, and price in a table format."""
                    elif "features" in user_prompt.lower() or "amenities" in user_prompt.lower():
                        prompt += """List the amenities available on each bus. Include columns for Bus Name, Amenities, and any special features. Provide a brief summary if detailed information is available."""
                    elif "help" in user_prompt.lower() or "guidance" in user_prompt.lower():
                        prompt += """Provide a brief guide on how to use the service or app effectively, including steps to search for buses, filter results, and book tickets."""
                    elif "feedback" in user_prompt.lower() or "complaint" in user_prompt.lower():
                        prompt += """Acknowledge the user's feedback or complaint and provide a polite response. Suggest steps for the user to officially lodge a complaint or provide feedback through appropriate channels."""

                    full_prompt = prompt + user_prompt
                    response_text = generate_response(full_prompt, images)
                    st.markdown(response_text)
            else:
                st.write("Please enter a query to solve.")
    else:
        st.write("Please upload screenshots to proceed.")

if __name__ == "__main__":
    main()
