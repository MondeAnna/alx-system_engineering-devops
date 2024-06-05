### Summary

Between April 22nd and 23rd, requests to `holbertonschool/265-0` servers returned a curl 52 error.

<br />

#### Duration

- Timezone: UTC +02:00
    - Start:    06:00, April 22nd
    - End:      17:16, April 23rd

<br />

#### Impact

Requests to the docker containerised `holbertonschool/265-0` web-servers had empty replies.

<br />

#### Root Cause

Web-server services was not running

<br />

#### Timeline

- Timezone: UTC +02:00
    - 06:00, April 22nd: Detection made
    - 18:00, April 22nd: Emulate error repeatedly in test environment
    - 11:00, April 23rd: Determine `Apache` not running
    - 17:16, April 23rd: Resolve issue

<br />

#### Means of Detection

Being currently in a build phase, the servers are sent requests every 30 minutes. Where a non-`200` response code is provided, an alert is sent to the production team.

<br />

#### Actions Taken

- The sending of a `ping` to ensure the issue was not a network outage
- Deliberately sending requests from multiple desktops
- An `ssh` into the server
    - Explore whether or not the server files were present
    - Check of running services

<br />

#### Resolution

In checking what services were running on the server hardware, it became was clear that the `Apache` service was not running. Starting this services saw requests come back to normal.

<br />

#### Preventative Measures

- The addition of a `service apache start` line in the command of the `docker-compose` scripts
- An additional script that runs `service apache start` should this service no longer register as running

<br />
