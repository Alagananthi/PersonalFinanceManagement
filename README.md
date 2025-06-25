# 💸 Personal Finance Management (PersonalFinance)

A simple and efficient **Python-based command-line application** designed to help individuals manage their personal finances.  
Built during my **MCA internship at InnoByte Services**, this app lets users record transactions, set monthly budgets, monitor financial reports, and even visualize expenses through pie charts.

---

## Folder Overview

PersonalFinanceApp/
│

├── main.py             # Main CLI program

├── db.py               # SQLite3 database connection and setup

├── auth.py             # User registration & login system

├── finance.py          # Add / view / edit / delete transactions

├── budget.py           # Monthly budget setting feature

├── reports.py          # Generates summaries & monthly reports

├── chart.py            # Pie chart visualization (matplotlib)

├── backup_restore.py   # Optional backup and restore logic

├── PersonalFinance.db  # Local SQLite database

└── README.md           # This file

##  What You Can Do With It


## 🚀 Key Functionalities

### 🔐 User Access
- Unique username registration
- Login system tied to local user data

### 💼 Income & Expense Management
- Add income and expense transactions
- Supports categorization (e.g., Salary, Food, Travel, Bills)
- View, edit, and delete entries

### 📉 Budget Management
- Set budget for each category per month
- Alerts when you exceed budget limits

### 📊 Reports & Analytics
- View financial summaries per user
- Pie chart to visualize expense categories (uses `matplotlib`)

### 💾 Backup System
- Save your database manually and restore it anytime

---

## 🛠 Technologies Used

| Component        | Technology       |
|------------------|------------------|
| Language         | Python 3.10       |
| Database         | SQLite3           |
| Visualization    | Matplotlib        |
| Testing (optional) | Pytest          |
| Environment      | CLI (Terminal)    |

---

## 🧪 How to Run the Project

### 🔧 Requirements

- Python 3.8 or higher
- pip (Python package manager)
---
### 📥 Installation Steps

1. **Clone this repository**
  
   git clone  https://github.com/Alagananthi/PersonalFinanceManagement.git
   
   cd PersonalFinanceManagement
   
2.**Install the required library**
   
    pip install matplotlib
    
3.**Run the application**
   python main.py

---
**Author**
Alagananthi E
Intern @ InnoByte Services
[MCA Student – Project Work]
GitHub
