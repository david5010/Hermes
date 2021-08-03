#webscrap and then send interesting links to main
#potentially have the function to update on new job postings regarding specific tags i.e consultant/swe/python...etc.

import requests
from bs4 import BeautifulSoup
import user_commands as UC

class Job:
  def __init__(self, keywords):
    self.url = UC.timesjob(keywords)
    self.response = None #variable for url requests. If 200, then connected
    self.soup = None
    self.job = None
    
    self.job_app = None

  def _set_response(self):
    '''
    establishes the connection and sets requests
    '''
    self.response = requests.get(self.url)
    if self.response.status_code != 200:
      print("Connection Error")
      return ConnectionError

  def _set_soup(self):
    '''
    sets the soup for the scrapper
    '''
    self.soup = BeautifulSoup(self.response.text, 'lxml')

  def _set_job(self):
    '''
    sets the job and gets the card on the page
    '''
    self.job = self.soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')

  def _set_job_page(self):
    '''
    sets the job_app as the application page using the href link
    '''
    self.job_app =  self.job.find('h2').find('a')['href']
  
  def send_job_page(self):
    self._set_response()
    self._set_soup()
    self._set_job()
    self._set_job_page()
    return self.job_app