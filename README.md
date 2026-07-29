# 📚 The Book Worm — Library Management System

A console-based **Library Management System** built in Python, backed by a MySQL database. It supports two roles — **Admin** and **User** — each with their own menu-driven workflow for managing books, members, and day-to-day library operations.

---

## ✨ Features

**Admin**
- 📖 Book Management — Add / View / Search / Update / Delete book records
- 👥 User Management — Add / View / Search / Update / Delete member records
- 🔐 Admin Management — Add / View / Search / Update / Delete admin accounts
- Login protected with a 3-attempt limit

**User**
- Browse the full book catalog
- Issue a book (with real-time availability check)
- View currently issued book(s)
- Return a book
- Leave feedback and rate the library out of 10
- Create an account and log in with a 3-attempt limit

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Database | MySQL |
| DB Connector | `mysql-connector-python` |
| Interface | Command-line (CLI) |

---

## 📁 Project Structure

```
LIBRARY_MANAGEMENT_SYSTEM/
├── Login.py            # Entry point — handles admin/user login & account creation
├── Main_menu.py         # Routes to the Admin or User menu after login
├── Operations.py        # Sub-menus that call into Books / User / Admin modules
├── Books.py              # All book-related database operations
├── User.py                # All user-related database operations
├── Admin.py                # All admin-account database operations
├── Tables.py                # Creates the MySQL tables on first run (+ seed data)
├── database/
│   └── schema.sql            # Standalone SQL schema, for manual DB setup/reference
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🗄️ Database Schema

Everything lives inside a MySQL database called `project`, across four tables:

| Table | Purpose | Key Columns |
|---|---|---|
| `BookRecord` | Every book in the library | `BookID` (PK), `BookName`, `Author`, `Publisher` |
| `UserRecord` | Every registered member | `UserID` (PK), `UserName`, `Password`, `BookID` (FK → BookRecord) |
| `AdminRecord` | Admin login credentials | `AdminID` (PK), `Password` |
| `Feedback` | Member feedback & ratings | `Feedback` (PK), `Rating` |

`Tables.py` creates these automatically the first time the app runs, and seeds a few sample users/admins for testing. See [`database/schema.sql`](database/schema.sql) if you'd rather set them up manually.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- MySQL Server installed and running
- pip

### 1. Clone the repository
```bash
git clone https://github.com/Ishaansinghal3/LIBRARY_MANAGEMENT_SYSTEM.git
cd LIBRARY_MANAGEMENT_SYSTEM
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up the database connection
Every module currently connects using:
```python
mydb = mysql.connector.connect(host="localhost", user="root", passwd="default", database="project")
```
Update `passwd` (and `user` / `host` if different) in **Admin.py, Books.py, Login.py, Operations.py, Tables.py, and User.py** to match your own MySQL setup. *(See "Known Limitations" below for a cleaner long-term fix.)*

### 4. Create the database
In MySQL:
```sql
CREATE DATABASE project;
```
The tables are created automatically the first time you run the app.

### 5. Run it
```bash
python Login.py
```

---

## 🧪 Sample Login (seed data)

| Role | ID | Password |
|---|---|---|
| User | `101` | `1234` |
| Admin | `Kunal1020` | `123` |

*(These come from `Tables.py`'s seed data — feel free to change or remove them.)*

---

## 🔭 Known Limitations & Future Improvements

- Database credentials are hardcoded in each file — moving them to environment variables (a `.env` file) would be safer and easier to maintain.
- A few queries build SQL using string formatting instead of fully parameterized queries — worth revisiting to guard against SQL injection.
- Passwords are stored in plain text — hashing (e.g. with `bcrypt`) would be a solid next step.
- No due-date/fine system yet for late returns.
- CLI only for now — a GUI (Tkinter) or web version (Flask/Django) would make a great v2.

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

## 👤 Author

**Ishaan Singhal**
B.Tech IT Engineering
