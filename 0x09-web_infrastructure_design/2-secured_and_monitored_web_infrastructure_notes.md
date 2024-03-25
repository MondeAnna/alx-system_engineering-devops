### Secured and Monitored Web Infrastructure Specs:

_Additions to Infrastructure:_

* 3 firewalls
* 1 SSL certificate to serve www.foobar.com over HTTPS
* 3 monitoring clients (data collector for Sumologic or other monitoring services)

<br />

### Rationale Behind Additions

#### Firewalls

Each portion of the infrastructure is afforded its own zone of protection. This means that should we have to scale, each server can be duplicated without that design being a hamper.

At the load balancer, we get a general wall meant to keep bad actors out. Within the system, this gives us the change to optimise/replace each firewall per server.

Here, there is the concern that the chosen firewall is open source and thus may be subject to faults such as:
* Being abandoned
* Slow response to new threats
* Little to no changes made when dependencies are found to have vulnerabilities
* Issue Tracking

<br />

#### SSL Certificate

This is to ensure encrypted communication between us and clients is possible. Of note, we will have to install this certificate on a the `A record` as well.

<br />

#### Monitoring Clients

Here we use a third-party open source product by New Relic. The company uses a Premium model, has partnerships with existing hosting sites and with that in mind, is likely to be long lived. The reason being using the monitoring in the first place is that it allows us to always know the state of the product. From that state of the hardware to the traffic and even the response times.

The great benefit in this is that it affords us data that we can then later use when making decisions, such as whether or not to keep the design, is scaling needed, are the performance issues and so on.

<br />

#### What are firewalls for?

Firewalls are for keeping bad actors out of the system.

<br />

#### Why is the traffic served over HTTPS?

The traffic is encrypted by the sender and decrypted by the receiver, thus reducing the likelihood of said data being stolen.

<br />

#### What monitoring is used for?

As per the name, to monitor the state of the system. From the state of the hardware to performance related matters such as number of requests, Read-Write cases, logs and so forth, all dependent on the product being used.

<br />

#### How the monitoring tool is collecting data?

A multitude of areas including, but not limited to, Network Analytics, Application Uptime, Hardware Utilization, Software Performance, Internal Links, Errors and Crashes.

<br />

#### Explain what to do if you want to monitor your web server QPS?

* Via Monitoring: Find the metric in the logs
* Manually: Sum the total number of queries over a period (in secods) and divide by that periof

<br />

### Are there any faults with this infrastructure, especially related to:

#### Why terminating SSL at the load balancer level is an issue?

We have unencrypted data within the system. This makes it vulnerable to bad actors internal to the organisation. See [The Day Google Forgot to Check Passwords](https://www.youtube.com/watch?v=y4GB_NDU43Q)

<br />

#### Why having only one MySQL server capable of accepting writes is an issue?

Where that Primary fails, new writes are lost.

<br />

#### Why having servers with all the same components (database, web server and application server) might be a problem?

* Resources have to be shared
* DBMS are often charged per CPU, thus by placing it on a separate server, that may amount to savings as the product scales

<br />
