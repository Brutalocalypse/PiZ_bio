# PiZ_bio ##

# For Raspberry Pi
RPi SSH Setup (need to setup SFTP on Pi in order to push file from Pi to Windows PC)
  in terminal: ssh-keygen.exe (generate a public ssh key)
    in .ssh directory - ~/.ssh
    pass this key onto Windows in the Authorized Key file under "ssh" under Username
  Make a ssh config for better use
    sudo nano config (information for connecting)
      in .ssh directory (~/.ssh)
      
      Host Name
        Hostname ipAddress
        User Username
        
   Test via command line on Pi
    scp present_directory/filename name(from ssh.config):remote_path/filename
    
Connecting to new remote client PC
  will have to erase cache each time even though fingerprint key has been input!!!!
  ssh-keygen -f "/home/pi/.ssh/known_hosts" -R 192.168.137.1

# For Windows Client Machines
Windows SSH Setup
  Download the latest OpenSSH for Windows binaries (package OpenSSH-Win32.zip)
  Extract the package to C:\Program Files\OpenSSH
  As the Administrator, install SSHD and ssh-agent services: 
  powershell.exe -ExecutionPolicy Bypass -File install-sshd.ps1
  As the Administrator, generate server keys by running the following commands from the C:\Program Files\OpenSSH: 
  .\ssh-keygen.exe -A
  Open a port for the SSH server in Windows Firewall:
  Either run the following PowerShell command (Windows 8 and 2012 or newer only), as the Administrator: 
  New-NetFirewallRule -Protocol TCP -LocalPort 22 -Direction Inbound -Action Allow -DisplayName SSH
  or go to Control Panel > System and Security > Windows Firewall > Advanced Settings > Inbound Rules and add a new rule for port 22.
  To allow a public key authentication, as an Administrator, from C:\Program Files\OpenSSH, run: 
  powershell.exe -ExecutionPolicy Bypass -File install-sshlsa.ps1 
  and restart the machine
  Start the service and/or configure automatic start:
  Go to Control Panel > System and Security > Administrative Tools and open Services. Locate SSHD service.
  If you want the server to start automatically when your machine is started: Go to Action > Properties. In the Properties dialog, change Startup type to Automatic and confirm.
  Start the SSHD service by clicking the Start the service.

  for further instructions
  https://winscp.net/eng/docs/guide_windows_openssh_server#installing_sftp_ssh_server

Operation
  SSH Port Forward for Windows Machines
    # Advanced Firewall Settings -> Inbound Rules, port 22
    -- This is needed to allow the file transfer to occur, more specifically enable a SSH connection
  GUI Application
    # Visual Studio or the Application_file.exe

Notes
  TCP/IP port 50525
    # Windows Firewall appears to not require to have this port opened
  SSHPASS and SSH Keys
    # SSH Keys should be used in this implementation. At some point there was a bug with key authentication
    # that was never resolved as focus had to be diverted towards other elements. The quick-fix was
    # to use SSHPASS but I recommended against using and storing passwords.

Debugging
  Ping Tests
    # For Windows Machines, must enable Inbound Rules "File and Printer Sharing (Echo Request - ICMPv4-In)"
    # in Advanced Firewall Settings (Private and Domain, shouldn't need Public)
  Running Python Scripts
    # Install Python 2.7
    # Add Python 2.7 to Environment Variables PATH
    -- Variable name: Path, Variable value: C:\Python27
  Testing GUI
    # Install Visual Studio
  Code hangs at File Transfer
    # Ensure Port 22 is Forwarded in Windows Firewall Advanced Settings
    -- if Port 22 is an Enabled Inbound Rule, proceed to the following steps
    
    # Found that the authentication can fall and can be solved by running SCP without sshpass -p "password"
    -- SFTP.py -> sshpass -p 'password' scp %s Brutalocalypse@192.168.137.1:Desktop
    -- in terminal, "scp source_filename Remote_Username@ip_address:remote_path/remote_filename"
      * source file path not needed if running in same working directory
      * remote_filename not needed if wanting to keep the original name
    # Running the above will trigger a warning about a unknown identify compared to the known_hosts file
    # Accept/Yes, then run the suggested command to clear the known_hosts file
    # Now run the command with the sshpass portion
    -- in terminal, "sshpass -p 'password' scp source_filename Remote_Username@ip_address:remote_path/remote_filename"
  
