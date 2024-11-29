from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 创建WebDriver实例
driver = webdriver.Edge()

# 打开登录页面
driver.get("http://120.26.37.204:8088/marks/login")

# 最大化浏览器窗口
driver.maximize_window()

# 等待页面加载
time.sleep(2)


# 输入用户名
username_input = driver.find_element(By.NAME, "userName")
username_input.send_keys("admin")

# 输入密码
password_input = driver.find_element(By.NAME, "passWord")
password_input.send_keys("123456")

# 点击登录按钮
login_button = driver.find_element(By.ID, "loginFormBtn")
login_button.click()

# 等待登录过程完成
time.sleep(1)

# 选择【系统用户管理】
driver.find_element(By.LINK_TEXT, '系统用户管理').click()

# 点击登录按钮
driver.find_element(By.ID, "add").click()
# 输入账号密码
# 请确保这里的账号密码是唯一的，不可重复
new_username = '111222333' + str(time.time())  # 使用时间戳确保唯一性
new_password = '123456' + str(time.time())
driver.find_element(By.ID, 'new_username').send_keys(new_username)
driver.find_element(By.ID, 'new_password').send_keys(new_password)

# 在这里添加其他必要的操作，如保存新用户信息

input("请输入任意内容以关闭窗口\n")

#截屏
driver.save_screenshot("webtest_1.png")


# 关闭浏览器
# driver.quit()