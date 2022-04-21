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
    <img src="images/pyspy.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">PySPY</h3>

  <p align="center">
    Python Script for gathering information of a machine and mailing it to a desired email. Can be used as a payload to monitor Target and gather intel.
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
        <li><a href="#configure-mail-account">Configure E-Mail Account</a></li>
      </ul>
    <li>
      <a href="#configure-and-customize-script-setup">Configure & Customize Script</a>
      <ul>
        <li><a href="#target-script-setup">Target-Script Setup</a></li>
        <li><a href="#attacker-script-setup">Attacker-Script Setup</a></li>
      </ul>
    </li>
    <li><a href="#usage-and-possible-upgrades">Usage & Possible Upgrades</a></li>
      <ul>
        <li><a href="#target-machine-script">Target Machine Script</a></li>
        <li><a href="#attacker-machine-script">Attacker Machine Script</a></li>
      </ul>
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
- __Target Machine Script__
    - Runs on the target machine
    - Contains 9 functions and 1 main function
    - Collects System information, screenshots, audio, clipboard data & key-logs
    - Responsible for :
        - Gathering data
        - Encrypting data
        - Compressing data
        - Mailing data
        - Deleting data

- __Attacker Machine Script__
    -  Runs on the user's machine
    -  One script created to assist the user with the results of Victm Machine script
    -  Help the user to do it all in console
    -  Created to assist the user for the following :
        - Key generation
        - Decryption of Data
        - Get zip information
        - Unzipping   
<br />

<p align="right">(<a href="#top">Back to top</a>)</p>

<br />


<!-- KEY FEATURES -->
## Key Features 
* __Highly__ and __easily customizable__ as per the requirements
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



<p align="right">(<a href="#top">Back to top</a>)</p>

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


