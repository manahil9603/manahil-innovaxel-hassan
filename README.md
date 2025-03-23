# URL Shortener

A simple URL shortening service built with **Flask** (backend) and **HTML/CSS/JavaScript** (frontend). This project allows users to shorten long URLs, retrieve the original URLs, update or delete existing short URLs, and view access statistics.

---

## Features

- **Shorten URLs**: Convert long URLs into short, easy-to-share codes.
- **Retrieve Original URLs**: Get the original URL from a short code.
- **Update URLs**: Update the original URL associated with a short code.
- **Delete URLs**: Remove a short URL from the system.
- **URL Statistics**: View the number of times a short URL has been accessed.

---

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **API**: RESTful API with endpoints for CRUD operations

---

## Setup Instructions

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone git clone https://github.com/manahil9603/manahil-innovaxel-hassan.git 
```
### Step 2: Set Up the Backend
Navigate to the project directory:

```bash
cd manahil-innovaxel-hassan
```
#### Install the required Python packages:

```bash
pip install -r requirements.txt
```
#### Run the Flask application:

```bash
python app.py
```
The backend will start running at http://127.0.0.1:5000.

### Step 3: Set Up the Frontend
Open the frontend/index.html file in your browser (e.g., by double-clicking it or using a live server).
Interact with the frontend to shorten, retrieve, update, delete, and view statistics for URLs.

---
## How to Contribute
Fork the repository.

- Create a new branch (git checkout -b feature/YourFeatureName).
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature/YourFeatureName).
- Open a pull request.
