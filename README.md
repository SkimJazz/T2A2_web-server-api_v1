# GeoLab API

## Project Overview and Requirements

---

### R1️⃣: Problem Identification

The aim of this web server API project is to address the challenges faced by Geotechnical 
engineering companies in managing projects and testing processes. The current system, which relies 
heavily on physical documents such as Test-Requests, presents several problems:

1. **Data Loss**: Physical documents are susceptible to loss or damage, leading to significant data 
loss that can disrupt operations.
2. **Inefficiency**: Managing and retrieving information from physical documents is time-consuming, 
slowing down the testing process and leading to inefficiencies.
3. **Lack of Real-Time Updates**: Physical documents do not allow for real-time updates or easy 
sharing of information, leading to communication gaps and delays in decision-making.
4. **Storage Issues**: Physical documents require storage space, and as the volume of tests 
increases, so does the need for storage, leading to clutter and difficulties in organizing and 
retrieving documents.
5. **Error-Prone**: (Human-Prone) Manual entry of data increases the likelihood of errors, 
affecting the accuracy of test results and leading to incorrect conclusions.

By building a web server API, we aim to provide a centralized platform where users can manage 
projects, allocate tests, and track testing progress efficiently. This digital transformation will
effectively address the above challenges, leading to improved efficiency, accuracy, and 
collaboration in the laboratory environment. Thus, the development of this API is a solution to a 
real-world problem that needs solving. It will revolutionize the way Geotechnical engineering 
companies manage their projects and testing processes, making them more streamlined and efficient.

---

### R2️⃣: Why is it a problem that needs solving?

Without a dedicated system, managing projects and tests in engineering companies can be cumbersome 
and prone to errors. Coordination between different teams involved in testing processes can be 
challenging without a centralized platform. Automating these processes can streamline operations, 
reduce errors, and improve overall efficiency. This Flask Web Server API addresses several key 
challenges in managing projects in a Geotechnical Engineering laboratory environment:


- The most important is **Elimination of Physical Documentation**: In a traditional laboratory 
environment, managing hard copies of Test-Requests and other physical representations of laboratory 
workings can be cumbersome and prone to errors. The API digitizes these processes, making it easier
to track, manage, and archive test requests and results.

- **Centralized Data Management**: The API provides a centralized system for storing and managing 
data related to engineering companies, projects, users, and tests. This eliminates the need for 
disparate systems and streamlines data management.

- **Improved Efficiency**: By automating data entry and retrieval processes, the API can 
significantly reduce the time and effort required to manage projects, thereby improving efficiency.

- **Enhanced Collaboration**: The API facilitates better collaboration among different entities 
such as engineering companies, project teams, and testers. It allows for easy sharing and access 
of project and test data.

- **Scalability**: The API is designed to handle a large amount of data, making it suitable for 
large-scale projects involving numerous tests.

- **Real-time Access**: The API allows for real-time access to data, enabling quick decision-making
and timely project management.

  
The development of this API is a strategic move towards solving the complexities 
involved in managing projects in a laboratory environment. It not only simplifies data management 
but also enhances operational efficiency and collaboration. It addresses the challenges of managing 
physical documentation, thereby reducing errors and improving the overall workflow.


---

### R3️⃣: Chosen database system? What are the drawbacks compared to others?

I have chosen PostgreSQL as the database system for this Flask Web Server API project, and 
here's why:

- **Robustness and Reliability**: PostgreSQL is renowned for its stability and dependability. 
It ensures a high degree of data integrity and accuracy, which is vital for an application like 
this that oversees crucial project management and testing procedures.

- **Complex Relational Data Support**: PostgreSQL is capable of handling intricate relational data 
models. This is advantageous for this project, which involves multiple entities (User, Engineering 
Company, Project, Test, Testing) with various interconnections.

- **Advanced Features**: PostgreSQL comes with sophisticated features such as JSON data types 
support, full-text search, and comprehensive indexing capabilities. These features can significantly
enhance the application's functionality and performance.

