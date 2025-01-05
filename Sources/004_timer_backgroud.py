import pyb

def f_background(timer):
    my_OUT_tim.value(not my_OUT_tim.value())

def main():
    global my_OUT_tim
    my_user_LED = pyb.Pin('PA5', mode =pyb.Pin.OUT_PP)
    my_OUT_tim = pyb.Pin('PA6', mode =pyb.Pin.OUT_PP)
    my_tim =  pyb.Timer(2, freq = float(1/0.150))
    my_tim.callback(f_background)

    while True:
        my_user_LED.value(not my_user_LED.value())
        pyb.delay(300)

main()