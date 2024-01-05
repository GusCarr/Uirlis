#!usr/bin/python
# -*- coding: latin-1 -*-

import numpy as np

class Model(object):

    def __init__(self, x  = [0.0], a0  =  0.0, a1  =  0.0, a2  =  0.0, a3  =  0.0, a4  =  0.0, a5  =  0.0, a6  =  0.0, texto  =  'Holi', parent = None, name = None):

        self.Id = None
        self.parentId = None
        self.parent = parent
        self.name = name                                # Name of the equation, can be changed.

        self.model_name = "InversePolinomial"

        # ------------------- Dictionaries.
        self.dict_setters = dict(x = self.set_x,
                a0 = self.set_a0,
                a1 = self.set_a1,
                a2 = self.set_a2,
                a3 = self.set_a3,
                a4 = self.set_a4,
                a5 = self.set_a5,
                a6 = self.set_a6,
                texto = self.set_texto)

        self.dict_getters = dict(x = self.get_x,
                a0 = self.get_a0,
                a1 = self.get_a1,
                a2 = self.get_a2,
                a3 = self.get_a3,
                a4 = self.get_a4,
                a5 = self.get_a5,
                a6 = self.get_a6,
                texto = self.get_texto)

        # ------------------- Attributes.
        self.x  = x 
        self.a0  = a0 
        self.a1  = a1 
        self.a2  = a2 
        self.a3  = a3 
        self.a4  = a4 
        self.a5  = a5 
        self.a6  = a6 
        self.texto  = texto 


        self.dict_setters.update(dict(name = self.set_name,
                parentId = self.set_parentId,
                type = self.set_type))

        self.dict_getters.update(dict(name = self.get_name,
                parentId = self.get_parentId,
                type = self.get_type))

        
        # UIkeys list.
        self.dict_UIkeys = ['x','a0','a1','a2','a3','a4','a5','a6','text']

        # UIlabels list.
        self.dict_UIlabels = dict(x  = "",
                a0  = " Constant.",
                a1  = " Coefficient for 1/x^1        ",
                a2  = " Coefficient for 1/x^2",
                a3  = " Coefficient for 1/x^3",
                a4  = " Coefficient for 1/x^4",
                a5  = " Coefficient for 1/x^5",
                a6  = " Coefficient for 1/x^6",
                texto  = "")

        return None

    # --------------------------------------------- Dictionaries getters and ATTRIBUTESs managing methods.
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


    def get_ATTRIBUTESs(self):
        return self.get_dict_setters().keys()

    def set_ATTRIBUTES(self, ATTRIBUTES, newValue):
        changed = False
        try:
            oldValue = self.get_dict_getters()[ATTRIBUTES]
            if oldValue != newValue:    changed = True
            self.get_dict_setters()[ATTRIBUTES] = newValue
            self.get_parent().update(self.get_name())
            return True
        except:
            return False

        
    # --------------------------------------------- Setters and getters
    def set_x(self, x):
        self.x = x
        return None

    def get_x(self):
        return self.x


    def set_a0(self, a0):
        self.a0 = a0
        return None

    def get_a0(self):
        return self.a0


    def set_a1(self, a1):
        self.a1 = a1
        return None

    def get_a1(self):
        return self.a1


    def set_a2(self, a2):
        self.a2 = a2
        return None

    def get_a2(self):
        return self.a2


    def set_a3(self, a3):
        self.a3 = a3
        return None

    def get_a3(self):
        return self.a3


    def set_a4(self, a4):
        self.a4 = a4
        return None

    def get_a4(self):
        return self.a4


    def set_a5(self, a5):
        self.a5 = a5
        return None

    def get_a5(self):
        return self.a5


    def set_a6(self, a6):
        self.a6 = a6
        return None

    def get_a6(self):
        return self.a6


    def set_texto(self, texto):
        self.texto = texto
        return None

    def get_texto(self):
        return self.texto


    # Independent variable.
    def set_indepVar(self, value):
        self.set_x = value
        return None

    def get_indepVar(self):
        return self.get_x()


    def set_model_name(self, model_name):
        self.model_name = model_name
        return None

    def get_model_name(self):
        return self.model_name

    # --------------------------------------------- Methods
    def is_equation(self):
        return True


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


    def get_data_as_dict(self):

        self.dic = dict()
        getters = self.get_dict_getters()
        for clave in getters.keys():        # devuelve las claves o valores de los atributos en una lista.
            attrib = getters[clave]()       # devuelve el valor (u objeto) del getter.
            if type(attrib) == type([1,2]):
                lista = []
                for item in attrib:
                    try:
                        obj = item.get_data_as_dict()
                        lista.append(obj)
                    except:
                        lista.append(item)
                self.dic[clave] = lista
            else:
                try:
                    obj = attrib.get_data_as_dict()
                    self.dic[clave] = obj
                except:
                    self.dic[clave] = attrib

        return self.dic        
        
        
    def eval(self, indepVar=None):

        if indepVar == None:
            indepVar = self.get_indepVar()
        
        x = self.get_x()
        a0 = self.get_a0()
        a1 = self.get_a1()
        a2 = self.get_a2()
        a3 = self.get_a3()
        a4 = self.get_a4()
        a5 = self.get_a5()
        a6 = self.get_a6()
        texto = self.get_texto()

        y_out = []
        x_out = []        

        for xi in x:
            
            try:
                y = a0 + a1/xi + a2/xi**2 + a3/xi**3 + a4/xi**4 + a5/xi**5 + a6/xi**6
                y_out.append(y)
                x_out.append(xi)
            except:
                pass

        return x_out, y_out


# --------------------------------
if __name__ == '__main__':
    modelo = Model()

    
