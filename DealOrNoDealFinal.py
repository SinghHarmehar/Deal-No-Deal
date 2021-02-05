# Authors:Harmehar Singh
# Date: October 13th 2020
# Class: ICS4U with Mr. Bulhao
# Program: Deal or No Deal
# Description: this program is a re-creation of the iconic Deal or No Deal game

#I imported the random module from Python
import random
#I imported the Tk, Frame, Label, PhotoImage, Button, and messagebox modules from tkinter
from tkinter import Tk, Frame, Label, PhotoImage, Button
from tkinter import messagebox
#Here I created a list of all the values that each briefcase could have in ascending order (unshuffledListValues). This becomes helpful in the functions below    
unshuffledListValues= [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]      
#This function gets a photo from the list imgBriefcases and returns said image
def increaseX(n):
    photo= imgBriefcases[n]
    return photo
#This function runs if the user clicks the exit button in order to make sure that they really do want to exit the game
def closeOption():
    answer = messagebox.askyesno("EXIT", "Are you sure you want to exit?")

    if answer == True:
        messagebox.showinfo("", "Thank you for playing Deal or No Deal")
        exit()
#This function creates as well as places all the frames (other than the initial frame) used in this program
def createFrames():
    global westframe, eastframe, centerframe, lastrowframe
    westframe = Frame(frame, padx=10, pady=10, bg="black")
    eastframe = Frame(frame, padx=10, pady=10, bg="black")
    centerframe = Frame(frame, padx=10, pady=10, bg="black", width=380, height=280)
    lastrowframe= Frame(centerframe, bg="black")

    westframe.grid(row=1, column=0)
    eastframe.grid(row=1, column=2)
    centerframe.grid(row=1, column=1)
    lastrowframe.grid(row=5, column=0, columns=6)
#This function creates a 2D List that holds buttons and places them on their designated spots. Each button holds an image of a numbered briefcase
def createButtons():
    global briefcaseList
    #I initialized a jagged list called briefcaseList
    briefcaseList= [[] for cols in range(5)]
    #I set the length of the rows in briefcaseList (except for the last row)
    briefcaseList[0]= [0] * 5
    briefcaseList[1]= [0] * 5
    briefcaseList[2]= [0] * 5
    briefcaseList[3]= [0] * 5
    #x is set to 0
    x= 0
    #While x is less than 20, the commands below will run
    while x < 20:
        #A button is created and added to each index location in briefcaseList (excluding the last row)
        for rows in range(len(briefcaseList)):
            for cols in range(len(briefcaseList[rows])):
                photo= increaseX(x)
                briefcaseList[rows][cols]= Button(centerframe, bg="black", bd=0, image= photo, command=lambda r=rows, c=cols: evaluateBriefcases(r, c))
                briefcaseList[rows][cols].grid(row=rows+1, column=cols, padx=7, pady=7, sticky="e")   
                #x increases by 1    
                x += 1
    #The length of the last row in briefcaseList is set here          
    briefcaseList[4]= [0] * 6
    #While x is higher than 19 but smaller than 26, the commands below will run
    while x > 19 and x < 26:
        #A button is created and added to each index location in the last row of briefcaseList
        for cols in range(len(briefcaseList[4])):
            photo= increaseX(x)
            briefcaseList[rows][cols]= Button(lastrowframe, bg="black", bd=0, image= photo, command=lambda r=rows, c=cols: evaluateBriefcases(r, c))
            briefcaseList[rows][cols].grid(row=rows+1, column=cols, padx=7, pady=7, sticky="e")
            #x increases by 1   
            x += 1
#This function creates the money labels that appear on either side of the buttons              
def showSideLabels():
    #r1 and r2 are set as 0
    r1= 0
    r2= 0
    for i, x in enumerate(labelList):
        #if i is less then 13 then the commands below will run
        if i < 13:
            #If x is equal to True, a label with an image of the money label is created
            if x == True:
                y= Label(westframe, image= imgCashLetter[i], background="black")
            #If x is not equal to True, a label with a blank image is created
            else:
                y= Label(westframe,  background="black", image= imgBlankLabel)
            #The label that was created is placed on westframe
            y.grid(row=r1, column=0, pady=3)
            #r1 increases by 1
            r1 += 1
        #if i is not less than 13 then the commands below will run
        else:
            #If x is equal to True, a label with an image of the money label is created
            if x == True:
                y= Label(eastframe, image= imgCashLetter[i], background="black")
            #If x is not equal to True, a label with a blank image is created
            else:
                y= Label(eastframe, background="black", image= imgBlankLabel)
            #The label that was created is placed on eastframe
            y.grid(row=r2, column=0, pady=3)
            #r2 increases by 1
            r2 += 1
#This function gets the value from listValues that would match the button that the user clicks (for example the first briefcase button matches the value at index 0 of listValues etc.)
def getBriefcaseVal(r, c):
    global boxNumber
    #If r is 5, then the commands below will run
    if r == 5:
        #The index of listValues which matches the index of the briefcase button clicked can be found by adding c and 20 together
        index= 20 + c
        #boxNumber is determined by adding 1 to index
        boxNumber= index + 1
        #The matching value from listValues is found here, assigned to the variable a, and returned
        a= listValues[index]
     
    #If r is not 5, then the commands below will run
    else:
        #The index of listValues which matches the index of the briefcase button clicked can be found by adding c to r times 5
        index= c + r * 5
        #boxNumber is determined by adding 1 to index
        boxNumber= index + 1
        #The matching value from listValues is found here, assigned to the variable a, and returned
        a= listValues[index]
    return a
#This function looks at the value of the briefcase button chosen and then uses the unshuffledListValues in order to remove the image of the money label with that value    
def removeLabel(r, c):
    #The getBriefcaseVal() function is called here and the resulting value is assigned to briefcaseVal
    briefcaseVal= getBriefcaseVal(r, c)
    #The index() function finds the index where briefcaseVal is located within unshuffledListValues and assigns that value to the variable index
    index= unshuffledListValues.index(briefcaseVal)
    #The value at the location index in labelList is set to False
    labelList[index]= False
    showSideLabels()
#This function asks the player if they want to play the game again and takes action based on their answer    
def askPlayAgain():
    answer= messagebox.askyesno("Exit", "Do you want to play again?")
         
    if answer == True:
        defaultSettings()
    elif answer == False:
        messagebox.showinfo("", "Thank you for playing Deal or No Deal")
        exit()
#This function creates the bankers offer based the total money left in the game and the round number    
def offerMoney():
    global totalMoney, counter, roundNum, briefcasesLeft, chosenBriefcaseVal, moneyVal, lblMessage
    #The offer is calculated by dividing totalMoney by the amount of boxes left multiplied by roundNum divided by 10
    offer= (totalMoney / (26 - counter)) * roundNum / 10
    offer= "{:,.2f}".format(offer)
    #The user is asked if they want to take the offer or not and the program takes action based on their answer
    answer= messagebox.askyesno("", "The banker's offer is $" + str(offer) + "\nWould you like to take the deal?")
    #If the user says yes, then the user is told what amount of money they are going home with (offer) and what amount of money they could have gone home with (chosenBriefcaseVal)
    if answer == True:
        chosenBriefcaseVal= "{:,.2f}".format(chosenBriefcaseVal)
        messagebox.showinfo("", "Congrats...you are going home with $" + offer)
        messagebox.showinfo("", "You could have gone home with $" + chosenBriefcaseVal)
        #The user is asked if they want to play again because the askPlayAgain() function is called here
        askPlayAgain()
    #If the user says yes, the game moves to the next round and the amount of briefcases that the user can remove (briefcasesLeft) is updated
    elif answer == False:
        roundNum += 1
        
        if roundNum == 2:
            briefcasesLeft= 5
        elif roundNum == 3:
            briefcasesLeft= 4
        elif roundNum == 4:
            briefcasesLeft= 3
        elif roundNum == 5:
            briefcasesLeft= 2
        else:
            briefcasesLeft= 1
            
        lblMessage.config(text="Choose " + str(briefcasesLeft) + " briefcase(s) to remove")
        counter += 1  
    #If counter is 25, then the commands below will run 
    if counter == 25:
        #lastBriefcaseVal is calculated by subtracting chosenBriefcaseVal from totalMoney
        lastBriefcaseVal= totalMoney - chosenBriefcaseVal
        lastBriefcaseVal= "{:,.2f}".format(lastBriefcaseVal)
        #The user is told that there is one more case left and is asked if they want to select that case or keep their own case
        answer2= messagebox.askyesno("", "There is only one case left!\nWould you like to keep your case?")
        #If the user chooses to keep their case, they are told how much money they can go home with (chosenBriefcaseVal)
        if answer2 == True:
            chosenBriefcaseVal= "{:,.2f}".format(chosenBriefcaseVal)
            messagebox.showinfo("", "Congrats...you're going home with $" + chosenBriefcaseVal)
        #If the user chooses to go with the other case, they are told how much money they can go home with (lastBriefcaseVal)
        elif answer2 == False:
            messagebox.showinfo("", "Congrats...you're going home with $" + lastBriefcaseVal)
        #The user is asked if they want to play again because the askPlayAgain() function is called here
        askPlayAgain()
#This function will place the chosen briefcase on lblPlayersCase if the counter is 0, otherwise if the counter is more than 0 then the user will be 
#  allowed to remove a certain amount of briefcases. If the counter is at certain values then the offerMoney function is called  
def evaluateBriefcases(r, c):
    global counter, totalMoney, briefcasesLeft, chosenBriefcaseVal, moneyVal, lblMessage, lblPlayersCase, boxNumber
    #If the counter is equal to 0, the commands below will run
    if counter == 0:
        #The getBriefcaseVal() function is called here and the resulting value is assigned to the chosenBriefcaseVal variable
        chosenBriefcaseVal= getBriefcaseVal(r, c)
        #The image from the briefcase button that the user chose is assigned to the chosenBriefcase variable
        chosenBriefcase= briefcaseList[r][c].cget("image")
        #The button the user chose is disabled and the image on the button is set to a blank black image
        briefcaseList[r][c].config(state="disabled", image=imgBlank)
        #chosenBriefcase is added onto lblPlayersCase
        lblPlayersCase.config(image=chosenBriefcase)
        #The message on lblMessage is configured to tell the user how many briefcases they can remove and counter is increased by 1
        lblMessage.config(text="Choose " + str(briefcasesLeft) + " briefcase(s) to remove")
        counter += 1 
    #If counter is equal to or higher than 1
    elif counter >= 1:
        #briefcasesLeft is reduced by 1
        briefcasesLeft -= 1
        #The getBriefcasesVal() function is called and the resulting value is assigned to the moneyVal variable
        moneyVal= getBriefcaseVal(r, c)
        #The removeLabel() function is called here
        removeLabel(r, c)
        #The user is shown a messagebox that tells them how much money was in the briefcase they removed
        messagebox.showinfo("", "Box #" + str(boxNumber) + " contains $" + "{:,.2f}".format(moneyVal))
        #totalMoney is updated by subtracting moneyVal from totalMoney
        totalMoney= totalMoney - moneyVal
        #The button that the user chose is disabled and the image on the button is set to a blank black image
        briefcaseList[r][c].config(state="disabled", image=imgBlank)
        #If the counter is equal to any of the values listed below, the commands below will run
        if counter in [6, 11, 15, 18, 20, 21, 22, 23, 24, 25]:
            #The message on lblMessage is configured to tell the user how many briefcases they can remove and the offerMoney() function is called here
            lblMessage.config(text="Choose " + str(briefcasesLeft) + " briefcase(s) to remove")
            offerMoney()
        #If the counter is not equal to any of the values listed below, the commands below will run
        elif counter not in [0, 6, 11, 15, 18, 20, 21, 22, 23, 24, 25]:
            #The message on lblMessage is configured to tell the user how many briefcases they can remove and counter is increased by 1
            lblMessage.config(text="Choose " + str(briefcasesLeft) + " briefcase(s) to remove")
            counter += 1   
#This function defines and resets all the values and restarts the game if the user wants to play another round     
def defaultSettings():
    global counter, totalMoney, roundNum, briefcasesLeft, chosenBriefcaseVal, moneyVal, labelList, listValues, lblMessage, lblPlayersCase
    #I defined a new list called labelList and added 26 True's to the list
    labelList= [True] * 26
    #I created the counter, totalMoney, roundNum, briefcasesLeft, chosenBriefcasesVal, and moneyVal variables which will be used below
    counter= 0
    totalMoney= 3418416.01
    roundNum= 1
    briefcasesLeft= 6
    chosenBriefcaseVal= 0
    moneyVal= 0
    #I created a list called listValues that holds all the values each briefcase can have
    listValues= [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]  
    #I shuffled listValues to randomize the list
    random.shuffle(listValues)
    #A label that holds the title of the game (lblTitle) is created and placed onto the initial frame
    lblTitle = Label(frame, image=imgTitle, border=0)
    lblTitle.grid(row=0, column=0, columns=3)
    #A label that holds a message at the bottom of the window (lblMessage) is created and placed onto the initial frame
    lblMessage = Label(frame, width=35, bg="black", font=("Century Gothic", 14, "bold"), fg="#fcea97", text="Choose one of the briefcases!", justify="center")   
    lblMessage.grid(row=2, column=1, padx=10, pady=5)
    #A label that will hold the user's chosen briefcase (lblPlayersCase) is created and placed onto the initial frame
    lblPlayersCase = Label(frame, image=imgBlank, bg="black")
    lblPlayersCase.grid(row=2, column=0)
    #The createFrames(), createButtons(), and showSideLabels() functions are called here
    createFrames()
    createButtons()
    showSideLabels()
