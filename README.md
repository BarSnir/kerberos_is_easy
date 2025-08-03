# kerberos_is_easy
Simple repo to demonstrate how to connect kerberos with clients

# Setup
## Kadmin principal & ticket
docker exec -it kdc bash
kadmin.local
addprinc -pw mypassword user@EXAMPLE.COM
addprinc -randkey HTTP/service.example.com@EXAMPLE.COM
ktadd -k /etc/krb5.keytab HTTP/service.example.com@EXAMPLE.COM

## Kclient connect & verify key
docker exec -it kerberos-client bash
apt update && apt install -y krb5-user
echo 123456 | kinit user@EXAMPLE.COM
klist


## Install Python dependencies &&
apt update && apt install -y python3-pip python3-venv libkrb5-dev gcc
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install gssapi


# Run to generate ticket token
python main.py

# TODO
[1] Organize dockers
[2] Add Zookeepers only
[3] Add 3 Kraft controller
[4] Add 3 Broker
[5] Add Schema Registry
[6] Add Java producer
[7] Add Java consumer
[8] Add Cluster Link