![distributed system](1-distributed_web_infrastructure.png)

# LOAD BALANCER (HAProxy)

The load balancer is used to reduce system load, in the case of our system it is done using the round robin distribution algorithm that sends traffic or passes a connection to the next server in line, so task A will be sent to the first server, task B will be sent to the second sever, task C will be sent to the first server and so on and so forth.


# SERVERS

Cloning the existing server and creating a new server helps to reduce downtime by ensuring users can always access data in situations where one of the servers is unresponsive or maintenance is being done on one of the servers. Having multiple server also helps to backup data and prevent loss of data.

# Issues of the above infrastructure

- SPOF (Single Point Of Failure): there is a SPOF in this scenario since we only have one database and if this fails then the entire system fails.
- Security: the above infrastructure has no firewall and no HTTPS so it is vulnerable to attack from unknown IP addresses.
- No monitoring: there is no monitoring in the above infrastructure hence it would be difficult to know what component or item in the infrastructure is not working and why.

