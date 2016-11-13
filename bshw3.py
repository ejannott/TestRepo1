# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import requests
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Prepare the site for use with BeautifulSoup
base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
html = urllib.request.urlopen(base_url).read()
soup = BeautifulSoup(html, "html.parser")

# prettify turns the text contained by 'soup' into a string formated like an html
htmlText = soup.prettify()

# apply replacements to the html text in htmlText
htmlText = htmlText.replace('student', "AMAZING student")
htmlText = htmlText.replace('https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg', 'ethan206pic.jpg')
# # # not totally sure why the below replaces local images on the page
htmlText = htmlText.replace('logo2.png', 'media/logo.png')

file = open('projectpage.html', 'w')
file.write(htmlText)