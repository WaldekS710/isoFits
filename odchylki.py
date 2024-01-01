import re 

klasa = ['IT01', 'IT0', 'IT1','IT2','IT3','IT4','IT5','IT6','IT7','IT8','IT9','IT10','IT11','IT12','IT13','IT14','IT15','IT16','IT17','IT18']

OtworyAdoG_przedzialy=[3, 6, 10, 14, 18, 24, 30, 40, 50, 65, 80, 100, 120, 140, 160, 180, 200, 225, 250, 280, 315, 355, 400, 450, 500]
przedzialy = [3, 6, 10, 18, 30, 50, 80, 120, 180, 250, 315, 400, 500]

OtworyAdoG_litery = ['A', 'B', 'C', 'CD', 'D', 'E', 'EF', 'F', 'FG', 'G']
OtworyAdoG_EI = {3:  [+270, +140, +60, +34, +20, +14, +10, +6, +4, +2],
                6:  [+270, +140, +70, +46, +30, +20, +14, +10, +6, +4],
                10:  [+280, +150, +80, +56, +40, +25, +18, +13, +8, +5],
                14:  [+290, +150, +95, +70, +50, +32, +23, +16, +10, +6],
                18:  [+290, +150, +95, +70, +50, +32, +23, +16, +10, +6],
                24:  [+300, +160, +110, +85, +65, +40, +28, +20, +12, +7],
                30:  [+300, +160, +110, +85, +65, +40, +28, +20, +12, +7],
                40:  [+310, +170, +120, +100, +80, +50, +35, +25, +15, +9],
                50:  [+320, +180, +130, +100, +80, +50, +35, +25, +15, +9],
                65:  [+340, +190, +140, "-", +100, +60, "-", +30, "-", +10],
                80:  [+360, +200, +150, "-", +100, +60, "-", +30, "-", +10],
                100:  [+380, +220, +170, "-", +120, +72, "-", +36, "-", +12],
                120:  [+410, +240, +180, "-", +120, +72, "-", +36, "-", +12],
                140:  [+460, +260, +200, "-", +145, +85, "-", +43, "-", +14],
                160:  [+520, +280, +210, "-", +145, +85, "-", +43, "-", +14],
                180:  [+580, +310, +230, "-", +145, +85, "-", +43, "-", +14],
                200:  [+660, +340, +240, "-", +170, +100, "-", +50, "-", +15],
                225:  [+740, +380, +260, "-", +170, +100, "-", +50, "-", +15],
                250:  [+820, +420, +280, "-", +170, +100, "-", +50, "-", +15],
                280:  [+920, +480, +300, "-", +190, +110, "-", +56, "-", +17],
                315:  [+1050, +540, +330, "-", +190, +110, "-", +56, "-", +17],
                355:  [+1200, +600, +360, "-", +210, +125, "-", +62, "-", +18],
                400:  [+1350, +680, +400, "-", +210, +125, "-", +62, "-", +18],
                450:  [+1500, +760, +440, "-", +230, +135, "-", +68, "-", +20],
                500:  [+1650, +840, +480, "-", +230, +135, "-", +68, "-", +20]}
