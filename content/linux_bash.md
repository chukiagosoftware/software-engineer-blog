Title: The Devops Rough cli / Bash Guide
Category: SRE
Tags: DevOps, Bash, Linux, BadEmojis
Date: July 24, 2021

# Uno que otro comando Bash, con bad emojis
#### copylefted from StackOverflow, Google, bottle tested

 :toolbox:

## 1.  Use iterm2 or csshX

The best terminal software will practically do your job for you. Just install, sit back and cash in.

If you don't know what either is, try iterm2 first. If you can find csshX and install it, then all your problems will be solved.

You will have new ones, for sure. :crocodile: but the old ones, gone. Using multiple windows efficiently is almost better than actually automating anything.  It can be lot's of fun, and also very dangerous.

:cactus:

### iterm Shortcuts

    Ctrl-shift-i - Send output to all windows AND tabs (watch out!)
    Ctrl-D - Open a window to the right
    Ctrl-Shift-D - Open a window below
    Ctrl-Shift-Return - toggle current window full screen (fill iterm2 window)
    
 
 *If you need or WANT to have dozens of servers open and send commands to different sub groups, and, and, and....*
 
 :ramen:
 
 [Get csshX](https://formulae.brew.sh/formula/csshx) !!! Then, relax and  get some Ramen if you want.


## 2. top

:dragon:

The Linux *top* command is pretty well documented. 

I like to type "zbx" when I start it, and then capital *I* and *1* to check the number of cpus/cores.

This doesn't do much, but it looks nice.

##### options

    -  *x*:    enable bold for current sort_by column
    -  *z*:     enable color
    -  *Z*:     edit colors
    -  *I*:     Irix mode - detects single cpu
    -  *b*:     toggle solid column/row highlight background
    -  *k*:     kill pid
    -  *m*:     memory ( I think, check the man page)
    -  *l*:     *load* haha but really, just type *uptime*


## 3. find 

#### Find the largest directories or files in a tree

    find . -type d -print0 | xargs -0 du -s | sort -n | tail -15 | cut -f2 | xargs -I{} du -sh {}
    
    
#### Run a command on the findings

    find . -mtime 0 -exec stat '{}' \;


## 4. capture whole packets 

    tcpdump -n -A -q -w /tmp/packet.cap <some filter>
 
 *udp port 5060*   SIP
 *tcp port 443*    nginx
 *tcp port 9093*   Kafka
 
    nc -v -u google.org 5060

read captures in CLI
    
    tcpdump -r | less


## 5. ssh and scp

    scp -o 'ProxyJump user@bastion' -i key user@host:/path/to/remote/file /local/path/file
    
You should always be using secure shell with strong RSA keys and a good key management system. 

Other than that, use your ~/.ssh/config file to set some sensible defaults

    Host *
       UseKeyChain yes
       AddKeysToAgent yes
       IdentityFile ~/.ssh/id_rsa_private_keyfile 

 Add ssh keys to the macOS agent, if that's your OS. If not, it won't work.
 
     ssh-add -l
     ssh-add ~/path/to/my/key
     ssh-add -l
     
  Use a passphrase on your keys. Why not.

## 6. Awk and sed and cut

Learn them well. Don't trust some blaaagh on the internet. 


#### Use *sed* to replace text with regex
 
 Sed allows simple regular expression matching which is what you're going to have to do to fix your mistakes. All of them.
  
    sed -i "s/component_secret =.*/component_secret = \"$JICOFO_SECRET\"/" $PROSODY_HOST_CONF
 
    sed -i "s#some_text/next_one#next_one#g" $INPUT_FILE
     
 On Ubuntu Hirsute 21.04 get a list of only IPv4 addresses.  Can be done in better ways, probably.
 
 
       ip -4 addr | awk '{ print $2 }' | sed 's#/.*##' | sed "s#^[^0-9].*##" | sed '/^$/d' | sed 1d
   
 * Awk is a full programming language, but we can use it to get text fields or csv columns from text.
 * *sed* regular expression replace with the 's/old/new/g' command and global switches
 * Regex '[^0-9].*' match starts with a non-digit
 * sed Delete the first line, localhost and empty lines 
 * Use pound "#" separator if you need to match a "/" forward slash
 
    
## 7.  While and For Loops

These are also useful

    for i in More content coming soon 
        do 
            if [ $RANDOM -le 7000 ]
                then echo "$i groovy"
            else echo "$i questionable" 
            fi
        done

## 8. :leopard:


:pause_button:
