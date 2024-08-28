from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_inner_text(driver, selector):
    """Get the inner text of an element identified by a CSS selector."""
    # Wait for the element to be visible
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, selector)))
    return element.text