import csv
import requests
from bs4 import BeautifulSoup
import sched, time
import csv
import json
 


def do_something(scheduler): 

    scheduler.enter(60, 1, do_something, (scheduler,))
    print("Doing stuff...")

 
    file = open('linkedin-jobs.csv', 'a')
    write = csv.writer(file)
    write.writerow(['job_title', 'company_name', 'company_location', 'job_url'])



    def scraper(webpage, page_number):
        next_page = webpage + str(page_number)
        print(str(next_page))
        response = requests.get(str(next_page))
        soup = BeautifulSoup(response.content,'html.parser')


        """the jobs variable define for accessing the jobs fields
        with find method and html tags in inspect page on website."""
        jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
        for job in jobs:
            job_title = job.find('h3', class_='base-search-card__title').text.strip()
            company_name = job.find('h4', class_='base-search-card__subtitle').text.strip()
            company_location = job.find('span', class_='job-search-card__location').text.strip()
            job_url = job.find('a', class_='base-card__full-link')['href']

            
            write.writerow([job_title.encode('utf-8'),
                            company_name.encode('utf-8'),
                            company_location.encode('utf-8'),
                            job_url.encode('utf-8')
                            ])
            
        if page_number < 25: 
            page_number = page_number + 25
            scraper(webpage, page_number)
        else:
            file.close()
            print('File closed')

    scraper('https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=python&location=London%2BArea%2C%2BUnited%2BKingdom&geoId=90009496&trk=public_jobs_jobs-search-bar_search-submit&start=', 0)

 
  
    def make_json(csvFilePath, jsonFilePath):
        data = []
        
        with open(csvFilePath, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            
            
            for row in csvReader: 
                data.append(row)
    
        with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))

    csvFilePath = r'linkedin-jobs.csv'
    jsonFilePath = r'linkedin-jobs.json'
    
    # call the make_json().
    make_json(csvFilePath, jsonFilePath)

   
my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(60, 1, do_something, (my_scheduler,)) 
my_scheduler.run()

