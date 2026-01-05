cmake_minimum_required(VERSION 3.14)
project(cppcore VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Create header-only library (INTERFACE library)
add_library(cppcore INTERFACE)

# Set target properties
set_target_properties(cppcore PROPERTIES
    VERSION ${PROJECT_VERSION}
)

# Set include directories
target_include_directories(cppcore INTERFACE
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)

# Optional: Set up installation
include(GNUInstallDirs)

install(TARGETS cppcore
    EXPORT cppcoreTargets
)

install(EXPORT cppcoreTargets
    FILE cppcoreTargets.cmake
    NAMESPACE cppcore::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/cppcore
)

