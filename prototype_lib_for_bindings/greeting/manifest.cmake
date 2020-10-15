set(_headers
    Hello.h
)

set(_sources
    Hello.cpp
)

foreach (path ${_headers})
    list(APPEND LIB_HEADERS ${CMAKE_CURRENT_SOURCE_DIR}/GreetingCPP/inc/${path})
endforeach(path)

foreach (path ${_sources})
    list(APPEND LIB_SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/GreetingCPP/src/${path})
endforeach(path)
