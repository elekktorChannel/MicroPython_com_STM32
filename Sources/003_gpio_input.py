import pyb

my_modes = {0:"entrada",1:"saida",2:"AF",3:"analogica"}

def main():
    print(f"PA5 = {my_modes[pyb.Pin("PA5").mode()]}") 
    print(f"PC13 = {my_modes[pyb.Pin("PC13").mode()]}")         
    green_led_user = pyb.Pin('PA5', mode=pyb.Pin.OUT_PP)
    button_user =  pyb.Pin('PC13', mode=pyb.Pin.IN)

    while True:
        if button_user.value() == 0:
            green_led_user.value(1)
        else:
            green_led_user.value(0)
        
main()