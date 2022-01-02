from selenium.webdriver.common.by import By


def xpath(query):
    return By.XPATH, query


def xpath_with_dti(element_type, data_test_id_value):
    return xpath(f'{element_type}[@data-testid="{data_test_id_value}"]')


def xpath_with_attribute(element_type, attribute_type, attribute_value):
    return xpath(f'//{element_type}[@{attribute_type}="{attribute_value}"]')