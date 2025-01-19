import pyb
import stm


def f_adc_init_start():
    # Habilita clock GPIOA
    stm.mem32[stm.RCC + stm.RCC_AHB1ENR] |= (1<<0)
    
    # Configura PA1 como analogica
    stm.mem32[stm.GPIOA + stm.GPIO_MODER] |=(3<<2)
    
    # Habilita clock ADC
    stm.mem32[stm.RCC + stm.RCC_APB2ENR] |= (1<<8)
    
    # Reseta sequencias e configura para somente uma única conversão
    stm.mem32[stm.ADC1 + stm.ADC_SQR1]  = 0x00000000
    stm.mem32[stm.ADC1 + stm.ADC_SQR2]  = 0x00000000
    stm.mem32[stm.ADC1 + stm.ADC_SQR3]  = 0x00000000
    stm.mem32[stm.ADC1 + stm.ADC_SQR3]  |= (1<<0)
    
    # Configura conversão em 480 cycles
    stm.mem32[stm.ADC1 + stm.ADC_SMPR2] |= (7<<3)
    
    # Habilita conversão continua ou não continua
    #stm.mem32[stm.ADC1 + stm.ADC_CR2]  |= (1<<1)
    stm.mem32[stm.ADC1 + stm.ADC_CR2]  &= ~(1<<1)
    
    # ADC = ON
    stm.mem32[stm.ADC1 + stm.ADC_CR2]  |= (1<<0)
    
    # Inicia a conversão
    stm.mem32[stm.ADC1 + stm.ADC_CR2]  |= (1<<30)


def main():
    
    f_adc_init_start()
    
    while True: 
        # Aguardar completar a conversão
        while(stm.mem32[stm.ADC1 + stm.ADC_SR] & (1<<1)) != (1<<1) :
            pass
    
        # Obtem o resultado da conversão
        sensor_value = stm.mem32[stm.ADC1 + stm.ADC_DR]
        print("Sensor value : ",str(sensor_value))
        # Inicia nova conversão
        stm.mem32[stm.ADC1 + stm.ADC_CR2]  |= (1<<30)
        # Atraso para não carregar demais buffer da função print
        for i in range(10000):
            pass
        

main()
        
    
    
    
    


    
    







