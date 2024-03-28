### LAMP Stack Specs:

* 1 server
* 11 web server (Nginx)
* 11 application server
* 11 application files (your code base)
* 11 database (MySQL)
* 11 domain name `foobar.com` configured with a `www` record that points to your server IP `8.8.8.8`

<br />

#### What is a server?

This would be a hardware/software platform whereby one can host products.

<br />

#### What is the role of the domain name?

The provision of a human readable name for the domain, that is, something simpler than IP Addresses.

<br />

#### What type of DNS record _www_ is in _www.foobar.com_?

That would be the `CNAME`.

<br />

#### What is the role of the web server?

This part of the product hosts the HMTL related portion.

<br />

#### What is the role of the application server?

This would be the business logic.

<br />
#### What is the role of the database?

To retain data, as per the name.

<br />

#### What is the server using to communicate with the computer of the user requesting the website?

That would be `HTTP` responses.

<br />

### Are there any faults with this infrastructure, especially related to:

#### SPOF

* _One Server:_ Should this fail, then the whole product fails
* _Code Base:_ Though a separate topic, issues herein also negatively impact the entire product
* _Web App:_ This acts as part of the pipeline towards business logic, a failure or delay here impacts the efficiency of the product as well as possibly causing a failure
* _App Server:_ This would be an inability to execute business logic, either due to overload or an inherent failure to the server
* _Database:_ This expands on the `App Server`, likewise, the lack of a backup

<br />

#### Planned Downtime

In this case, the entire website has to be made unavailable to users. Concerns over this may be addressed in a handful of ways:
* Inform users that there will be downtime prior to the event
* Choose a time that has historically had the least amount of traffic
* Provide a static landing informing users of the planned downtime

<br />

#### Scaling due to too much traffic

The limitation here is the degree of bandwidth and system resources which can be directed at the single server is. That is, the "limitation" is the host provider.

<br />