- **Scalability**: PostgreSQL is highly scalable, capable of managing a large number of concurrent 
users and substantial data volumes. This is beneficial for a web server API like this one, which 
will need to scale up to accommodate increased traffic or data.

But, like any other database system, PostgreSQL has its limitations. Compared to other databases
like MySQL or SQLite, PostgreSQL is more challenging to learn and definitely demanded more 
resources in terms of memory(my Brain) and CPU. This could potentially make it more difficult to set
up and manage, particularly for smaller teams or projects with limited resources.

For instance, **SQLite** is a lightweight database that is simple to set up and use. It doesn't 
necessitate a separate server process and allows the database to be stored in a single file on disk.
This makes it an excellent choice for smaller projects or for development and testing environments.
However, SQLite lacks some of the advanced features of PostgreSQL and is not as scalable, making it
less suitable for larger, more complex applications.

On the other hand, **MySQL** is also a popular choice for web applications. It is user-friendly and 
delivers good performance. However, it doesn't fully comply with SQL standards and lacks some of 
the advanced features provided by PostgreSQL.

So, while PostgreSQL might require more setup and resources, its robustness, advanced 
features, and scalability make it a suitable choice for this Flask Web Server API project. However,
the choice between PostgreSQL, SQLite, and MySQL would depend on the specific requirements and 
constraints of the project. For smaller projects or for development and testing environments, 
SQLite could be a good choice due to its simplicity and ease of setup. On the other hand, for 
larger, more complex applications that require advanced features and scalability, PostgreSQL would 
be more suitable.

---

### R4️⃣: Identify and discuss the key functionalities and benefits of an ORM.

Object-Relational Mapping (ORM) simplifies database interactions by abstracting away the
complexities of SQL queries. Key functionalities and benefits include:

- **Simplified database operations:**
    Developers can interact with the database using familiar object-oriented paradigms, reducing the 
    need to write raw SQL queries.

- **Portability:**
    ORM frameworks often support multiple database systems, allowing easy migration between different 
    databases.

- **Abstraction of database schema:**
    Changes to the database schema can be handled transparently by the ORM, minimizing the impact on 
    application code.

- **Improved security:**
    ORM frameworks often provide mechanisms to mitigate common security vulnerabilities such as SQL 
    injection.

- **Increased productivity:**
    ORM reduces boilerplate code, allowing developers to focus on application logic rather than 
    database interactions.
- **Improved code Quality:**
    ORM frameworks enforce best practices and design patterns, leading to cleaner and more maintainable 
    code.


In the context of this Flask application, the selection of **SQLAlchemy** as the ORM system brings 
several key benefits and functionalities. This Flask web server API project can engage with the 
database securely and efficiently through SQLAlchemy. Furthermore, it aids in maintaining the 
codebase clean and manageable. The following are some of the key functionalities and benefits of
SQLAlchemy in this project:


1. **Simplified Database Operations**: SQLAlchemy allows developers to interact with the database 
using Python, which is more intuitive and less error-prone than writing raw SQL queries. 
For example, in the `cli_contr.py` file, the `create_tables` and `drop_tables` functions use 
SQLAlchemy's `create_all` and `drop_all` methods to create and drop tables in the database.

2. **Data Abstraction**: SQLAlchemy provides a high-level, Pythonic interface to the database that 
abstracts the underlying SQL. This means that developers can focus on the business logic of the 
application, rather than the specifics of the SQL syntax. For instance, in the `user_contr.py` 
file, the `UserRegister` class uses SQLAlchemy to add a new user to the database without having to 
write any SQL.

3. **Security**: SQLAlchemy automatically escapes data that is sent in a query, protecting the 
application from SQL injection attacks. This is evident in the `proj_contr.py` file, where 
user-provided data is used to update a project in the database.

4. **Database Agnosticism**: SQLAlchemy supports multiple database systems, which means that you 
can switch the underlying database of this Flask application without changing the Python code that 
interacts with it. The `.env` file shows that this application is currently using a PostgreSQL 
database, but it could easily be switched to another database supported by SQLAlchemy.

