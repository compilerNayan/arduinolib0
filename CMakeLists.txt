cmake_minimum_required(VERSION 3.14)
project(arduinolib0 VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Create header-only library (INTERFACE library)
add_library(arduinolib0 INTERFACE)

# Set target properties
set_target_properties(arduinolib0 PROPERTIES
    VERSION ${PROJECT_VERSION}
)

# Set include directories
target_include_directories(arduinolib0 INTERFACE
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)

# Optional: Set up installation
include(GNUInstallDirs)

install(TARGETS arduinolib0
    EXPORT arduinolib0Targets
)

install(EXPORT arduinolib0Targets
    FILE arduinolib0Targets.cmake
    NAMESPACE arduinolib0::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/arduinolib0
)

