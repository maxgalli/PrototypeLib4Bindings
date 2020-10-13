#file(COPY cpp/greeting/inc DESTINATION ${CMAKE_BINARY_DIR}/inc)

add_library(hello_lib SHARED extensions/src/Hello.cpp)

target_include_directories(hello_lib PUBLIC extensions/inc)

install(TARGETS hello_lib LIBRARY DESTINATION prototype_lib_4_bindings)
