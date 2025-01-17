import pyb
import stm

def f_signed_to_unsined_32(v_num):
    if v_num < 0:
        return (v_num + 2**32)
    else:
        return v_num
    
def f_In_Pin (pPort, pPin, pType, pPUPD):
    # *********************************************
    # Configura um pino como saída
    # Cinco argumentos são obrigatórios
    # pPort: 'A' ou 'B' ou 'C'
    # pPin: nummero do pino
    # pType: 'PP' ou 'OD'
    # pPUPD: 'NPUNPD' ou 'PU' ou 'PD'
    # *********************************************
    l_Port = ['A','B','C']
    l_Pin = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    l_Type = ['PP','OD']
    l_PUPD = ['NPUNPD','PU','PD']
    
    if (pPort not in l_Port):
        print('Argumento pPort com problema...')
        return
    if (pPin not in l_Pin):
        print('Argumento pPin com problema...')
        return
    if (pType not in l_Type):
        print('Argumento pType com problema...')
        return
    if (pPUPD not in l_PUPD):
        print('Argumento pPUPD com problema...')
        return        
    
    if (pPort == 'A'):
        GPIOx = stm.GPIOA
    if (pPort == 'B'):
        GPIOx = stm.GPIOB
    if (pPort == 'C'):
        GPIOx = stm.GPIOC
        
    stm.mem32[GPIOx + stm.GPIO_MODER] &= (0xFFFFFFFF - (3 << 2*pPin))
    
    if (pType == 'PP'):
        stm.mem32[GPIOx + stm.GPIO_OTYPER] &= (0xFFFFFFFF - (1 << pPin))
    if (pType == 'OD'):
        stm.mem32[GPIOx + stm.GPIO_OTYPER] |= (1 << pPin)
        
    if (pPUPD == 'NPUNPD'):
        stm.mem32[GPIOx + stm.GPIO_PUPDR] &= (0xFFFFFFFF - (3 << 2*pPin))
    if (pPUPD == 'PU'):
        stm.mem32[GPIOx + stm.GPIO_PUPDR] &= (0xFFFFFFFF - (3 << 2*pPin))
        stm.mem32[GPIOx + stm.GPIO_PUPDR] |= (1 << 2*pPin)
    if (pPUPD == 'PD'):
        stm.mem32[GPIOx + stm.GPIO_PUPDR] &= (0xFFFFFFFF - (3 << 2*pPin))
        stm.mem32[GPIOx + stm.GPIO_PUPDR] |= (2 << 2*pPin)
            

def main():
    print()
    print(f'GPIOA_MODER = {bin(f_signed_to_unsined_32(stm.mem32[stm.GPIOA + stm.GPIO_MODER]))}')
    print(f'GPIOA_OTYPER = {bin(f_signed_to_unsined_32(stm.mem32[stm.GPIOA + stm.GPIO_OTYPER]))}')
    print(f'GPIOA_OSPEEDR = {bin(f_signed_to_unsined_32(stm.mem32[stm.GPIOA + stm.GPIO_OSPEEDR]))}')
    print(f'GPIOA_PUPDR = {bin(f_signed_to_unsined_32(stm.mem32[stm.GPIOA + stm.GPIO_PUPDR]))}')
    print()
    print(f'GPIOC_MODER = {bin(f_signed_to_unsined_32(stm.mem32[stm.GPIOC + stm.GPIO_MODER]))}')
    print(f'GPIOC_OTYPER = {bin(f_signed_to_unsined_32(stm.mem32[stm.GPIOC + stm.GPIO_OTYPER]))}')
    print(f'GPIOC_OSPEEDR = {bin(f_signed_to_unsined_32(stm.mem32[stm.GPIOC + stm.GPIO_OSPEEDR]))}')
    print(f'GPIOC_PUPDR = {bin(f_signed_to_unsined_32(stm.mem32[stm.GPIOC + stm.GPIO_PUPDR]))}')
    print()


main()
f_In_Pin('A',8,'OD','NPUNPD')
f_In_Pin('C',9,'PP','PU')
main()