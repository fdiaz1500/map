# MAP

Move and Pivot


## INTRO

An adventure game.

## USAGE
On Linux or Mac:

    $ cd /path/to/this/directory
    $ chmod +x run-linux-or-mac.sh
    $ ./run-linux-or-mac.sh

On Windows:

    $ cd /path/to/this/directory
    $ ./run-windows.bat


## PROJECT SNAPSHOT


```
map/
├── docs
│   └── guide.pdf
├── README.md
├── run-linux-or-mac.sh
├── run-windows.bat
└── src
    ├── game.py
    ├── items.py
    └── player.py

3 directories, 7 files
```


## HTTP SERVER

Question:   Why would I want to run this as a http server?

Answer:     To play this game over the web. 



#### USAGE

```
Step 1:  Execute the following in your terminal:

    $  cd /path/to/this/directory
    $  python3 web_http.py


Step 2:  Verify the following result

    Starting web server on port 8000...


Step 3:  Visit the following URL in a browser

    http://localhost:8000


Step 4:  Verify the following message

    "Welcome to the web application"
```



