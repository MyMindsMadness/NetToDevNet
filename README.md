# NetToDevNet
This repo is for Network engineers trying to get in to DevNet and using articles from the MyMindsMadness.com blog pages. 

So far this repo has the following projects. 

## dhcp_learn_python

This is linked to a small series of videos on YouTube. The idea of this repo is to have a Network Theamed project that can be used to grow your skills in python, from Beginner to Advanced. 
Learn about 

 - Libraries
 - Lists
 - Loops
 - Dictionaries
 - Functions
 - and More...

## Git_Repo_Template

A simple Git Template linked to "My First Repo" project.

## interface_reconfig

This project runs 2 main scripts, a reconnaissance script (reconn.py) and the Reconfiguration script. (reconfig.py). 
This script is ideal to make mass interfaces changes within an enterprise environment. within the script we look to change the line 
    "authentication order dot1x mab" to "authentication order mab dot1x"

To do this it searches for a string existing within the desired interfaces. 
For example a common description or common confiuguration setting. Where this string is detected, the interface will be reconfigured.  
In addition the script will output several files. 
    1. A Backup of the file backup/ip.add.re.ss.txt
    2. An audit of which interfaces will be changed

Complete the json file with your device details. 
Change the seach string to your desired common string and run. 

## Interface Parser

This project is to parse interface of the Cisco IOS interfaces, breaking it down in to machine friendly json. 
There are other projects better suited to performing this task, such as NCT_Templates, or Ansible. This was simply an experiment to play with.

## MyFirstRepo

This project is about getting your git repos set up correctly. How to use the .gitignore file and how to handle secret. You are best to follow the blog on this one. 

Blog URL: https://www.mymindsmadness.com/post/git-repository-basics 

## NetToDev

This project is linked to the YouTube shorts Series (supercut found here: https://youtu.be/OOfyiGjsBqQ )
This takes the a blank script and over 12 parts turns it in to a usable piece of code that can function in your lab or network. 
Perfect for anyone just beginning their Python Journey. 
Learn the following 

 - Variables
 - for loops
 - dynamically create configuration
 - connect to a device
 - Send show and configuration commands 
 - Retrieve output from device
 - Create a change log (writing out to file)
 - keep secrets 
 - and more. 

## Print_IP_Addresses

This project is to print out all IPv4 Private addresses. It is designed to be a simple script with an aim to bring a network concept into your first coding experience. 

Blog URL: https://www.mymindsmadness.com/post/simple-network-python-script

## Thank you

I hope you enjoy these projects. 
