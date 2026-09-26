# Portfolio Website Link Checker (Selenium)

A simple Python automation script that uses Selenium to scan a locally hosted portfolio website and list every link on the page, along with its text and URL.

## 🎥 Demo Video

Watch the code walkthrough here: [Project Demo](https://drive.google.com/file/d/1RqJgkTUueMOj75B5ZtYfpbhKkYCaRjpn/view?usp=drive_link)

## 📌 Overview

This script opens a locally hosted website (`http://localhost:8000`) in Chrome, finds all `<a>` tags on the page, and prints out:
- The total number of links found
- The visible text of each link
- The URL (`href`) each link points to

It's a lightweight way to audit a website's links — useful for checking that a portfolio site's navigation and outbound links are all present and correctly set.

## 🛠️ Tech Stack

- **Python**
- **Selenium WebDriver**
- **Chrome / ChromeDriver**

## 📂 File

- `test_2_.py` – main script

## ▶️ How to Run

1. Make sure Google Chrome and a matching [ChromeDriver](https://chromedriver.chromium.org/) are installed.
2. Install Selenium:
   ```bash
   pip install selenium
   ```
3. Start your local portfolio site so it's being served at `http://localhost:8000` (e.g. `python -m http.server 8000` from your site's folder).
4. Run the script:
   ```bash
   python test_2_.py
   ```

## 🔍 What It Does

1. Launches a Chrome browser window
2. Navigates to `http://localhost:8000` and maximizes the window
3. Finds all elements with tag `<a>` on the page
4. Prints the total link count
5. Loops through each link, printing its text and URL
6. Waits 5 seconds, then closes the browser

## 👤 Author

Built by GOGO as part of an active data analyst portfolio and job search.
