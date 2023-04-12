# 开发时间：2023-03-27 16:54
# 开发人员：林坚洪
# encodeing "UTF-8"
from selenium import webdriver
import selenium


driver = selenium.webdriver()
# 没有环境变量时使用executable_path指定路径：
# driver = selenium.webdriver.PhantomJS(executable_path=r'D:\softs\phantomjs-2.1.1\phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.close()

# 测试webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://www.gaokao.cn/school/search')
browser.close()

# 替换webdriver浏览器里网页的节点（修改网页源码）：
# driver.execute_script('document.querySelector("body").innerHTML="{}";'.format)