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
     python -m venv .venv
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
<br>

3. **Install the Required Packages**
   - Install the required packages using pip:
     ```bash
     pip install -r requirements.txt
     ```
<br>

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


6. **Client Setup (Insomnia)**
   - Install Insomnia if it's not already installed.
   - Download the Insomnia workspace file from the GitHub repo
   - Import the workspace file into Insomnia.
   - Setup the API endpoints in Insomnia for testing.
