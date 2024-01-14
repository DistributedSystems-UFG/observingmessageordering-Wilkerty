#To Do: Replace all this with a naming service

# With local addresses (within the same cloud region)
#PEERS = ['172.31.78.41','172.31.65.227','172.31.74.212','172.31.75.17','172.31.72.48','172.31.75.162']

# With public addresses (in the same region of the cloud)
# The last one is not fixed and must be changed each time the lab is restarted.
PEERS_SAME_REGION = ['52.2.237.129','44.196.1.199','44.206.78.114','44.219.39.15']

# With public addresses (in two separate regions - last two servers in Oregon)
PEERS_TWO_REGIONS = ['52.2.237.129','44.196.1.199','44.206.78.114','44.219.39.15','34.213.67.236','52.24.179.149']


PEER_UDP_PORT = 4567
PEER_TCP_PORT = 5679
N = 4   # Number of peers
SERVER_ADDR ='52.2.237.129'
SERVER_PORT = 5678

