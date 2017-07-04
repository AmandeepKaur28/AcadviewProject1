# importing classes Spy,ChatMsg and list (friends) and object named spy of class Spy
from spy_detail import spy,Spy,friends,ChatMsg
from steganography.steganography import Steganography  # importing Steganography library for message encoding
from termcolor import *  #import all the files from termcolor module to print colored text on terminal
import colorama #import colorama file to print the colored text on terminal
colorama.init()

STATUS_MESSAGE = ["hey!their i am using whatsapp", "Sleeping", "At gym"]  # for default status
print "Hello! Let\'s get started"

response = "continue as " + spy.sal + " " + spy.name + "(Y/N)??"   # to continue with the default user
existing = raw_input(response)

# def is used to create a function , add status is a function to add new status or to select status from existing status
def add_status():

    updated_status_message = None

    if spy.current_status_message != None:

        print "your current status message is %s " % (spy.current_status_message)

    else:
        print "you don't have any status"

    default = raw_input("do you want to select status from older status [Y/N]??")

    if default.upper() == "N":  # upper function will convert lower case letter to upper case letter
        new_status_message = raw_input("What status message do you want to set?")

        if len(new_status_message) > 0:
            STATUS_MESSAGE.append(new_status_message)  # append function  is basically used in Python to add one element
            updated_status_message = new_status_message



    elif default.upper() == "Y":  #upper function will convert lower case letter to upper case letter

        item_position = 1

        for message in STATUS_MESSAGE:  # to print the status list loop is applied
            print ("%d %s")%(item_position,message)
            item_position = item_position + 1

        msg_selection = int(raw_input(" choose from above status\n"))


        if len(STATUS_MESSAGE) >= msg_selection:
            updated_status_message = STATUS_MESSAGE[msg_selection - 1]  # in zero base indexing  the first element is at index 0
    else:
        print "The option you chose is not valid! Press either y or n."


    return updated_status_message

#add_friend function is used to add no of friends ,in this we create object as new_friend of Spy class
def add_friend():
    new_friend =Spy('','',0,0.0)


    new_friend.name = raw_input("enter your name")
    # len function checks the length text to prevent from empty input to the name
    if len(new_friend.name) > 0 and new_friend.name.isspace() == False: #isspace() checks whether the string consists of whitespace
        new_friend.salutation = raw_input("Are they Mr. or Miss.?: ")
        if new_friend.salutation == "Mr." or new_friend.salutation == "Miss.":

            new_friend.name = new_friend.salutation + " " + new_friend.name
            new_friend.age = int(raw_input("enter your age"))
            new_friend.rat = float(raw_input("enter your rating"))

            if new_friend.age > 12 and new_friend.rat > spy.rating:
                friends.append(new_friend)
                print "friend added"

            else:
                print "please enter valid age or rating"

        else:
            print "please enter valid salutation"

    else:
        print "Sorry!!we can't move further please enter valid spy name"

    return len(friends) # it returns no of friends which are added in the fri

# select_friend () is used to choose friend from your friend list
def select_friend():
    item_number=0

    for friend in friends:
        print "%d. %s %s aged %d with rating %.2f" % (item_number +1, friend.sal,friend.name,friend.age,friend.rating)
        item_number = item_number+1

    friend_choice=raw_input("choose friend from your friend list")

    friend_choice_position=int(friend_choice)-1

    return friend_choice_position

# send_message () will select friends from friend list to whom you want to send message ,sends the message to other
# friend by encoding the message
def send_message():
  friend_choice = select_friend()

# ask to give input to which user want to encode
  original_image = raw_input("what is the name of your image??")
  output_path = "output.jpg"
  text = str(raw_input("What do you want to say?"))  # ask to enter message which you want to hide
  list_of=text.split(" ")
  if len(list_of)>=100:
      print "you cross your limit"

  else:
      print "Your secret message is ready!"

      #Using the Steganography library hide the message inside the image
      Steganography.encode(original_image, output_path, text)
      new_chat =ChatMsg(text,True)

     #Append the chat message to 'chats' key for the friends list.
      friends[friend_choice].chats.append(new_chat)


# read_message() It should call the select_a_friend method to get which friend is to be communicated
def read_message():
      sender = select_friend()

      #Ask the user for the name of the image they want to decode the message from
      output_path = raw_input("What is the name of the file?")

      secret_text = Steganography.decode(output_path)

      new_chat =  ChatMsg(secret_text,False)

     #Append the chat dictionary to chats key for the particular friend
      friends[sender].chats.append(new_chat)

      print "Your secret message has been saved!" +secret_text
      list_of = secret_text.split(" ")
      for ele in list_of:
          if ele == "SOS" or ele == "sos" or ele == "SAVE" or ele == "save" or ele == "help" or ele == "HELP":  # If a spy sends a message with special words such as SOS or SAVE ME or HELP ,then display a message and exit the application.
              print "Spy is in danger!"
              exit()


#It used to print the chat history for that particular friend
def read_chat_history():
    read_for=select_friend()
    for chat in friends[read_for].chats:

        if chat.sent_by_me:
            cprint("[%s]" % chat.time.strftime("%d %B %Y"), "blue")  # print chat history using different colors
            cprint("%s" % "you said:", "red")
            print "%s" % chat.message
        else:
            cprint("[%s]" % chat.time.strftime("%d %B %Y"), "blue")
            cprint("%s said:" % friends[read_for].name, "red")
            print "%s" % chat.message


# spy_chat() function has multiple choices to do
def spy_chat(spy):

    spy.name=spy.sal+" "+spy.name

    if spy.age > 12 and spy.age < 50:

        print "Authentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "what you want to do? 1.add a status \n 2.add a friend \n 3.Send a scret message\n 4.Read a secret message\n 5.Read chat history\n 6.Close Application"
            menu_choice =raw_input(menu_choices)

            if len(menu_choice) > 0:
               menu_choice = int(menu_choice)
               if menu_choice == 1:
                   spy.current_status_message = add_status()
               elif menu_choice == 2:
                  number_of_friends = add_friend()
                  print "you have %d friends" % (number_of_friends)
               elif menu_choice == 3:
                   send_message()
               elif menu_choice == 4:
                   read_message()
               elif menu_choice == 5:
                  read_chat_history()

               elif menu_choice==6:
                   show_menu = False


    else:
        print "Sorry you are not of the correct age to be a spy"

# if spy wants to continue as default user
if (existing == "Y" or existing == "y"):
    print " Welcome you can continue with your existing account " + spy.name + " " + str(spy.age)
    spy_chat(spy)

#  For new user app should ask for the name of the user,age and for rating
else:
    spy = Spy('','',0,0.0)
    spy.name = raw_input("welcm to the spy chat,plss enter your name first:")
    if len(spy.name) >0 and spy.name.isspace()==False:

        spy.sal = raw_input("Should i call you Mr.or Miss.")

        if spy.sal=="Mr." or spy.sal=="Miss.":

            spy.age = int(raw_input("enter your age"))


            spy.rating = float(raw_input("enter spy rating"))

            spy_chat(spy)

        else:
            print "please enter the valid salutation"

    # when spy wants to enter without valid name
    else:
        print "Please add a valid spy name"


