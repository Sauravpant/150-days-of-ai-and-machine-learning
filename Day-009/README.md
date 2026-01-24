### Day 9 – Introduction to SQLite

Today I explored **SQLite**, a lightweight, serverless, and self-contained relational database engine that runs embedded within applications, making it perfect for local data storage and manipulation.

---

#### **Key Points**

- **SQLite3 comes built-in with Python** – serverless, zero-configuration database in a single `.db` file
- Established connections using `sqlite3.connect()` and created **cursor objects** for query execution
- Performed **CRUD operations**: Create, Read, Update, Delete using SQL queries
- Used **parameterized queries** with `?` placeholders to prevent SQL injection
- Implemented **bulk inserts** with `executemany()` for efficient data insertion
- Applied **transaction management** with `commit()` and `rollback()` for error handling
- Created **database indexes** for query optimization and performance improvement
- Implemented **backup and restoration** using `shutil.copy()` to duplicate database files
- Properly closed connections to prevent database locks

---