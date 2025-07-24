import time 

timestamp = time.strftime("%H:%M:%S" , time.localtime())
print("Current time:", timestamp)

# while True:
#     # timestamp = time.strftime("%H:%M:%S")
#     if timestamp == "21:37:30":
#         print("It's noon!")
#         break
#     else:
#         print("Waiting for noon...")
#         time.sleep(1)