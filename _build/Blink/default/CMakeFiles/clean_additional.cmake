# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "")
  file(REMOVE_RECURSE
  "E:\\Documents\\GitHub\\EC5801_21-10225\\out\\Blink\\default.cmf"
  "E:\\Documents\\GitHub\\EC5801_21-10225\\out\\Blink\\default.hex"
  "E:\\Documents\\GitHub\\EC5801_21-10225\\out\\Blink\\default.hxl"
  "E:\\Documents\\GitHub\\EC5801_21-10225\\out\\Blink\\default.mum"
  "E:\\Documents\\GitHub\\EC5801_21-10225\\out\\Blink\\default.o"
  "E:\\Documents\\GitHub\\EC5801_21-10225\\out\\Blink\\default.sdb"
  "E:\\Documents\\GitHub\\EC5801_21-10225\\out\\Blink\\default.sym"
  )
endif()
