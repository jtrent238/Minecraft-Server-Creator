#!/usr/bin/python

from raven import Client

import os
import time
import webbrowser

# import sleep to show output for some time period
from time import sleep

import urllib.request
import wget

#client = Client('https://a65471b6dda6414ebcdb13f9fce338ea:7ec6f32c1b4347e6b768358d0590d24a@sentry.io/1268907')

#Raven.config('https://a65471b6dda6414ebcdb13f9fce338ea@sentry.io/1268907', { release: '0e4fdef81448dcfa0e16ecc4433ff3997aa53572'});

print("==========================================================================")
print("======== Minecraft Server Creator By jtrent238 | Version 1.0.0.0 =========")
print("==========================================================================")

sleep(2)

#vanilla downloads
mc_1_13_2 = "https://launcher.mojang.com/v1/objects/3737db93722a9e39eeada7c27e7aca28b144ffa7/server.jar"
mc_1_13_1 = "https://launcher.mojang.com/v1/objects/fe123682e9cb30031eae351764f653500b7396c9/server.jar"
mc_1_13 = "https://launcher.mojang.com/v1/objects/d0caafb8438ebd206f99930cfaecfa6c9a13dca0/server.jar"
mc_1_12_2 = "https://launcher.mojang.com/v1/objects/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar"
mc_1_12_1 = "https://launcher.mojang.com/v1/objects/561c7b2d54bae80cc06b05d950633a9ac95da816/server.jar"
mc_1_12 = "https://launcher.mojang.com/v1/objects/8494e844e911ea0d63878f64da9dcc21f53a3463/server.jar"
mc_1_11_2 = "https://launcher.mojang.com/v1/objects/f00c294a1576e03fddcac777c3cf4c7d404c4ba4/server.jar"
mc_1_11_1 = "https://launcher.mojang.com/v1/objects/1f97bd101e508d7b52b3d6a7879223b000b5eba0/server.jar"
mc_1_11 = "https://launcher.mojang.com/v1/objects/48820c84cb1ed502cb5b2fe23b8153d5e4fa61c0/server.jar"
mc_1_10_2 = "https://launcher.mojang.com/v1/objects/3d501b23df53c548254f5e3f66492d178a48db63/server.jar"
mc_1_10_1 = "https://launcher.mojang.com/v1/objects/cb4c6f9f51a845b09a8861cdbe0eea3ff6996dee/server.jar"
mc_1_10 = "https://launcher.mojang.com/v1/objects/a96617ffdf5dabbb718ab11a9a68e50545fc5bee/server.jar"
mc_1_9_4 = "https://launcher.mojang.com/v1/objects/8e897b6b6d784f745332644f4d104f7a6e737ccf/server.jar"
mc_1_9_3 = "https://launcher.mojang.com/v1/objects/8e897b6b6d784f745332644f4d104f7a6e737ccf/server.jar"
mc_1_9_2 = "https://launcher.mojang.com/v1/objects/2b95cc7b136017e064c46d04a5825fe4cfa1be30/server.jar"
mc_1_9_1 = "https://launcher.mojang.com/v1/objects/bf95d9118d9b4b827f524c878efd275125b56181/server.jar"
mc_1_9 = "https://launcher.mojang.com/v1/objects/b4d449cf2918e0f3bd8aa18954b916a4d1880f0d/server.jar"
mc_1_8_9 = "https://launcher.mojang.com/v1/objects/b58b2ceb36e01bcd8dbf49c8fb66c55a9f0676cd/server.jar"
mc_1_8_8 = "https://launcher.mojang.com/v1/objects/5fafba3f58c40dc51b5c3ca72a98f62dfdae1db7/server.jar"
mc_1_8_7 = "https://launcher.mojang.com/v1/objects/35c59e16d1f3b751cd20b76b9b8a19045de363a9/server.jar"
mc_1_8_6 = "https://launcher.mojang.com/v1/objects/2bd44b53198f143fb278f8bec3a505dad0beacd2/server.jar"
mc_1_8_5 = "https://launcher.mojang.com/v1/objects/ea6dd23658b167dbc0877015d1072cac21ab6eee/server.jar"
mc_1_8_4 = "https://launcher.mojang.com/v1/objects/dd4b5eba1c79500390e0b0f45162fa70d38f8a3d/server.jar"
mc_1_8_3 = "https://launcher.mojang.com/v1/objects/163ba351cb86f6390450bb2a67fafeb92b6c0f2f/server.jar"
mc_1_8_2 = "https://launcher.mojang.com/v1/objects/a37bdd5210137354ed1bfe3dac0a5b77fe08fe2e/server.jar"
mc_1_8_1 = "https://launcher.mojang.com/v1/objects/68bfb524888f7c0ab939025e07e5de08843dac0f/server.jar"
mc_1_8 = "https://launcher.mojang.com/v1/objects/a028f00e678ee5c6aef0e29656dca091b5df11c7/server.jar"
mc_1_7_10 = "https://launcher.mojang.com/v1/objects/952438ac4e01b4d115c5fc38f891710c4941df29/server.jar"
mc_1_7_9 = "https://launcher.mojang.com/v1/objects/4cec86a928ec171fdc0c6b40de2de102f21601b5/server.jar"
mc_1_7_8 = "https://launcher.mojang.com/v1/objects/c69ebfb84c2577661770371c4accdd5f87b8b21d/server.jar"
mc_1_7_7 = "https://launcher.mojang.com/v1/objects/a6ffc1624da980986c6cc12a1ddc79ab1b025c62/server.jar"
mc_1_7_6 = "https://launcher.mojang.com/v1/objects/41ea7757d4d7f74b95fc1ac20f919a8e521e910c/server.jar"
mc_1_7_5 = "https://launcher.mojang.com/v1/objects/e1d557b2e31ea881404e41b05ec15c810415e060/server.jar"
mc_1_7_4 = "https://launcher.mojang.com/v1/objects/61220311cef80aecc4cd8afecd5f18ca6b9461ff/server.jar"
mc_1_7_3 = "https://launcher.mojang.com/v1/objects/707857a7bc7bf54fe60d557cca71004c34aa07bb/server.jar"
mc_1_7_2 = "https://launcher.mojang.com/v1/objects/3716cac82982e7c2eb09f83028b555e9ea606002/server.jar"
mc_1_6_4 = "https://launcher.mojang.com/v1/objects/050f93c1f3fe9e2052398f7bd6aca10c63d64a87/server.jar"
mc_1_6_2 = "https://launcher.mojang.com/v1/objects/01b6ea555c6978e6713e2a2dfd7fe19b1449ca54/server.jar"
mc_1_6_1 = "https://launcher.mojang.com/v1/objects/0252918a5f9d47e3c6eb1dfec02134d1374a89b4/server.jar"
mc_1_5_2 = "https://launcher.mojang.com/v1/objects/f9ae3f651319151ce99a0bfad6b34fa16eb6775f/server.jar"
mc_1_5_1 = "https://launcher.mojang.com/v1/objects/d07c71ee2767dabb79fb32dad8162e1b854d5324/server.jar"
mc_1_4_7 = "https://launcher.mojang.com/v1/objects/2f0ec8efddd2f2c674c77be9ddb370b727dec676/server.jar"
mc_1_4_5 = "https://launcher.mojang.com/v1/objects/c12fd88a8233d2c517dbc8196ba2ae855f4d36ea/server.jar"
mc_1_4_6 = "https://launcher.mojang.com/v1/objects/a0aeb5709af5f2c3058c1cf0dc6b110a7a61278c/server.jar"
mc_1_4_4 = "https://launcher.mojang.com/v1/objects/4215dcadb706508bf9d6d64209a0080b9cee9e71/server.jar"
mc_1_4_2 = "https://launcher.mojang.com/v1/objects/5be700523a729bb78ef99206fb480a63dcd09825/server.jar"
mc_1_3_2 = "https://launcher.mojang.com/v1/objects/3de2ae6c488135596e073a9589842800c9f53bfe/server.jar"
mc_1_3_1 = "https://launcher.mojang.com/v1/objects/82563ce498bfc1fc8a2cb5bf236f7da86a390646/server.jar"
mc_1_2_5 = "https://launcher.mojang.com/v1/objects/d8321edc9470e56b8ad5c67bbd16beba25843336/server.jar"
mc_1_2_4 = "https://launcher.mojang.com/v1/objects/d8321edc9470e56b8ad5c67bbd16beba25843336/server.jar"
mc_1_2_3 = "http://assets.minecraft.net/1_2/minecraft_server.jar"
mc_1_2_2 = "http://assets.minecraft.net/1_2/minecraft_server.jar"
mc_1_2_1 = "http://assets.minecraft.net/1_2/minecraft_server.jar"

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

