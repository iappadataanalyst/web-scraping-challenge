
def scrape():
        #!/usr/bin/env python
        # coding: utf-8
        
        # In[1]:
        
        
        #Import Dependencies
        
        
        # In[2]:
        
        
        # import dependencies
        import pandas as pd
        from splinter import Browser
        from bs4 import BeautifulSoup as bs
        import requests
        from datetime import datetime
        import os
        import time
        import re
        
        # In[3]:
        
        
        # Capture path to Chrome Driver & Initialize browser
        executable_path = {'executable_path': 'chromedriver.exe'}
        browser = Browser('chrome', **executable_path, headless=False)
        
        
        # # NASA Mars News!
        
        # In[4]:
        
        
        # Page to Visit
        url = "https://mars.nasa.gov/news/"
        browser.visit(url)
        
        
        # In[5]:
        
        
        # Retrieve page with the requests module
        response = requests.get(url)
        # Create BeautifulSoup object; parse with 'lxml'
        soup = bs(response.text, 'lxml')
        #print(soup.prettify())
        
        
        # In[6]:
        
        
        # scrape the latest title and paragraph
        #title
        title = soup.find_all('div', class_='content_title')
        title = title[0].text.strip()
        
        title
        
        
        # In[7]:
        
        
        # paragraph
        paragraph = soup.find_all('div', class_='rollover_description')
        paragraph = paragraph[0].text.strip()
        
        paragraph
        
        
        # In[8]:
        
        
        print(f"Title: {title}")
        print(f"Paragraph: {paragraph}")
        
        
        # # Mars Space Images!
        
        # In[9]:
        
        
        image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        
        # Retrieve page with the requests module
        response = requests.get(image_url)
        # Create BeautifulSoup object; parse with 'lxml'
        soup = bs(response.text, 'lxml')
        
        #print(soup.prettify())
        
        
        # In[10]:
        
        
        # scrape the feature image
        #image_url1=soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
        #image_url1 = soup.find(id='full_image').get('data-fancybox-href')
        #first_image=soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
        #image_url1 = soup.find(id='full_image').get('background-image')
        imagebaseurl= 'https://www.jpl.nasa.gov/'
        image_url1 = soup.find(id='full_image').get('data-fancybox-href')
        
        #full_image = image_url + first_image
        full_image = imagebaseurl + image_url1
        print(full_image)
        
        
        # In[11]:
        
        
        
        image = soup.find('article', class_='carousel_item')['style']
        image = image.split('spaceimages')
        image = image[1].split("'")
        image = 'https://www.jpl.nasa.gov/spaceimages'+image[1]
        
        image
        
        
        # # Mars Weather!
        
        # In[12]:
        
        
        ## visit website
        #base_weather_url = 'https://twitter.com/marswxreport?lang=en'
        #weather_url='https://twitter.com/MarsWxReport/status/1233751572125028354'
        #browser.visit(weather_url)
        
        
        # In[13]:
        
        
        ## create html object and parse with beautifulsoup
        #time.sleep(1)
        #weather_html = browser.html
        #weather_soup = bs(weather_html, 'lxml')
        ##weather_soup = bs(weather_html, 'html.parser')
        
        
        # In[14]:
        
        
        ## scrape the weather information
        #weather = weather_soup.find('title')
        #weather = weather.text
        #print(weather)
        
        
        # In[15]:
        
        
        # URL of page to be scraped
        url = 'https://twitter.com/marswxreport?lang=en'
        
        # Retrieve page with the requests module
        response = requests.get(url)
        # Create BeautifulSoup object; parse with 'lxml'
        soup = bs(response.text, 'lxml')
        #print(soup.prettify())
        
        
        # In[16]:
        
        
        weather = soup.find_all('p', class_='js-tweet-text')
        
        weather_tweets = []
        # skip tweets that are not weather reports
        for tweet in weather:
            if (tweet.text).startswith('InSight') == True:
                weather_tweets.append(tweet.contents[0])
            else:
                notweather = 0
        
        weather = weather_tweets[0]
        
        weather = weather.replace('\n',' ')
        
        weather
        
        
        # # Mars Facts
        
        # In[17]:
        
        
        # visit the webset 
        facts_url = 'https://space-facts.com/mars/'
        
        # extract mars facts and make it a dataframe
        facts = pd.read_html(facts_url)
        facts_df = facts[0]
        
        facts_df.columns = ["Parameter", "Mars Values"]
        facts_df.set_index(["Parameter"])
        facts_df.reset_index()
        #facts_df
        
        
        # In[ ]:
        mars_html_table1 = facts_df.to_html()
        mars_html_table1 = mars_html_table1.replace("\n", "")
        mars_html_table1
        
        
        
        
        
        # In[18]:
        
        
        # visit the webset 
        #facts2_url = 'https://space-facts.com/mars/'
        
        # extract mars facts and make it a dataframe
        #facts2 = pd.read_html(facts2_url)
        facts2_df = facts[1]
        facts2_df.columns = ["Parameter", "Mars Values", "Earth Values"]
        facts2_df.set_index(["Parameter"])
        facts2_df.reset_index()    
        #facts2_df
        

    
        # In[20]:
        
        
        facts2_df = facts[1]
        #facts2_df.columns = ['Parameter', 'Mars Values', 'Earth Values']
        #facts2_df = df_mars_facts2.set_index('Parameter')
        #facts2_df.reset_index()
        #facts2_df
        
        
        # In[21]:
        
        
        mars_html_table2 = facts2_df.to_html()
        mars_html_table2 = mars_html_table2.replace("\n", "")
        mars_html_table2
        
        
        # # Mars Hemispheres
        
        # In[22]:
        
        
        # visit the web
        base_hemi_url = 'https://astrogeology.usgs.gov'
        hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemi_url)
        
        
        # In[23]:
        
        
        # create html object and parse with beautifulsoup
        hemi_html = browser.html
        hemi_soup = bs(hemi_html, 'html.parser')
        
        
        # In[24]:
        
        
        # scrape the hemisphere titles and images
        hemisphere_image_urls = []
        hemi_container = hemi_soup.find('div', id='product-section')
        hemi_images = hemi_container.find_all('div', class_='item')
        for images in hemi_images:
            title = images.find('h3').text
            link = images.find('a')['href']
            browser.visit(base_hemi_url + link)
            soup = bs(browser.html, 'html.parser')
            downloads = soup.find('div', class_='downloads')
            url = downloads.find('a')['href']
            hemisphere_image_urls.append({'title': title, 'img_url' : url})
        hemisphere_image_urls
        
        
        # Hemi 1
        
        # In[25]:
        
        
        hemi1 = hemisphere_image_urls[0]
        hemi1_title = hemi1["title"]
        hemi1_title
        
        
        # In[26]:
        
        
        hemi1 = hemisphere_image_urls[0]
        hemi1_img = hemi1["img_url"]
        hemi1_img
        
        
        # Hemi 2
        
        # In[27]:
        
        
        hemi2 = hemisphere_image_urls[1]
        hemi2_title = hemi2["title"]
        hemi2_title
        
        
        # In[28]:
        
        
        hemi2 = hemisphere_image_urls[1]
        hemi2_img = hemi2["img_url"]
        hemi2_img
        
        
        # Hemi 3
        
        # In[29]:
        
        
        hemi3 = hemisphere_image_urls[2]
        hemi3_title = hemi3["title"]
        hemi3_title
        
        
        # In[30]:
        
        
        hemi3 = hemisphere_image_urls[2]
        hemi3_img = hemi3["img_url"]
        hemi3_img
        
        
        # Hemi 4
        
        # In[31]:
        
        
        hemi4 = hemisphere_image_urls[3]
        hemi4_title = hemi4["title"]
        hemi4_title
        
        
        # In[32]:
        
        
        hemi4 = hemisphere_image_urls[3]
        hemi4_img = hemi4["img_url"]
        hemi4_img
        
        
        # # Dictionary
        
        # In[33]:
        
        browser.quit()
        mars_dict={"news_title":title,
                "news_paragraph": paragraph,
                "featured_image_url":full_image,
                "weather":weather,
                #"facts1":facts_df,
                "facts1":mars_html_table1,
                #"facts2":facts2_df,
                "facts2":mars_html_table2,
                "hemisphere_images_urls":hemisphere_image_urls,
                "hemi1_title": hemi1_title,
                "hemi1_img": hemi1_img,
                "hemi2_title": hemi2_title,
                "hemi2_img": hemi2_img,
                "hemi3_title": hemi3_title,
                "hemi3_img": hemi3_img,
                "hemi4_title": hemi4_title,
                "hemi4_img": hemi4_img,
                }
        #print(mars_dict)
        
        return mars_dict
      
        
