import pyb

def main():
    i = 0
    timer2 = pyb.Timer(2, freq=1000)
    timer2_ch1 = timer2.channel(1, pyb.Timer.PWM, pin=pyb.Pin.board.PA5, pulse_width_percent=0)
    
    while True:
        i  = i + 1
        
        if i >= 100:
            i = 0
        
        timer2_ch1.pulse_width_percent(i)
        pyb.delay(5)
        
main()