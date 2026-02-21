---
title: "The Devops Rough cli / Bash Guide"
date: 2021-07-24
categories: ["SRE"]
tags: ['DevOps', 'Bash', 'Linux', 'Emojis']
author: "Eric Arellano"
description: "Useful bash commands for DevOps"
draft: false
---

## Useful Bash commands for DevOps work    {{< emoji toolbox >}}

So Bash is no longer the hottest ticket on the market. Happens. I may have seen the actual point where this peaked 
and let me tell you, that's something. Still, there's some cool stuff to be done with Bash.

For example, if you are writing a quick and dirty Terraform configuration, you can get really far with TF templates, 
HCL interpolation and well placed Bash commands:  

[Terraform Bash template for Jitsi installation](https://github.
com/edamsoft-sre/jitsi-azure-terraform/blob/trunk/environments/prod/templates
/setup.tpl)


### 1.  iterm2 or csshX  {{< emoji tv >}}

The best terminal software will practically do your job for you. Just install, sit back and cash in. If you don't 
know what either is, try iterm2 first. If you can find csshX and install it, then all your problems will be solved.  
You will have new ones, for sure. {{< emoji crocodile >}} but the old ones, gone.  Using multiple windows efficiently is almost 
better than actually automating anything.  It can be lot's of fun, and also very dangerous.



###### iterm Shortcuts {{< emoji cactus >}}

    Ctrl-shift-i - Send output to all windows AND tabs (watch out!)
    Ctrl-D - Open a window to the right
    Ctrl-Shift-D - Open a window below
    Ctrl-Shift-Return - toggle current window full screen (fill iterm2 window)
    
 
 *If you need or WANT to have dozens of servers open and send commands to different sub groups, and, and, and....*

 [Get csshX](https://formulae.brew.sh/formula/csshx) !!! Then, relax and eat some ramen {{< emoji ramen >}} 
***

#### 2. top   {{< emoji crystal_ball >}}

The Linux *top* command is pretty well documented. 

I like to type "zbx" when I start it, and then capital *I* and *1* to check the number of cpus/cores.

This doesn't do much, but it looks nice.

***

###### options

    -  *x*:    enable bold for current sort_by column
    -  *z*:     enable color
    -  *Z*:     edit colors
    -  *I*:     Irix mode - detects single cpu
    -  *b*:     toggle solid column/row highlight background
    -  *k*:     kill pid
    -  *m*:     memory ( I think, check the man page)
    -  *l*:     *load* haha but really, just type *uptime*

***

### 3. find 

Find the largest directories or files in a tree

    find . -type d -print0 | xargs -0 du -s | sort -n | tail -15 | cut -f2 | xargs -I{} du -sh {}

Xargs allows us to pass multiple arguments to a command like Python *map*, so the disk usage *du* command receives 
each subsequent file result from find and gets its size. Then we do some table transformation, basically, and re-run 
the results through *xargs* and *du* to generate a final listing that is sorted across all results.
    
 
***

### Run a command on the findings

Another way to find files or directories and execute on command with them is the explicit *-exec* switch.

    find . -mtime 0 -exec stat '{}' \;

***

### 4. capture whole packets 

    tcpdump -n -A -q -w /tmp/packet.cap <some filter>
 
Capturing packets is a lot of fun, if you're an evil hacker. Otherwise it's a huge pain in the ass. Most likely, you 
kids will be looking at packet statistics aggregated in a nice GUI like Grafana, Kibana, or not at all thanks to 
advances in the software industry. You're welcome. 
 
    nc -v -u google.org 5060

read captures in CLI
    
    tcpdump -r | less

***

### 5. ssh and scp

    scp -o 'ProxyJump user@bastion' -i key user@host:/path/to/remote/file /local/path/file
    
You should always be using secure shell with strong RSA keys and a good key management system. 

Other than that, use your ~/.ssh/config file to set some sensible defaults

    Host *
       UseKeyChain yes
       AddKeysToAgent yes
       IdentityFile ~/.ssh/id_rsa_private_keyfile 

 Add ssh keys to the macOS agent, if that's your OS. If not, it won't work. Well, it should but who knows what the 
 Ubuntu or RedHat options are. Who cares?
 
     ssh-add -l
     ssh-add ~/path/to/my/key
     ssh-add -l
     
 {{< emoji bulb >}} Use a passphrase on your keys. Why not.

***

### 6. Awk and sed and cut

Learn them well, you can really go down a rabbithole with these tools. Through probably the late 90's they were best 
in class. But you still have thousands of websites and production platforms relying on a well placed Awk or Sed, 
trust me.


 {{< emoji bulb >}} Use *sed* to replace text with regex
 
 Sed allows simple regular expression matching which is what you're going to have to do to fix your mistakes. All of them.
  
    sed -i "s/component_secret =.*/component_secret = \"$JICOFO_SECRET\"/" $PROSODY_HOST_CONF
 
    sed -i "s#some_text/next_one#next_one#g" $INPUT_FILE
     
 On Ubuntu Hirsute 21.04 get a list of only IPv4 addresses.  Can be done in better ways, probably, but you get the jist.

       ip -4 addr | awk '{ print $2 }' | sed 's#/.*##' | sed "s#^[^0-9].*##" | sed '/^$/d' | sed 1d
   
 * Awk is a full programming language, but we can use it to get text fields or csv columns from text.
 * *sed* regular expression replace with the 's/old/new/g' command and global switches
 * Regex '[^0-9].*' match starts with a non-digit
 * sed Delete the first line, which is localhost, and Delete empty lines 
 * Use a pound "#" separator if you need to match a "/" forward slash.,
 
***

### 7.  While and For Loops

These are also useful.  You can make a list of numbers like {1..100}. This is where you realize Bash really IS a 
programming language. Imagine that!  {{< emoji unlock >}}

    for i in {1..100};
       do echo "Some interesting thing one hundred times with an index: $i";
    done

    content = "content coming soon"

    for i in More
        do 
            if [ $RANDOM -le 7000 ]
                then echo "$i groovy $content"
            else echo "$i questionable $content" 
            fi
        done

Ultimately, you will not use very much Bash scripting, unless you want to. But you can get really far, accessing 
Databases and stuff. Thought you should know.

***

###  8. Let us know your favorite commands! 


      read feedback;
      echo $feedback > /dev/null


{{< emoji pause_button >}}
