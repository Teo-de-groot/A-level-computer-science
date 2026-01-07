def gespalten(dasfeld):
    mittelteil = (len(dasfeld)//2)
    dasfeldlinks = []
    dasfeldrechts = []
    for verzeichnis in range(len(dasfeld)):
        if verzeichnis < mittelteil:
            dasfeldlinks.append(dasfeld[verzeichnis])
        else:
            dasfeldrechts.append(dasfeld[verzeichnis])
    return dasfeldlinks, dasfeldrechts 

def verschmelzen(dasfeldein,dasfeldzwei):
    schalterein = 0
    schalterzwei = 0
    erzeugnis =[]
    while schalterein <len(dasfeldein)-1 and schalterzwei<len(dasfeldzwei)-1:
        if dasfeldein[schalterein] < dasfeldzwei[schalterzwei]:
            erzeugnis.append(dasfeldein[schalterein])
            schalterein+=1
        else:
            erzeugnis.append(dasfeldzwei[schalterzwei])
            schalterzwei+=1
    if schalterein == len(dasfeldein) and schalterzwei != len(dasfeldzwei):
        erzeugnis.append(dasfeldzwei[schalterzwei:len(dasfeldzwei)-1])
    if schalterzwei == len(dasfeldzwei)and schalterein != len(dasfeldein):
        erzeugnis.append(dasfeldein[schalterein:len(dasfeldein)-1])
    return erzeugnis
def sortierungzusammenführen(dasfeld):
    if len(dasfeld) <= 1:
        return dasfeld
    else:
        links = gespalten(dasfeld)[0]
        rechts = gespalten(dasfeld)[1]
        sortierungzusammenführen(links)
        sortierungzusammenführen(rechts)
        return verschmelzen(links,rechts)
print(sortierungzusammenführen([1,0,2,3,5,67,8,1]))