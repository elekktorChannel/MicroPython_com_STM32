import pyb
import stm

def f_signed_to_unsined_32(v_num):
    if v_num < 0:
        return (v_num + 2**32)
    else:
        return v_num

def main():
    print()
    print("APB1")
    print(f'@TIM2   = {hex(stm.TIM2)}')
    print(f'@TIM3   = {hex(stm.TIM3)}')
    print(f'@TIM4   = {hex(stm.TIM4)}')
    print(f'@RTC    = {hex(stm.RTC)}')
    print(f'@WWDG   = {hex(stm.WWDG)}')
    print(f'@IWDG   = {hex(stm.IWDG)}')
    print(f'@USART2 = {hex(stm.USART2)}')
    print(f'@I2C1   = {hex(stm.I2C1)}')
    print(f'@I2C2   = {hex(stm.I2C2)}')
    print(f'@I2C3   = {hex(stm.I2C3)}')
    print(f'@PWR    = {hex(stm.PWR)}')
    print()
    print("APB2")
    print(f'@TIM1   = {hex(stm.TIM1)}')
    print(f'@USART1 = {hex(stm.USART1)}')
    print(f'@USART6 = {hex(stm.USART6)}')
    print(f'@ADC1   = {hex(stm.ADC1)}')
    print(f'@SDIO   = {hex(stm.SDIO)}')
    print(f'@SPI1   = {hex(stm.SPI1)}')
    print(f'@SPI4   = {hex(stm.SPI4)}')
    print(f'@SYSCFG = {hex(stm.SYSCFG)}')
    print(f'@EXTI   = {hex(stm.EXTI)}')
    print(f'@TIM9   = {hex(stm.TIM9)}')
    print(f'@TIM10  = {hex(stm.TIM10)}')
    print(f'@TIM11  = {hex(stm.TIM11)}')
    print(f'@SPI5   = {hex(stm.SPI5)}')
    print()
    print("AHB1")
    print(f'@GPIOA  = {hex(stm.GPIOA)}')
    print(f'@GPIOB  = {hex(stm.GPIOB)}')
    print(f'@GPIOC  = {hex(stm.GPIOC)}')
    print(f'@GPIOD  = {hex(stm.GPIOD)}')
    print(f'@GPIOH  = {hex(stm.GPIOH)}')
    print(f'@RCC    = {hex(stm.RCC)}')
    print(f'@FLASH  = {hex(stm.FLASH)}')
    print(f'@DMA1   = {hex(stm.DMA1)}')
    print(f'@DMA2   = {hex(stm.DMA2)}')
    print()
    print("AHB2")
    print(f'@USB_OTG_FS  = {hex(stm.USB_OTG_FS)}')
    print()
    print(f'Offset @GPIO_MODER   = {hex(stm.GPIO_MODER)}')
    print(f'Offset @GPIO_OTYPER  = {hex(stm.GPIO_OTYPER)}')
    print(f'Offset @GPIO_OSPEEDR = {hex(stm.GPIO_OSPEEDR)}')
    print(f'Offset @GPIO_PUPDR   = {hex(stm.GPIO_PUPDR)}')
    print(f'Offset @GPIO_IDR     = {hex(stm.GPIO_IDR)}')
    print(f'Offset @GPIO_ODR     = {hex(stm.GPIO_ODR)}')
    print(f'Offset @GPIO_LCKR    = {hex(stm.GPIO_LCKR)}')
    print()
    print(f'Offset @RCC_CR         = {hex(stm.RCC_CR)}')
    print(f'Offset @RCC_PLLCFGR)   = {hex(stm.RCC_PLLCFGR)}')
    print(f'Offset @RCC_CFGR       = {hex(stm.RCC_CFGR)}')
    print(f'Offset @RCC_CIR        = {hex(stm.RCC_CIR)}')
    print(f'Offset @RCC_AHB1RSTR   = {hex(stm.RCC_AHB1RSTR)}')
    print(f'Offset @RCC_AHB2RSTR   = {hex(stm.RCC_AHB2RSTR)}')
    print(f'Offset @RCC_APB1RSTR   = {hex(stm.RCC_APB1RSTR)}')
    print(f'Offset @RCC_APB2RSTR   = {hex(stm.RCC_APB2RSTR)}')
    print(f'Offset @RCC_AHB1ENR    = {hex(stm.RCC_AHB1ENR)}')
    print(f'Offset @RCC_AHB2ENR    = {hex(stm.RCC_AHB2ENR)}')
    print(f'Offset @RCC_APB1ENR    = {hex(stm.RCC_APB1ENR)}')
    print(f'Offset @RCC_APB2ENR    = {hex(stm.RCC_APB2ENR)}')
    print(f'Offset @RCC_AHB1LPENR  = {hex(stm.RCC_AHB1LPENR)}')
    print(f'Offset @RCC_AHB2LPENR  = {hex(stm.RCC_AHB2LPENR)}')
    print(f'Offset @RCC_APB1LPENR  = {hex(stm.RCC_APB1LPENR)}')
    print(f'Offset @RCC_APB2LPENR  = {hex(stm.RCC_APB2LPENR)}')
    print(f'Offset @RCC_BDCR       = {hex(stm.RCC_BDCR)}')
    print(f'Offset @RCC_CSR        = {hex(stm.RCC_CSR)}')
    print(f'Offset @RCC_SSCGR      = {hex(stm.RCC_SSCGR)}')
    print(f'Offset @RCC_PLLI2SCFGR = {hex(stm.RCC_PLLI2SCFGR)}')
    print(f'Offset @RCC_DCKCFGR    = {hex(stm.RCC_DCKCFGR)}')
    print()    
    print(f'GPIOA_MODER = {bin(f_signed_to_unsined_32(stm.mem32[stm.GPIOA + stm.GPIO_MODER]))}')
    print(f'GPIOA_MODER = {hex(f_signed_to_unsined_32(stm.mem32[stm.GPIOA + stm.GPIO_MODER]))}')
    print(f'GPIOB_MODER = {bin(f_signed_to_unsined_32(stm.mem32[stm.GPIOB + stm.GPIO_MODER]))}')
    print(f'GPIOB_MODER = {hex(f_signed_to_unsined_32(stm.mem32[stm.GPIOB + stm.GPIO_MODER]))}')
    print(f'RCC_AHB1ENR = {bin(f_signed_to_unsined_32(stm.mem32[stm.RCC + stm.RCC_AHB1ENR]))}')
    print(f'RCC_AHB1ENR = {hex(f_signed_to_unsined_32(stm.mem32[stm.RCC + stm.RCC_AHB1ENR]))}')
    

main()    