### Distributed Web Infrastructure Specs:

_Additions to Infrastructure:_

* 2 servers
* 1 web server (Nginx)
* 1 application server
* 1 load-balancer (HAproxy)
* 1 set of application files (your code base)
* 1 database (MySQL)

<br />

### Rationale Behind Additions

#### 2 Servers

* The first server is to act as a load balancer
    * this goes in tandum with the addition of the `HAproxy` load balancer

* The second duplicates the [LAMP Stack](0-simple_web_stack_notes.md) that already powers the product
    * this goes in tandum with the web and app server additions

<br />

#### What distribution algorithm your load balancer is configured with and how it works

As for now, a round robin algorithm is best. It's simple, requires no monitoring and should be easy to maintain.

<br />

#### Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both

The whole notion does not apply here as there is but one load balancer. Thus is neither setup. Note that Active-Active is when both load balancers process requests and responses, whereas Active-Passive is when one load balancer does the processing and second unit lies in wait as a backup.

<br />

#### How a database Primary-Replica (Master-Slave) cluster works

In one way, data is written to the Primary and then replicated to the slave. Another is to also be able to write onto the Replica, meaning the data newer or only present on the Replica is to also be re-synced onto the Primary.

<br />

#### What is the difference between the Primary node and the Replica node in regard to the application

In the application, both nodes have Read-Write privileges. Any re-sync would be either strong or eventual depending on how the delta for consistency.

<br />

### Are there any faults with this infrastructure, especially related to:

#### Where are SPOF

* Here, we have moved the single point of failure from the [product's server](0-simple_web_stack_notes.md) onto the load balancer. Owing to how the load balancer has less work to do, this should mean an overall reduction in failures

<br />

#### Security Issues

* We have no firewall
* Communication is via `HTTP`

<br />

#### No Monitoring

At present we are unaware of the state of the system. The only way to find out is to load the product, enter as admin, etc... That is, we have to proactively and manual check as to whether or not it is up.

<br />
