from bs4 import BeautifulSoup
import requests
import json
import csv 
baseURL = "http://www.xiachufang.com"  
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
response = requests.get(baseURL, headers=headers) 
soup = BeautifulSoup(response.text,'html.parser')

# find the ul of naviation
ul_part = soup.find(class_ = "plain homepage-cats")

# creat the list of li in ul
li_part = ul_part.find_all('li',recursive = False)
categories = []
for item in li_part:
    category_url = baseURL+item.find('a')['href']
    categories.append(category_url)
    
recipes = []
filename = 'recipes.csv'
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)   
    for categoryURL in categories:
        
        nextPage = categoryURL
        
        i = 1
        while i<15 and  nextPage is not None:
            i+=1
            response = requests.get(nextPage, headers=headers) 
            soup = BeautifulSoup(response.text,'html.parser')
            ul_part = soup.find(class_ = "normal-recipe-list")
            li_part = ul_part.find_all('li',recursive = True)
            nextPage = baseURL+soup.find(class_ = 'next')['href']
            for li in li_part:
                recipeURL = li.find('a')['href']
                recipeURL=baseURL+recipeURL
                res = requests.get(recipeURL, headers=headers)
                recipeSoup = BeautifulSoup(res.text,'html.parser')
                name = recipeSoup.find(id = 'steps')
                if name is not None:
                    name = name.getText().strip()
                else:
                    name = ''
                stepList = recipeSoup.find_all('li', class_ = "container")
                stepStr = name+' '
                for step in stepList:
                    stepStr+=step.find('p').getText()
                recipes.append(stepStr)
                temp = [stepStr]
                csvwriter.writerow(temp)
        
        






