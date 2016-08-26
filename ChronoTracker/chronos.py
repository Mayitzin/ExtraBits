# -*- coding: utf-8 -*-
"""
Json handler for Chronological Tracker of entries.

@author: Mario Garcia
www.mayitzin.com
"""

import json
import time

class Date(object):
    """This class represents the dates"""
    def __init__(self, date=time.strftime("%Y%m%d", time.gmtime())):
        self.date = date

    def isValid(self):
        print self


class Event(object):
    """This class represents the chronological events"""
    def __init__(self):
        # Set Date
        timeNow = time.gmtime()
        self.dateID = time.strftime("%Y%m%d", timeNow)
        self.year = time.strftime("%Y", timeNow)
        self.month = time.strftime("%m", timeNow)
        self.day = time.strftime("%d", timeNow)
        self.date = self.day+"."+self.month+"."+self.year
        # self.date = setDate(self)
        # Set Information
        self.description = "Description of the event"
        self.references = ["This is a list of references"]
        self.links = ["This is a list of links"]
        # Build dictionary with information of event
        self.d = self.buildDict()

    def setDate(self, date):
        # Default values
        self.year = "0000"
        self.month = "00"
        self.day = "00"
        self.dateID = date
        if "." in date:
            dateElems = date.split(".")
            if len(dateElems)==3:
                self.year = self.dateID[:4]
                self.month = self.dateID[4:6]
                self.day = self.dateID[6:8]
            self.dateID = "".join([self.year,self.month,self.day])
        if len(self.dateID)==8:
            self.year = self.dateID[:4]
            self.month = self.dateID[4:6]
            self.day = self.dateID[6:8]
        self.date = self.day+"."+self.month+"."+self.year
        self.dateID = self.year+self.month+self.day

    def setDescription(self, description=None):
        self.description = description
        if self.description == None:
            self.description = ""

    def setReferences(self, references=None):
        self.references = references
        if self.references == None:
            self.references = [""]

    def setLinks(self, links=None):
        self.links = links
        if self.links == None:
            self.links = [""]

    def buildDict(self):
        self.d = {self.dateID:{self.date:{"year":self.year,"month":self.month,"day":self.day},"description":self.description,"references":self.references,"links":self.links}}
        return self.d

    def saveEvent(self, fileName="output.dat"):
        with open(fileName, 'w') as jsonFile:
            json.dump(self.d, jsonFile)

    def printDict(self):
        print json.dumps(self.d, sort_keys=True, indent=4)


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


new_event2 = Event()
new_event2.setDate("1987.02.13")
new_event2.setDescription("My Birthday")
new_event2.setReferences(["ref1", "ref2"])
new_event2.setLinks(["link1","link2"])

print new_event2.date
print new_event2.description

new_event2.printDict()

printInfo(new_event2)

printInfo()

new_event2.saveEvent("output.txt")