5. **Session Management and Transactions**: SQLAlchemy provides a session for managing transactions.
In this application, you can see this in action in the `seed_tables` function in the `cli_contr.py` 
file, where a series of database operations are committed to the database at once.

6. **Relationships and Joins**: SQLAlchemy provides an abstraction for dealing with relationships 
between tables in a database. In the `project_test.py` file, a many-to-many relationship is created 
between the `Project` and `Test` models using SQLAlchemy's relationship function.




---
### R5️⃣: API Endpoints

The following are the API endpoints that are implemented in this Web Server application:
Refer to GitHub Repo to download the Insomnia JSON file for the API Endpoints.


**Users:**

- `POST /register` - Create new user (Super & Admin)
- `POST /login` - Authenticate user
- `GET /user/<id>` - Get user by ID
- `DEL /user/<id>` - Delete user by ID (Admin)

**Companies:**

- `GET /company` - Get list of all companies
- `GET /company/<id>` - Get company by ID
- `POST /company` - Register new company (Admin)
- `DEL /company/<id>` - Delete company by ID (Admin)

**Projects:**

- `GET /project` - Get all project data
- `GET /project/<id>` - Get project by ID
- `POST /project` - Create new project (Admin)
- `PUT/project/<id>` - Update project by ID (User)
- `DEL/project/<id>` - Delete project by ID (Admin)

**Tests:**

- `GET/company/<id>/test` - Get List of Tests in a Company by ID
- `GET/test/<id>` - Get info on a Test by ID
- `POST/company/<id>/test` - Create a Test in a Company
- `POST/project/<id>/test/<id>` - Link a Project in a Company with a Test from same Company
- `DEL/project/<id>/test` - Unlink Test from a Project
- `DEL/test/<id>` - Delete a Test with no associated Projects (Admin)

<br>

#### 🌐 USER ENDPOINTS


1. **Endpoint: `/register`**
   - **HTTP Request Verb: `POST`**
     - Description: `Create a new user`
     - Required Data: `username`, `password`, `email`, and optionally `is_admin`
     - Expected Response Data: A message indicating successful user creation
     - Authentication Methods: None

<br>

2. **Endpoint: `/login`**
   - **HTTP Request Verb: `POST`**
     - Description: `Authenticate user`
     - Required Data: `username` and `password`
     - Expected Response Data: An access token for the authenticated user
     - Authentication Methods: None
   
<br>

3. **Endpoint: `/user/<int:user_id>`**
   - **HTTP Request Verb: `GET`**
     - Description: `Get user by ID`
     - Required Data: `user_id` (in the URL)
     - Expected Response Data: User details
     - Authentication Methods: None

   - **HTTP Request Verb: `DEL`**
     - Description: `Delete user by ID`
     - Required Data: `user_id` (in the URL)
     - Expected Response Data: A message indicating successful user deletion
     - Authentication Methods: JWT (JSON Web Token) authentication, with admin privileges required

<br>

#### 🌐 COMPANY ENDPOINTS

1. **Endpoint: `/company`**
    - **HTTP Request Verb: `GET`**
        - Description: `Get list of all Companies`
        - Required Data: None
        - Expected Response Data: A list of all companies in the `CompanyModel`.
        - Authentication Methods: None
    - **HTTP Request Verb: `POST`**
        - Description: `Create New Company`
        - Required Data: Accepts a `CompanySchema` object as input.
        - Expected Response Data: Returns the created company in the `CompanyModel`. If a company with the same name already exists, it returns a `400` status code. If there's an error creating the company, it returns a `500` status code.
        - Authentication Methods: None

<br>

2. **Endpoint: `/company/<string:company_id>`**
    - **HTTP Request Verb: `GET`**
        - Description: `Get Company by ID`
        - Required Data: None
        - Expected Response Data: Returns the company in the `CompanyModel` with the given `company_id`.
        - Authentication Methods: None
      
    - **HTTP Request Verb: `DEL`**
        - Description: `Delete Company by ID`
        - Required Data: None
        - Expected Response Data: Deletes the company in the `CompanyModel` with the given `company_id`. Returns a `200` status code with a message "Company deleted".
        - Authentication Methods: This endpoint requires JWT authentication and admin privileges.