OtworyPdoZC_litery = ['P',  'R',  'S',  'T',  'U',  'V',  'X',  'Y',  'z',  'ZA',  'ZB',  'ZC']
OtworyPdoZC_ES={3:  [-6, -10, -14, "-", -18, "-", -20, "-", -26, -32, -40, -60],
                    6:  [-12, -15, -19, "-", -23, "-", -28, "-", -35, -42, -50, -80],
                    10:  [-15, -19, -23, "-", -28, "-", -34, "-", -42, -52, -67, -97],
                    14:  [-18, -23, -28, "-", -33, "-", -40, "-", -50, -64, -90, -130],
                    18:  [-18, -23, -28, "-", -33, -39, -45, "-", -60, -77, -108, -150],
                    24:  [-22, -28, -35, "-", -41, -47, -54, -63, -73, -98, -136, -188],
                    30:  [-22, -28, -35, -41, -48, -55, -64, -75, -88, -118, -160, -218],
                    40:  [-26, -34, -43, -48, -60, -68, -80, -94, -112, -148, -200, -274],
                    50:  [-26, -34, -43, -54, -70, -81, -97, -114, -136, -180, -242, -325],
                    65:  [-32, -41, -53, -66, -87, -102, -122, -144, -172, -226, -300, -405],
                    80:  [-32, -43, -59, -75, -102, -120, -146, -174, -210, -274, -360, -480],
                    100:  [-37, -51, -71, -91, -124, -146, -178, -214, -258, -335, -445, -585],
                    120:  [-37, -54, -79, -104, -144, -172, -210, -254, -310, -400, -525, -690],
                    140:  [-43, -63, -92, -122, -170, -202, -248, -300, -365, -470, -620, -800],
                    160:  [-43, -65, -100, -134, -190, -228, -280, -340, -415, -535, -700, -900],
                    180:  [-43, -68, -108, -146, -210, -252, -310, -380, -465, -600, -780, -1000],
                    200:  [-50, -77, -122, -166, -236, -284, -350, -425, -520, -670, -880, -1150],
                    225:  [-50, -80, -130, -180, -258, -310, -385, -470, -575, -740, -960, -1250],
                    250:  [-50, -84, -140, -196, 284, -340, -425, -520, -640, -820, -1050, -1350],
                    280:  [-56, -94, -158, -218, -315, -385, -475, -580, -710, -920, -1200, -1550],
                    315:  [-56, -98, -170, -240, -350, -425, -525, -650, -790, -1000, -1300, -1700],
                    355:  [-62, -108, -190, -268, -390, -475, -590, -730, -900, -1150, -1500, -1900],
                    400:  [-62, -114, -208, -294, -435, -530, -660, -820, -1000, -1300, -1650, -2100],
                    450:  [-68, -126, -232, -330, -490, -595, -740, -920, -1100, -1450, -1850, -2400],
                    500:  [-68, -132, -252, -360, -540, -660, -820, -1000, -1250, -1600, -2100, -2600]}
OtworyJ_IT6doIT8_ES = {3: [+2, +4, +6], 6: [+5, +6, +10], 10: [+5, +8, +12], 14: [+6, +10, +15], 18: [+6, +10, +15],
                        24: [+8, +12, +20], 30: [+8, +12, +20], 40: [+10, +14, +24], 50: [+10, +14, +24], 65: [+13, +18, +28],
                        80: [+13, +18, +28], 100: [+16, +22, +34], 120: [+16, +22, +34], 140: [+18, +26, +41], 160: [+18, +26, +41],
                        180: [+18, +26, +41], 200: [+22, +30, +47], 225: [+22, +30, +47], 250: [+22, +30, +47], 280: [+25, +36, +55],
                        315: [+25, +36, +55], 355: [+29, +39, +60], 400: [+29, +39, +60], 450: [+33, +43, +66], 500: [+33, +43, +66]}
OtworyK_doIT8_ES = {3:  '0',6:  '-1+Delta',10:  '-1+Delta',14:  '-1+Delta',18:  '-1+Delta',24:  '-2+Delta',30:  '-2+Delta',
                 40:  '-2+Delta',50:  '-2+Delta',65:  '-2+Delta',80:  '-2+Delta',100:  '-3+Delta',120:  '-3+Delta',
                 140:  '-3+Delta',160:  '-3+Delta',180:  '-3+Delta',200:  '-4+Delta',225:  '-4+Delta',250:  '-4+Delta',
                 280:  '-4+Delta',315:  '-4+Delta',355:  '-4+Delta',400:  '-4+Delta',450:  '-5+Delta',500:  '-5+Delta'}
OtworyM_doIT8_i_powyzej_ES = {3: ['-2', -2],  6: ['-4+Delta', -4], 10: ['-6+Delta', -6], 14: ['-7+Delta', -7], 18: ['-7+Delta', -7],
                             24: ['-8+Delta', -8], 30: ['-8+Delta', -8], 40: ['-9+Delta', -9], 50: ['-9+Delta', -9],
                             65: ['-11+Delta', -11], 80: ['-11+Delta', -11], 100: ['-13+Delta', -13], 120: ['-13+Delta', -13],
                            140: ['-15+Delta', -15], 160: ['-15+Delta', -15], 180: ['-15+Delta', -15], 200: ['-17+Delta', -17],
                            225: ['-17+Delta', -17], 250: ['-17+Delta', -17], 280: ['-20+Delta', -20],315: ['-20+Delta', -20],
                            355: ['-21+Delta', -21], 400: ['-21+Delta', -21], 450: ['-23+Delta', -23], 500: ['-23+Delta', -23]}
