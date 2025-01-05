import pyb
import stm
import machine

def f_signed_to_unsined_32(v_num):
    if v_num < 0:
        return (v_num + 2**32)
    else:
        return v_num

def main():
    print()
    print("Ola mundo!")
    print()
    print("*** ENDEREÇOS PERIFERICOS ***")
    print("AHB1")
    print(f'@GPIOA  = {hex(stm.GPIOA)}')
    print(f'@GPIOB  = {hex(stm.GPIOB)}')
    print(f'@RCC    = {hex(stm.RCC)}')
    print()
    print("*** OFFSET GPIO_MODER ***")
    print(f'Offset @GPIO_MODER     = {hex(stm.GPIO_MODER)}')
    print()
    print("*** OFFSET RCC_AHB1ENR ***")
    print(f'Offset @RCC_AHB1ENR    = {hex(stm.RCC_AHB1ENR)}')
    print()
    print("*** CONTEUDOS ***")
    print(f'GPIOA_MODER = {bin(f_signed_to_unsined_32(stm.mem32[stm.GPIOA + stm.GPIO_MODER]))}')
    print(f'GPIOA_MODER = {hex(f_signed_to_unsined_32(stm.mem32[stm.GPIOA + stm.GPIO_MODER]))}')
    print()
    print(f'GPIOB_MODER = {bin(f_signed_to_unsined_32(stm.mem32[stm.GPIOB + stm.GPIO_MODER]))}')
    print(f'GPIOB_MODER = {hex(f_signed_to_unsined_32(stm.mem32[stm.GPIOB + stm.GPIO_MODER]))}')
    print()
    print(f'RCC_AHB1ENR = {bin(f_signed_to_unsined_32(stm.mem32[stm.RCC + stm.RCC_AHB1ENR]))}')
    print(f'RCC_AHB1ENR = {hex(f_signed_to_unsined_32(stm.mem32[stm.RCC + stm.RCC_AHB1ENR]))}')
   

main()