<br>

#### 🌐 PROJECT ENDPOINTS


1. **Endpoint: `/project/<string:project_id>`**
    - **HTTP Request Verb: `GET`**
      - Description: `Get Project by ID`
      - Required Data: `project_id` in the URL
      - Expected Response Data: Returns the project with the given `project_id`. If the project does not exist, it returns a 404 status code with the message "Project does not exist."
      - Authentication Methods: None

   - **HTTP Request Verb: `DEL`**
     - Description: `Delete Project by ID`
     - Required Data: `project_id` in the URL
     - Expected Response Data: If the project does not exist, it returns a 404 status code with the message "Project does not exist." Otherwise, it deletes the project and returns a message "Project deleted."
     - Authentication Methods: JWT authentication and admin privileges

   - **HTTP Request Verb: `PUT`**
     - Description: `Update Project by ID`
     - Required Data: `project_id` in the URL and `project_data` in the request body
     - Expected Response Data: If the project does not exist, it creates a new project with the given `project_id` and the provided data. If the project exists, it updates the project with the new data provided.
     - Authentication Methods: None

<br>

2. **Endpoint: `/project`**
   
    - **HTTP Request Verb: `GET`**
      - Description: `Get all project data from the database`
      - Required Data: None
      - Expected Response Data: Returns a list of all projects in the database.
      - Authentication Methods: None
      
    - **HTTP Request Verb: `POST`**
      - Description: `Create New Project`
      - Required Data: `project_data` in the request body
      - Expected Response Data: Before creating the project, it checks if the company exists and if a project with the same name exists in the same company. If the company does not exist, it returns a 400 status code with the message "Company does not exist." If a project with the same name exists in the same company, it returns a 400 status code with the message "A project with this name already exists in this company." Otherwise, it creates the project and returns the project data.
      - Authentication Methods: None

<br>

#### 🌐 TEST ENDPOINTS


1. **Endpoint**: `/company/<string:company_id>/test`
    - **HTTP Request Verb: `GET`**
      - Description: `Get List of Tests in a Company by ID`
      - Required Data: `company_id` in the URL
      - Expected Response Data**: A list of all tests for the specified company
      - Authentication Methods**: None

    - **HTTP Request Verb: `POST`**
      - Description: `Create a Test in a Company`
      - Required Data: `company_id` in the URL and `test_data` in the body
      - Expected Response Data: The created test
      - Authentication Methods: None

<br>

2. **Endpoint**: `/project/<string:project_id>/test/<string:test_id>`
    - **HTTP Request Verb: `POST`**
      - Description: `Link a Project in a Company with a Test from the same Company`
      - Required Data: `project_id` and `test_id` in the URL
      - Expected Response Data: The test that was added to the project
      - Authentication Methods: None

    - **HTTP Request Verb: `DEL`**
      - Description: `Unlink Test from a Project`
      - Required Data: `project_id` and `test_id` in the URL
      - Expected Response Data: A message indicating the project was removed from the test, and the project and test data
      - Authentication Methods: JWT token and admin role

<br>

3. **Endpoint**: `/test/<string:test_id>`
    - **HTTP Request Verb: `GET`**
      - Description: `Get info on a Test by ID`
      - Required Data: `test_id` in the URL
      - Expected Response Data: The requested test
      - Authentication Methods: None

    - **HTTP Request Verb: `DEL`**
      - Description: `Delete a Test with no associated Projects`
      - Required Data: `test_id` in the URL
      - Expected Response Data: A message indicating the test was deleted, or an error message if the test is associated with any projects
      - Authentication Methods: JWT token and admin role


___


### R6️⃣: Entity Relationship Diagram (ERD)


The ERD (Entity-Relationship Diagram) for the application will illustrate the relationships between 
the User, Engineering Company, Project, Test, and Testing entities, including their attributes and 
cardinalities.


![Alt text](/assets/ERD_GeoLab(2).png?raw=true "ERD_GeoLab")
Entity-Relationship Diagram (ERD) for GeoLab API project

 

