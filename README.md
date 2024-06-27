
<p align="center">
<img src="ui/icons/readme-logo.png" width="250" /><br />
</p>

## Introduction

SwiftNotes is a lightweight desktop application to keep track of tasks
across multiple projects. It is written in Python using the Qt binding 
Pyside6.

## Setup for development
The `\utils` directory holds script to enable and help developing.
To set up a conda environment with the needed dependencies
(see `environment.yml`)navigate into the `\utils` directory and
simply run `00_create_conda_env.bat`. Adapt the file in case you
want to use a specific name for the environment.

To create an executable run `utils\01_create_exe.bat`. This will create the 
`\exe` directory in which you will find `SwiftNotes.exe` under `\dist`. If
you used a different name for the environment adapt it in this `.bat` too.

User interface elements like icons and fonts can be found in `\ui`. If you
want to add resources add them to `resources.qrc` and run
`utils\create_resources_rc.bat` from `\ui` to update `resources_rc.py` in
`\src`.

The source code is provided in `\src`. Entry point to the application is
`main.py`.