OtworyNdoIT8iPowyzej_ES = {3: ['-4', -4], 6: ['-8+Delta', 0], 10: ['-10+Delta', 0], 14: ['-12+Delta', 0], 18: ['-12+Delta', 0], 
                           24: ['-15+Delta', 0], 30: ['-15+Delta', 0], 40: ['-17+Delta', 0], 50: ['-17+Delta', 0], 65: ['-20+Delta', 0], 
                           80: ['-20+Delta', 0], 100: ['-23+Delta', 0], 120: ['-23+Delta', 0], 140: ['-27+Delta', 0], 160: ['-27+Delta', 0], 
                           180: ['-27+Delta', 0], 200: ['-31+Delta', 0], 225: ['-31+Delta', 0], 250: ['-31+Delta', 0], 280: ['-34+Delta', 0], 
                           315: ['-34+Delta', 0], 355: ['-37+Delta', 0], 400: ['-37+Delta', 0], 450: ['-40+Delta', 0], 500: ['-40+Delta', 0]}

Tolerancja = {3:[0.3, 0.5, 0.8, 1.2, 2, 3, 4, 6, 10, 14, 25, 40, 60, 100, 140, 250, 400, 600, 1000, 1400],
    6:[0.4, 0.6, 1, 1.5, 2.5, 4, 5, 8, 12, 18, 30, 48, 75, 120, 180, 300, 480, 750, 1200, 1800],
    10:[0.4, 0.6, 1, 1.5, 2.5, 4, 6, 9, 15, 22, 36, 58, 90, 150, 220, 360, 580, 900, 1500, 2200],
    18:[0.5, 0.8, 1.2, 2, 3, 5, 8, 11, 18, 27, 43, 70, 110, 180, 270, 430, 700, 1100, 1800, 2700],
    30:[0.6, 1, 1.5, 2.5, 4, 6, 9, 13, 21, 33, 52, 84, 130, 210, 330, 520, 840, 1300, 2100, 3300],
    50:[0.6, 1, 1.5, 2.5, 4, 7, 11, 16, 25, 39, 62, 100, 160, 250, 390, 620, 100, 1600, 2500, 3900],
    80:[0.8, 1.2, 2, 3, 5, 8, 13, 19, 30, 46, 74, 120, 190, 300, 460, 740, 1200, 1900, 3000, 4600],
    120:[1, 1.5, 2.5, 4, 6, 10, 15, 22, 35, 54, 87, 140, 220, 350, 540, 870, 1400, 2200, 3500, 5400],
    180:[1.2, 2, 3.5, 5, 8, 12, 18, 25, 40, 63, 100, 160, 250, 400, 630, 1000, 1600, 2500, 4000, 6300],
    250:[2, 3, 4.5, 7, 10, 14, 20, 29, 46, 72, 115, 185, 290, 460, 720, 1150, 1850, 2900, 4600, 7200],
    315:[2.5, 4, 6, 8, 12, 16, 23, 32, 52, 81, 130, 210, 320, 520, 810, 1300, 2100, 3200, 5200, 8100],
    400:[3, 5, 7, 9, 13, 18, 25, 36, 57, 89, 140, 230, 360, 570, 890, 1400, 2300, 3600, 5700, 8900],
    500:[4, 6, 8, 10, 15, 20, 27, 40, 63, 97, 155, 250, 400, 630, 970, 1550, 2500, 4000, 6300, 9700]
}

