from mcstatus import MinecraftServer
while 1 == 1:
    print('Welcome to the Minecraft Server Checker!')
    serverinput = input('Enter the Server IP!')
    server = MinecraftServer.lookup(serverinput)
    status = server.status()
    print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
    ask = input("Do you want to check another Server?")
    if ask != "yes":
        break
