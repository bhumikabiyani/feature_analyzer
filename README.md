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
### Prompting Strategy

### Prompting Strategy Description

The prompting strategy in the **User Assistance Web App** involves:

1. **Contextual Prompts**: Prompts are tailored based on user queries and the context provided by uploaded images. For example, if a user asks about "bus details," the app generates a prompt specifically asking for bus details visible in the screenshots.

2. **Task-Specific Prompts**: Different prompts are designed for specific tasks, such as describing bus features, listing offers, sorting buses by price or rating, and filtering by departure or arrival times. This ensures that the model provides precise and relevant responses.

3. **Adaptive Prompting**: The prompts adapt based on keywords identified in user queries. For example, if the query contains "sort by price," the prompt instructs the model to organize bus data by price. This approach enables the app to handle a wide range of user requests flexibly.

4. **Guidance and Engagement**: The prompts are crafted to be assistive, clear, and engaging, ensuring users receive easily understandable and actionable information. The strategy focuses on maintaining a conversational tone to enhance user experience.


## Usage

1. **Upload Images**: Click on the "Upload Images" button to select screenshots related to bus services.
2. **Describe Features**: Click the "Describe Features" button to get a description of visible features in the screenshots.
3. **Enter a Query**: Use the text input to enter a query (e.g., "Show bus details", "Any offers available?").
4. **Solve Query**: Click the "Solve Query" button to receive answers based on your query and the uploaded screenshots.

