# ML Metrics Tracker Frontend

This repository contains the Streamlit-based frontend for the ML Metrics Tracker application. The frontend allows users to interact with the system for dataset management, metrics evaluation, and viewing performance results.

---

## Features

- **Dataset Management**: Upload and preprocess datasets.
- **Metrics Evaluation**: Evaluate ML model performance metrics such as accuracy, precision, recall, and F1 score.
- **Metrics History**: View previously saved metrics for performance tracking.
- **User-friendly Interface**: Built using Streamlit for an intuitive and interactive user experience.

---

## Prerequisites

Ensure the following are installed on your system:
- Python 3.11+
- `pip` (Python package installer)

Backend services must be running and accessible for API interaction. Refer to the [Backend Repository](#) for details.

---

## Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-repo>/ml-metrics-tracker-frontend.git
   cd ml-metrics-tracker-frontend
Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
Install Dependencies
pip install -r requirements.txt
Environment Variables Create a .env file in the root directory with the following:
BACKEND_BASE_URL=http://127.0.0.1:8000  # Update based on your backend URL
Running the Application

Start the Streamlit application:

streamlit run app.py
Access the application in your browser at http://localhost:8501.

Project Structure

ml-metrics-tracker-frontend/
├── .env                # Environment variables
├── app.py              # Main Streamlit application entry point
├── api_client.py       # API client for interacting with the backend
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── venv/               # Virtual environment (not tracked in Git)
Usage

Dataset Management
Navigate to the "Datasets" section.
Upload datasets and preprocess them as needed.
Metrics Evaluation
Select a dataset and model type.
Click "Evaluate Metrics" to compute performance metrics.
Save metrics using the "Save Metrics" button.
Previous Results
View a history of saved metrics for tracking performance over time.
Known Issues

API Connectivity: Ensure the backend services are running and reachable. Update the .env file if the backend URL changes.
Dataset Upload Limits: Dataset size is limited by backend and network configurations.
Browser Cache: Clear your browser cache if changes to the Streamlit app are not reflected.
Future Enhancements

Improve UI/UX for a more seamless user experience.
Add a dashboard to visualize metrics trends over time.
Integrate user authentication for secure access.
Contributing

We welcome contributions! Follow these steps to contribute:

Fork the repository.
Create a new branch: git checkout -b feature-name.
Commit your changes: git commit -m "Add feature-name".
Push to the branch: git push origin feature-name.
Open a pull request.
License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

For questions or support, contact:

Developer Name: Your Name
Repository: GitHub Repository

This `README.md` provides clear instructions for setup, usage, and contribution. Let me know if you'd like any modifications!