Walek_przedzialy =    [3, 6, 10, 14, 18, 24, 30, 40, 50, 65, 80, 100, 120, 140, 160, 180, 200, 225, 250, 280, 315, 355, 400, 450, 500]
Walek_es = ['a', 'b', 'c', 'cd', 'd', 'e', 'ef', 'f', 'fg', 'g', 'h', 'js']
Walek_ei = ['m', 'n', 'p', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'za', 'zb', 'zc']
walek_a_do_g_es ={3: [-270,-140, -60, -34, -20, -14, -10, -6, -4, -2], 6: [-270,-140, -70, -46, -30, -20, -14, -10, -6, -4],
                10: [-280,-150, -80, -56, -40, -25, -18, -13, -8, -5],   14: [-290,-150, -95, -70, -50, -32, -23, -16, -10, -6],
                18: [-290,-150, -95, -70, -50, -32, -23, -16, -10, -6],  24: [-300,-160, -110, -85, -65, -40, -25, -20, -12, -7],
                30: [-300,-160, -110, -85, -65, -40, -25, -20, -12, -7], 40: [-310,-170, -120, -100, -80, -50, -35, -25, -15, -9],
                50: [-320,-180, -130, -100, -80, -50, -35, -25, -15, -9],65: [-340,-190, -140, '-', -100, -60, '-', -30, '-', -10],
                80: [-360,-200, -150, '-', -100, -60, '-', -30, '-', -10],100: [-380,-220, -170, '-', -120, -72, '-', -36, '-', -12],
                120: [-410,-240, -180, '-', -120, -72, '-', -36, '-', -12],140: [-460,-260, -200, '-', -145, -85, '-', -43, '-', -14],
                160: [-520,-280, -210, '-', -145, -85, '-', -43, '-', -14],180: [-580,-310, -230, '-', -145, -85, '-', -43, '-', -14],
                200: [-660,-340, -240, '-', -170, -100, '-', -50, '-', -15],225: [-740,-380, -260, '-', -170, -100, '-', -50, '-', -15],
                250: [-820,-420, -280, '-', -170, -100, '-', -50, '-', -15],280: [-920,-480, -300, '-', -190, -110, '-', -56, '-', -17],
                315: [-1050,-540, -330, '-', -190, -110, '-', -56, '-', -17],355: [-1200,-600, -360, '-', -210, -125, '-', -62, '-', -18],
                400: [-1350,-680, -400, '-', -210, -125, '-', -62, '-', -18],450: [-1500,-760, -440, '-', -230, -135, '-', -68, '-', -20],
                500: [-1650,-840, -480, '-', -230, -135, '-', -68, '-', -20]}
walek_j_ei = {3:[-2, -4,-6], 6:[-2, -4,'-'], 10:[-2, -5,'-'], 14:[-3, -6,'-'], 18:[-3, -6,'-'], 24:[-4, -8,'-'],
            30:[-4, -8,'-'], 40:[-5, -10,'-'], 50:[-5, -10,'-'], 65:[-7, -12,'-'], 80:[-7, -12,'-'], 100:[-9, -15,'-'],
            120:[-9, -15,'-'], 140:[-11, -18,'-'], 160:[-11, -18,'-'], 180:[-11, -18,'-'], 200:[-13, -21,'-'],
            225:[-13, -21,'-'], 250:[-13, -21,'-'], 280:[-16, -26,'-'], 315:[-16, -26,'-'], 355:[-18, -28,'-'],
            400:[-18, -28,'-'], 450:[-20, -32,'-'], 500:[-20, -32,'-']}
