import os
os.system("clear")
print("please wait")
print("\033[0;34m")
import time
import amino
os.system("clear")
print ("COINS TRANSFER BY SID")
time.sleep(0.5)
print("\n")
print("MADE BY DASH")
time.sleep(0.5)
print("\n")
client=amino.Client()
sid=input("SID: ")
client.login_sid(SID=sid)
time.sleep(0.5)
print("\n")
print("PUT ANY LINK OF BLOG BELONG TO THE PERSON YOU WANT TO SEND TO")

time.sleep(0.5)
print("\n")

link=input("THE LINK: ")
gpid=client.get_from_code(link)
blogid=gpid.objectId
comid=gpid.path[1:gpid.path.index("/")]

subclient = amino.SubClient(comId=comid, profile=client.profile)


coins=int(input("how much coins you want to send: "))

subclient.send_coins(coins=coins, blogId=blogid)
print("DONE")