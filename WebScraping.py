import re
import mechanize
import os
import urllib2

br = mechanize.Browser()
br.open("http://164.100.69.66/jsearch/title.php?scode=31")

response1 = br.response()
print(br.title())
print(response1.geturl())
print(response1.info())  # headers
print(response1.read())  # body

br.select_form(name="form3")

respose=br.response()
br.form['titlesel']=['O']
br.form["p_name"] = "" 
br.form.set_all_readonly(False)
br.form["frdate"] = "03/09/2021"  
br.form["todate"] = "03/09/2021" 

response2 = br.submit()



print(response2)
def downloadlink(linkUrl, referer):
    r = br.click_link(linkUrl)
    r.add_header("Referer", referer)
    br.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101')] # add a referer header, just in case
    response = br.open(r)
   
    filename = os.path.basename(linkUrl.url)

    f = open(filename, "w") #TODO: perhaps ensure that file doesn't already exist?
    f.write(response.read()) # write the response content to disk
    print (filename," has been downloaded")
    br.back()
    
print ("Get all PDF links\n")
filetypes=["pdf", "PDF"] # pattern matching for links, can add more kinds here
myfiles=[]
br._factory.is_html=True
for l in br.links():
    #check if this link has the file extension or text we want
    myfiles.extend([l for t in filetypes if t in l.url or t in l.text])

for l in myfiles:
    downloadlink(l,"http://164.100.69.66/jsearch/title.php?scode=31" )
print(l)