import requests as rq
import pandas as pd

class Weather:

    base_Url = "http://api.weatherapi.com/v1/{endpoint}.json"

    def __init__(self,api_key,city):
       self.api_key=api_key 
       self.city=city
       self.base_url = ("http://api.weatherapi.com/v1/{endpoint}.json")
       self.days=None
       self.dt=None
       self.alerts="yes"
       self.aqi="yes"
       self.lang=None
       self.session =rq.Session()
       # just making a session and opens it to avoid making a request every time 
        

    def request(self, endpoint, **params) -> dict: # this is the function that makes a request 
       
        url = self.base_Url.format(endpoint=endpoint)
       
        params.update({"key": self.api_key,"q": self.city,"lang":self.lang})
        resp = self.session.get(url, params=params)
        data = resp.json()
        return data

    def getCurrentWeather(self) -> dict: # this function returns a dicyionary as it gets the wweather now 
        
        return self.request("current")

    def getForecast(self) -> dict  : # you should set the number of days first initialy it is set to the current time this function gives the 
                                       #forecast to number of days you can turn of the alerts , or the aqi , and you can control the language 
        params = {"days":self.days,"alerts":self.alerts,"aqi":self.aqi}
        return self.request("forecast",**params)

    def setaqi(self,flag):
           self.aqi=flag
    def setDay(self,days):  
           self.days=days
    def setCity(self,city):
           self.city=city
    def setAlert(self,flag):
           self.alerts=flag
    def setlanguage(self,s):
        self.lang=s
        
       
    def setdt(self,dt):
           for i in range(len(dt)):
               if (i<4) : 
                   if not dt[i].isdigit():
                       return "you must enter a valid date *"
               
               if dt[i]!="-" and i==4 :
                   return "you must enter a valid date**"
           
               if (4<i<7) : 
                   if not dt[i].isdigit():
                       return "you must enter a valid date***"
           
               if dt[i]!="-" and i==7:
                   return "you must enter a valid date****"
               if (7<i<10):
                   if not dt[i].isdigit():
                       return "you must enter a valid date *"
       
           self.dt=dt
   # this function  requires  a subscription to a website         
    def history(self):
         
          params={"dt":self.dt}  
          return self.request("history",**params)

w=Weather("72d29dcc81924d5096884701252206","cairo")

w.setDay(2)
dframe = pd.Series(w.getForecast())

print(dframe)
