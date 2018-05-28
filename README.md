This is an example README file for the doxygit project
======================================================

This is an example project for students learning how to use doxygen and git / github. It contains a Readme-file with basic installation instructions as well as an example Python project.

Related Links
-------------


- [Doxygen download (Windows binary)](https://www.stack.nl/~dimitri/doxygen/download.html)
- [git download](https://git-scm.com/downloads)
- [Graphviz download (use the .msi for Windows)](http://www.graphviz.org/download/)
- [Generate keys for github, requires git to be installd](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
- [Notepad++, Windows only](https://notepad-plus-plus.org/)
- [Markdown](https://daringfireball.net/projects/markdown/)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Pro Git book](https://git-scm.com/book/en/v2)
- [Pro Git book (German)](https://git-scm.com/book/de/v2) (incomplete
  translation, w.i.p.)

Installation
------------

### Windows and Anaconda

- Optional: Install Notepad++
- Open an Anaconda Prompt
- Install Graphviz: `conda install -c conda-forge graphviz`
- Install Doxygen: `conda install -c conda-forge doxygen`
- Install git: `conda install -c conda-forge git`
- During the tutorial, use the Anaconda Prompt to handle the files

### Windows and native Installation

- Optional: Install Notepad++
- Download git, Doxygen and Graphviz from the webpages mentioned above
- Install git. Set Notepad++ (or another editor) as the default editor. Ensure that "Use Git from the Windows Command Prompt" is checked. Leave all other settings to the default values.
- Install Doxygen. You can use the default values.
- Install Graphviz. You can use the default values.
- Add Graphiviz to the `PATH` variable

### Linux (Debian-based)

It is recommended to install all required tools via the default repositories.

- `sudo apt update`
- `sudo apt install doxygen doxygen-gui git`


### MacOS

- Doxygen and Graphviz are for example available on Homebrew
- git has an installer for MacOS (see link above)


Setup
-----

- If not already done: Create a github account at
  [github.com](https://github.com/). This is required for the tutorial and your
  project. If you not want to continue working with github, you can remove it
  later on. Github is a platform for sharing source code and free of charge
  for public repositories.
- Open a terminal (Windows, Linux) / command line window (Windows) / the anaconda prompt (Windows with anaconda) check if all of the following commands work without any problems. All of them should give some output different to "command not found".
    - doxygen
    - git
    - dot
- Setup git in this window:
    - Set your name: `git config --global user.name "John Doe"`
    - Set your mail address: `git config --global user.email
      johndoe@example.com`. The mail address should be the same you entered for
      github.
- Create a public / private key pair: `ssh-keygen -t rsa -b 4096 -C
  "johndoe@example.com"`

Further information can be found online on
[github](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)




FAQ
---

### Add a Program to the path variable (Windows)

- Find out the path of the application from the Windows Explorer. (i.e. `C:\Program Files (x86)\Graphviz(VersionNumber)` for Graphviz
- Copy this path.
- Open *Erweiterte Systemeinstellungen* / *Advanced System Settings*
- Open the tab *Erweitert* / *Advanced*
- Open *Umgebungsvariablen* / *Environment Variables*
- In the field *Systemvariablen* / *System Variables*, locate the variable *Path*
- Click *Bearbeiten* / *Edit*
- Add the path from the first step to the lower field. The different paths are
  separated by semicolons. **Do not remove any values from the existing line.**
  Only add the path for the new app.

**Background:** The path variable exists on all major operating systems. When
working on the command line, the interpreter checks the paths in the path
variable for executables. In case of for example Graphviz, this is required for
Doxygen to find the dot tool which is used for creating dependency graphs.


### The dot tool is not found (Windows)

- Ensure that the dot tool is in the path variable.
- In case this does not work, you can also manually set the path to the dot
  tool in the `Doxyfile` (value of `DOT_PATH`).
- Remember to set this value for each project in which you use Doxygen

### What is the name of this weird style used in this Readme file

It is called [*Markdown*](https://daringfireball.net/projects/markdown/). The
objective is to create a file which has a nice rich text format and can easily
be converted to a more sophisticated format (HTML, pdf, doc).
