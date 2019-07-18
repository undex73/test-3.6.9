link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_show_basken_button(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".btn.btn-lg.btn-primary")
