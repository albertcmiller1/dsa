'''
aka Pub/Sub 

YouTube is the Subject aka Publisher 
Users are the Observers aka Subscribers 


how to make abstract class / interface in python 
'''

from abc import ABC, abstractclassmethod

class YouTubeChannel: 
    def __init__(self, name): 
        self.name = name 
        self.subscribers = []

    def subscribe(self, sub): 
        self.subscribers.append(sub)

    def notify(self, event): 
        for sub in self.subscribers: 
            sub.sendNotification(self.name, event)


class ABC: 
    pass 


class YouTubeSubcriber(ABC): 
    @abstractmethod
    def sendNotification(self, event): 
        pass 


class YouTubeUser(YouTubeSubcriber): 
    def __init__(self, name): 
        self.name = name 

    def sendNotification(self, channel, event):
        print(f"user {self.name} received notification from {channel}: {event}")
        return 


channel = YouTubeChannel("needcode") 

channel.subscribe(YouTubeUser("albert"))
channel.subscribe(YouTubeUser("mo"))
channel.subscribe(YouTubeUser("chris"))

channel.notify("a new video released")