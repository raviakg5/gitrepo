import collections
import numpy as np
import pandas as pd

class LoggerHelper():
    def __init__(self,mesg,*args):
        self.mesg = mesg
        self.__args = args
        self.st = None
    def __mystr(self,var):
        if isinstance(var,str):
            return("\""+var+"\"")
        if isinstance(var,type):
            t = str(var)
            return("\""+t+"\"")
        if isinstance(var,(pd.DataFrame,pd.Series,pd.Index,np.ndarray)):
            self.st = var.copy()
            return('self.st')
        if isinstance(var,(collections.abc.keysView,Exception)):
            return("\""+str(var)+"\"")

        return(str(var))
    def __str__(self):
        try:
            exec("""self.q=self.mesg.format({})""".format(','.join((self.__mystr(w) for w in self.__args))))
            return(self.q)
        except Exception as e:
            return ""



