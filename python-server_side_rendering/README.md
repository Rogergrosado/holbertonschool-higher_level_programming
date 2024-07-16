# Server-Side Rendering with Flask Assignments

This repository contains Python Flask applications that demonstrate server-side rendering techniques using various data sources and templates.

## Assignments Overview

### 1. Basic HTML Template in Flask

**Objective:** Set up a basic Flask application to render a simple HTML template using Jinja for dynamic content rendering.

**Files:**
- `task_01_jinja.py`: Flask application script.
- `templates/` directory: Contains `index.html`, `header.html`, and `footer.html` templates.

### 2. Dynamic Template with Loops and Conditions

**Objective:** Enhance the Flask application to dynamically render content using Jinja's loop and conditional constructs from JSON data.

**Files:**
- `task_02_logic.py`: Flask application script.
- `items.json`: JSON file with items data.
- `templates/items.html`: HTML template for displaying items dynamically.

### 3. Displaying Data from JSON or CSV Files

**Objective:** Extend the Flask application to read and display product data from JSON or CSV files based on query parameters.

**Files:**
- `task_03_files.py`: Flask application script.
- `products.json`: JSON file with product data.
- `products.csv`: CSV file with product data.
- `templates/product_display.html`: HTML template for displaying products.

### 4. Extending Dynamic Data Display to Include SQLite in Flask

**Objective:** Integrate SQLite database functionality into the Flask application to fetch and display product data.

**Files:**
- `task_04_db.py`: Flask application script.
- `create_database.py`: Python script to create and populate SQLite database (`products.db`).
- `products.db`: SQLite database file.
- `templates/product_display.html`: Same as in Task 3, used to display products.

## Running the Applications

1. Install Flask if not already installed:
   ```bash
   pip install Flask

