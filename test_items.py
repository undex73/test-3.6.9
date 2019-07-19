import time
import pytest

@pytest.mark.parametrize('language', ["es", "fr", "ru"], ids=lambda val: 'language_' + val)
def test_show_button(browser, language):
    link = "http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/".format(language)
    browser.get(link)
    time.sleep(10)
    browser.find_element_by_css_selector(".btn.btn-lg.btn-primary")
