#!/usr/bin/python

import importlib

class Router:
    def myImport(name):
        package, module = name.split('.')
        mod = importlib.import_module('.'+module, package)
        #mod = getattr(mod, components[2:])
        return mod

    def go(theModule, theClass, theMethod):
        myModule = Router.myImport(theModule)
        myClass = getattr(myModule, theClass)
        return getattr(myClass(), theMethod)
        
