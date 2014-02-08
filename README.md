dogemo
======

Such doge.

To run the project in development mode on OSX.

Install [Fig](http://orchardup.github.io/fig/install.html) via docker-osx.

    $ curl https://raw.github.com/noplay/docker-osx/0.7.6/docker-osx > /usr/local/bin/docker-osx
    $ chmod +x /usr/local/bin/docker-osx
    $ docker-osx shell

Now you should be inside the VM shell.  Next install Fig:

    $ sudo pip install -U fig
    
Run ``fig up`` and navigate to ``http://localdocker:8000/``.

