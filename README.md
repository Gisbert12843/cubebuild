# cubebuild

A small script wrapper that provides automated development of C++ code for `.ioc` files using ST's CubeMX Code Generation.

# HOW TO USE
## Quick Start

1. **Install**: Install the `.deb` file or use the absolute path to the `cubebuild` script
2. **Configure**: Set up the `build.conf` file according to your workspace
3. **View commands**: Run `cubebuild` or `cubebuild -h` to see available commands
4. **Build & Flash**: Run `cubebuild all` to generate, patch, build, and flash your project

## Minimum Project Structure

```
/
├── ###.ioc
├── build.conf
└── ###/
    └── main.cpp
```

*Note: The location of the main.cpp's parent folder (Source Folder) must be declared in the `build.conf` file.*

## build.conf Structure

```conf
Project
    MyProject

BuildType
    Debug
    # Release
    
IncludeFolders
    Inc

SourceFolders
    Src

CompileOptions
    # -Wall
    # -Wextra
    # -Werror
    # -g
    # -O0
    -fexceptions

Libraries
    # my_library ../my_library

Languages
    C
    CXX
    ASM

GlobalDefines
    # USE_HAL_DRIVER
```

## Important Notes

- Keywords may be removed or commented but **cannot be altered** and still be expected to work
- At least one `SourceFolder` must be specified to locate `main.cpp`
- build.conf indentation for child elements must be respected