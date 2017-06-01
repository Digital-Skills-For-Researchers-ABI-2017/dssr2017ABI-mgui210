#In this Interface script, an object of class "figureCreate" is created for each of
#the ___ models in the journal article titled _______. The name of each of these objects
#is simply "Figure_" + the Figure number (e.g. Figure_1).  Each figureCreate object
#has 4 attributes:
#   1) The Figure number
#   2) The Main Model needed to generate the data within the figure
#   3) The specific cross-bridge model that the main model requires
#   4) The specific Ca2+ model that the main model requires

import matplotlib.pyplot as plt

class figureCreate:
    def __init__(self, figureNumber, mainModel, xbModel, ca2Model, xVariables, yVariables, contractionType, ca2Type):
        self.figureNumber = figureNumber #This is an integer value
        self.mainModel = mainModel #This is a cellml file
        self.xbModel = xbModel #This is a cellml file
        self.ca2Model = ca2Model #This is a cellml file
        self.xVariables = xVariables #This is the CSV column title(s) (e.g. [A, A])
        self.yVariables = yVariables #This is the CSV column title(s) (e.g. [B, D])
        self.contractionType = contractionType # This could be work-loop (WL), Isometric (Iso), or quick-release (QR)
        self.ca2Type = ca2Type #This is either fixed (F) or dynamic (D)
        

def main():
    Figures = []
    Figures.append(figureCreate(1, "Main", "XB", "Ca2", ["xdata1", "xdata2", "xdata3"], ["ydata1", "ydata2", "ydata3"]))
    Figures[1 - 1].afterloads = [0.12, 0.15, 0.2]
    Figures[1 - 1].sarcomereLengths = [1.9359, 2.0139, 2.1054]
    

    #Depending on the number of figures ("x"), there will be x number of "Figure_x" objects 


    #Once each Figure from article ____ has a corresponding object of the class figureCreate,
    #A mechanism will be developed that grabs the appropriate models and runs them on hpc
    #based on what figure (Figure_1, Figure_2, etc...) the user wants to replicate.

    userInput = int(input("Please type the Figure number you wish to reproduce: "))
    fig2Reproduce =  Figures[userInput-1]
    figureNumber = "Figure" + str(userInput)
    print(figureNumber)
    print("Reproducing " + "Figure " + str(userInput) + ", please wait")

    #Run the MeganModel

    #Create the .csv output data file (this could happen in the protocol .py document itself?)

    #Identify which file to access (which file has the data you need) based on an objects attributes and the matching filename
        #To grab the correct file from the Output folder, I need to know:
        # 1) the figureNumber
        # 2) the contraction type (e.g. WL, Iso, QR) --> this comes from the Model version run
        # 3) Fixed or dynamic [Ca2+]i (e.g. F, D) --> this also comes from the model version run
        # 4) The afterload value or sarcomere length(e.g. 0.15)
        # ^ THIS IS THE NAMING CONVENTION FOR THE DATA PRODUCED BY THIS CODE
        
        # 5) I also need to know the .CSV columns that hold the data.  This information is saved in an object attribute

    for i in range(len(fig2Reproduce.afterloads)):
        dataFile = figureNumber + "_contractionType" + "_ForD" + "_" + str(fig2Reproduce.afterloads[i])
        
            
    print(dataFile)
        
    #Plot the figure!
    lengthData = len(fig2Reproduce.xVariables)
    print(lengthData)

    
    #data2Plot = 
    #plt.plot(
    plt.plot([0.76,0.79,0.85,0.9], [1,17,30,40], ':')
    # 'o', '--', ':', '-.'
    plt.axis([0.75, 1, 0, 60])
    plt.ylabel('Normalised Force')
    plt.xlabel('Sarcomere Length (um)')
    plt.show()

if __name__ == "__main__":
    main()




