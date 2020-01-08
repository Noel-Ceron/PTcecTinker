# -*- coding: utf-8 -*-
from cec.celery import app
import subprocess
from subprocess import call


@app.task
def servicio_interruptor(equis):
    call(["sudo", "cec-ctl", "--playback", "-t0"])

    if equis == 1 :
        call(["sudo", "cec-ctl", "--image-view-on", "-t0"])

    elif equis == 2:
        call(["sudo", "cec-ctl", "--standby", "-t0"])

    else :
        return ("Opción no reconocida")
    
    return "comando enviado a TV"

@app.task
def servicio_interruptor_T(equis):
    
    if equis == 1 :
        print("Tinker encendida")
    elif equis == 2:
        call(["sudo","systemctl", "suspend"])
    else :
        return ("Opción no reconocida")
    
    return "comando enviado a Tinker"


@app.task
def servicio_volumen(equis):
    
    if equis == "25%" :
        call(["amixer","sset", "Master", "25%"])
    elif equis == "50%":
        call(["amixer","sset", "Master", "50%"])
    elif equis == "80%":
        call(["amixer","sset", "Master", "80%"])
    else :
        return ("Opción no reconocida")
    
    return "comando enviado a volumen"

@app.task
def servicio_mudo(equis):

    if equis == 0 :
        call(["amixer","sset", "Master", "unmute"])
    elif equis == 1:
        call(["amixer","sset", "Master", "mute"])
    else :
        return ("Opción no reconocida")
    
    return "comando enviado a Mute"
