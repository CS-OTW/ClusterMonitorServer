# ClusterMonitorServer

- Download Project

  `$ git clone git@github.com:CS-OTW/ClusterMonitorServer.git`
  `$ cd ClusterMonitorServer`
- [Install Anaconda 3](https://www.anaconda.com/download/#linux)/ConfigEnv
  - add install-directory to ENV
  
     write `PATH=/opt/modules/Anaconda3/bin:$PATH` line into `~/.bash_profile` file
     
    `source .bash_profile`
  - after installation create a environment with python 3.6
  
    `$ conda create -n ClusterMonitorServer python=3.6`
  - install essential package
  
    modify the yml file `prefix` to your env path
    
    Windows System
    
    `$ conda env update -f ClusterMonitorServer-Win.yml`
    
    Linux System
    
    `$ conda env update -f ClusterMonitorServer-Linux.yml`
  - enable env
    
    `$ source activate ClusterMonitorServer`
  - Configure settings.py file

    `vim ClusterMonitorServer/settings.py`
  
   - add you ip address to `ALLOWED_HOSTS`
  
      `ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'ip:port']`
- New a screen

  `$ screen -S ClusterMonitorServer`
- Run

  `$ python manage.py runserver 0.0.0.0:8000`
  deattach screen 
  `Ctrl-A-D`
- Access the website from browser

  http://yourip:yourport
