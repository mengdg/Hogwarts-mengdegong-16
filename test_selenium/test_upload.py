from test_selenium.base import Base
import time


class TestUpload(Base):
    def test_file_upload(self):
        self.driver.get('https://image.baidu.com/')
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        time.sleep(2)
        self.driver.find_element_by_id('stfile').send_keys('/Users/mengdegong/Downloads/WX20200521-143315@2x.png')
        time.sleep(5)
