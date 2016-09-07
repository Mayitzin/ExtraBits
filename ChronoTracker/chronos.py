# -*- coding: utf-8 -*-
"""
Handler for Chronological Tracker of entries.

@author: Mario Garcia
www.mayitzin.com
"""

import json
import datetime
import time


class Event(object):
    """This class represents the chronological events"""
    def __init__(self):
        # Set Date
        timeNow = time.gmtime()
        self.dateID = time.strftime("%Y%m%d", timeNow)
        self.year = time.strftime("%Y", timeNow)
        self.month = time.strftime("%m", timeNow)
        self.day = time.strftime("%d", timeNow)
        self.hour = time.strftime("%H", timeNow)
        self.minute = time.strftime("%M", timeNow)
        self.second = time.strftime("%S", timeNow)
        self.date = self.day+"."+self.month+"."+self.year
        self.setDate(self.date)
        # Set Information
        self.description = "Description of the event"
        self.references = ["This is a list of references"]
        self.links = ["This is a list of links"]
        # Build dictionary with information of event
        self.d = self.buildDict()

    def setDate(self, date):
        # Default values
        self.year, self.month, self.day = "0000", "00", "00"
        self.hour, self.minute, self.second = "00", "00", "00"
        self.dateID = date
        if "." in date:
            dateElems = date.split(".")
            if len(dateElems)==3:
                self.month = dateElems[1]
                if len(dateElems[0])==4:
                    self.year = dateElems[0]
                    self.day  = dateElems[2]
                elif len(dateElems[2])==4:
                    self.year = dateElems[2]
                    self.day  = dateElems[0]
            self.dateID = "".join([self.year,self.month,self.day])
        if len(self.dateID)==8:
            self.year  = self.dateID[:4]
            self.month = self.dateID[4:6]
            self.day   = self.dateID[6:8]
        self.date = self.day+"."+self.month+"."+self.year
        self.dateID = str(date2unix(self.date))

    def setDescription(self, description=None):
        self.description = description
        if self.description == None:
            self.description = ""
        self.updateDict()

    def setReferences(self, references=None):
        self.references = references
        if self.references == None:
            self.references = [""]
        self.updateDict()

    def setLinks(self, links=[]):
        self.links = links
        if len(self.links)==0:
            self.links = [""]
        self.updateDict()

    def buildDict(self):
        self.d = {self.dateID:{
                      self.date:{"year":self.year,"month":self.month,"day":self.day,\
                      "hour":self.hour, "minute":self.minute, "second":self.second },\
                      "description":self.description,"references":self.references,"links":self.links } }
        return self.d

    def updateDict(self):
        self.d[self.dateID] = {}
        self.d[self.dateID][self.date] = {}
        self.d[self.dateID][self.date]["day"] = self.day
        self.d[self.dateID][self.date]["month"] = self.month
        self.d[self.dateID][self.date]["year"] = self.year
        self.d[self.dateID][self.date]["hour"] = self.hour
        self.d[self.dateID][self.date]["minute"] = self.minute
        self.d[self.dateID][self.date]["second"] = self.second
        self.d[self.dateID]["description"] = self.description
        self.d[self.dateID]["links"] = self.links
        self.d[self.dateID]["references"] = self.references

    def saveEvent(self, fileName="output.dat"):
        with open(fileName, 'w') as jsonFile:
            json.dump(self.d, jsonFile)

    def printJson(self):
        print json.dumps(self.d, sort_keys=True, indent=4)


def date2unix(dateAndTime):
    year, day, month = 0, 0, 0
    hour, mins, secs = 0, 0, 0
    dateStr = str(day)+"."+str(month)+"."+str(year)
    timeStr = str(hour)+":"+str(mins)+":"+str(secs)
    if type(dateAndTime) != str:
        print dateAndTime, "is not a string"
        return dateAndTime
    if " " in dateAndTime:
        dateStr = dateAndTime.split(" ")[0]
        timeStr = dateAndTime.split(" ")[1]
    else:
        dateStr = dateAndTime
    if "." in dateStr:
        dateElems = dateStr.split(".")
        if len(dateElems)==3:
            month = int(dateElems[1])
            if len(dateElems[0])==4:
                year = int(dateElems[0])
                day  = int(dateElems[2])
            elif len(dateElems[2])==4:
                year = int(dateElems[2])
                day  = int(dateElems[0])
    if ":" in timeStr:
        timeElems = timeStr.split(":")
        hour = int(timeElems[0])
        mins = int(timeElems[1])
        if len(timeElems)==3:
            secs = int(timeElems[2])
    unixTime = datetime.datetime(year, month, day, hour, mins, secs)
    return time.mktime(unixTime.timetuple())

def unix2date(unixTime):
    return datetime.datetime.fromtimestamp(float(unixTime)).strftime("%d.%m.%Y %H:%M:%S")

def printInfo(event=None):
    if event == None:
        event = Event()
        print "Printing information of a generic event"
    else:
        print "Printing information of event occured on", event.date
    print "\tDate:", event.date
    print "\tEvent:", event.description
    print "\tRefs:", event.references
    print "\tLinks:", event.links


new_event = Event()
new_event.setDate("13.02.1987")
new_event.setDescription("My Birthday")
new_event.setReferences(["ref1", "ref2"])
new_event.setLinks(["link1","link2"])
new_event.saveEvent("output.txt")

new_event.printJson()
printInfo(new_event)
