# Changelog
## 0.2.0
- Added C file support (.c)
  - Compiles using GCC
  - Runs executable
  - Optional cleanup after execution
  - Skips compilation if up-to-date (faster repeated runs)
- Added Java file support (.java)
  - Compiles using javac
  - Runs class using java
  - Skips compilation if up-to-date
- Error messages for C/Java now show compiler output
- Python project support unchanged
- Timer continues to show execution time for all languages
## 0.1.0
- Run project folders (run .)
- Automatic project detection
- nex.config support
- Python project auto detection

## 0.0.1
- Added --version command
- Added --help command
- Added execution time measurement
- Improved error handling

## 0.0.0
- Basic runner for Python, C, Java
