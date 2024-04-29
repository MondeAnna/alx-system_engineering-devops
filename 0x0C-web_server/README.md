### [ALX](https://www.alxafrica.com/) System Engineering Plus

Studies carried out in the **[ALX Software Engineering Plus](https://www.alxafrica.com/software-engineering-plus/)** course

<br />

#### Technologies

* Bash:     5.1-6ubuntu1
* Docker:   24.0.5
* Ubuntu:   20.04 LTS

<br />

#### Context

In this project, some of the tasks will be graded on 2 aspects:

* Is your `web-01` server configured according to requirements
* Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file `/tmp/test` containing the string `hello world` and modify the configuration of Nginx to listen on port `8080` instead of `80`, I can use `emacs` on my server to create the file and to modify the Nginx configuration file `/etc/nginx/sites-enabled/default`

<br />

But my answer file would contain:

```
sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu
```

<br />

As you can tell, I am not using `emacs` to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an [SRE](https://www.atlassian.com/incident-management/devops/sre), that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the `root` user, you do not need to use the `sudo` command.

The best [programmers are lazy](https://www.techwell.com/techwell-insights/2013/12/why-best-programmers-are-lazy-and-act-dumb).

<br />

#### Tips

To test your answer Bash script, feel free to reproduce the checker environment:

* start a `Ubuntu 16.04` sandbox
* run your script on it
* see how it behaves

<br />

#### Learning Objectives

* At the end of this project, you are expected to be able to `explain to anyone`, **without the help of Google**:
    * General
        * What is the main role of a web server
        * What is a child process
        * Why web servers usually have a parent process and child processes
        * What are the main HTTP requests

    * DNS
        * What DNS stands for
        * What is DNS main role

    * DNS Record Types
        * A
        * CNAME
        * TXT
        * MX

<br />

#### Resources

* _[How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)_
* _[Nginx](https://en.wikipedia.org/wiki/Nginx)_
* _[How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)_
* _[Processes](https://www.gnu.org/software/libc/manual/html_node/Processes.html#Processes)_
* _[Root and sub domain](https://landingi.com/help/domains-vs-subdomains/)_
* _[HTTP requests](https://www.tutorialspoint.com/http/http_methods.htm)_
* _[HTTP redirection](https://moz.com/learn/seo/redirection)_
* _[Not found HTTP response code](https://en.wikipedia.org/wiki/HTTP_404)_
* _[Logs files on Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)_

<br />

#### SysEng and DevOps Projects

* _[`Transfer File to Server`](0-transfer_file)_
* _[`Install Web Server`](1-install_nginx_web_server)_
* _[`Provide Domain Name`](2-setup_a_domain_name)_
* _[`Permanent Redirection`](3-redirection)_
* _[`Custom 404 Message`](4-not_found_page_404)_
* _[`Server Config with Puppet`](7-puppet_install_nginx_web_server.pp)_

<br />
