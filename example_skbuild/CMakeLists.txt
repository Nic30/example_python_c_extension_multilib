cmake_minimum_required(VERSION 3.5.0)

project(python_c_extension_multilib)

find_package(PythonInterp REQUIRED)
find_package(PythonLibs REQUIRED)
find_package(PythonExtensions REQUIRED)

add_subdirectory(lib0)
add_subdirectory(ext0)

#file(WRITE "${CMAKE_BINARY_DIR}/python_c_extension_multilib_test.py" "# python_c_extension_multilib_test.py")
#install(FILES "${CMAKE_BINARY_DIR}/python_c_extension_multilib_test.py" DESTINATION ".")
