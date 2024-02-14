#arbitary arguments

def connect(*args,sep="/"):
 return sep.join(args)
connect("Earth","mars","venus",sep='.') 
