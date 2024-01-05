#!usr/bin/python
# -*- coding: latin-1 -*-
# Filename: MircoModel2003.py


import numpy as np
#~ from Equation.py import Equation

# -------------------------
class Equation(object):
    def __init__(self, name = None):

        self.Id = None
        self.parentId = None
        self.parent = None

        self.dict_UIkeys = []   # a llenarse con las claves de los parámetros modificables en pantalla.

        self.dict_setters = dict(name = self.set_name,
                parentId = self.set_parentId,
                type = self.set_type)

        self.dict_getters = dict(name = self.get_name,
                parentId = self.get_parentId,
                type = self.get_type)

        return None


    # ----- setters y getters.
    def set_Id(self, Id):           # este método se utiliza al deshidratar y rehidratar los objetos.
        self.Id = Id
        return None

    def get_Id(self):               # este método se utiliza al deshidratar y rehidratar los objetos.
        return self.Id


    def set_name(self, name):           # este método se utiliza durante el uso normal del objeto.
        self.name = name
        return None

    def get_name(self):                 # este método se utiliza durante el uso normal del objeto.
        return self.name


    def set_parent(self, parent):       # este método se utiliza durante el uso normal del objeto.
        self.parent = parent
        return None

    def get_parent(self):               # este método se utiliza durante el uso normal del objeto.
        return self.parent


    def set_parentId(self, parentId):# este método se utiliza al deshidratar y rehidratar los objetos.
        self.parentId = parentId
        return None

    def get_parentId(self):          # este método se utiliza al deshidratar y rehidratar los objetos.
        return self.parentId
        
        
    def set_type(self, type):
        # no se setea, es un método dummy
        return None
        
    def get_type(self):                 # este método se utiliza al deshidratar los objetos y sirve como clave para rehidratarlos.
        return str(type(self)).strip()


    def set_debug(self, debug):
        self.debug = debug
        return None

    def get_debug(self):
        return self.debug


    # ----- interfaces.
    def get_dict_setters(self):
        pass

    def get_dict_getters(self):
        pass

    def get_dict_UIkeys(self):
        pass

    def get_UILabels(self):
        pass

    def set_indepVar(self, value):
        pass

    def get_indepVar(self):
        pass

    def eval(self, indepVar=None):
        pass

    def is_equation(self):
        return True

    # ----- fin interfaces.


    def get_data_as_dict(self):

        self.dic = dict()
        print '   en get_data_as_dict() del objeto:  ',self.get_name()

        getters = self.get_dict_getters()

        for clave in getters.keys():       # devuelve las claves o valores de los atributos en una lista.

            attrib = getters[clave]()       # devuelve el valor (u objeto) del getter.

            print '   En elemento:',self.get_name(),'.   atributo:',attrib, 'tipo :',type(attrib)

            if type(attrib) == type([1,2]):     #~ print 'es lista'
                print '                     .... el atributo es lista. Iterando elementos...'
                lista = []
                for item in attrib:

                    print '             en clase base Element, item de attrib:',item
                    try:
                        print '                                             intentando pedir data_as_dict del objeto.'
                        obj = item.get_data_as_dict()
                        lista.append(obj)

                    except:
                        print '                                             no dio data as dict, haciendo append del objeto.'
                        lista.append(item)

                self.dic[clave] = lista

            else:
                print '                     .... el atributo no es lista. Pidiendo data_as_dict'
                try:
                    obj = attrib.get_data_as_dict()
                    self.dic[clave] = obj
                    print '              self.dic[clave] = obj:  self.dic[',clave,']=',obj

                except:
                    self.dic[clave] = attrib

        return self.dic

# -------------------------
#
#
#
#
# -------------------------

