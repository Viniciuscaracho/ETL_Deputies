## Project Overview

This project is a comprehensive system divided into two main components: an ETL (Extract, Transform, Load) process implemented in Python, and a web application developed using Ruby on Rails. The ETL process fetches data from the Brazilian Chamber of Deputies' open data portal (https://www2.camara.leg.br/transparencia/dados-abertos/), processes it, and stores it in a PostgreSQL database. The web application then utilizes this data to provide a user-friendly interface for exploring detailed information about the deputies.

### ETL Component

The ETL process is responsible for:
1. **Extracting Data:** Fetching raw data from the Brazilian Chamber of Deputies' API.
2. **Transforming Data:** Cleaning, normalizing, and transforming the data into a structured format suitable for the web application.
3. **Loading Data:** Inserting the processed data into a PostgreSQL database.

#### Key Technologies and Tools
- **Python:** Main programming language for the ETL process.
- **Requests:** Python library used to make HTTP requests to the Chamber of Deputies' API.
- **Pandas:** Used for data manipulation and transformation.
- **SQLAlchemy:** Used for database operations.
- **PostgreSQL:** Database system used to store the processed data.

### Web Application Component

The web application is responsible for:
1. **User Interface:** Providing a web interface for users to interact with the data.
2. **Data Presentation:** Listing deputies and displaying detailed information about them.
3. **Database Interaction:** Querying the PostgreSQL database to fetch and display the necessary data.

#### Key Technologies and Tools
- **Ruby on Rails:** Main framework for the web application.
- **PostgreSQL:** Database system used to store and retrieve data.
- **Turbo (Hotwire):** Enhances the navigation experience by replacing only the necessary content without reloading the entire page.
- **Stimulus (Hotwire):** Adds dynamic behaviors to HTML elements with minimal JavaScript.

### Project Structure

\`\`\`
project-root/
│
├── etl/
│   ├── Entities
│      └── deputy.py 
│      └── propositions.py
│   ├── Extract
│      └── process.py 
│   ├── db_config.py
│   ├── main.py
│
├── web/
│   ├── app/
│   ├── config/
│   ├── db/
│   ├── public/
│   ├── Gemfile
│   ├── Gemfile.lock
│   └── ...
│
├── README.md
└── ...
\`\`\`

### How to Run the Project

#### ETL Component
1. **Setup the Python Environment:**
   - Navigate to the `etl` directory.
   - Install the required Python packages: \`pip install -r requirements.txt\`.
2. **Run the ETL Process:**
   - Execute the ETL script to fetch, process, and load data into the PostgreSQL database: \`python main.py\`.

#### Web Application Component
1. **Setup the Ruby on Rails Environment:**
   - Navigate to the `web` directory.
   - Install the required gems: \`bundle install\`.
   - Setup the database: \`rails db:create db:migrate db:seed\`.
2. **Run the Web Application:**
   - Start the Rails server: \`rails server\`.

### Usage

1. **Accessing the Web Application:**
   - Open a web browser and navigate to \`http://localhost:3000\`.
   - Browse the list of deputies.
   - Select a deputy to view detailed information.

### Future Enhancements

- Implement advanced search and filtering options.
- Add visualizations for statistical data.
- Integrate additional data sources.

---

This README provides an overview of the project, detailing its structure, setup, and usage instructions. Feel free to contribute or reach out for any collaboration opportunities!
