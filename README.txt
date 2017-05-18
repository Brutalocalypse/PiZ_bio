# PiZ_bio

# For Windows Client Machines
Operation
  SSH Port Forward for Windows Machines
    # Advanced Firewall Settings -> Inbound Rules, port 22
    -- This is needed to allow the file transfer to occur, more specifically enable a SSH connection
  Visual Studio or the Application_file.exe

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
    # in Advanced Firewall Settings (Public, maybe Private and Domain)
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
  
