import pyb
import stm
import machine

def f_signed_to_unsined_32(v_num):
    if v_num < 0:
        return (v_num + 2**32)
    else:
        return v_num

PWR_CR_VOS  = (stm.mem32[stm.PWR + stm.PWR_CR] >> 14) & 0b11

FLASH_ACR_LATENCY = (stm.mem32[stm.FLASH + stm.FLASH_ACR] >> 0) & 0b1111
FLASH_ACR_PRFTEN = (stm.mem32[stm.FLASH + stm.FLASH_ACR] >> 8) & 0b1
FLASH_ACR_ICEN = (stm.mem32[stm.FLASH + stm.FLASH_ACR] >> 9) & 0b1
FLASH_ACR_DCEN = (stm.mem32[stm.FLASH + stm.FLASH_ACR] >> 10) & 0b1

RCC_APB1ENR_PWR = (stm.mem32[stm.RCC + stm.RCC_APB1ENR] >> 28) & 0b1

RCC_CFGR_SW  = (stm.mem32[stm.RCC + stm.RCC_CFGR] >> 0) & 0b11
RCC_CFGR_SWS = (stm.mem32[stm.RCC + stm.RCC_CFGR] >> 2) & 0b11
RCC_CFGR_HPRE = (stm.mem32[stm.RCC + stm.RCC_CFGR] >> 4) & 0b1111
RCC_CFGR_PPRE1 = (stm.mem32[stm.RCC + stm.RCC_CFGR] >> 10) & 0b111
RCC_CFGR_PPRE2 = (stm.mem32[stm.RCC + stm.RCC_CFGR] >> 13) & 0b111

RCC_PLLCFGR_PLLM = (stm.mem32[stm.RCC + stm.RCC_PLLCFGR] >> 0) & 0b111111
RCC_PLLCFGR_PLLN = (stm.mem32[stm.RCC + stm.RCC_PLLCFGR] >> 6) & 0b111111111
RCC_PLLCFGR_PLLP = (stm.mem32[stm.RCC + stm.RCC_PLLCFGR] >> 16) & 0b11
RCC_PLLCFGR_PLLSRC = (stm.mem32[stm.RCC + stm.RCC_PLLCFGR] >> 22) & 0b1

if RCC_PLLCFGR_PLLP == 0:
    RCC_PLLCFGR_PLLP = 2
elif RCC_PLLCFGR_PLLP == 1:
    RCC_PLLCFGR_PLLP = 4
elif RCC_PLLCFGR_PLLP == 2:
    RCC_PLLCFGR_PLLP = 6
else:
    RCC_PLLCFGR_PLLP = 8

def main():
    print()
    print(machine.freq())
    print()
    print(f'RCC_CFGR_SW = {RCC_CFGR_SW}')
    print(f'RCC_CFGR_SWS = {RCC_CFGR_SWS}')
    print(f'RCC_CFGR_HPRE = {RCC_CFGR_HPRE}')
    print(f'RCC_CFGR_PPRE1 = {RCC_CFGR_PPRE1}')
    print(f'RCC_CFGR_PPRE2 = {RCC_CFGR_PPRE2}')
    print()
    print(f'RCC_PLLCFGR_PLLM = {RCC_PLLCFGR_PLLM}')
    print(f'RCC_PLLCFGR_PLLN = {RCC_PLLCFGR_PLLN}')
    print(f'RCC_PLLCFGR_PLLP = {RCC_PLLCFGR_PLLP}')
    print(f'RCC_PLLCFGR_PLLSRC = {RCC_PLLCFGR_PLLSRC}')
    print(f'Freq_Out_PLL = {8*(RCC_PLLCFGR_PLLN/RCC_PLLCFGR_PLLM)/RCC_PLLCFGR_PLLP} MHz')
    print()
    print(f'RCC_CFGR = {bin(f_signed_to_unsined_32(stm.mem32[stm.RCC + stm.RCC_CFGR]))}')
    print(f'RCC_CFGR = {hex(f_signed_to_unsined_32(stm.mem32[stm.RCC + stm.RCC_CFGR]))}')
    print(f'RCC_PLLCFGR = {bin(f_signed_to_unsined_32(stm.mem32[stm.RCC + stm.RCC_PLLCFGR]))}')
    print(f'RCC_PLLCFGR = {hex(f_signed_to_unsined_32(stm.mem32[stm.RCC + stm.RCC_PLLCFGR]))}')
    print()
    print(f'PWR_CR_VOS = {PWR_CR_VOS}')
    print()
    print(f'FLASH_ACR_LATENCY = {FLASH_ACR_LATENCY}')
    print(f'FLASH_ACR_PRFTEN = {FLASH_ACR_PRFTEN}')
    print(f'FLASH_ACR_ICEN = {FLASH_ACR_ICEN}')
    print(f'FLASH_ACR_DCEN = {FLASH_ACR_DCEN}')
    print()
    print(f'RCC_APB1ENR_PWR = {RCC_APB1ENR_PWR}')
    print()

main()