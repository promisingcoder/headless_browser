def load_cookies(driver, path):
    """Load cookies from a specified file into the browser."""
    driver.get("https://www.linkedin.com")  # Navigate to the correct domain

    with open(path, 'r') as f:
        cookies = eval(f.read())  # Assuming cookies are stored in a list of dicts

    for cookie in cookies:
        driver.add_cookie(cookie)  # Add each cookie