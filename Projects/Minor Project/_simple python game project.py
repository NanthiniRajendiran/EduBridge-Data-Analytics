#!/usr/bin/env python
# coding: utf-8

# In[20]:



print("""WELCOME! TO THIS GAME!!!
you are in a hurry to catch the train.Will you take the train ticket? (Yes / No)""")

answer_yes = ["yes","y"]
answer_no = ["no","n"]


ans1 = input("->")

if ans1 in answer_yes:
    print("\n Good.But you lost the train.Will you wait for the next train to arrive?(Yes / No)\n")

    ans2 = input("->")

    if ans2 in answer_yes:
        print("\n Then wait for next 45 mins.Game Over")

    elif ans2 in answer_no:
        print("\n Then take other mode of transport.Game Over")

    else:
        print("\nYou typed the wrong input. GOODBYE!")

elif ans1 in answer_no:
     print("\n yeah! you caught the train.will you pay the penalty? (Yes / No)\n")

     ans3 = input("->")

     if ans3 in answer_yes:
           print("\n Then pay the fine amount Happy Journey!.Game Over")

     elif ans3 in answer_no:
           print("\n You are handled over to Railway Protection Force(RPF).GAME OVER")

     else:
           print("\nYou typed the wrong input. GOODBYE!")

else:
    print("\nYou typed the wrong input. GOODBYE!")


# In[ ]:





# 

# In[ ]:





# In[ ]:




