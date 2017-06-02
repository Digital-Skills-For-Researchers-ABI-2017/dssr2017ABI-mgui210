#In this Interface script, an object of class "figureCreate" is created for each of
#the ___ models in the journal article titled _______. The name of each of these objects
#is simply "Figure_" + the Figure number (e.g. Figure_1).  Each figureCreate object
#has 4 attributes:
#   1) The Figure number
#   2) The Main Model needed to generate the data within the figure
#   3) The specific cross-bridge model that the main model requires
#   4) The specific Ca2+ model that the main model requires

import numpy as np
import matplotlib.pyplot as plt
import csv
import os

class figureCreate:
    def __init__(self, figureNumber, mainModel, xbModel, ca2Model, xVariables, yVariables, ca2Type):
        self.figureNumber = figureNumber #This is an integer value
        self.mainModel = mainModel #This is a cellml file
        self.xbModel = xbModel #This is a cellml file
        self.ca2Model = ca2Model #This is a cellml file
        self.xVariables = xVariables #This is the CSV column title(s) (e.g. [A, A])
        self.yVariables = yVariables #This is the CSV column title(s) (e.g. [B, D])
        self.ca2Type = ca2Type #This is either fixed (F) or Dynamic (D)
        

def main():
    Figures = []
    Figures.append(figureCreate(1, "Main", "XB", "Ca2", ["xdata1", "xdata2", "xdata3"], ["ydata1", "ydata2", "ydata3"], "D"))
    Figures[1 - 1].afterloads = [0.12, 0.15, 0.2]
    Figures[1 - 1].sarcomereLengths = [1.9359, 2.0139, 2.1054]
    

    #Depending on the number of figures ("x"), there will be x number of "Figure_x" objects 


    #Once each Figure from article ____ has a corresponding object of the class figureCreate,
    #A mechanism will be developed that grabs the appropriate models and runs them on hpc
    #based on what figure (Figure_1, Figure_2, etc...) the user wants to replicate.

    userInput = int(input("Please type the Figure number you wish to reproduce: "))
    fig2Reproduce =  Figures[userInput-1]
    figureNumber = "Figure" + str(userInput)
    print("Reproducing " + "Figure " + str(userInput) + ", please wait...")

    #Run the MeganModel

    #Create the .csv output data file (this could happen in the protocol .py document itself?)

    #Identify which file to access (which file has the data you need) based on an objects attributes and the matching filename
        #To grab the correct file from the Output folder, I need to know:
        # 1) the figureNumber
        # 2) Fixed or dynamic [Ca2+]i (e.g. F, D) --> this also comes from the model version run
        # 3) the contraction type (e.g. WL, Iso, QR) --> this comes from the Model version run
        # 4) The afterload value or sarcomere length(e.g. 0.15)
        # ^ THIS IS THE NAMING CONVENTION FOR THE DATA PRODUCED BY THIS CODE
        
        # 5) I also need to know the .CSV columns that hold the data.  This information is saved in an object attribute

    #How to determine whether a createFigureobject has a .aftreload attribute (indicating work-loops), a .sarcomereLengths attribute (indicating Isometric contractions), or both
    TorF_WL = hasattr(fig2Reproduce, "afterloads")
    TorF_Iso = hasattr(fig2Reproduce, "sarcomereLengths")
    
    if TorF_WL == True:
        for i in range(len(fig2Reproduce.afterloads)):
            outputDataFiles = os.listdir("Test_Output")
            dataFile = figureNumber + "_" + str(fig2Reproduce.ca2Type) + "_" + "WL" + str(fig2Reproduce.afterloads[i]) + ".CSV"
            outputDataPath = os.path.join("Test_Output", dataFile)
            print(outputDataPath)

            xData = []
            yData = []
            with open(outputDataPath, 'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=',')
                next(plots, None) #Skip the header line
                for row in plots:
                    xData.append(float(row[1])/2.3)
                    yData.append(float(row[3]))

            plt.plot(xData, yData, label='Loaded from file!')
            plt.axis([0.75, 1, 0, 0.5])
        plt.show()
                    

    if TorF_Iso == True:
        for i in range(len(fig2Reproduce.afterloads)):
            #ataFile = Test_Output\ figureNumber + "_" + str(fig2Reproduce.ca2Type) + "_" + "Iso" + str(fig2Reproduce.sarcomereLengths[i]) + ".CSV"
            print("test")
    
        
    #Plot the figure!
    lengthData = len(fig2Reproduce.xVariables)
    print(lengthData)

    
    #data2Plot = 
    #plt.plot(
##    plt.plot([0.76,0.79,0.85,0.9], [1,17,30,40], ':')
##    # 'o', '--', ':', '-.'
##    plt.axis([0.75, 1, 0, 60])
##    plt.ylabel('Normalised Force')
##    plt.xlabel('Sarcomere Length (um)')
##    plt.show()

if __name__ == "__main__":
    main()




