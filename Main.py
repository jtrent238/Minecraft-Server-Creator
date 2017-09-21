#!/usr/bin/python


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
ask_spawn_monsters = input("Do you want monsters to spawn? (Enter true or false)")
ask_spawn_animals = input("Do you want animals to spawn? (Enter true or false)")
ask_hardcore = input("Do you want to enable hardcore? (Enter true or false)")
ask_whitelist= input("Do you want to enable Whitelist?  (Enter true or false)")
ask_npcs= input("Do you want to enable whitelist?  (Enter true or false)")
ask_seed= input("Seed: ");
ask_permlvl= input("Permission Level: ");
ask_world_name= input("World Name: ");
ask_flight= input("Do you want to enable flight?  (Enter true or false)")
ask_proxy= input("Do you want to enable proxy?  (Enter true or false)")
ask_port= input("Port: (Reccomended: 25565)");
ask_world_size= input("World Size: (Reccommended: 29999984)");
ask__forcegamemode= input("Do you want to force gamemode?  (Enter true or false)")
ask_buildheight= input("Build Height: (Reccomended: 256)");
ask_snooper= input("Do you want to enable snooper?  (Enter true or false)")
ask_onlinemode= input("Do you want to enable online mode?  (Enter true or false)")
ask_pvp= input("Do you want to enable pvp?  (Enter true or false)")
ask_difficulty= input("Difficulty: [0 = Peaceful, 1 = Easy, 2, = Normal, 3 = Hard]");
ask_cmdblock= input("Do you want to enable Command Blocks?  (Enter true or false)")
ask_gamemode= input("Gamemode: [0 = Survival, 1 = Creative, 2, = Adventure, 3 = Spectator]");
ask_maxplayers= input("Max Players: ");

server_properties = open("Server/server.properties", "w")
server_properties.write("motd=" + ask_motd);
server_properties.write("generate-structures=" + ask_generate_structures);
server_properties.write("spawn-monsters=" + ask_spawn_monsters);
server_properties.write("spawn-animals=" + ask_spawn_animals);
server_properties.write("hardcore=" + ask_hardcore);
server_properties.write("white-list" + ask_whitelist);
server_properties.write("spawn-npcs=" + ask_npcs);
server_properties.write("view-distance=10");
server_properties.write("player-idle-timeout=0");
server_properties.write("server-ip=");
server_properties.write("network-compression-threshold=256");
server_properties.write("resource-pack-sha1=");
server_properties.write("level-type=DEFAULT");
server_properties.write("level-seed=" + ask_seed);
server_properties.write("generator-settings=");
server_properties.write("op-permission-level=" + ask_permlvl);
server_properties.write("level-name=" + ask_world_name);
server_properties.write("allow-flight=" + ask_flight);
server_properties.write("prevent-proxy-connections=" + ask_proxy);
server_properties.write("server-port=" + ask_port);
server_properties.write("max-world-size=" + ask_world_size);
server_properties.write("force-gamemode=" + ask__forcegamemode);
server_properties.write("max-build-height=" + ask_buildheight);
server_properties.write("snooper-enabled=" + ask_snooper);
server_properties.write("online-mode=" + ask_onlinemode);
server_properties.write("resource-pack=");
server_properties.write("pvp=" + ask_pvp);
server_properties.write("difficulty=" + ask_difficulty);
server_properties.write("enable-command-block=" + ask_cmdblock);
server_properties.write("gamemode=" + ask_gamemode);
server_properties.write("max-players=" + ask_maxplayers);
server_properties.close();
print("Server Properties Configured!")