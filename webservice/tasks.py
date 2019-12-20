# -*- coding: utf-8 -*-
from cec.celery import app
import subprocess
from subprocess import call


@app.task
def servicio_interruptor(equis):
    process = subprocess.run(["sudo", "cec-ctl", "--playback", "-S", "-t0"])
    process
    if equis == 1 :
        process = subprocess.run(["sudo", "cec-ctl", "--image-view-on", "-t0"])
        process
    elif equis == 2:
        process = subprocess.run(["sudo", "cec-ctl", "--standby", "-t0"])
        process
    else :
        return ("Opción no reconocida")
    
    return "comando enviado a TV"

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
