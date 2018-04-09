import ptvsd

ptvsd.enable_attach("my_secret", address = ('0.0.0.0', 8887))

#Enable the below line of code only if you want the application to wait untill the debugger has attached to it
ptvsd.wait_for_attach()