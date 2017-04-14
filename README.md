# jurymatic
The final solution for creating jury booklets for events of the European Youth Parliament

[![Home Page of jurymatic](http://i.imgur.com/whWcu7O.png)](https://www.youtube.com/playlist?list=PLWqZWxSNRmk83SRJ2hx3tqCu2GrglyhFW)

## Installation
If you like watching video tutorials, you can have a look at this [playlist of videos on how to use `jurymatic`](https://www.youtube.com/playlist?list=PLWqZWxSNRmk83SRJ2hx3tqCu2GrglyhFW). If you're not into that, here's the quick rundown.

### macOS

1. Download the latest release from the [releases section](https://github.com/wolfskaempf/jurymatic/releases).
2. Unpack it and open the folder it contains.
3. Right-click on `install.command` and click `Open`.
4. Click `Open` again, indicating that you trust the source of the file.
5. Follow the steps on the screen. Enter your computer's password when asked.

### Linux

Any popular Linux distribution should be fine. Ubuntu 16.10 was used for the following step-by-step installation.

1. Download the latest release from the [releases section](https://github.com/wolfskaempf/jurymatic/releases).
2. Unpack it and open the folder it contains. If you are using the standard file browser nautilus with Ubuntu 16.10, right-click anywhere in the folder and select `Open in Terminal`. Alternatively, open a Terminal (Ctrl+Alt+T) and navigate into the folder. Make sure you are in the root directory of the project.
3. Install any potentially missing dependency by executing the following command:
`sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk python-dev python`
4. Start installation by executing `./install.command`
5. Follow the steps on the screen. Enter sudo password when asked.

If you encounter issues during installation, make sure at least the libjpeg and zlib [requirements for pillow](http://pillow.readthedocs.io/en/3.0.x/installation.html) are satisfied for your distribution.

### Windows

`jurymatic` requires both PowerShell (version 3.0 or newer) and Python 2 to work on Windows. Since neither are part of a standard installation, you have to install the software manually before using `jurymatic`. To make this as easy as possible, you can just double-click the included file `install-prerequisites.bat`. If your default browser is not _Internet Explorer_ or _Edge_ please copy and paste the following URL into either manually: `http://boxstarter.org/package/nr/dotnet4.5.1,powershell,python2` You might have to confirm the installation and enter your (Administrator's) password. After the script has finished, restart your computer.

1. Download the latest release from the [releases section](https://github.com/wolfskaempf/jurymatic/releases).
2. Unpack it and open the folder it contains.
3. Double-click on `install.bat`.
4. Allow the program to be executed despite security warnings when asked.

## Usage

After you're done installing the program, you can easily start `jurymatic` each time you need it. All data will be saved so you can easily add or change data.

**macOS**: Right-click `start.command`, select `Open` twice and `jurymatic` will start.

**Windows**: Double-click on `start.bat`

**Linux**: Execute `./start.command` in the root directory of the project.

To quit `jurymatic` after using it, just close the window called _Terminal_ (macOS, Linux) or _cmd_ (Windows).

## Video Tutorials
If you'd like to watch videos to understand how to use `jurymatic`, you can do so [here on YouTube](https://www.youtube.com/playlist?list=PLWqZWxSNRmk83SRJ2hx3tqCu2GrglyhFW).
