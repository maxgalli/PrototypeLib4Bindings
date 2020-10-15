cmake_minimum_required(VERSION 3.16)

project(prototype_lib_for_bindings)

list(INSERT CMAKE_MODULE_PATH 0 ${CMAKE_SOURCE_DIR}/cmake)
find_package(Cppyy REQUIRED)

add_subdirectory(prototype_lib_for_bindings)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
