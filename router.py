#!/usr/bin/python

from models.object import Object
import importlib

class Router(Object):
    def myImport(name):
        package, module = name.split('.')
        mod = importlib.import_module('.'+module, package)
        #mod = getattr(mod, components[2:])
        return mod

    def go(self, theModule, theClass, theMethod):
        myModule = Router.myImport(theModule)
        myClass = getattr(myModule, theClass)
        return getattr(myClass(), theMethod)
        
