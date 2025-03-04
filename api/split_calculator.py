def split_calc(Hours,Minutes,Seconds,Race_Distance,Race_Units,Split_Distance,Split_Units):
    
    #import datetime
    from datetime import timedelta
    def convert(racetime):
        isec, fsec = divmod(round(racetime*100), 100)
        racetime="{}.{:02.0f}".format(timedelta(seconds=isec), fsec)
        racetime= racetime.lstrip("0,:")
        return racetime


    #get time in seconds   
    time=Seconds + (Minutes*60) + (Hours*3600)
    #Race Distance in m,km,or mi = convert to meters


    if Race_Units == 'Meters':
        meters=Race_Distance
    if Race_Units == 'Kilometers':
        meters=Race_Distance * 1000
    if Race_Units == 'Miles':
        meters=Race_Distance * 1609

    #calculate pace as sec/meter 
    pace=time/meters
    
    #Split Distance
    if Split_Units=='Meters':
        splitdistance=Split_Distance
    if Split_Units=='Kilometers':
        splitdistance=Split_Distance * 1000
    if Split_Units=='Miles':
        splitdistance=Split_Distance * 1609

    #pace / splitdistance = splittime
    splittime= pace * splitdistance

    split=convert(splittime)
    return split
    
