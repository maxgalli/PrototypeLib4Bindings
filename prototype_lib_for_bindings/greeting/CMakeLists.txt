#file(COPY cpp/greeting/inc DESTINATION ${CMAKE_BINARY_DIR}/inc)

add_library(hello_lib SHARED GreetingCPP/src/Hello.cpp)

target_include_directories(hello_lib PUBLIC GreetingCPP/inc)

install(TARGETS hello_lib LIBRARY DESTINATION prototype_lib_4_bindings)

cppyy_add_bindings(
   "greeting_extension"
   LANGUAGE_STANDARD "17"
   SELECTION_XML  ${CMAKE_CURRENT_SOURCE_DIR}/selection.xml
   INTERFACE_FILE ${CMAKE_CURRENT_SOURCE_DIR}/GreetingCPP/inc/Hello.h
   HEADERS        ${CMAKE_CURRENT_SOURCE_DIR}/GreetingCPP/inc/Hello.h
   INCLUDE_DIRS   ${CMAKE_CURRENT_SOURCE_DIR}/GreetingCPP/inc
   LINK_LIBRARIES hello_lib
)
