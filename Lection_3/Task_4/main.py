import pycurl
from io import BytesIO

# argument list of urls, get http code, and return list of http codes, who accept.
def getHttpCodes(*Urls):
    
    listOfHttpCodes = []
    for url in listOfUrls:
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.perform()
        listOfHttpCodes.append(curl.getinfo(pycurl.HTTP_CODE))
        curl.close()
    return listOfHttpCodes

# validate Ok and FAIL http code return dict with it values by url
def validation(listOfUrls, listOfCodes, listOfTrueCodes):
    urlsToCodes = {}
    counter = 0
    for url in listOfUrls:
        currentCode = listOfHttpCodes[counter]
        if currentCode in listOfTrueCodes:
            urlsToCodes[url] = [currentCode, "OK"]
        else:
            urlsToCodes[url] = [currentCode, "FAIL"]
        counter += 1
    return urlsToCodes

# Print data in easy-read table
def uiResult(result):
    print("URL" + " - "*3 +"CODE" + " - "*3 +"STATUS")
    for key in result.keys():
        print(key + " - "*3 + str(result[key][0]) + " - "*3 + str(result[key][1]))

# Main
listOfTrueCodes = [200, 302]
listOfUrls = ["https://tasks.ngcourses.net", "google.com", "youtube.com", "ru.wikipedia.org/wiki/CURL", "github.com/DiachenkoRP/NG_2023_Ruslan_Diachenko", "mail.google.com", "www.google.com/search?client=firefox-b-lm&q=github"]
listOfHttpCodes = getHttpCodes(listOfUrls)

validationResult = validation(listOfUrls, listOfHttpCodes, listOfTrueCodes)
uiResult(validationResult)
    
