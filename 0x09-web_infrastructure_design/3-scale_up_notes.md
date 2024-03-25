### Secured and Monitored Web Infrastructure Specs:

_Additions to Infrastructure:_

* 1 server
* 1 load-balancer (HAproxy) configured as cluster with the other one
* Split components (web server, application server, database) with their own server

<br />

### Rationale Behind Additions

#### Server

This affords another environment/node within which to host the product

<br />

#### 1 Load Balancer

This allows an Active-Passive algorithm for the load balancers. Thus, should one fail, then the other is there as an immediate backup. Owing to these being software, they can be run on the same hardware.

<br />

#### Split Components

There was a temptation to have a separate server for `web`, `app` and `database`, yet this makes little sense as:
* We have the same SPOF as the simple web stack
* Instroduce things such as latency
* Produce a pipeline, whereby when a request makes it into the system, it is still at risk of being dropped intransit between servers

As an alternative, a third node has been selected, keeping with the trusty design.

<br />