#A new window is initialized by using the Tk() function
root = Tk()
#Calling the title() function allowed the window to be renamed
root.title("Deal or No Deal")
#I used the protocol() function to install a handler for the close window protocol
root.protocol("WM_DELETE_WINDOW", closeOption)
#The initial frame was created and placed onto the window using pack()
frame = Frame(root, padx=10, pady=10, bg="black")
frame.pack()
#Here the title is converted into a PhotoImage and assigned to the imgTitle variable
imgTitle = PhotoImage(file="images/dond_logo.png")
#Here I created a list of PhotoImages that contain all 26 briefcases and assigned said list to the imgBriefcases variable
imgBriefcases= [PhotoImage(file="images/suitcases/case1.png"), PhotoImage(file="images/suitcases/case2.png"), PhotoImage(file="images/suitcases/case3.png"),
                PhotoImage(file="images/suitcases/case4.png"), PhotoImage(file="images/suitcases/case5.png"), PhotoImage(file="images/suitcases/case6.png"),
                PhotoImage(file="images/suitcases/case7.png"), PhotoImage(file="images/suitcases/case8.png"), PhotoImage(file="images/suitcases/case9.png"),
                PhotoImage(file="images/suitcases/case10.png"), PhotoImage(file="images/suitcases/case11.png"), PhotoImage(file="images/suitcases/case12.png"),
                PhotoImage(file="images/suitcases/case13.png"), PhotoImage(file="images/suitcases/case14.png"), PhotoImage(file="images/suitcases/case15.png"),
                PhotoImage(file="images/suitcases/case16.png"), PhotoImage(file="images/suitcases/case17.png"), PhotoImage(file="images/suitcases/case18.png"),
                PhotoImage(file="images/suitcases/case19.png"), PhotoImage(file="images/suitcases/case20.png"), PhotoImage(file="images/suitcases/case21.png"),
                PhotoImage(file="images/suitcases/case22.png"), PhotoImage(file="images/suitcases/case23.png"), PhotoImage(file="images/suitcases/case24.png"),
                PhotoImage(file="images/suitcases/case25.png"), PhotoImage(file="images/suitcases/case26.png")]
#Here I created a list of PhotoImages that contain all 26 money labels and assigned said list to the imgCashLetter variable
imgCashLetter= [PhotoImage(file="images/money/0.01.png"), PhotoImage(file="images/money/1.png"), PhotoImage(file="images/money/5.png"), PhotoImage(file="images/money/10.png"), PhotoImage(file="images/money/25.png"),
                PhotoImage(file="images/money/50.png"), PhotoImage(file="images/money/75.png"), PhotoImage(file="images/money/100.png"), PhotoImage(file="images/money/200.png"), PhotoImage(file="images/money/300.png"), 
                PhotoImage(file="images/money/400.png"), PhotoImage(file="images/money/500.png"), PhotoImage(file="images/money/750.png"), PhotoImage(file="images/money/1000.png"), PhotoImage(file="images/money/5000.png"), 
                PhotoImage(file="images/money/10000.png"), PhotoImage(file="images/money/25000.png"), PhotoImage(file="images/money/50000.png"), PhotoImage(file="images/money/75000.png"), PhotoImage(file="images/money/100000.png"), 
                PhotoImage(file="images/money/200000.png"), PhotoImage(file="images/money/300000.png"), PhotoImage(file="images/money/400000.png"), PhotoImage(file="images/money/500000.png"), PhotoImage(file="images/money/750000.png"), 
                PhotoImage(file="images/money/1000000.png")] 
#Here a blank image for the suitcases is converted into a PhotoImage and assigned to the imgBlank variable
imgBlank= PhotoImage(file= "images/suitcases/blankcase.png")
#Here a blank image for the money labels is converted into a PhotoImage and assigned to the imgBlankLabel variable
imgBlankLabel= PhotoImage(file="images/money/blankmoney.png")
#The defaultSettings() function is called here
defaultSettings()
#Calling the .mainloop() function here allows the window to form on the desktop
root.mainloop()
