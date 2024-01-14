#To Do: Replace all this with a naming service

# With local addresses (within the same cloud region)
#PEERS = ['172.31.78.41','172.31.65.227','172.31.74.212','172.31.75.17','172.31.72.48','172.31.75.162']

# With public addresses (in the same region of the cloud)
# The last one is not fixed and must be changed each time the lab is restarted.
PEERS_SAME_REGION = ['172.31.22.98','172.31.28.132','172.31.23.195','172.31.31.9']

# With public addresses (in two separate regions - last two servers in Oregon)
PEERS_TWO_REGIONS = ['172.31.22.98','172.31.28.132','172.31.23.195','172.31.31.9','172.31.29.97','172.31.17.61']


PEER_UDP_PORT = 4567
PEER_TCP_PORT = 5679
N = 4   # Number of peers
SERVER_ADDR ='172.31.22.98'
SERVER_PORT = 5678

