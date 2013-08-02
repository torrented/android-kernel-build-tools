#! /usr/bin/python

# This will generate the 'Kerneltools-build-config' needed by the Builder

import fileinput
import sys
import os

# Getting Device Spec's

def devicespec():
  a = raw_input('\nCROSS_COMPILE=~/')
  b = raw_input('LOCAL_BUILD_DIR=~/')
  c = raw_input('TARGET_DIR=~/')
  d = raw_input('SYSTEM_PARTITION=/dev/block/mmcblk0p')
  e = raw_input('DEFCONFIG=')
  f = raw_input('N_CORES=')
  g = raw_input('VERSION=')
# Print Device Spec's

  print '\n=====================================\n'
  print 'CROSS_COMPILE=~/' + a
  print 'HOST_CC=gcc'
  print 'LOCAL_BUILD_DIR=~/' + b 
  print 'TARGET_DIR=~/' + c
  print 'SYSTEM_PARTITION=\"/dev/block/mmcblk0p' + d + '\"'
  print 'DEFCONFIG=' + e
  print "\nFLASH_BOOT='write_raw_image(\"/tmp/boot.img\", \"boot\")'"
  print '\n# ----\n'
  print 'N_CORES=' + f
  print 'VERSION=' + g
  print '\n# ----\n\n'
  print'BANNER=`cat <<EOF'
  print'ui_print("**********************************************");'
  print'ui_print("*                                            *");'
  print'ui_print("  VERSION: ' + g + '                     ");'
  print'ui_print("*                                            *");'
  print'ui_print("**********************************************");'
  print'EOF`'
  print '\n=====================================\n'

# Generate kerneltools-build-config
  
  answer1 = raw_input('\nDoes this Look Correct? y or n? ')

  if answer1 == 'n':
    main()
  else:

    print '\nDefault filename: kerneltools-build-config'
   
    answer2 = raw_input('\nUse default name? y or n? ')

    if answer2 == 'n':
       nf = raw_input('\nSet File name to: ')
    else:
       print '\nSaving FILE as: kerneltools-build-config'
       nf = 'kerneltools-build-config'
  
    outfile = open(nf, 'w')
    outfile.write('CROSS_COMPILE=~/' + a)
    outfile.write('\nHOST_CC=gcc')
    outfile.write('\nLOCAL_BUILD_DIR=~/' + b)
    outfile.write('\nTARGET_DIR=~/' + c)
    outfile.write('\nSYSTEM_PARTITION=\"/dev/block/mmcblk0p' + d + '\"')
    outfile.write('\nDEFCONFIG=' + e)
    outfile.write("\n\nFLASH_BOOT='write_raw_image(\"/tmp/boot.img\", \"boot\")'")
    outfile.write('\n\n# ----')
    outfile.write('\n\nN_CORES=' + f)
    outfile.write('\nVERSION=' + g)
    outfile.write('\n\n# ----\n\n')
    outfile.write('BANNER=`cat <<EOF\n')
    outfile.write('ui_print("**********************************************");\n')
    outfile.write('ui_print("*                                            *");\n')
    outfile.write('ui_print("  VERSION: ' + g + '                     ");\n')
    outfile.write('ui_print("*                                            *");\n')
    outfile.write('ui_print("**********************************************");\n')
    outfile.write('EOF`')
    outfile.close()
    sys.exit

    x = os.path.dirname(os.path.realpath(__file__)) + '/' + nf
    print '\nSaving FILE to: ' + x + '\n'

def main():
  devicespec()
  print 'REMEMBER TO MOVE THIS FILE TO THE TOP DIR OF YOUR KERNEL SOURCE!\n'

if __name__ == '__main__':
  main()