# EULA = "null"


# ask_eula = input("Do you accept the Minecraft EULA? (Enter Yes or No)");
# webbrowser.open('https://account.mojang.com/documents/minecraft_eula')  # Go to example.com

# if(ask_eula is "Yes" or "YEs" or "YES" or "yes" or "YeS" or "yeS" or "yEs" or "yES"): 
	# EULA = "true"
	# print("ThankYou for accepting the Minecraft EULA!")
	# eula = open("Server/eula.txt", "w")
	# eula.write("eula=true");
# if(ask_eula is "No" or "no" or "NO" or "nO"): 
	# EULA = "false"
	# print("You MUST accept the Minecraft EULA!" + "\n")
	# print("This will close in 30 seconds!")
	# time.sleep(30)
	# exit

# if(EULA is "true"): 
	# print("ThankYou for accepting the Minecraft EULA!")
	# eula = open("Server/eula.txt", "w")
	# eula.write("eula=true");

# if(EULA is "false"): 
	# print("You MUST accept the Minecraft EULA!" + "\n")
	# print("This will close in 30 seconds!")
	# time.sleep(30)
	# exit
	
eula = open("Server/eula.txt", "w")
eula.write("eula=true");
	
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
time.sleep(2)
 
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

os.system('cd Server');
os.system('directory');
os.system('java -Xincgc -Xmx1G -jar ' + minecraftversion + '.jar -o false nogui');
