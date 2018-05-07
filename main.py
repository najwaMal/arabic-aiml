import aiml

kernal = aiml.Kernel()
kernal.learn("./aiml/botdata/standard/*.aiml")
while True:
    print(kernal.respond(input("> ")))
    
message = "Hello World"

print message 
