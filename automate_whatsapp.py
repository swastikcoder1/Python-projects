import pywhatkit
import time
print('''
_________________________________________________________________________________
|NOTE:-                                                                          |
| 1. Open your default browser and make it to full screen before sending message |
| 2. Please ensure that you have a good internet speed before using this         |
----------------------------------------------------------------------------------
''')
time.sleep(3)
poll=input('''
1. Send in Phone no.
2. Send in Group.
      Type either 1 or 2
        ''')

message=input("Enter the message:\n")
time1=int(input("Enter hour according to 24 hr clock:\n "))
time2=int(input("Enter minutes:\n"))
if poll=="1":
    phone_no=input("Enter the Phone no. along with country code: \n")
    pywhatkit.sendwhatmsg(phone_no,message,time1,time2)

elif poll=="2":
    group_id=input("Enter the Group ID:\n")
    pywhatkit.sendwhatmsg_to_group(group_id,message,time1,time2)
