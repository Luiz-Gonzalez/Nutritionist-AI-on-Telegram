# Nutritionist AI on Telegram

This project is a Telegram bot that acts as a personal nutritionist, powered by AI. It leverages the LangChain framework and OpenAI's GPT models to provide a conversational interface for users to manage their diet and track their progress.

## How it Works

The bot is built using the `pyrogram` library to interact with the Telegram API. It handles text messages and photos, and uses a `NutritionistAgent` to process user requests. The agent is a LangChain agent that uses a set of tools to perform various tasks.

### Core Components

*   **Telegram Bot (`nutritionist/chat/telegram.py`):** This is the main entry point for the bot. It sets up handlers for different types of messages (text, photos, commands) and passes them to the `NutritionistAgent`.
*   **Nutritionist Agent (`nutritionist/agents/nutritionist.py`):** This is the brain of the bot. It uses a LangChain agent with a set of tools to handle user requests. The agent is responsible for understanding the user's intent and calling the appropriate tool to fulfill the request.
*   **Tools (`nutritionist/tools/`):** The tools are the individual functions that the agent can call to perform specific tasks. These include:
    *   `FoodImageAnalyzerTool`: Analyzes images of food to identify the ingredients and estimate nutritional information.
    *   `UserRegistrationTool`: Registers new users and collects their personal information (age, weight, height, etc.).
    *   `UserInfoTool`: Retrieves the user's information.
    *   `DietPlanTool`: Creates personalized diet plans based on the user's goals and preferences.
    *   `WeightUpdateTool`: Updates the user's weight.
    *   `MealEntryTool`: Records the user's meal entries.
    *   `ReportTool`: Generates reports on the user's progress.
*   **Database (`nutritionist/database/` and `nutritionist/repositories/`):** The bot uses a database to store user information, diet plans, meal entries, and weight history. The repositories provide an abstraction layer for interacting with the database.
*   **Models (`nutritionist/models/`):** These are the data models that represent the different entities in the system (User, DietPlan, MealEntry, etc.).

## Features

*   **Conversational Interface:** Users can interact with the bot in natural language.
*   **Food Image Analysis:** Users can send a photo of their meal, and the bot will analyze it to identify the food and provide nutritional information.
*   **Personalized Diet Plans:** The bot can create personalized diet plans based on the user's goals, preferences, and dietary restrictions.
*   **Progress Tracking:** Users can track their weight, log their meals, and generate reports to monitor their progress.
*   **User Management:** The bot can register new users and store their information.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Luiz-Gonzalez/Nutritionist-AI-on-Telegram.git
    ```
2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up the environment variables:**
    Create a `.env` file in the root directory and add the following variables:
    ```
    TELEGRAM_API_ID=<your_telegram_api_id>
    TELEGRAM_API_HASH=<your_telegram_api_hash>
    TELEGRAM_TOKEN=<your_telegram_bot_token>
    OPENAI_API_KEY=<your_openai_api_key>
    ```
4.  **Run the bot:**
    ```bash
    python nutritionist/app.py
