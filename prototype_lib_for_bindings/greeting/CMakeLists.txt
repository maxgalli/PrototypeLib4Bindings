#
# Headers and libraries are listed in a cmake file.
#
include(${CMAKE_CURRENT_SOURCE_DIR}/manifest.cmake)

#
# Set up hello shared lib
#
add_library(hello SHARED ${LIB_SOURCES})
set_target_properties(hello PROPERTIES PUBLIC_HEADER ${LIB_HEADERS})
target_include_directories(hello PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/GreetingCPP/inc)
install(TARGETS hello
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

cppyy_add_bindings(
   "greeting_extension"
   LANGUAGE_STANDARD "17"
   SELECTION_XML  ${CMAKE_CURRENT_SOURCE_DIR}/selection.xml
   INTERFACE_FILE ${CMAKE_CURRENT_SOURCE_DIR}/GreetingCPP/inc/Hello.h
   HEADERS        ${CMAKE_CURRENT_SOURCE_DIR}/GreetingCPP/inc/Hello.h
   INCLUDE_DIRS   ${CMAKE_CURRENT_SOURCE_DIR}/GreetingCPP/inc
   LINK_LIBRARIES hello
)
