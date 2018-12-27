
add_library(_ext0 MODULE ext0.cpp)
python_extension_module(_ext0)
target_link_libraries(_ext0 lib0)

install(TARGETS _ext0 LIBRARY DESTINATION ext0)
