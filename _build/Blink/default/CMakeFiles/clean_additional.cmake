# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "")
  file(REMOVE_RECURSE
  "C:\\Users\\Cesar\\Documents\\PIC16F13145\\out\\Blink\\default.cmf"
  "C:\\Users\\Cesar\\Documents\\PIC16F13145\\out\\Blink\\default.hex"
  "C:\\Users\\Cesar\\Documents\\PIC16F13145\\out\\Blink\\default.hxl"
  "C:\\Users\\Cesar\\Documents\\PIC16F13145\\out\\Blink\\default.mum"
  "C:\\Users\\Cesar\\Documents\\PIC16F13145\\out\\Blink\\default.o"
  "C:\\Users\\Cesar\\Documents\\PIC16F13145\\out\\Blink\\default.sdb"
  "C:\\Users\\Cesar\\Documents\\PIC16F13145\\out\\Blink\\default.sym"
  )
endif()
