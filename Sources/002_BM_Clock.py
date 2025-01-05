import pyb
import stm
import machine

def f_signed_to_unsined_32(v_num):
    if v_num < 0:
        return (v_num + 2**32)
    else:
        return v_num

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

main()