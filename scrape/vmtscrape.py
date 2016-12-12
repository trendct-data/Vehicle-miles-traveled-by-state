# Download all excel files from this url: 
# https://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm
from BeautifulSoup import BeautifulSoup
import requests, re

def dl_xls(download_page="https://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
           base_url="https://www.fhwa.dot.gov/policyinformation/travel_monitoring/"):

    html = requests.get(download_page).content

    soup = BeautifulSoup(html)

    for link in soup.findAll("a",href=True):
        if (".XLS" not in link["href"].upper()):
            continue


        # remove web path and replace non-alphanum characters with underscores
        filename = re.sub("_xls",".xls",
                          re.sub(r"[^a-z0-9]+","_",
                                 re.sub(r"/ohim/tvtw/","",link["href"].lower())))

        if link["href"].startswith("/"):
            base_url = "https://www.fhwa.dot.gov"
        print "Downloading " + filename + " " + base_url + link["href"]

        # Download the file
        download_dir = "data/"

        outfh = open(download_dir + filename,"wb")
        outfh.write(requests.get(base_url + link["href"]).content)
        outfh.close()
    
dl_xls()

