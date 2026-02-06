### Day 10 – Introduction to Python Logging

Today I explored **Python's logging module**, a robust framework for capturing, formatting, and managing log messages across applications for debugging, monitoring, and error tracking.

---

#### **Key Points**

- **logging module comes built-in with Python** – provides structured, configurable logging superior to `print()` statements
- Configured logging using `basicConfig()` with filename, filemode, level, format, and date format parameters
- **Logging Levels**: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` – control message severity and filtering
- Created **custom log formats** using format specifiers like `%(asctime)s`, `%(name)s`, `%(levelname)s`, `%(message)s`
- Used logging functions: `logging.info()`, `logging.warning()`, `logging.error()`, `logging.debug()`, `logging.critical()`
- **Created multiple loggers** for different modules using `getLogger()` with independent logging configurations
- Applied **different logging levels to individual loggers** for fine-grained control over output
- Implemented **handlers** like `StreamHandler` to direct logs to different destinations (console, files, email, etc.)
- **Logged to files** while simultaneously displaying output in the console for comprehensive monitoring
- Managed log file modes (`'w'` overwrite, `'a'` append) for different use cases
- Covered multithreading basics with `threading`, shared data, and race conditions
- Covered multiprocessing patterns and examples for CPU-bound tasks and isolation
- Covered a simple web scraping example using requests and HTML parsing
- Covered logging utilities and basic testing for reusable logger setup
- Practiced with logging notebooks to observe output formatting and levels
