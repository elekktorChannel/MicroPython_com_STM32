import pyb

my_board_IO_pins = ["PA0","PA1","PA2","PA3","PA4","PA5","PA6","PA7","PA8","PA9","PA10",
                  "PA11","PA12","PA15","PB0","PB1","PB2","PB3","PB4",
                  "PB5","PB6","PB7","PB8","PB9","PB10","PB12","PB13","PB14","PB15",
                  "PC0","PC1","PC2","PC3","PC4","PC6","PC7","PC8","PC9","PC10","PC11",
                  "PC12","PC13","PC14","PC15","PD2","PH0","PH1"]

def main():
    for each_pin in my_board_IO_pins:
        print(f"AF de {each_pin} = {pyb.Pin(each_pin).af_list()}")

main()