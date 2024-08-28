import undetected_chromedriver as uc
from time import sleep
import chromedriver_autoinstaller
from click_element import click_element
from fill_input import fill_input
from load_cookies import load_cookies
from save_cookies import save_cookies
from get_attribute_value import get_attribute_value
from get_inner_text import get_inner_text
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import os
import shutil
import csv


class HeadlessBrowser:
    def __init__(self):
        chromedriver_autoinstaller.install()  # Automatically installs the correct ChromeDriver
        self.driver = uc.Chrome(options=self.get_options(), version_main=127)  # Use your current Chrome major version

    def get_options(self):
        options = uc.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        return options

    def quit(self):
        self.driver.quit()


class Browser:
    def __init__(self):
        self.headless_browser = HeadlessBrowser()

    def navigate(self, url):
        self.headless_browser.driver.get(url)

    def close(self):
        self.headless_browser.quit()

    def fill_input(self, selector, value):
        """Fill an input field identified by a CSS selector."""
        fill_input(self.headless_browser.driver, selector, value)  # Call the existing function

    def click_element(self, selector):
        """Click an element identified by a CSS selector."""
        click_element(self.headless_browser.driver, selector)  # Call the existing function

    def load_cookies_from_file(self, path):
        """Load cookies from a specified file into the browser."""
        load_cookies(self.headless_browser.driver, path)

    def save_cookies_to_file(self, output_file_path):
        """Save cookies from the browser to a specified file."""
        save_cookies(self.headless_browser.driver, output_file_path)  # Pass the driver object

    def get_inner_text(self, selector):
        """Get the inner text of an element identified by a CSS selector."""
        return get_inner_text(self.headless_browser.driver, selector)

    def get_attribute(self, selector, attribute):
        """Get the value of a specified attribute from an element identified by a CSS selector."""
        return get_attribute_value(self.headless_browser.driver, selector, attribute)





def scrape_profile(browser, profile_url):
    """Scrape the relevant parts of the LinkedIn profile using the Browser instance."""
    browser.navigate(profile_url)
    sleep(3)  # Wait for the page to load

    profile_data = {}
    
    # Scrape the profile name
    profile_data['name'] = browser.get_inner_text('//h1[contains(@class, "text-heading-xlarge")]')
    
    # Scrape the profile headline
    profile_data['headline'] = browser.get_inner_text('//div[contains(@class, "text-body-medium break-words")]')
    
    # Scrape the current company
    profile_data['current_company'] = browser.get_inner_text('//li[contains(@class, "QFGPtOjAtpOifhDynMlyCYJuGDRoyIVoQfcaMc")]//span[contains(@class, "xPpxwuFnHVOTjkbRBnNSrqGFHgEcQKsIHrukLXWA")]')
    
    # Scrape the location
    profile_data['location'] = browser.get_inner_text('//div[contains(@class, "VidZoTAElguBIpzFCpQhxQbSSzKBZuYtY mt2")]//span[contains(@class, "text-body-small inline t-black--light break-words")]')
    
    return profile_data

def scrape_contact_info(browser):
    """Click on the 'Contact info' link and scrape the contact information using the Browser instance."""
    browser.click_element('//a[@id="top-card-text-details-contact-info"]')
    sleep(2)  # Wait for the modal to load

    contact_info = {}
    
    # Scrape the LinkedIn profile URL
    contact_info['linkedin_url'] = browser.get_inner_text('//section[contains(@class, "pv-contact-info__contact-type")]//a[contains(@class, "BpMziKPlBXPxCpwxevWbCmxplvQlqLyZHzMs")]')
    
    # Scrape the websites
    websites = browser.headless_browser.driver.find_elements(By.XPATH, '//section[contains(@class, "pv-contact-info__contact-type")]//a[contains(@class, "pv-contact-info__contact-link")]')
    contact_info['websites'] = [website.get_attribute('href') for website in websites]
    
    return contact_info
def save_to_csv(profile_data, contact_info):
    """Save the profile and contact information to a CSV file named after the profile."""
    fieldnames = ['name', 'headline', 'current_company', 'location', 'linkedin_url', 'websites']
    
    # Combine profile_data and contact_info into a single dictionary
    combined_data = {**profile_data, **contact_info}
    
    # Convert websites list to a string
    combined_data['websites'] = ', '.join(combined_data['websites'])
    
    # Create a filename based on the profile name
    filename = f"{profile_data['name'].replace(' ', '_')}.csv"
    
    # Write to CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write header
        writer.writeheader()
        
        # Write data
        writer.writerow(combined_data)
def main():
    browser = Browser()
    profile_url = "https://www.linkedin.com/in/meyeresqfamilyprotection/"
    
    # Load cookies
    browser.load_cookies_from_file("linkedin_cookies.txt")
    
    # Scrape profile information
    profile_data = scrape_profile(browser, profile_url)
    print("Profile Data:", profile_data)
    
    # Scrape contact information
    contact_info = scrape_contact_info(browser)
    print("Contact Info:", contact_info)
    # Save to CSV
    save_to_csv(profile_data, contact_info)
    browser.close()

if __name__ == "__main__":
    main()