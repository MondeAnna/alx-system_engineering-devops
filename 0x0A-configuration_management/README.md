### [ALX](https://www.alxafrica.com/) System Engineering Plus

Studies carried out in the **[ALX Software Engineering Plus](https://www.alxafrica.com/software-engineering-plus/)** course

<br />

#### Technologies

* Bash:     5.1-6ubuntu1
* Docker:   24.0.5
* Puppet:   8.4.0
* Ubuntu:   20.04 LTS

<br />

#### Learning Objectives

* At the end of this project, you are expected to be able to `explain to anyone`, **without the help of Google**:
    * You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
    * You must be able to explain what each component is doing
    * You must be able to explain system redundancy
    * Know all the mentioned acronyms: LAMP, SPOF, QPS

<br />

#### Resources

* _[Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)_
* _[Puppet resource type: file (check "Resource types" for all manifest types in the left menu)](https://www.puppet.com/docs/puppet/5.5/types/file.html)_
* _[Puppet lint](http://puppet-lint.com/)_

<br />

#### Requirements

* Your Puppet manifests must:
    * Pass `puppet-lint` version `2.1.1` without any errors
    * Run without error
    * Have the first as a comment explaining what the Puppet manifest is about
    * Have the file end with the extension `.pp`

<br />

#### Installation: puppet

```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

<br />

#### Installation: puppet-lint

```
$ gem install puppet-lint
```

<br />