walek_m_do_zc_ei ={3:[+2, +4, +6, +10, +14, '-', +18, '-', +20, '-', +26, +32, +40, +60], 
                    6:[+4, +8, +12, +15, +19, '-', +23, '-', +28, '-', +35, +42, +50, +80], 
                    10:[+6, +10, +15, +19, +23, '-', +28, '-', +34, '-', +42, +52, +67, +97], 
                    14:[+7, +12, +18, +23, +28, '-', +33, '-', +40, '-', +50, +64, +90, +130], 
                    18:[+7, +12, +18, +23, +28, '-', +33, +39, +45, +39, +60, +77, +108, +150], 
                    24:[+8, +15, +22, +28, +35, '-', +41, +47, +54, +63, +73, +98, +136, +188], 
                    30:[+8, +15, +22, +28, +35, +41, +48, +55, +64, +75, +88, +118, +160, +218], 
                    40:[+9, +17, +26, +34, +43, +48, +60, +68, +80, +94, +112, +148, +200, +274], 
                    50:[+9, +17, +26, +34, +43, +54, +70, +81, +97, +114, +136, +180, +242, +325], 
                    65:[+11, +20, +32, +41, +53, +66, +87, +102, +122, +144, +172, +226, +300, +405], 
                    80:[+11, +20, +32, +43, +59, +75, +102, +120, +146, +174, +210, +274, +360, +480], 
                    100:[+13, +23, +37, +51, +71, +91, +124, +146, +178, +214, +258, +335, +445, +585], 
                    120:[+13, +23, +37, +54, +79, +104, +144, +172, +210, +254, +310, +400, +525, +690], 
                    140:[+15, +27, +43, +63, +92, +122, +170, +202, +248, +300, +365, +470, +620, +800], 
                    160:[+15, +27, +43, +65, +100, +134, +190, +228, +280, +340, +415, +535, +700, +900], 
                    180:[+15, +27, +43, +68, +108, +146, +210, +252, +310, +380, +465, +600, +780, +1000], 
                    200:[+17, +31, +50, +77, +122, +166, +236, +284, +350, +425, +520, +670, +880, +1150], 
                    225:[+17, +31, +50, +80, +130, +180, +258, +310, +385, +470, +575, +740, +960, +1250], 
                    250:[+17, +31, +50, +84, +140, +196, +284, +340, +425, +520, +640, +820, +1050, +1350], 
                    280:[+20, +34, +56, +94, +158, +218, +315, +385, +475, +580, +710, +920, +1200, +1550], 
                    315:[+20, +34, +56, +98, +170, +240, +350, +425, +525, +650, +790, +1000, +1300, +1700], 
                    355:[+21, +37, +62, + 108, +190, +268, +390, +475, +590, +730, +900, +1150, +1500, +1900], 
                    400:[+21, +37, +62, +114, +208, +294, +435, +530, +660, +820, +1000, +1300, +1650, +2100], 
                    450:[+23, +40, +68, + 126, +232, +330, +490, +595, +740, +920, +1100, +1450, +1850, +2400], 
                    500:[+23, +40, +68, +132, +252, +360, +540, +660, +820, +1000, +1250, +1600, +2100, +2600]}
walek_k_ei = {3:[0,0], 6:[+1,0], 10:[+1,0], 14:[+1,0], 18:[+1,0], 24:[+2,0], 30:[+2,0], 
            40:[+2,0], 50:[+2,0], 65:[+2,0], 80:[+2,0], 100:[+3,0], 120:[+3,0], 140:[+3,0], 
            160:[+3,0], 180:[+3,0], 200:[+4,0], 225:[+4,0], 250:[+4,0], 280:[+4,0], 
            315:[+4,0], 355:[+4,0], 400:[+4,0], 450:[+5,0], 500:[+5,0]}

def PoprawkaDelta(wymiar, Klasa):
    wymiar=zokragl(przedzialy,wymiar)
    T1 = Tolerancja[wymiar][klasa.index("IT"+str(Klasa))]
    T2 = Tolerancja[wymiar][klasa.index("IT"+str(Klasa-1))]
    return T1-T2

def zokragl(lista,wymiar):
    for i in lista:
        if wymiar<=i:
            return i
    return -1

def OtworPoprawnaTolerancja(Nominalny, Litera, KlasaDokladnosci):
    if Litera in OtworyAdoG_litery + OtworyPdoZC_litery:
       # dowolna klasa dokładności wykonania
        if Litera in ['CD', 'EF', 'FG']:
            if Nominalny > 50:
                return False
        if Litera in ['T', 'V', 'Y']:
            if Nominalny<=24 and Litera =='T':
                return False
            if Nominalny<=14 and Litera =='V':
                return False
            if Nominalny<=18 and Litera =='Y':
                return False
    elif Litera == "J" and not KlasaDokladnosci in [6,7,8]:
            return False
    elif Litera == "K" and KlasaDokladnosci>8 and Nominalny>3:
            return False
    else:
        return True
        

