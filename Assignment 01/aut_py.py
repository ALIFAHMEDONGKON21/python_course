import pyautogui
from time import sleep

sleep(10)
n = int(input())
pyautogui.write('#', interval=0.25)
for i in range(1, n+1):
    
    for j in range(1, i+1):
        pyautogui.write('#', interval=0.25)
    pyautogui.write('\n', interval=0.25)



#
##
###
####
#####

