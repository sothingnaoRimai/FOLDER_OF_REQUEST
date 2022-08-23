import requests
import json
def request():  
    a = requests.get("http://saral.navgurukul.org/api/courses")
    x=a.json()
    print("No. Courses---ID")
    with open("courses.json","w") as f:
        json.dump(x,f,indent=4)
    with open("courses.json","r") as f:
        data = json.load(f)
        print(data) #till this will make a new file and append there + show html code

# request()
    id= [] 
    i = 0
    while i < len(data['availableCourses']):
        print(i+1,":",data['availableCourses'][i]['name'],"---",data['availableCourses'][i]['id'])
        id.append(data['availableCourses'][i]['id'])
        i+=1 
    user= int(input("**select the serial number:"))-1
    ex=requests.get("http://saral.navgurukul.org/api/courses/"+str(id[user])+"/exercises") #error
    a=ex.json()
    with open ("url link2.json","w")as k:
        json.dump(a,k,indent=4)
    with open ("url link2.json","r") as k:
        c=json.load(k)
    print(c) ## till this will gve  your output in terminal
# request()


    j=0
    l=0
    slug=[] # store all the slug here
    while j<len(c["data"]):
        print(l+1,c["data"][j]["name"])
        slug.append(c['data'][j]["slug"])
        l=l+1
        j=j+1
    print(slug)
    
   
    slugname=int(input("enter your slug no? "))-1
    sluglist=requests.get("http://saral.navgurukul.org/api/courses/"+ str(user)+"/exercise/getBySlug?slug=" + slug[slugname])
    b=sluglist.json()
    with open("slunglist.json","w") as k:
        json.dump(b,k,indent=4)
    with open("slunglist.json","r") as k:
        d=json.load(k)
    print(d)
    print(d["name"])
    print(d["slug"])
    print("CONTENT",b["content"])


    pre_next=input("enter previous or next?")
    if pre_next =="P":
        i=0
        while i<len(slug):
            print(slug[slugname-1])
        
            print(b["content"])
            i=i+1
            break
    elif pre_next=="N":
        i=0
        while i<len(slug):
            print(slug[slugname+1])
            print(b["content"])
            i=i+1
            break      
request()

def main():
    again_quit=input("DO U WANT TO TRY AGAIN? if  yes enter Y: if no enter quit")
    if again_quit=="Y":
           request()
    elif again_quit=="quit":
        print('QUIT')
        
main()