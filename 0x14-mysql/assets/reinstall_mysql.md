### How to Fresh Reset and Install mysql 5.7

**Before going through the guide try this command, if it is gonna install `MySQL 5.7` correctly, when you see the white windows you can jump to the configuration step, and see what to choose:**

```
sudo wget -O mysql57 https://raw.githubusercontent.com/nuuxcode/alx-system_engineering-devops/master/scripts/mysql57 && sudo chmod +x mysql57 &&  sudo ./mysql57
```

<br />

If this command did not install 5.7 correctly you can continue reading the following guide.

**NOTE AS YOU PROCEED: At any point in this guide, don't go to the next step if you have errors in the current step you are in, make sure there are no errors.**

<br />

### STEPS

#### Clean Running MySQL Processes

* Check for any running MYSQL Processes: `sudo ps aux | grep mysql`
* If MySQL is running, try stopping it: `sudo service mysql stop`
* Double-check if MySQL is no longer running: `sudo ps aux | grep mysql`
* If MySQL processes are still running, terminate them, remember to replace PID with the value of your PID: `sudo kill -9 <PID>`

<br />

#### Remove Existing MySQL Versions

* Remove MySQL packages: `sudo apt-get remove --purge mysql-server mysql-client mysql-common -y && sudo apt-get autoremove -y`
* If no errors occurs, proceed to next steps
* If prompted by a dialog to remove data directories, please select `YES` and press Enter

<br />

#### Remove MySQL Apt Configurations

* Run the following:
    * `sudo rm -rf /etc/apt/sources.list.d/mysql.list*`
    * `sudo rm -rf /var/lib/mysql-apt-config`
    * `sudo dpkg --purge mysql-apt-config`

<br />

#### Double Check and Remove Configuration File

* Check by running: `dpkg -l | grep mysql`
* The result from above should be none, on your terminal
* Now, remove configurations files: `sudo rm -rf /etc/mysql /var/lib/mysql`

<br />

#### Update the packages

* Check the `sources.list` file for `MySQL` repository entries (example: deb http://repo.mysql.com/apt/ubuntu bionic main)
    * `cat /etc/apt/sources.list | grep mysql`
* There should be none
* If there are entries, open the `sources.list` file: `sudo vi /etc/apt/sources.list`
* If no errors occur, proceed to the next step
* Update the package: `sudo apt update`
* Kill any running processses: `ps aux | grep apt`

<br />

#### Clean APT Cache

* `sudo apt clean`

<br />

#### Configure any Pending Packages and Install MySQL

* A few windows are going to show up, follow the prompts to select Ubuntu Bionic, change to MySQL 5.7 and set a password if needed
* `sudo dpkg --configure -a`
* `sudo wget -O mysql57 https://raw.githubusercontent.com/nuuxcode/alx-system_engineering-devops/master/scripts/mysql57 && sudo chmod +x mysql57 && sudo ./mysql57`
* After installation, check MySQL status: `sudo service mysql status`

<br />

#### If issues persist, use the following commands to debug

* `journalctl -u mysql.service`
* `cat /var/log/mysql/error.log`
* `journalctl -xe`

<br />

#### Check this post o learn more about MySQL

[Database Administration](https://shazaali.substack.com/p/database-administration)

<br />
