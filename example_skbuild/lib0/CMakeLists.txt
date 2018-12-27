
add_library(lib0 STATIC lib0.cpp)
#install(TARGETS lib0 LIBRARY DESTINATION lib0)
set_target_properties(lib0 PROPERTIES
  INTERFACE_INCLUDE_DIRECTORIES "${CMAKE_SOURCE_DIR}/lib0"
)
