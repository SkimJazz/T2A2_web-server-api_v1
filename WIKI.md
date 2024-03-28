# Installation and Setup

## Development Environment (Local)

Here are the steps to download, setup, and install the necessary components for using this Flask 
Web Server API. Good luck!

From GitHub, clone the repository to your local machine:
1. **Clone the Repository**
   - Open your terminal and navigate to the directory where you want to clone the repository.
   - Run the following command to clone the repository:
     ```bash
     git clone <repository_url>
     ```
     Replace `<repository_url>` with the URL of the repository.

<br>

2. **Setup the Virtual Environment**
   - Navigate into the cloned repository:
     ```bash
     cd <repository_name>
     ```
     Replace `<repository_name>` with the name of the repository.
   - Create a virtual environment:
     ```bash
     python3 -m venv .venv  # python3 for Unix or MacOS
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       .venv\Scripts\activate
       ```
     - On Unix or MacOS:
       ```bash
       source .venv/bin/activate
       ```

3. **Install the Required Packages**
   - Install the required packages using pip:
     ```bash
     pip install -r requirements.txt
     ```
4. **Setup the Local Database**
   - Install PostgreSQL if it's not already installed. The installation process will vary 
     depending on your operating system. But this Flask Web Server API was developed in WSL
     using Ubuntu 20.04 LTS.
   - Create a new database in PostgreSQL.
   - Update the database URI in your application's configuration to match the local database 
     setup loacated in the .env.example file:
     ```python
     # .env.example
      DATABASE_URI = "postgresql://localhost:5432/your_database_name"
     ```
5. **Seed the Database**
   - Run the following commands in the terminal to seed the database with the initial data:
     ```bash
     flask db drop #To drop existing data in database
     flask db create #To create the database
     flask db seed  #To seed the database
     ```

6. **Client Setup (Insomnia)**
   - Install Insomnia if it's not already installed.
   - Download the Insomnia workspace file from the GitHub repo (Or should be included in the 
     projects zip file)
   - Import the workspace file into Insomnia.
   - Setup the API endpoints in Insomnia for testing.
