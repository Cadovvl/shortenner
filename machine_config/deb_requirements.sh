apt-get update
apt-get install -y net-tools wget curl vim software-properties-common

# make host available by mDNS
apt-get install -y avahi-daemon

# docker

# suppose to be installed
# curl -fsSL https://get.docker.com -o get-docker.sh
# sh get-docker.sh 

apt-get install -y docker-compose


# sensors
apt-get install -y lm-sensors
apt-get install -y sysstat





