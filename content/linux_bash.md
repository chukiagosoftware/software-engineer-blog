Title: SRE Devops Linux CLI Bash Best Prácticas
Category: SRE
Tags: DevOps, Bash, Linux
Date: July 24, 2021

# Uno que otro comando Bash, y "best prácticas" devops con bad emojis
### copylefted from StackOverflow, Google, etc. Very much a work in progress

:peace:

## 1.  Use iterm2 or csshX

If you don't know what either is, try iterm2 first. If you can find csshX and install it, then all your problems will be solved.

You will have new ones, for sure. :crocodile: but the old ones, gonzo.

### iterm Shortcuts

    Ctrl-shift-i - Send output to all windows AND tabs (watch out!)
    Ctrl-D - Open a window to the right
    Ctrl-Shift-D - Open a window below
    Ctrl-Shift-Return - toggle current window full screen (fill iterm2 window)
    
 
 *If you need or WANT to have dozens of servers open and send commands to different sub groups, and, and, and....*
 
 :relaxed:
 
 [Get csshX](https://formulae.brew.sh/formula/csshx) !!!

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

#### Find the largest directories or files in path 

    find . -type d -print0 | xargs -0 du -s | sort -n | tail -15 | cut -f2 | xargs -I{} du -sh {}
    
 or
    
    -type f, -mtime +20, etc.

## 4. capture whole packets or verify connectivity

    tcpdump -n -A -q -w /tmp/packet.cap <some filter>
 
 *udp port 5060*   SIP
 *tcp port 443*    https
 *tcp port 9093*   Kafka SSL

read captures in CLI
    
    tcpdump -r 

## 5. ssh and scp

    scp -o 'ProxyJump user@bastion' -i key user@host:/path/to/remote/file /local/path/file

## 6. Awk and sed and cut

Learn them better. Don't trust some fool on the internet. 

Please post your findings so I can copy paste.

## 7.  While and For Loops

These are also useful. No, really

    for i in More content coming soon; do
      if [ $RANDOM -le 10000 ] ; then
        echo '$i groovy!'
      else
        echo "$i questionable"
    done



:pause_button:
