#this module is for functions that deal with user inputs
#use this as the parameters for the url search in scrapper

def timesjob(keywords:str)->str:
  '''
  uses keywords to return the constructed url
  '''
  base = "https://www.timesjobs.com/candidate/job-search.html?"
  search_type = "searchType=personalizedSearch&from=submit&"
  parameters = '&txtKeywords=' + keywords.strip().replace(' ', '+')
  location = '&txtLocation=United+States'
  work_experience = "&cboWorkExp1=0"
  return base+search_type+parameters+location+work_experience