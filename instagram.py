import time #time modülünü import ettik
from selenium import webdriver #selenium modülünün içindeki webdriver fonksiyonunu import ettik
from selenium.webdriver.common.keys import Keys# selenium modülünün Keys fonksiyonunu import ettik
from instaGirisInfo import username, password#kullanıcıdan aldığımız kullanıcı adı ve şifreyi import ettik

class Instagram: #Instagram adında bir class oluşturduk
    def __init__(self, username, password): #değişkenleri atamak ve işimizi kolaylaştırmak için __init__ fonksiyonunu kullandık
        self.browser = webdriver.Chrome()#sürekli webdriver.Chrome() fonksiyonunu kullanmamak için fonksiyonu self.browser a atadık
        self.username = username#username'i class içinde kullanabilmek için self.username'e atadık
        self.password = password#yukarıdaki gibi ama şifreyi atadık

    def signIn(self):#giriş işlemini yapması için bir fonksiyon oluşturduk
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")#instagram'a gitmek için bu kodu kullandık
        time.sleep(3)#diğer işlemi yapması için programı 3 saniye beklettik
        usernameInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')#username kısmı için input aldık
        passwordInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')#password kısmı için input aldık

        usernameInput.send_keys(self.username)#username inputuna kullanıcıdan aldığımız username'i yazdırdık
        passwordInput.send_keys(self.password)#password inputuna kullanıcıdan aldığımız password'ü yazdırdık
        passwordInput.send_keys(Keys.ENTER)#enter tuşuna bastıdık

        time.sleep(4)#programı diğer işlemi yapması için 2 saniye beklettik

    def getFollowes(self):#takipçileri göstermesi için bir fonksiyon oluşturduk
        self.browser.get(f"https:/www.instagram.com/{self.username}")#f-string kullanarak kullanıcın profil sayfasına gittik

        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div/span").click()#kullanıcının takipçi listesini görmek için takipçi kısmına bastıdık
        time.sleep(2)
        followers = self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li")#takipçilerin isimlerinin olduğu css selectorunu aldık

        for i in followers:#sadece bir takipçiyi değilde tüm takipçileri göstermesi için bir for düöngüsü oluşturduk
            link = i.find_element_by_css_selector("a").get_attribute("href")#takipçilerin adını almak için adının olduğu css selectorune ulaştıl
            print(link)#takipçilerin isimlerini yazdırdık

        self.browser.close()#tarayıcıyı kapatıyoruz

insta = Instagram(username, password)#classımızı nesneye dönüştürdük ve insta değişkenine atadık
insta.signIn()#giriş fonksiyonunu çağırdık
insta.getFollowes()#takipçi getirme fonksiyonunu kullandık
