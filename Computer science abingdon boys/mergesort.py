def gespalten(dasfeld):
    # تقسيم القائمة إلى نصفين
    mittelteil = (len(dasfeld)//2)
    dasfeldlinks = []
    dasfeldrechts = []
    for verzeichnis in range(len(dasfeld)):
        if verzeichnis < mittelteil:
            dasfeldlinks.append(dasfeld[verzeichnis])
        else:
            dasfeldrechts.append(dasfeld[verzeichnis])
    return dasfeldlinks, dasfeldrechts 

def verschmelzen(dasfeldein, dasfeldzwei):
    # دمج قائمتين مرتبتين في قائمة واحدة مرتبة
    schalterein = 0
    schalterzwei = 0
    erzeugnis = []

    while schalterein < len(dasfeldein) and schalterzwei < len(dasfeldzwei):
        if dasfeldein[schalterein] < dasfeldzwei[schalterzwei]:
            erzeugnis.append(dasfeldein[schalterein])
            schalterein += 1
        else:
            erzeugnis.append(dasfeldzwei[schalterzwei])
            schalterzwei += 1

    # إضافة العناصر المتبقية
    if schalterein < len(dasfeldein):
        erzeugnis.extend(dasfeldein[schalterein:])
    if schalterzwei < len(dasfeldzwei):
        erzeugnis.extend(dasfeldzwei[schalterzwei:])

    return erzeugnis

def sortierungzusammenführen(dasfeld):
    # شرط الإيقاف
    if len(dasfeld) <= 1:
        return dasfeld
    else:
        links, rechts = gespalten(dasfeld)
        # فرز كل نصف بشكل عودي
        links = sortierungzusammenführen(links)
        rechts = sortierungzusammenführen(rechts)
        # دمج النصفين
        return verschmelzen(links, rechts)

print(sortierungzusammenführen([1,0,2,3,5,67,8,1]))
