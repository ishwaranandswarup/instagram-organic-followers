from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint as rand

webdriver = webdriver.Chrome(executable_path='C:/Users/Ishwar/Downloads/chromedriver_win32/chromedriver.exe')#Choose your chromedriver path

webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(rand(8,12))

username = webdriver.find_element_by_name('username')
username.send_keys('enter_your_username')
password = webdriver.find_element_by_name('password')
password.send_keys('enter_your_password')

#the css_selector may differ in your case 
button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div')
button_login.click()
sleep(rand(8,12))

#comment below line, if you don't get a pop up asking about notifications
webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm').click() 

hashtag_list = ['animation', '3d', 'design', 'blender']

follow_list = []
followed = 0
like = 0
comment = 0

for hashtag in hashtag_list:
    
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag + '/')
    sleep(rand(8,12))
    #the css_selector may differ in your case
    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

    first_thumbnail.click()
    sleep(rand(8,12))    
    try:        
        for x in range(1,100):
            #the x_path may differ in your case
            username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
            y = rand(0,2)                                           
                                                        
            if username not in follow_list:
                #thex_path may differ in your case
                if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                                                    
                    webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                                                    
                    follow_list.append(username)
                    followed += 1
                    sleep(rand(8,12))
                    #the x_path may differ in your case
                    #Like the picture
                    webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
                    like += 1
                    
    
                    # Comment on picture
                    keys = ['Love that :)', 'Very Good!!']
                    
                    
                    webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[2]/button').click()
                                                        
                    comment_area = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
                    comment_area.send_keys(keys[y])
                    
                    # To post comment
                    comment_area.send_keys(Keys.ENTER)
                    comment += 1
                    sleep(rand(8,12))
    
                # Open Next picture
                webdriver.find_element_by_link_text('Next').click()
                sleep(rand(8,12))
            else:
                webdriver.find_element_by_link_text('Next').click()
                sleep(rand(8,12))
    # when hashtag stops refreshing photos, it continues to the next
    except:
        continue

for n in range(0,len(follow_list)):
    print(follow_list[n])
    
print('Liked {} photos.'.format(like))
print('Commented {} photos.'.format(comment))
print('Followed {} people.'.format(followed))
