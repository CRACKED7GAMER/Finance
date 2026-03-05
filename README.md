AI Personal Finance Advisor
Overview

AI Personal Finance Advisor is a web-based financial management application developed using Python and Streamlit. The system provides users with a centralized platform to monitor financial activities, analyze investment data, and calculate loan payments.

The application is designed to simplify financial decision-making through interactive visualizations and an intuitive dashboard interface.

Features

Secure user login system

Interactive financial dashboard

Investment data visualization

Loan payment calculator

CSV dataset upload support

Real-time charts and analytics

Multi-page navigation interface

Technologies Used
Technology	Purpose
Python	Core programming language
Streamlit	Web application framework
Pandas	Data processing and analysis
Plotly	Interactive data visualization
CSV	Data storage format
Project Structure
AI-Personal-Finance-Advisor
│
├── app.py
├── dataset.csv
├── requirements.txt
└── README.md

app.py – Main Streamlit application file

dataset.csv – Sample financial dataset

requirements.txt – Project dependencies

README.md – Project documentation

Installation
1. Clone the Repository
git clone https://github.com/yourusername/ai-personal-finance-advisor.git
2. Navigate to the Project Directory
cd ai-personal-finance-advisor
3. Create a Virtual Environment
python -m venv venv
4. Activate the Virtual Environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
5. Install Dependencies
pip install -r requirements.txt
Running the Application

Start the Streamlit application using the following command:

streamlit run app.py

The application will run locally and can be accessed through:

http://localhost:8501
Default Login Credentials

For demonstration purposes, the application includes a basic login system.

Username: admin
Password: 1234
Application Modules
Dashboard

Provides a visual overview of financial data through interactive charts and summaries.

Investments

Allows users to view and analyze investment-related information.

Loan Calculator

Calculates loan repayment amounts based on principal amount, interest rate, and loan duration.

Future Enhancements

AI-based financial recommendation system

Machine learning model for expense prediction

Secure database authentication

Budget planning and tracking module

Cloud deployment and API integration

Author

Harish Vetrivel
Artificial Intelligence Student
Interested in Artificial Intelligence, Machine Learning, and Financial Technology.

License

This project is developed for educational and academic purposes.
