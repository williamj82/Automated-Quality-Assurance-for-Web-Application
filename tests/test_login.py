def test_successful_login_standard_user(page): 
    page.goto("https://www.saucedemo.com/")  
    page.fill("#user-name", "standard_user")  
    page.fill("#password", "secret_sauce")  
    page.click("#login-button") 
    assert page.url == "https://www.saucedemo.com/inventory.html" 

def test_unsuccessful_login_locked_out_user(page): 
    page.goto("https://www.saucedemo.com/")  
    page.fill("#user-name", "locked_out_user")  
    page.fill("#password", "secret_sauce")  
    page.click("#login-button") 
    assert page.url != "https://www.saucedemo.com/inventory.html" 

def test_successful_login_problem_user(page): 
    page.goto("https://www.saucedemo.com/")  
    page.fill("#user-name", "problem_user")  
    page.fill("#password", "secret_sauce")  
    page.click("#login-button") 
    assert page.url == "https://www.saucedemo.com/inventory.html" 

def test_successful_login_performance_glitch_user(page): 
    page.goto("https://www.saucedemo.com/")  
    page.fill("#user-name", "performance_glitch_user")  
    page.fill("#password", "secret_sauce")  
    page.click("#login-button") 
    assert page.url == "https://www.saucedemo.com/inventory.html" 

def test_successful_login_performance_error_user(page): 
    page.goto("https://www.saucedemo.com/")  
    page.fill("#user-name", "error_user")  
    page.fill("#password", "secret_sauce")  
    page.click("#login-button") 
    assert page.url == "https://www.saucedemo.com/inventory.html" 

def test_successful_login_performance_visual_user(page): 
    page.goto("https://www.saucedemo.com/")  
    page.fill("#user-name", "visual_user")  
    page.fill("#password", "secret_sauce")  
    page.click("#login-button") 
    assert page.url == "https://www.saucedemo.com/inventory.html" 

def test_invalid_login_wrong_password_trailing_spaces(page):
    page.goto("https://www.saucedemo.com/")  
    page.fill("#user-name", "standard_user")  
    page.fill("#password", "  secret_sauce  ")  
    page.click("#login-button") 
    assert page.url != "https://www.saucedemo.com/inventory.html"

def test_invalid_login_wrong_password_completely(page):
    page.goto("https://www.saucedemo.com/")  
    page.fill("#user-name", "standard_user")  
    page.fill("#password", "wrong_password")  
    page.click("#login-button") 
    assert page.url != "https://www.saucedemo.com/inventory.html"

def test_invalid_login_empty_password(page):
    page.goto("https://www.saucedemo.com/")  
    page.fill("#user-name", "standard_user")  
    page.fill("#password", "")  
    page.click("#login-button") 
    assert page.url != "https://www.saucedemo.com/inventory.html"

def test_invalid_login_wrong_password_case(page):
    page.goto("https://www.saucedemo.com/")  
    page.fill("#user-name", "standard_user")  
    page.fill("#password", "SECRET_SAUCE")  
    page.click("#login-button") 
    assert page.url != "https://www.saucedemo.com/inventory.html"

