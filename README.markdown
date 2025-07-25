# AlumConnect 🌟

**AlumConnect** is a powerful, data-driven platform that connects students of the IIPS, DAVV Integrated MCA program with alumni. By leveraging web scraping and advanced data analytics, it provides actionable insights into career paths, hiring trends, and networking opportunities, fostering a thriving community for professional growth.

---

## 📋 Table of Contents

- [Features](#-features)
- [Technology Stack](#️-technology-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#-prerequisites)
  - [Installation](#️-installation)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [Project Lead](#-project-lead)
- [License](#-license)
- [Contact](#-contact)

---

## ✨ Features

- **Interactive Alumni Directory**: Easily search and filter alumni profiles by name, company, or role.
- **Insightful Dashboard**: Visualize career trends, top employers, and in-demand roles with dynamic charts.
- **Automated Data Acquisition**: Ethically scrape publicly available alumni data using custom Python scripts.
- **Community Contributions**: Alumni can submit and update their profiles to keep the directory up-to-date.

---

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript (React)
- **Database**: MySQL
- **Data Scraping**: Selenium, BeautifulSoup
- **Data Analysis**: Pandas, NumPy

---

## 🚀 Getting Started

Set up and run AlumConnect locally with these steps.

### 📋 Prerequisites

- Python 3.8 or higher
- PIP (Python package manager)
- MySQL Server 8.0 or higher
- Git

### 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/iuttkarshh0409/AlumConnect.git
   ```

2. **Navigate to the Project Directory**
   ```bash
   cd AlumConnect
   ```

3. **Set Up a Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure the Database**
   - Ensure MySQL Server is running.
   - Create a database named `alumconnect_db`:
     ```sql
     CREATE DATABASE alumconnect_db;
     ```
   - Update the database configuration in `config.py`:
     ```python
     DATABASE_CONFIG = {
         'host': 'localhost',
         'user': 'your_username',
         'password': 'your_password',
         'database': 'alumconnect_db'
     }
     ```

6. **Run the Application**
   ```bash
   flask run
   ```
   Visit `http://localhost:5000` in your browser.

---

## 🛠️ Troubleshooting

- **MySQL Connection Issues**: Ensure MySQL Server is running and credentials in `config.py` are correct.
- **Module Not Found**: Verify all dependencies are installed by re-running `pip install -r requirements.txt`.
- **Flask Not Starting**: Confirm the virtual environment is activated and Flask is installed (`pip show flask`).
- For further issues, check the [GitHub Issues](https://github.com/iuttkarshh0409/AlumConnect/issues) page.

---

## 🤝 Contributing

We welcome contributions to make AlumConnect even better! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

See our [Contributing Guidelines](CONTRIBUTING.md) for more details.

---

## 👨‍💻 Project Lead

- **Utkarsh Dubey** - *Project Lead & Backend Developer*  
  GitHub: [iuttkarshh0409](https://github.com/iuttkarshh0409) | Email: [dubeyutkarsh101@gmail.com](mailto:dubeyutkarsh101@gmail.com)

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

For questions or feedback, raise an issue on [GitHub](https://github.com/iuttkarshh0409/AlumConnect/issues) or email [dubeyutkarsh101@gmail.com](mailto:dubeyutkarsh101@gmail.com).

---

🌐 **Connect, Learn, Succeed with AlumConnect!**