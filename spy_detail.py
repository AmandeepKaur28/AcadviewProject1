from datetime import datetime
class Spy:

    def __init__(self,name,sal,age,rating):
        self.name=name
        self.sal=sal
        self.age=age
        self.rating=rating
        self.is_online=True
        self.chats=[]
        self.current_status_message=None


class ChatMsg:
    def __init__(self,message,sent_by_me):
        self.message=message
        self.time=datetime.now()
        self.sent_by_me=sent_by_me

friend1=Spy("Simran","Miss.",21,4.7)
friend2=Spy("Deep","Mr.",18,4.26)
friend3=Spy("Pooja","Miss.",22,4.56)
spy=Spy("Aman","Miss.",21,4.76)

friends=[friend1,friend2,friend3]








