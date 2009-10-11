import sys

global logDefault
try:
    logDefault
except: 
    logDefault=[]
    
global logWarning
try:
    logWarning
except: 
    logWarning=[]
    
global logError
try:
    logError
except: 
    logError=[]
    
global show
try:
    show
except: 
    show=False
    
    
def write(msg):
    logDefault.append(msg)
    if show:
        print msg
    
def cat( stream=sys.stdout ):
    print >>stream, '\n'.logDefault
    
del sys