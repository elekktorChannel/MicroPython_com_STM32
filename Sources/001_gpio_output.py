import pyb

def main():
    green_led = pyb.Pin('PA5', mode =pyb.Pin.OUT_PP)
    print(f"Lista de funções alternativas da porta {green_led.name()} = {green_led.af_list()}")
    print(f"A porta {green_led.name()} é identificada como Porta {green_led.port()}")

    while True:
        green_led.value(not green_led.value())          
        pyb.delay(100)

main()