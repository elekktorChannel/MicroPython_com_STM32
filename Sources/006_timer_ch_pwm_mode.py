import pyb

def main():
    pyb.Pin("PC6", mode=pyb.Pin.OUT_PP)
    pyb.Pin("PC8", mode=pyb.Pin.OUT_PP)
    
    print(pyb.Pin("PC6").mode())
    print(pyb.Pin("PC8").mode())
    print(pyb.Pin("PC6").af_list())
    print(pyb.Pin("PC8").af_list())
    
    timer3 = pyb.Timer(3, freq=1000)
    timer3_ch1 = timer3.channel(1, pyb.Timer.PWM, pin=pyb.Pin.board.PC6, pulse_width_percent=50)
    timer3_ch2 = timer3.channel(3, pyb.Timer.PWM, pin=pyb.Pin.board.PC8, pulse_width_percent=75)
  
main()