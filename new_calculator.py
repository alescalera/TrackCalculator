def alt_calc(Sex, Event, Hours, Minutes, Seconds, Elevation, Units, Prediction_Elevation):
    
    #import datetime
    from datetime import timedelta
    def convert(racetime):
   
        #racetime=(datetime.timedelta(seconds=round(racetime,2)))
        
        isec, fsec = divmod(round(racetime*100), 100)
        racetime="{}.{:02.0f}".format(timedelta(seconds=isec), fsec)
        #racetime= racetime.round(freq='milliseconds')
        #racetime=str(racetime)
        #racetime= ("{:.2f}".format(racetime))
        #racetime= f"{racetime:.2f}"

        #racetime=racetime[:-4] does not work returns 0:0 if the time does not have many decimals
        #print("The income tax is $" + str(round(incomeTax,2)))
        return racetime
    
    SeaLevel=150

    if (Units != "Meters"):
        Elevation=Elevation*(.3048)
        Prediction_Elevation=Prediction_Elevation*(.3048)

    Time=Seconds + (Minutes*60) + (Hours*3600)
            #Creating slopes and intercepts **make sure intercept is negative if necessary 
            #because the rest of the code always adds b so would be inaccurate if subtraction is needed if b is not negative
            
    if ((Sex=="Male") and (Event=="Mile")):
        m= 0.001871448342
        b= -0.231775873772
    elif ((Sex=="Female") and (Event=="Mile")):            
        m= 0.001841092683 
        b= -0.042428691489
    elif ((Sex=="Male") and (Event=="800m")):
        m= 0.000334921185 
        b= -0.025048730544
    elif ((Sex=="Female") and (Event=="800m")):
        m= 0.000628120990 
        b= -0.015506335730
    elif ((Sex=="Male") and (Event=="3000m")):
        m= 0.002211082547 
        b= -0.212251498962
    elif ((Sex=="Female") and (Event=="3000m")):
        m= 0.002345307492
        b= -0.154166328260
    elif ((Sex=="Male") and (Event=="5000m")):
        m= 0.002066578313 
        b= -0.015641727082
    elif ((Sex=="Female") and (Event=="5000m")):
        m= 0.001841092683 
        b= -0.042428691489
    elif ((Sex=="Male") and (Event=="10000m")):
        m= 0.001908811934 
        b= - 0.060623867008
    elif ((Sex=="Female") and (Event=="10000m")):
        m= 0.001830884701
        b= - 0.058148898108
    elif ((Sex=="Male") and (Event=="Half Marathon")):
        m= 0.001507700686 
        b= - 0.047884573788
    elif ((Sex=="Female") and (Event=="Half Marathon")):
        m= 0.001428200543 
        b= - 0.045359649250
    elif ((Sex=="Male") and (Event=="Marathon")):
        m= 0.001131854574 
        b= - 0.035947701281
    elif ((Sex=="Female") and (Event=="Marathon")):
        m= 0.001053186313 
        b= - 0.033449197286
#1)No Conversion
    if  ((Elevation <=SeaLevel) and (Prediction_Elevation <=SeaLevel)) or (Elevation==Prediction_Elevation):
        Prediction=convert(Time)
        return Prediction

#2)If converting up the mountain
    if (Elevation < Prediction_Elevation):
        SLpercent=(m) * Elevation + (b) #figure out the percent difference based on prediction equation
        Percent=(m) * Prediction_Elevation + (b) #figure out the percent difference for Prediction Elevation
        Delta=Percent-SLpercent #Predicted Elevation - Elevation percent
        Delta=Delta/100#divide percent by 100
        Predicted=Time+(Time*Delta)#Predicted is equal to time plus adjustment percent added
        Prediction=convert(Predicted)
        return Prediction
        #return Predicted

#3)If converting down the mountain
    elif (Prediction_Elevation < Elevation):
        SLpercent=(m) * Prediction_Elevation + (b) #figure out the percent difference based on prediction equation
        Percent=(m) * Elevation +(b) #figure out the percent difference for Elevation
        Delta=Percent-SLpercent #Predicted Elevation - Elevation percent
        Delta=Delta/100#divide percent by 100
        Predicted=Time/(1+Delta)#Predicted is equal to time MINUS adjustment percent 
        Prediction=convert(Predicted)
        return Prediction
        #return Predicted

        

