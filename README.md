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
- Main goal was to learn and practice how to write code to send attachments in e-mail secured by password.


## Technologies Used
- Python - version 3.10.2
- Google Gmail
- Pycharm


## Features
- Requesting from NBP API
- Creating CSV file
- Sending attachment in e-mail secured by password


## Setup
 - Google account of e-mail recipient has to be configured to get password for e-mail shipment.
 


## Project Status
Complete - it was just quick training for personal purpose.


## Room for Improvement
- Based on the code it would be nice to create program for automatic sending daily currency rate for whole list of email recipients in form of newsletter.
- Filled in password can be in hidden mode (only stars visible) for safety purpose.


## Acknowledgements
- Thanks to Marcin for inspiring me to do this task.
- E-mail configuration was based on (https://www.youtube.com/watch?v=cLjOl_GQZIc&ab_channel=WOWSCHOOL-programowanieiedukacja).


## Contact
Created by michal.gryszowka@gmail.com
