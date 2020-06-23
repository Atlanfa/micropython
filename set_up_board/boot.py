# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import connect_wifi
import gc
import webrepl
connect_wifi.do_connect()
webrepl.start()
gc.collect()
