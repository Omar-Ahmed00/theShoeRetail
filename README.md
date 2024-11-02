
# The Shoe Retail Project

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Welcome to **The Shoe Retail Project**, a comprehensive data engineering and web application project developed as part of the DEPI program. This project simulates the data management and retail operations of a multi-branch shoe store.

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Database Design](#database-design)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

---

## Overview

The Shoe Retail Project is built to manage essential operations for a multi-chain shoe retail business, focusing on data engineering practices such as data collection, cleaning, and database warehousing. The project consists of eight primary tables: **Customer**, **Supplier**, **Employee**, **Inventory**, **Order**, **Sales**, **Product**, and **Branches**, each representing core data points for business processes.

This project also features a Flask-based web application providing a user interface for managing sales, inventory, customer information, and employee details across multiple branches.

## Project Structure

The project is organized as follows:

- **app**: Contains Flask application files
- **static**: Holds all static assets (CSS, JavaScript, images)
- **templates**: HTML files for the web application
- **data**: Includes CSV files used for data import/export, including branches, inventory, and sales data
- **models**: Database schema and ORM models for managing data relationships
- **scripts**: Utility scripts for data cleaning and processing

## Database Design

The database design ensures data normalization, integrity, and efficiency across multi-branch operations. Key design elements include:

- **Branches** and **Inventory** tables for tracking stock levels across stores
- **Employee** table with constraints to limit manager roles (e.g., only 20 managers allowed)
- **Sales** table with error handling to convert empty "Reason" entries to `NaN` for analytics

The project also features relational links between tables, such as replacing `manager_name` with `manager_id` in **Branches** and mapping `branch_id` to inventory and sales.

## Key Features

- **Branch and Inventory Management**: Track stock levels and branch information, with random assignment of `branch_id` to inventory items.
- **Sales and Customer Data**: Real-time sales data handling, including error correction for analytics, stored in the **Sales** table.
- **User-Friendly Interface**: A web-based interface for branch managers to view, add, or modify inventory, orders, and employee data.
- **Data Warehousing**: Organized and optimized storage for efficient analytics and reporting.
- **Modular Design**: Separate modules for data processing, database modeling, and web functionality.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Omar-Ahmed00/theShoeRetail.git
    cd theShoeRetail
    ```

2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

``

3. Run the application:
    ```bash
    app.py
    ```

## Usage

Once the application is running, access it in a web browser at `http://localhost:5000`. From there, you can navigate the app's various sections:

- **Manage Inventory**: View, add, or edit stock levels across branches.
- **Sales Management**: Track sales entries and view customer transactions.
- **Employee Management**: Manage employee data and assign manager roles.

## Acknowledgments

This project was developed as part of the **DEPI program**. Special thanks to my team members, instructors, and coordinators for their guidance and support.

---