def OdchylkiOtworu(Nominalny, Litera, KlasaDokladnosci, opis=False, Dictionary=False):
    
    if not OtworPoprawnaTolerancja(Nominalny, Litera, KlasaDokladnosci):
        print("dla tolerancji {0}{1}{2} w normie PN-EN ISO 286-1: 2011P nie zdefiniowano odchyłek".format(Nominalny, Litera, KlasaDokladnosci))
        return 
    
    T = Tolerancja[zokragl(przedzialy,Nominalny)][klasa.index("IT"+str(KlasaDokladnosci))]
    o =  zokragl(OtworyAdoG_przedzialy,Nominalny)
    if Litera in OtworyAdoG_litery:
        o =  zokragl(OtworyAdoG_przedzialy,Nominalny)
        EI = OtworyAdoG_EI[o][OtworyAdoG_litery.index(Litera)]
        ES = T+EI
    if Litera in OtworyPdoZC_litery:
        o =  zokragl(OtworyAdoG_przedzialy,Nominalny)
        ES = OtworyPdoZC_ES[o][OtworyPdoZC_litery.index(Litera)]
        if KlasaDokladnosci<=7 :
            ES = ES+PoprawkaDelta(Nominalny, KlasaDokladnosci)
        EI = ES - T
    if Litera == "H":
        EI = 0
        ES = T
    if Litera in ['K', 'M', 'N']:
        Delta = PoprawkaDelta(Nominalny, KlasaDokladnosci)
        if Litera =='K':
            if KlasaDokladnosci<=8:
                ES = eval(OtworyK_doIT8_ES[o])
            else:
                blad = "Pasowanie K tylko do IT8"
        if Litera == 'M': # Dla M6 jest inaczej
            if KlasaDokladnosci<=8:
                if KlasaDokladnosci==6 and Nominalny>=250 and Nominalny<=315:
                    ES = -9
                else:
                    ES = eval(OtworyM_doIT8_i_powyzej_ES[o][0])
            else:
                ES = OtworyM_doIT8_i_powyzej_ES[o][1]
        if  Litera == 'N':
            if KlasaDokladnosci<=8:
                ES = eval(OtworyNdoIT8iPowyzej_ES[o][0])
            else:
                ES = OtworyNdoIT8iPowyzej_ES[o][1]
        EI = ES - T       
    if Litera == "JS":
        EI = -T/2
        ES = T/2
    if Litera == "J":
        o = zokragl(OtworyAdoG_przedzialy,Nominalny)
        k = [6,7,8]
        ES = OtworyJ_IT6doIT8_ES[o][k.index(KlasaDokladnosci)]
        EI = ES - T
    if opis:
        print(f"EI={EI}")
        print(f"ES={ES}")
        print(f"A=N+EI={Nominalny+EI/1000}")
        print(f"B=N+ES={Nominalny+ES/1000}")
    if Dictionary:
        return {"EI":EI, "ES":ES, "A":Nominalny+EI/1000, "B":Nominalny+ES/1000}
    return (EI,ES,Nominalny+EI/1000,Nominalny+ES/1000)

def WalekPoprawnaTolerancja(Nominalny, Litera, KlasaDokladnosci):
    o =  zokragl(OtworyAdoG_przedzialy,Nominalny)
    if Litera in ['cd', 'ef', 'fg']:
        if o > 50:
            return False
    elif Litera == "j" and KlasaDokladnosci == 8 and Nominalny > 3:
        return False
    elif Litera == "t" and Nominalny <=24: 
        return False
    elif Litera == "v" and Nominalny <=14: 
        return False
    elif Litera == "y" and Nominalny <=18: 
        return False
    else:
        return True

