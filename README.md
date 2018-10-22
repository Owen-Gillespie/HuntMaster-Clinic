# HuntMaster
HuntMaster is a modular framework made to create interactive puzzle hunts. You describe the hunt using our DSL, and HuntMaster creates a website to host it.

## What it does
With HuntMaster, it's easy to create custom experiences known as hunts. You provide the story and tasks, HuntMaster does the heavy lifting of creating a webapp for your players to interact with the hunt. Each "Hunt" is made up of a sequence of modules. Modules can present parts of the story, require players to enter a passphrase, go to a location, scan a QR code, and more. The system is also easily extensible, so you can create your own modules and add them to your hunts.

Want to create a guided tour of your campus? Make a hunt that directs players to various parts of your campus using their GPS. All you need to do is write a few lines of python, the instructions/descriptions, and deploy using HuntMaster.

## How to make a hunt:
1. Write your hunt as a sequence of modules. Check out the examples directory for examples of how to do this.
2. Run the ``save_module_data`` function from ``seek.py`` to export your hunt as a json file. Make sure that this file is in the same directory as ``main.py``
3. Run ``main.py``. Check that the website is working locally in your browser.

## How we built it
HuntMaster is built for the most part on python 3. It hosts a Flask server with a Bootstrap front-end. When a player in the hunt submits something, it's relayed to a python function which connects to whichever API is needed for that particular part of the hunt. 

Regarding modules,
* Feature detection is done through Google's Vision API
* GPS-based location tracking is done through HTML5
* Image comparison is done through OpenCV (specifically feature tracking with SIFT)
* QR Code generation is done through the `qrcode` python module

## Links

Demo: [https://seek-165508.appspot.com](https://seek-165508.appspot.com)

Devpost: [https://devpost.com/software/huntmaster](https://devpost.com/software/huntmaster)

---

HuntMaster was created by Jacky Lee, Cole Kurashige, and Owen Gillespie