<p align="right">(<a href="#top">Back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

__**NOTE :- TO BE USED FOR EDUCATIONAL PURPOSES ONLY**__

### Prerequisites
- [Python 3](https://www.python.org/downloads/)
- Python modules installed as mentioned <a href="#need-installation">here</a>
- E-mail Account with less secure app access


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/VENGENCE7/PySPY.git
   ```
2. Install [Python 3](https://www.python.org/downloads/) if not installed and set it up.   

3. Install required modules from the Requirements.txt file present in respective script <br />
   ```sh
   pip install -r /path/to/requirements.txt
   ```
   
   Check if required modules are present and verify with <a href="#need-installation">Modules needed</a> using : 
   ```sh
   pip freeze
   ```
   
   For missing modules use:
   ```sh
   pip install <module_name>
   ```

<p align="right">(<a href="#top">Back to top</a>)</p>

### Configure Mail Account

Setup E-mail for for sending mail to the recipient address.This requires to __allow less secure app access__ on ur mail account.

Refer below for setting up G-mail account so that the Script can access it.

* Turning on __'less secure apps'__ settings as mailbox user
    * Go to your _(Google Account)_.
    * On the left navigation panel, click Security.
    * On the bottom of the page, in the Less secure app access panel, click Turn on access.
    * If you don't see this setting, your administrator might have turned off less secure app account access (check the instruction above).
    * Click the Save button.

__**For other mail accounts look up for the required settings (Less Secure App Access) to be changed for mailing accordingly.**__

<p align="right">(<a href="#top">Back to top</a>)</p>


<!-- CONFIGURE AND CUSTOMIZE SCRIPT SETUP -->
## Configure and Customize Script Setup

For **configure the PySPY Script** for being operational and customizing it as per one's needs follow through the instructions below

### Target-Script Setup 

__**NOTE : Only edit [ Main.py ] in target machine unless you know what your doing**__ <br/>

__;)__ Programs are filled with comments to explain whats goin on __:)__.

__**Follow :**__

1. Go through the _comments of main.py_ for understanding whats being done 
2. All the places you need to change are mentioned with _+[EDIT and example for how to be changed]+_ in the code for ease 
3. Generate Key using Attacker Script or you can use a separate script too.
4. Make sure to save and keep the key safe,it will be needed for decrypting.

__**All changes needed to be entered are:**__
  
  - **File Path**
      - Make sure its valid.Do your research on target well ;)
      - If path is invalid it will use current directory path too :) 
  - **Key**
      - Your own key can be entered 
      - Use the **Attacker-Script** to generate one.
      - Can use the "**Key-Generate.py**" present in _Separate-scripts for individual use_ folder in the _Attacker-Script folder_
  - **Folder-Name**
      - Choose a unique name inorder to avoid script crash _ -_O _
  - **Zip File-Name**
  - **File-Names of**
      - All the Files that are going to be created during execution **with proper extensions**(its mentioned in the comments and code,read closely)
  + **Script Execution Settings** 
      + *FUll Script* Execution _time interval_ AND _iterations_
      + *Audio-Recording* time
      + *Clipboard-Copy* settings regarding iterations and time interval between each
      + *Screen-Shots* settings regarding iterations and time interval between each
  + **Mailing Details** ,Make sure to use proxy accoount
      + _From-Address_ Account
      + _Password_ of From address Account
      + _To-Address_ can be any valid mail-ID
      
<p align="right">(<a href="#top">Back to top</a>)</p>

### Attacker-Script Setup

_*No Setup required*_

Its a complimentary Script for PySPY to reduce the attackers work to access and perform operations from a single screen :)

Can create your own Script for your tasks its not mandatory to use this ><

- Just run the Script in powershell or cmd in windows.
- Its interactive 
- Choose options as per your needs
- Separate Scripts for each operation in the Script is also available if requried


<p align="right">(<a href="#top">Back to top</a>)</p>


<!-- USAGE AND Possible Upgrades -->
## Usage And Possible Upgrades

### Target Machine Script

1. Once Configured it can be **converted into an <a href="https://www.geeksforgeeks.org/convert-python-script-to-exe-file/">executable</a>** that can be sent to the Target and trick him to run it .
2. Can be used as a **Payload** to be used on the target machine .
3. Can be run as a **Script** on machines that are compromised .
4. Using an anonymous account and recipient account to **avoid any connection** that can compromise the attacker .
5. Can be used to:
    + To **monitor** target
    + Gather **intel** about the target
    + Allows to have a variety of data using just a single script 

__**Possible Upgrades**__

+ Application of asymetric encryption or any other complex encyption techniques
+ Configuring to create a hidden folder
+ Masking its working with additional programs
+ Perform other faster compressing techniques
+ Clearing logs of tasks
+ Creating password protected files
+ Record audios at multiple intervals
+ Gather additional information of network
+ Creating session for Screen share to have direct stream of the target
+ Get intel through camera access

<p align="right">(<a href="#top">Back to top</a>)</p>

### Attacker Machine Script

1. Allows **one screen access** to all functionality .
2. **Reduced post-attack work** .
3. Can be used as **a general script** for doing unzipping and getting zip info as well to lookout for malicious content . 

__**Possible Upgrades**__

+ To create a systematic way to store all intel according to a order by creating & integrating another Script for storing files accordingly,which can help in **scanning and investigating data** for any threats . 
+ For creating complex keys .
+ Faster execution of unzipping and decryption .
+ Integration of tasks like self zipping and decryption as per the file names(as we mention in target Script)
+ Judging a zip to be safe to be unzipped if any anonmalies detected and warm

<p align="right">(<a href="#top">Back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

__**Don't forget to give the project a star! Thanks again!**__

<p align="right">(<a href="#top">Back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the  License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">Back to top</a>)</p>



<!-- CONTACT -->
## Contact

__**Bhavish Anand**__ :- bhavish007anand@gmail.com

__**Project Link:**__ :- [PySPY](https://github.com/VENGENCE7/PySPY)

<p align="right">(<a href="#top">Back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [**Grant Collins**-For basic understanding of concept](https://www.youtube.com/watch?v=25um032xgrw&t=1946s)
* [**Tech with Tim**-For better understanding of a key-logger](https://www.youtube.com/c/TechWithTim)
* [**Stack Overflow**-For Solving all my queries regarding _threading_ ](https://stackoverflow.com/)
* [**Iampython**-For implementinf cryptography module for encryption](https://www.youtube.com/watch?v=bE7fl6qN-LY&t=511s)

<p align="right">(<a href="#top">Back to top</a>)</p>



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