# ================================= Model.
class Model(Equation):

    def __init__(self, aesmm = [0.02], C = 6.0e-10, m=2.2, kt=1., Yu=0.65, Y=1.12, dmm = 0.02, D=0.0, rho=0.0, DKthR=10.1, deltaSigmaR = 375., deltaSigmaN = 650., DKths = 2.0, eqType = 'Zheng', crackType = 'Long', name=None,parent = None):

        Equation.__init__(self, name = name)

        # ------------------- Diccionarios.
        self.dict_setters.update(dict(aesmm = self.set_aesmm,
                C = self.set_C,
                m = self.set_m,
                kt = self.set_kt,
                Yu = self.set_Yu,
                Y = self.set_Y,
                dmm = self.set_dmm,
                D = self.set_D,
                rho = self.set_rho,
                DKthR = self.set_DKthR,
                deltaSigmaR = self.set_deltaSigmaR,
                deltaSigmaN = self.set_deltaSigmaN,
                DKths = self.set_DKths,
                eqType = self.set_eqType,
                crackType = self.set_crackType,
                name = self.set_name,
                parentId = self.set_parentId))

        self.dict_getters.update(dict(aesmm = self.get_aesmm,
                C = self.get_C,
                m = self.get_m,
                kt = self.get_kt,
                Yu = self.get_Yu,
                Y = self.get_Y,
                dmm = self.get_dmm,
                D = self.get_D,
                rho = self.get_rho,
                DKthR = self.get_DKthR,
                deltaSigmaR = self.get_deltaSigmaR,
                deltaSigmaN = self.get_deltaSigmaN,
                DKths = self.get_DKths,
                eqType = self.get_eqType,
                crackType = self.get_crackType,
                name = self.get_name,
                parentId = self.get_parentId))
                
        self.model_name = "Chapetti2003"

        self.name = name
        self.aesmm = aesmm
        self.C = C
        self.m = m
        self.kt = kt
        self.Yu = Yu
        self.Y = Y
        self.dmm  = dmm
        self.D = D
        self.rho = rho
        self.DKthR = DKthR
        self.deltaSigmaR  = deltaSigmaR
        self.deltaSigmaN  = deltaSigmaN
        self.DKths  = DKths
        self.eqType  = eqType
        self.crackType  = crackType
        self.debug = True
        self.parent = parent

        self.dict_UIkeys = ['aesmm','C','m','kt','Yu','Y','rho','D','dmm','DKthR','deltaSigmaN','deltaSigmaR','DKths','eqType','crackType']
        self.dict_UIlabels = dict( aesmm = "Long. de fisura, a [mm]" ,
                                C = "C [ciclos/m]",
                                m = "m (adim)", 
                                kt = "kt",
                                Yu = "Coef 'Y' en el umbral de fisuras cortas",
                                Y = "Coeficiente de forma, 'Y'",
                                rho = "Rho [mm] ",
                                D = "D [mm]",
                                dmm = "d [mm]",
                                DKthR = "DKth long cracks",
                                DKths = "DKth short cracks",
                                deltaSigmaN = "Delta Sn aplicado",
                                deltaSigmaR = "Tensión límite fatiga plana",
                                eqType = "Tipo de ecuación [Zheng | Lukaś]",
                                crackType = "[Short | Long]")

        #~ self.dict_UIlabels = dict()
        #~ for item in self.get_dict_UIkeys():
            #~ self.dict_UIlabels.update(dict({item:item}))

        return None

    # --------------------------------------------- Setters and getters
    def get_dict_getters(self):
        return self.dict_getters

    def get_dict_setters(self):
        return self.dict_setters


    def get_dict_UIkeys(self):
        return self.dict_UIkeys

    def get_dict_UIlabels(self):
        return self.dict_UIlabels


    def get_UILabels(self):
        orden = self.get_dict_UIkeys()
        labelsTxt = []
        labels = self.get_dict_UIlabels()
        for item in orden:
             labelsTxt.append(labels[item])
        return labelsTxt


    def get_attributes(self):
        return self.get_dict_setters().keys()

    def set_attribute(self, attribute, newValue):
        changed = False
        try:
            oldValue = self.get_dict_getters()[attribute]
            if oldValue != newValue:    changed = True
            self.get_dict_setters()[attribute] = newValue
            self.get_parent().update(self.get_name())
            return True
        except:
            return False


    def set_aesmm(self, aesmm):
        self.aesmm = aesmm
        return None

    def get_aesmm(self):
        return self.aesmm


    # variable independiente.
    def set_indepVar(self, value):
        self.set_aesmm(value)
        return None

    def get_indepVar(self):
        return self.get_aesmm()



    def set_C(self, C):
        self.C = C
        return None

    def get_C(self):
        return self.C


    def set_m(self, m):
        self.m = m
        return None

    def get_m(self):
        return self.m


    def set_kt(self, kt):
        self.kt = kt
        return None

    def get_kt(self):
        return self.kt


    def set_Yu(self, Yu):
        self.Yu = Yu
        return None

    def get_Yu(self):
        return self.Yu


    def set_Y(self, Y):
        self.Y = Y
        return None

    def get_Y(self):
        return self.Y


    def set_dmm(self, dmm):
        self.dmm = dmm
        return None

    def get_dmm(self):
        return self.dmm


    def set_D(self, D):
        self.D = D
        return None

    def get_D(self):
        return self.D


    def set_rho(self, rho):
        self.rho = rho
        return None

    def get_rho(self):
        return self.rho


    def set_DKthR(self, DKthR):
        self.DKthR = DKthR
        return None

    def get_DKthR(self):
        return self.DKthR


    def set_deltaSigmaR(self, deltaSigmaR):
        self.deltaSigmaR = deltaSigmaR
        return None

    def get_deltaSigmaR(self):
        return self.deltaSigmaR


    def set_deltaSigmaN(self, deltaSigmaN):
        self.deltaSigmaN = deltaSigmaN
        return None

    def get_deltaSigmaN(self):
        return self.deltaSigmaN


    def set_DKths(self, DKths):
        self.DKths = DKths
        return None

    def get_DKths(self):
        return self.DKths


    def set_eqType(self, eqType):
        self.eqType = eqType
        return None

    def get_eqType(self):
        return self.eqType


    def set_crackType(self, crackType):
        self.crackType = crackType
        return None

    def get_crackType(self):
        return self.crackType


    def set_model_name(self, model_name):
        self.model_name = model_name
        return None

    def get_model_name(self):
        return self.model_name


    # --------------------------------------------- Methods

    def is_equation(self):
        return True


    def DK(self, aes, kt, Y, Dsigman, d, D=0.0, rho=0.0, f=2.0):

        DKap = []
        DKSN = []
        DKBN = []

        if rho == 0:

            DKap, DKSN, DKBN = self.DKsharp(aes, kt, Y, Dsigman, d, D, rho, f)
            if self.get_debug(): print 'Usando DK para fisuras agudas, DKap[0]=',DKap[0]

        else:

            for a in aes:

                DKBNi = Y * Dsigman * kt / np.sqrt(1 + 4.5 * a/rho) * np.sqrt(np.pi * 0.001 * a)
                DKSNi = Y * Dsigman * np.sqrt(np.pi * 0.001 * (a+D))

                g = f / np.sqrt(D*rho*0.001**2)

                # Modelo posterior a 2003, con transición a fisuras largas.
                #~ DKap.append(DKBNi + (DKSNi - DKBNi)*(1-np.e**(-g*(a-d)*0.001)))
                
                # Modelo paper Chapetti-2003.
                DKap.append(DKBNi) # + (DKSNi - DKBNi)*(1-np.e**(-g*(a-d)*0.001)))
                
                DKSN.append(DKSNi)
                DKBN.append(DKBNi)

            if self.get_debug(): print 'Usando DK para blunted notches, DKap=',DKap

        return DKap, DKSN, DKBN


    def DKsharp(self, aesmm, kt, Y, Dsigman, d=0.001, D=0.0, rho=0.0, f=2.):

        DKap = []
        DKSN = []
        DKBN = []

        for a in aesmm:
            DKap.append(Y * Dsigman * np.sqrt(np.pi * a*0.001 ))
            DKSN.append(0.0)
            DKSN.append(0.0)

        return DKap, DKSN, DKBN


    def DKth(self, aesmm, Y, DsigmaeR, dmm, DKthR):

        DKthap = []

        for aimm in aesmm:

            dKdR = self.DKdR(DsigmaeR, dmm) #Y * DsigmaeR * np.sqrt(np.pi * dmm * 0.001)
            k = 0.25/(dmm*0.001) * (dKdR /(DKthR-dKdR))

            DKthap.append(dKdR + (DKthR - dKdR) * (1.- np.e ** (-k*(aimm-dmm)*0.001) ))

        # DKthap[0]=0.0
        return DKthap


    def DKdR(self, DsigmaeR, dmm):

        # d en mm
        # Y debe ser 0.65 porque es el puto umbral.
        return 0.65 * DsigmaeR * np.sqrt(np.pi * dmm * 0.001)


    def dadN_Chapetti(self, aesmm, C, m, kt, Yu, Y, dmm, D, rho, DKthR, deltaSigmaR, deltaSigmaN, DKths, eqType, crackType):

        # aesmm: vector (npgrid) de longitudes de fisura en milímetros.
        # C: constante de la ecuación de Zheng o de Lukáŝ
        # m: constante de la ecuación de Zheng o de Lukáŝ
        # kt: factor de intensidad de tensiones.
        # Yu: constante geométrica en el umbral de fisura (=0.65).
        # Y: constante geométrica para calcular el DK.
        # dmm: barrera microestructural, en mm.
        # D: profundidad de entalla, en mm.
        # rho: radio de entalla, en mm.
        # DKthrR: DK umbral de fatiga para fisuras largas.
        # DKths: DK umbral para fisuras cortas.
        # deltaSigmaR: límite de fatiga plano.
        # deltaSigmaN: valor de tensiones alternativas.
        # eqType: flag del tipo de ecuación para calcular dadN.  (='Zheng' o 'Lukas')
        # crackSize: tamaño de fisura, para usar un DKthR o DKths

        # Funciones llamadas:
        # DKth(aesmm, kt, Yu, deltaSigmaR, dmm, D, rho, DKthR)
        # DKsharp(aesmm, kt, Y, deltaSigmaR)

        if self.get_debug():
            print '------------------------------'
            print 'Llamada a dadN_Chapetti:'
            print
            print 'mínimo de longitud de fisura a0 =',aesmm[0],'mm.'
            print 'máximo de longitud de fisura af =',aesmm[-1],'mm.'
            print 'tipo de ecuación: ',eqType
            print 'cálculo para fisuras:',crackType
            print 'factor C=',C
            print 'exponente m=',m
            print 'kt =',kt
            print 'd=',dmm,'mm.'
            print 'profundidad de la entalla (si hay) D=',D,'mm.'
            print 'radio de la entalla (si hay) rho=',rho,'mm.'
            print 'DsigmaR=',deltaSigmaR,'MPa.'
            print 'Dsigma aplicado=',deltaSigmaN,'MPa.'
            print 'umbral de fisuras largas DKthR=',DKthR,'MPa·m^0.5'
            print 'umbral de fisuras cortas DKths=',DKths,'MPa·m^0.5'
            print 'factor Y=',Y
            print 'factor Y umbral=',Yu
            print '------------------------------'


        try:
            aes = aesmm*0.001    # vector de longitudes de fisura en metros.
        except:
            aes = []
            for item in aesmm:
                aes.append(item*0.001)

        deltaK = []

        dadNsC = []     # acá van las da/dN de salida que no son NaN.
        deltasK = []    # acá van las de salida, que no dan NaN en da/dN.


        if (crackType != 'Long'):
            # short cracks y DKthR es

            dkth = self.DKth(aesmm, Yu, deltaSigmaR, dmm, DKthR)
            #~ dkth = self.DKth(aesmm, Yu, deltaSigmaR, dmm, DKths)

        #~ deltaK, dummy0, dummy1 = self.DKsharp(aesmm, kt, Y, deltaSigmaN) #, dmm, D, rho, f)
        deltaK, dummy0, dummy1 = self.DK(aesmm, kt, Y, deltaSigmaN, dmm, D, rho) #, f)

        for I in range(0,len(deltaK)):

            # modelo Chapetti "puro"
            if eqType == 'Zheng':
                if crackType == 'Long' or crackType == 'long':

                    #~ print 'Zheng, long crack.'
                    #~ dadNsC.append(C*(deltaK[I]-DKthR)**m)  #  Zheng y Hirst para fisuras largas, umbral fijo.
                    dadn =C*(deltaK[I]-DKthR)**m  #  Zheng y Hirst para fisuras largas, umbral fijo.
                else:
                    #~ print 'Zheng, short crack.'
                    #~ dadNsC.append(C*(deltaK[I]-dkth[I])**m) # Zheng y Hirst para fisuras largas, umbral variable.
                    dadn = C*(deltaK[I]-dkth[I])**m # Zheng y Hirst para fisuras largas, umbral variable.


            else:
                # Lukáŝ
                if crackType == 'Long' or crackType == 'long':
                    #~ print 'Lukáŝ, long crack.'
                    #~ dadNsC.append(C*(deltaK[I]**m-(DKthR)**m))  # Klesnil y Lukáŝ para fisuras largas, umbral fijo.
                    dadn = C*(deltaK[I]**m-(DKthR)**m)  # Klesnil y Lukáŝ para fisuras largas, umbral fijo.
                else:
                    #~ print 'Lukáŝ, short crack.'
                    #~ dadNsC.append(C*(deltaK[I]**m-(dkth[I])**m)) # Klesnil y Lukáŝ para fisuras largas, umbral variable.
                    dadn = C*(deltaK[I]**m-(dkth[I])**m) # Klesnil y Lukáŝ para fisuras largas, umbral variable.
            
            #~ if self.get_debug():    print '   evaluando ecuación:    DK=',deltaK[I],', da/dN=',dadn

            if not(np.isnan(dadn)) and not(np.isinf(dadn)):
                dadNsC.append(dadn)
                deltasK.append(deltaK[I])

        return deltasK, dadNsC


    def eval(self, indepVar=None):

        if indepVar == None:
            indepVar = self.get_indepVar()

        '''
        dadN_Chapetti(aesmm, C, m, kt, Yu, Y, dmm, D, rho, DKthR, deltaSigmaR, deltaSigmaN, DKths = 2.0, eqType = 'Zheng', crackType='Long'):

        # aesmm: vector (npgrid) de longitudes de fisura en milímetros.
        # C: constante de la ecuación de Zheng o de Lukáŝ
        # m: constante de la ecuación de Zheng o de Lukáŝ
        # kt: factor de intensidad de tensiones.
        # Yu: constante geométrica en el umbral de fisura (=0.65).
        # Y: constante geométrica para calcular el DK.
        # dmm: barrera microestructural, en mm.
        # D: profundidad de entalla, en mm.
        # rho: radio de entalla, en mm.
        # DKthrR: DK umbral de fatiga para fisuras largas.
        # deltaSigmaR: umbral de fatiga plana.
        # deltaSigmaN: valor de tensiones alternativas.
        # DKths: DK umbral para fisuras cortas.
        # eqType: flag del tipo de ecuación para calcular dadN.  (='Zheng' o 'Lukas')
        # crackSize: tamaño de fisura 'Long' o 'Short', para usar un DKthR o DKths

        # Funciones llamadas:
        # DKth(aesmm, kt, Yu, deltaSigmaR, dmm, D, rho, DKthR)
        # DKsharp(aesmm, kt, Y, deltaSigmaR)

        '''

        deltaK, dadN  = self.dadN_Chapetti(indepVar, self.get_C(), self.get_m(), self.get_kt(), self.get_Yu(), self.get_Y(), self.get_dmm(), self.get_D(), self.get_rho(),
                self.get_DKthR(), self.get_deltaSigmaR(), self.get_deltaSigmaN(), self.get_DKths(), self.get_eqType(), self.get_crackType())

        return deltaK, dadN



# -------------------------------------------------- fin class MircoModel.
#
