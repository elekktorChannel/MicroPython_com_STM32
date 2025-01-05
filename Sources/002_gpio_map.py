import pyb

my_board_IO_pins = ["PA0","PA1","PA2","PA3","PA4","PA5","PA6","PA7","PA8","PA9","PA10",
                  "PA11","PA12","PA15","PB0","PB1","PB2","PB3","PB4",
                  "PB5","PB6","PB7","PB8","PB9","PB10","PB12","PB13","PB14","PB15",
                  "PC0","PC1","PC2","PC3","PC4","PC5","PC6","PC7","PC8","PC9","PC10","PC11",
                  "PC12","PC13","PC14","PC15","PD2","PH0","PH1"]

my_modes = {0:"entrada",1:"saida",2:"AF",3:"analogica"}

def main():
    v_count = 0
    for v_pin in my_board_IO_pins:
        v_count = v_count + 1
        #print(f"Modo {v_pin} = {pyb.Pin(v_pin).mode()}")
        print(f"{v_count} - Configuração {v_pin} = {my_modes[pyb.Pin(v_pin).mode()]}")

main()