# SAMB HEXAGONAL

# Stock Market Analysis System

## Description
The Stock Market Analysis System is a Django application that allows you to execute positions based on specific market conditions, using financial asset data, indicators, and multiple machine learning models.

## Features
- **Trend analysis** based on the last 5 market movements.
- **Utilization of three main indicators:**
  - SMA 50 (Simple Moving Average over 50 periods)
  - SMA 10 (Simple Moving Average over 10 periods)
  - RSI (Relative Strength Index)
- **Management of session reports** sent via SMTP, divided weekly into days and session type.
- **Implementation of hexagonal architecture**:
  - **Handlers (Presentations)**
  - **Controllers (Routers e instance of services)**
  - **Services (Routers of logic)**
  - **Entities (Business Logic)**
  - **Repositories (Persistence)**
- **Implementation of Unit Testing (TDD)**
- **Machine Learning Models:**
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Neural Network
- **Machine Learning Workflow:**
  - Creation
  - Training
  - Evaluation (Implementation of confusion matrices)
  - Predictions
  - Model Persistence

## Technologies Used
- **Programming Language:** Python
- **Framework:** Django
- **Libraries:**
  - Pandas (for data handling)
  - Scikit-learn (for Machine Learning models)
  - NumPy (for numerical operations)
  - Django Rest Framework (for building APIs)
  - TestCase (for unit testing the API and machine learning predictions)
  - Pickle (for saving and loading the machine learning models)
  - Decouple (for environment variable management)
  - Seaborn (for data visualization)
  - Matplotlib (for plotting graphs and charts)
- **Data Format:** JSON
- **Database:** MySQL (To provide traceability to positions)
- **Machine Learning Models:** Stored in `.pkl` files
- **Containerization:** Docker (Used for packaging and deploying the application in a consistent environment)

## Usage
To use the system, follow these steps:

### Trend Analysis
- Observe trends based on the last 5 market movements.

### Available Indicators
- Use SMA 50, SMA 10, and RSI indicators to make informed decisions on your positions.

### Machine Learning
- Utilize one of the four machine learning models (Logistic Regression, Decision Tree, Random Forest, Neural Network) to make informed trading decisions.

### Management Reports
- Schedule the sending of session reports via telegram.
- - Schedule the sending of crons reports via teelgram.

## License
This project is licensed under the MIT License.