---

### R7️⃣: Detail any third-party services that your app will use

Third-party services included in the application are:

- **Flask**: Flask is a lightweight WSGI web application framework. It is designed to make getting 
started quick and easy, with the ability to scale up to complex applications. It began as a 
simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web 
application frameworks.

- **Flask-Smorest**: Flask-Smorest is an extension for Flask that adds support for quickly building
REST APIs. It is built on top of Flask, Marshmallow, and Webargs. It provides a set of tools to 
simplify the creation of RESTful APIs, including input parsing, output formatting, and automatic 
API documentation generation. 

- **Python-dotenv**: Python-dotenv is a Python module that allows you to specify environment 
variables in traditional UNIX-like ".env" files. It reads key-value pairs from a .env file and can 
set them as environment variables. It helps in the development of applications following the 
12-factor principles.

- **Psycopg2-binary**: Psycopg2-binary is a PostgreSQL database adapter for Python. It is a 
fully-featured PostgreSQL adapter and it supports many PostgreSQL features like notifications, 
asynchronous queries, COPY command, etc. It is designed for multi-threaded applications and manages
its own connection pool.

- **SQLAlchemy**: SQLAlchemy is a SQL toolkit and Object-Relational Mapping (ORM) system for Python.
It provides a full suite of well-known enterprise-level persistence patterns, designed for efficient
and high-performing database access, adapted into a simple and Pythonic domain language.

- **Flask-SQLAlchemy**: Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy
to your application. It aims to simplify using SQLAlchemy with Flask by providing useful defaults 
and extra helpers that make it easier to accomplish common tasks.

- **Flask-JWT-Extended**: Flask-JWT-Extended is an extension for Flask that adds support for JSON 
Web Tokens (JWT) to your application. It provides secure and easy-to-use JWT-based authentication 
and authorization for Flask applications.

- **Passlib**: Passlib is a password hashing library for Python. It provides cross-platform 
implementations of over 30 password hashing schemes, and also offers a framework for managing 
existing password hashes, and a large collection of utilities for various tasks such as password 
generation, password hashing, password verification, etc.

---

### R8️⃣: Description of the Project's Models and there relationships

In the context of this projects models and there relationships, this Web Server API project, 
has several models interacting to represent different entities. These models include `
COMPANY`, `USER`, `PROJECT_TEST`, `TEST`, and `PROJECT`. Each model has unique attributes and 
relationships that define their interactions.

The **COMPANY** model represents engineering companies, each uniquely identified by `company_id`. 
It has attributes such as `name`, `registration number`, `industry sector`, and `services` that 
provide detailed information about the company. In the code, it's related to the `USER` and 
`PROJECT` models. 

The **USER** model represents users, each uniquely identified by `user_id`. It stores the user's 
login credentials and contact information in attributes like `username`, `password`, and `email`. 
In the code, it's related to the `COMPANY` model through `company_id`.

The **PROJECT_TEST** model acts as a junction table between the `PROJECT` and `TEST` models. It's 
uniquely identified by `project_test_id` and stores the identifiers of the related project and test 
through `project_id` and `test_id`.

The **TEST** model represents tests, each uniquely identified by `test_id`. It has attributes like 
`name`, `description`, `test_type`, and `test_method` that provide detailed information about the 
test. In the code, it's related to the `COMPANY` model through `company_id` and is connected to the
`PROJECT` model via the `PROJECT_TEST` model.

The **PROJECT** model represents projects, each uniquely identified by `project_id`. It has 
attributes like `name`, `budget`, `description`, and `client` that provide detailed information 
about the project. In the code, it's related to the `COMPANY` model through `company_id` and is 
connected to the `TEST` model via the `PROJECT_TEST` model.

For the parent-child relationships, the `CompanyModel` is a parent to `ProjectModel`, `TestModel`, 
and `UserModel`, indicated by the `db.relationship` function calls in the `CompanyModel` 
class. The `back_populates` argument is used to specify the attribute that should be used on the 
related model for the back-reference. 

