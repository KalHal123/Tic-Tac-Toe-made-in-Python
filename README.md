# Tic-Tac-Toe

## Contents
- [Tic-Tac-Toe](#tic-tac-toe)
- [Contents](#contents)
- [Description](#description)
- [Installing Requirements](#installing-requirements)
- [How to Run](#how-to-run)
  - [How to Run the EXE Build](#how-to-run-the-exe-build)
  - [How to Run the Source Code](#how-to-run-the-source-code)
- [License](#license)

### Description
A simple console-based Tic-Tac-Toe game with an optional AI opponent, made in Python.

## How to Run

### How to Run the EXE Build

**Notice: The current Build/Release is made for x64 Windows and tested to work on Windows 10 and upwards.**

**If you want to run the EXE without an AI opponent:**
1. Run the EXE by double-clicking it or through the console by typing:
    ```bash
    TicTacToe.exe
    ```
    or
    ```bash
    TicTacToe.exe -ai False
    ```

**If you want to run the EXE with an AI opponent:**
1. Run the EXE through the console by typing:
    ```bash
    TicTacToe.exe -ai True
    ```
---------------------------------
### How to Run the Source Code

1. Ensure you have Python installed.
2. Navigate to the project directory.
3. Navigate to the [game](game/) folder
4. Run the game using:
    ```bash
    python module1.py
    ```

**If you want to run the Source Code with or without the AI opponent, you can add the same parameters to the launch command in the console as described [here](#how-to-run-the-exe-build). They also work for the source code.**

-----------------------------------------
## License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

## Installing Requirements

The game has some dependencies, they can be installed using the `requirements.txt` file.

1. Ensure you have [Python](https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe) and [pip](https://files.pythonhosted.org/packages/12/3d/d899257cace386bebb7bdf8a872d5fe3b935cc6381c3ddb76d3e5d99890d/pip-24.1.2.tar.gz) installed.
2. Navigate to the project directory.
3. Install the required packages by running:
    ```bash
    pip install -r requirements.txt
    ```

This will install all the necessary packages listed in the `requirements.txt` file.
