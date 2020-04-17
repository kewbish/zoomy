# Zoomy - a Zoom utility for the terminal
Made with Python, April 2020.  
Created by [Kewbish](https://kewbish.github.io).  
Available on [PyPi as Zoomy](https://pypi.org/project/zoomy/).
Released under the [GPLv3 License](https://www.gnu.org/licenses/gpl-3.0.en.html).  
Issues are welcome!  

## :camera: Why Zoomy?
For the developer, the power user, the student who's just tired of going through countless emails to find a link, then flip through for passwords, and finally try to join the call.  
Zoomy is for you. Quick to use, light, and besides, *cool automation*.  
Also works in signed-out mode - just in case (like me) you don't want to give Zoom your personal information!  

## :movie_camera: Usage
Run `zoomy [alias]` to open your `alias` meeting. For example, `zoomy math` to open your math meeting.  
Run `zoomy add [alias] [confno] [pwd]` or `zoomy a [alias] [confno] [pwd]` to add a meeting called `alias` with the conference number `confno` and the password `pwd`. Adding a password is optional. Your meetings cannot be called `add`, `delete`, or `list` (or `a` / `d` / `l`). This option can also be used to edit currently saved meetings.  
Run `zoomy delete [alias]` or `zoomy d [alias]` to delete your `alias` meeting. For example, `zoomy d math` to delete your math meeting.  
Run `zoomy list` or `zoomy l` to list all your available meetings.  

## :wrench: Installation
Install via PyPi by running `pip install zoomy`. This requires Python to be installed.  
Alternatively, build from source by running the `setup.py` after downloading the ZIP.  

## :gear: How it works
Zoom actually comes with a [custom URL scheme](https://medium.com/zoom-developer-blog/zoom-url-schemes-748b95fd9205), most of which is technically deprecated, but still works well.  
Your conference number is passed in from a saved configuration file, and passed to the URL, which is then started with your system's equivalent of `start`.  
It simplifies the process of remembering all those links and passwords, especially if you don't use Zoom signed in or if you don't keep passwords saved.  

> :warning: - This does expose your meeting IDs and passwords (if you choose to supply them), and it *is* possible, if a hacker decided, to `grep` your entire system for a `.zmy` file and infiltrate your meeting. Use at your own risk.  

## :fast_forward: Changelog
**0.2**:   
- Feature: Add list meetings function  
- Docs: Update docs with additional instructions for list and warning about commas  
- Docs: Add long description to PyPi  
- Docs: Add changelog  
**0.2.1**:  
- Bugfix: Implement file generator if fresh install  
**0.2.2**:  
- Feature: Add support for passwords with commas  
**0.2.3**:
- Delete requirements.txt

**0.1**:
- Started project!
- Docs: Create docs
