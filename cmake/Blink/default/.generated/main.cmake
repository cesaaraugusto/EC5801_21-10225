include("${CMAKE_CURRENT_LIST_DIR}/rule.cmake")
include("${CMAKE_CURRENT_LIST_DIR}/file.cmake")

set(Blink_default_library_list )

# Handle files with suffix (s|as|asm|AS|ASM|As|aS|Asm), for group default-XC8
if(Blink_default_default_XC8_FILE_TYPE_assemble)
add_library(Blink_default_default_XC8_assemble OBJECT ${Blink_default_default_XC8_FILE_TYPE_assemble})
    Blink_default_default_XC8_assemble_rule(Blink_default_default_XC8_assemble)
    list(APPEND Blink_default_library_list "$<TARGET_OBJECTS:Blink_default_default_XC8_assemble>")

endif()

# Handle files with suffix S, for group default-XC8
if(Blink_default_default_XC8_FILE_TYPE_assemblePreprocess)
add_library(Blink_default_default_XC8_assemblePreprocess OBJECT ${Blink_default_default_XC8_FILE_TYPE_assemblePreprocess})
    Blink_default_default_XC8_assemblePreprocess_rule(Blink_default_default_XC8_assemblePreprocess)
    list(APPEND Blink_default_library_list "$<TARGET_OBJECTS:Blink_default_default_XC8_assemblePreprocess>")

endif()

# Handle files with suffix [cC], for group default-XC8
if(Blink_default_default_XC8_FILE_TYPE_compile)
add_library(Blink_default_default_XC8_compile OBJECT ${Blink_default_default_XC8_FILE_TYPE_compile})
    Blink_default_default_XC8_compile_rule(Blink_default_default_XC8_compile)
    list(APPEND Blink_default_library_list "$<TARGET_OBJECTS:Blink_default_default_XC8_compile>")

endif()


# Main target for this project
add_executable(Blink_default_image_qZd_yAR0 ${Blink_default_library_list})

set_target_properties(Blink_default_image_qZd_yAR0 PROPERTIES
    OUTPUT_NAME "default"
    SUFFIX ".elf"
    ADDITIONAL_CLEAN_FILES "${output_extensions}"
    RUNTIME_OUTPUT_DIRECTORY "${Blink_default_output_dir}")
target_link_libraries(Blink_default_image_qZd_yAR0 PRIVATE ${Blink_default_default_XC8_FILE_TYPE_link})

# Add the link options from the rule file.
Blink_default_link_rule( Blink_default_image_qZd_yAR0)