def OdchylkiWalka(Nominalny, Litera, KlasaDokladnosci,opis=False, Dictionary=False):
    
    if not WalekPoprawnaTolerancja(Nominalny, Litera, KlasaDokladnosci):
        print("dla tolerancji {0}{1}{2} w normie PN-EN ISO 286-1: 2011P nie zdefiniowano odchyłek".format(Nominalny, Litera, KlasaDokladnosci))
        return         
    
    o =  zokragl(OtworyAdoG_przedzialy,Nominalny)
    T = Tolerancja[zokragl(przedzialy,Nominalny)][klasa.index("IT"+str(KlasaDokladnosci))]
    if Litera in Walek_es:
        if Litera == "h":
            es = 0
        elif Litera == "js":
            es = T/2
        else:
            es = walek_a_do_g_es[o][Walek_es.index(Litera)]
        ei = es - T
    if Litera in Walek_ei+['j','k']:
        if Litera == "j":
            if KlasaDokladnosci in [5,6]:
                ei = walek_j_ei[o][0]
            elif KlasaDokladnosci == 7:
                ei = walek_j_ei[o][1]
            elif KlasaDokladnosci == 8 and Nominalny <= 3:
                ei = walek_j_ei[o][2]
            else:
                ei = "-"
        elif Litera =="k":
            if KlasaDokladnosci in [4,5,6,7]:
                ei = walek_k_ei[o][0]
            else:
                ei = walek_k_ei[o][1]
        else:
            ei = walek_m_do_zc_ei[o][Walek_ei.index(Litera)]
        es = T+ei
    if opis:
        print(f"ei={ei}")
        print(f"es={es}")
        print(f"A=N+ei={Nominalny+ei/1000}")
        print(f"B=N+es={Nominalny+es/1000}")
    if Dictionary:
        return {"ei":ei, "es":es, "A":Nominalny+ei/1000, "B":Nominalny+es/1000}
    return (ei,es,Nominalny+ei/1000,Nominalny+es/1000)     

def podziel(tolerancja):
    wzor = re.compile(r'(\d{1,3})([A-Za-z]{1,2})(\d{1,2}).([A-Za-z]{1,2})(\d{1,2})|(\d*)([A-Za-z]{1,2})(\d{1,2})')
    x = []
    for i in re.split(wzor, tolerancja):
        if i:
            if i.isnumeric():
                x.append(eval(i))
            else:
                x.append(i)
    return tuple(x)

def luz(Nominalny, TolOtworu, KlasaOtworu, TolWalka, KlasaWalka,opis=False,Dictionary=False):
    otwor = OdchylkiOtworu(Nominalny, TolOtworu, KlasaOtworu)
    walek = OdchylkiWalka(Nominalny, TolWalka, KlasaWalka)
    #     print(otwor)
    #     print(walek)
    TolerancjaPasowania = walek[1]-walek[0]+otwor[1]-otwor[0]
    LuzMinimalny  = otwor[0] - walek[1]
    LuzMaksymalny = otwor[1] - walek[0]
    if opis:
        print(f"T={TolerancjaPasowania}")
        print(f"L_min={LuzMinimalny}")
        print(f"L_max={LuzMaksymalny}")
    if Dictionary:
        return {"T":TolerancjaPasowania, "L_min":LuzMinimalny, "L_max":LuzMaksymalny}    
    return (TolerancjaPasowania,LuzMinimalny, LuzMaksymalny)

def isotol(*t,opis=False,Dictionary=False):
    if len(t)==1:
        a=podziel(t[0])
    else:
        a=t
    if len(a)==3:
        if a[1][0].isupper():
            return OdchylkiOtworu(a[0],a[1].upper(),a[2],opis,Dictionary)
        else:
            return OdchylkiWalka(a[0],a[1],a[2],opis,Dictionary) 
    elif len(a)==5:
        return luz(a[0],a[1],a[2],a[3],a[4],opis,Dictionary)

if __name__=="__main__":
    print(OdchylkiWalka(25, 'p', 6))
    print(isotol("25p6"))
    print(isotol("25p6",Dictionary=True))
    print(isotol(25,"p",6))
    print(isotol("25H6"))
    print(isotol(25,"H",6))
    print(f'100Js9 ->{isotol("100Js9",Dictionary=True)}')
    print(f'100js9 ->{isotol("100js9",Dictionary=True)}')
    print(f'24s10 ->{isotol("24s10",Dictionary=True)}')
    print(isotol("100K6/d5",opis=True,Dictionary=True))
    print(isotol(100,"K",6,"d",5))
    print(f'29h7 {isotol("29h7",Dictionary=True)}')
    print(f'29h7 {isotol("29h7")}')
    print(f'29H7 {isotol("29H7",Dictionary=True)}')
    print(f'29H7/h8 {isotol("29H7/h8",Dictionary=True )}')
    