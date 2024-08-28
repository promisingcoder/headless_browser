import time  # Ensure to import time at the top

def save_cookies(driver, output_file_path):
    """Wait for user input and save cookies to a specified file."""
    input("Press Enter to save cookies...")

    # Wait for a few seconds to ensure the page is fully loaded
    time.sleep(10)  # Adjust the sleep time as necessary

    # Check if the driver has the get_cookies method
    if hasattr(driver, 'get_cookies'):
        cookies = driver.get_cookies()
    else:
        raise AttributeError("The driver object does not have a method 'get_cookies'.")

    with open(output_file_path, 'w') as f:
        f.write(str(cookies))
    print(f'Saved cookies to: {output_file_path}')