The `ProjectModel` and `TestModel` are children to `CompanyModel`, represented by the company 
attribute and the `company_id` foreign key. They also have a many-to-many relationship with each 
other through the `ProjectTest` association table. This is represented by the tests attribute in 
`ProjectModel` and the projects attribute in `TestModel`, which are dynamic SQLAlchemy relationships.

The `ProjectTest` model serves as an association table for the many-to-many relationship between 
`ProjectModel` and `TestModel`. It has two foreign keys, `project_id` and `test_id`, which reference
the primary keys of the `ProjectModel` and `TestModel` tables respectively.

The `UserModel` is a child to `CompanyModel`, represented by the company attribute and the 
`company_id` foreign key.

These relationships allow for efficient querying and manipulation of related data. For example, you 
can easily retrieve all projects associated with a company, or all tests associated with a project.

The models and their relationships represented in the ERD are depicted clearly. The ERD shows
five entities: COMPANY, USER, PROJECT_TEST, TEST, and PROJECT. The `PROJECT_TEST` model serves as a 
junction table facilitating many-to-many relationships between `PROJECT` and `TEST`. This design 
allows each project to have multiple tests and each test to be associated with multiple projects.
It also enables users to be associated with multiple companies and projects. This structure provides
flexibility and scalability, making it suitable for a web server API project in a geotechnical 
engineering laboratory.

---

### R9️⃣: Database relations to be implemented

With reference to the ERD, The Geotechnical Engineering Laboratory Web Server API project involves 
several models that interact with each other to represent different entities. These models include 
`ENGO COMPANY`, `USER`, `PROJECT_TEST`, `TEST`, and `PROJECT`. Each model has unique attributes and
relationships that define their interactions.

The `ENGO COMPANY` model represents engineering companies and is related to the `USER` and `PROJECT`
models. The `USER` model represents users and is related to the `ENGO COMPANY` model. The 
`PROJECT_TEST` model acts as a junction table between the `PROJECT` and `TEST` models. The `TEST` 
model represents tests and is related to the `ENGO COMPANY` model and connected to the `PROJECT` 
model via the `PROJECT_TEST` model. Lastly, the `PROJECT` model represents projects and is related 
to the `ENGO COMPANY` model and connected to the `TEST` model via the `PROJECT_TEST` model.

This structure facilitates many-to-many relationships between `PROJECT` and `TEST`, providing 
flexibility and scalability suitable for a web server API project in a geotechnical engineering 
laboratory. The ERD effectively depicts these relationships and provides a visual representation of
the database schema. It serves as a useful tool for understanding the data flow and relationships 
within the system. This understanding is crucial for the successful implementation and management 
of the project. 

The ERD and the associated models provide a comprehensive view of the entities involved in 
this Web Server API project and their interrelationships. This understanding is vital for effective
database design and management, ensuring the project's success.

---

### R🔟: Describe the way tasks are allocated and tracked in this project

Tasks that need to be completed for the project that are currently in Trello and need images. 
The tasks are divided into different categories based on the project's requirements and priorities.


**Project Setup**
- Card: Create a new Python virtual environment.
- Card: Install Flask, SQLAlchemy, and other required libraries.
- Card: Initialize the Flask app and set up configurations.

**Database Design**
- Card: Develop ERD diagrams for `Company`, `User`, `Project`, `Test`, and `ProjectTest` models.
- Card: Implement the models in Python using SQLAlchemy ORM.

**API Design**
- Card: Create controllers (`cli_contr.py`, `comp_contr.py`, etc.) to handle requests.
- Card: Implement CRUD operations for each resource.

**User Authentication**
- Card: Implement user registration functionality.
- Card: Implement user login functionality.
- Card: Set up JWT authentication and define user roles and permissions.

**Testing**
- Card: Write unit tests for each endpoint.
- Card: Perform integration testing for the entire application.

**Documentation**
- Card: Document the API endpoints and their usage.
- Card: Write a comprehensive README for the project.

**Deployment**
- Card: Prepare the application for deployment.
- Card: Deploy the application to a production server.

