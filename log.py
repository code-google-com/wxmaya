
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
    
import sys, m
    
def write(msg):
    logDefault.append(msg)
    if show:
        import sys
        sys.stderr.write('wxmaya log: %s\n' % msg )
    
def cat( stream=sys.stdout ):
    print >>stream, '\n'.join(logDefault)
    
del sys