set(TARGET_BINARY_NAME ${CURRENT_TARGET})

project(${TARGET_BINARY_NAME})

file(GLOB SOURCES "sources/*.cpp")


find_package(OpenCV 3.4.8 EXACT REQUIRED HINTS /home/era/libraries_installs/opencv3.4.8/share/OpenCV)
include_directories(${OpenCV_INCLUDE_DIRS})

include_directories(${Boost_INCLUDE_DIRS})

add_definitions(${Boost_LIB_DIAGNOSTIC_DEFINITIONS})

add_executable(${TARGET_BINARY_NAME} ${SOURCES})

target_link_libraries(${TARGET_BINARY_NAME} ${OpenCV_LIBRARIES} ${Boost_LIBRARIES} pthread)
