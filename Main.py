#!/usr/bin/python

import os
 
# import sleep to show output for some time period
from time import sleep

import urllib.request
import wget

print("==========================================================================")
print("======== Minecraft Server Creator By jtrent238 | Version 1.0.0.0 =========")
print("==========================================================================")

sleep(2)

# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

# Example
createFolder('./Server/')
# Creates a folder in the current directory called data

#ask_eula = input("Do you accept the Minecraft EULA? (Enter Yes or No)");

#if(ask_eula = "Yes"): set(EULA = true)
#if(ask_eula = "No"): set(EULA = false)

#if(EULA = true): 
#Print "ThankYou for accepting the Minecraft EULA!"
eula = open("Server/eula.txt", "w")
eula.write("eula=true");

#if(EULA = false): 
#Print "You MUST accept the Minecraft EULA!"
	
ask_motd = input("Server MOTD: ");
ask_generate_structures = input("Do you want to generate structures? (Enter true or false) ");
ask_spawn_monsters = input("Do you want monsters to spawn? (Enter true or false) ")
ask_spawn_animals = input("Do you want animals to spawn? (Enter true or false) ")
ask_hardcore = input("Do you want to enable hardcore? (Enter true or false) ")
ask_whitelist= input("Do you want to enable Whitelist?  (Enter true or false) ")
ask_npcs= input("Do you want to npcs to spawn?  (Enter true or false) ")
ask_seed= input("Seed: ");
ask_permlvl= input("Permission Level: ");
ask_world_name= input("World Name: ");
ask_flight= input("Do you want to enable flight?  (Enter true or false) ")
ask_proxy= input("Do you want to enable proxy?  (Enter true or false) ")
ask_port= input("Port: (Reccomended: 25565)");
ask_world_size= input("World Size: (Reccommended: 29999984) ");
ask__forcegamemode= input("Do you want to force gamemode?  (Enter true or false) ")
ask_buildheight= input("Build Height: (Reccomended: 256) ");
ask_snooper= input("Do you want to enable snooper?  (Enter true or false) ")
ask_onlinemode= input("Do you want to enable online mode?  (Enter true or false) ")
ask_pvp= input("Do you want to enable pvp?  (Enter true or false) ")
ask_difficulty= input("Difficulty: [0 = Peaceful, 1 = Easy, 2, = Normal, 3 = Hard] ");
ask_cmdblock= input("Do you want to enable Command Blocks?  (Enter true or false) ")
ask_gamemode= input("Gamemode: [0 = Survival, 1 = Creative, 2, = Adventure, 3 = Spectator] ");
ask_maxplayers= input("Max Players: ");

server_properties = open("Server/server.properties", "w")
server_properties.write("motd=" + ask_motd + "\n");
server_properties.write("generate-structures=" + ask_generate_structures + "\n");
server_properties.write("spawn-monsters=" + ask_spawn_monsters + "\n");
server_properties.write("spawn-animals=" + ask_spawn_animals + "\n");
server_properties.write("hardcore=" + ask_hardcore + "\n");
server_properties.write("white-list" + ask_whitelist + "\n");
server_properties.write("spawn-npcs=" + ask_npcs + "\n");
server_properties.write("view-distance=10" + "\n");
server_properties.write("player-idle-timeout=0" + "\n");
server_properties.write("server-ip=" + "\n");
server_properties.write("network-compression-threshold=256" + "\n");
server_properties.write("resource-pack-sha1=" + "\n");
server_properties.write("level-type=DEFAULT" + "\n");
server_properties.write("level-seed=" + ask_seed + "\n");
server_properties.write("generator-settings=" + "\n");
server_properties.write("op-permission-level=" + ask_permlvl + "\n");
server_properties.write("level-name=" + ask_world_name + "\n");
server_properties.write("allow-flight=" + ask_flight + "\n");
server_properties.write("prevent-proxy-connections=" + ask_proxy + "\n");
server_properties.write("server-port=" + ask_port + "\n");
server_properties.write("max-world-size=" + ask_world_size + "\n");
server_properties.write("force-gamemode=" + ask__forcegamemode + "\n");
server_properties.write("max-build-height=" + ask_buildheight + "\n");
server_properties.write("snooper-enabled=" + ask_snooper + "\n");
server_properties.write("online-mode=" + ask_onlinemode + "\n");
server_properties.write("resource-pack=" + "\n");
server_properties.write("pvp=" + ask_pvp + "\n");
server_properties.write("difficulty=" + ask_difficulty + "\n");
server_properties.write("enable-command-block=" + ask_cmdblock + "\n");
server_properties.write("gamemode=" + ask_gamemode + "\n");
server_properties.write("max-players=" + ask_maxplayers + "\n");
server_properties.close();

# sleep for 2 seconds after printing output
sleep(2)
 
# now call function we defined above
#clear()

print("========================================================================")
print("Server Properties Configured!")
print("========================================================================")
print("NOTE: Some options will need to be manually configured if you want something other than default values because they were skipped!")
print("========================================================================")

ask_minecraftversion= input("What version of Minecraft do you want your server to be? [ex. 1.12] ")
minecraftversion = 'spigot-' + ask_minecraftversion;

# Download Minecraft Server Files
print('Version ' + minecraftversion + ' Selected!');
print('Beginning download of Minecraft ' + minecraftversion + '...');
#url = 'https://launcher.mojang.com/mc/game/' + minecraftversion + '/server/fe123682e9cb30031eae351764f653500b7396c9/server.jar'

url = 'https://cdn.getbukkit.org/spigot/' + minecraftversion + '.jar'
urllib.request.urlretrieve(url, 'Server/' + minecraftversion + '.jar');
print('Version ' + minecraftversion + ' downloaded!');

#os.system('cd Server');
#os.system('dir');
#os.system('java -Xincgc -Xmx1G -jar ' + minecraftversion + '.jar -o false nogui');
