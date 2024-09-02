# User Assistance Web App

## Overview

The **User Assistance Web App** is a Streamlit application that assists users in obtaining information about bus services based on uploaded screenshots. The app uses the Google Generative AI (Gemini) model to provide descriptions of bus features, solve queries, and respond to user requests based on visual and textual input.

## Features

- **Image Upload**: Users can upload multiple screenshots (JPEG, JPG, PNG) related to bus services.
- **Feature Description**: Describes visible features in the uploaded screenshots, such as bus amenities and layout.
- **Query Resolution**: Responds to user queries about bus details, offers, routes, amenities, and more.
- **Interactive Interface**: Users can enter prompts and receive responses in a user-friendly manner.

## Prerequisites

- Python 3.7 or higher
- Streamlit
- Google Generative AI SDK (`google-generativeai`)
- PIL (Python Imaging Library)
- dotenv

## Setup and Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/feature_analyzer.git
    cd feature_analyzer
    ```

2. **Install the Required Packages**

    Install the necessary Python packages using pip:

    ```bash
    pip install -r requirements.txt

    ```

3. **Configure API Key**

    - Create a `.env` file in the root directory of your project.
    - Add your Google Generative AI API key to the `.env` file:

    ```bash
    GEMINI_API_KEY=your_gemini_api_key
    ```

4. **Run the Application**

    Launch the Streamlit app using the following command:

    ```bash
    streamlit run app.py
    ```

## Usage

1. **Upload Images**: Click on the "Upload Images" button to select screenshots related to bus services.
2. **Describe Features**: Click the "Describe Features" button to get a description of visible features in the screenshots.
3. **Enter a Query**: Use the text input to enter a query (e.g., "Show bus details", "Any offers available?").
4. **Solve Query**: Click the "Solve Query" button to receive answers based on your query and the uploaded screenshots.

