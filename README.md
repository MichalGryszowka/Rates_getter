# Rates getter
> A short program for checking the USD, CHF and GBP currencies from nbp.pl and sending them in csv format by e-mail

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- Program is checking actual rate of USD, CHF and GBP currencies from NBP API, adding rate to previous history and calculating average rate.
Final result is stored in CSV format and sent in the attachment by e-mail. Shipment of e-mail is locked by password.
- Main goal was to learn and practice how to write code to send attachments by emial with password protection.


## Technologies Used
- Python - version 3.10.2
- Google Gmail
- Pycharm


## Features
List the ready features here:
- Requesting from NBP API
- Creating CSV file
- Sending attachment in e-mail secured by password


## Setup
 - Google account of e-mail recipient has to be configured to get password for e-mail shipment.
 


## Project Status
Complete - it was just quick training for personal purpose.


## Room for Improvement
Based on the code it would be nice to create program for automatic sending daily currency rate for whole list of email recipients in form of newsletter.

Room for improvement:
- Filled in passowrd can be in hidden mode (only stars visible) for safety purpose.


## Acknowledgements
Give credit here.
- This project was inspired by my mentor Marcin. Many thanks goes to him for help.
- This project was based on [this tutorial](https://www.youtube.com/watch?v=cLjOl_GQZIc&ab_channel=WOWSCHOOL-programowanieiedukacja).


## Contact
Created by [@flynerdpl](https://www.flynerd.pl/) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
