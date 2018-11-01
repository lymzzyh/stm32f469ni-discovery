import os

# cpu options
ARCH            = 'arm'
CPU             = 'cortex-m4'
FPU             = 'fpv4-sp-d16'
ABI             = 'hard'

# toolchains options
CROSS_TOOL      = 'gcc' #iar keil
RTT_ROOT        = 'rt-thread'
GCC_PATH        = ''
IAR_PATH        = ''
MDK_PATH        = ''
ENABLE_ARMCLANG = True

# build options
BUILD = 'debug'
#BUILD = 'release'

if os.getenv('RTT_ROOT'):
    RTT_ROOT = os.getenv('RTT_ROOT')

if os.getenv('RTT_CC'):
    CROSS_TOOL = os.getenv('RTT_CC')

if  CROSS_TOOL  == 'gcc' :
    PLATFORM    = 'gcc'
    EXEC_PATH   = GCC_PATH
elif CROSS_TOOL == 'iar' :
    PLATFORM    = 'iar'
    EXEC_PATH   = IAR_PATH
elif CROSS_TOOL == 'keil' :
    if ENABLE_ARMCLANG :
        PLATFORM = 'armclang'
    else :
        PLATFORM = 'armcc'
    EXEC_PATH   = IAR_PATH
else :
    print('Please Set cross tool!')
    exit(0)


if PLATFORM == 'gcc':
    LinkScript  = 'project/gcc/link.ld'
    PREFIX = 'arm-none-eabi-'
    CC = PREFIX + 'gcc'
    CXX = PREFIX + 'g++'
    AS = PREFIX + 'gcc'
    AR = PREFIX + 'ar'
    LINK = PREFIX + 'gcc'
    TARGET_EXT = 'elf'
    SIZE = PREFIX + 'size'
    OBJDUMP = PREFIX + 'objdump'
    OBJCPY = PREFIX + 'objcopy'
	
    DEVICE  = ' -mcpu=' + CPU
    DEVICE += ' -mthumb -mfpu=' + FPU
    DEVICE += ' -mfloat-abi=' + ABI

    CFLAGS = DEVICE + '-ffunction-sections -fdata-sections -std=c99'

    AFLAGS = ' -c' + DEVICE + ' -x assembler-with-cpp -Wa,-mimplicit-it=thumb '

    LFLAGS = DEVICE + ' -Wl,--gc-sections,-Map=build/bin/rtthread.map,-cref,-u,Reset_Handler -T ' + LinkScript

    CPATH = ''
    LPATH = ''

    if BUILD == 'debug':
        CFLAGS += ' -O0 -gdwarf-2 -g'
        AFLAGS += ' -gdwarf-2'
    else:
        CFLAGS += ' -Os -Otime'

    CXXFLAGS = CFLAGS

    POST_ACTION = OBJCPY + ' -O binary $TARGET rtthread.bin\n' + SIZE + ' $TARGET \n'
    POST_ACTION = OBJCPY + ' -O ihex $TARGET rtthread.hex\n' + SIZE + ' $TARGET \n'
