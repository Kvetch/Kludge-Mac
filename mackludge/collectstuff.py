import subprocess, os
import variables as var
import logger as log
import cmdlnr as cmdlnr
import dirhandler as dirhandlr

class CollectStuff(object):

    def __init__(self):
        self = self
        dir = dirhandlr.DirHandler()
        dir.create_dir()
        self.collector()
        
# RE-ORDER CMDS TO COLLECT IN ORDER OF VOLATILITY
# Procs, SysInfo, Network, Memory, Logs, Browser, TLN, Software
    def collector(self):
        command = cmdlnr.CmdLnr()
        # caffeinate -u -t 3600
        # caffeinate -s mac-kludge.py
        command.run_acmd("ps -ef", "Procs/ps.txt")
        command.run_acmd("crontab -l", "Procs/crontab.txt")
        command.run_acmd("sw_vers", "Software/sw_vers.txt")
        command.run_acmd("uname -av", "SysInfo/uname.txt")
        command.run_acmd("date", "SysInfo/date.txt")
        command.run_acmd("ulimit", "SysInfo/ulimit.txt")
        command.run_acmd("uptime", "SysInfo/uptime.txt")
        command.run_acmd("hostinfo", "SysInfo/HostInfo.txt")
        command.run_acmd("nvram -p", "SysInfo/Nvram.txt")
        command.run_acmd("env", "SysInfo/env.txt")
        command.run_acmd("systemsetup -getcomputername", "SysInfo/SystemSetup.txt")     
        command.run_acmd("systemsetup -getdate", "SysInfo/SystemSetup.txt")
        command.run_acmd("systemsetup -gettimezone", "SysInfo/SystemSetup.txt")
        command.run_acmd("systemsetup -getusingnetworktime", "SysInfo/SystemSetup.txt")
        command.run_acmd("systemsetup -getnetworktimeserver", "SysInfo/SystemSetup.txt")
        command.run_acmd("systemsetup -getsleep", "SysInfo/SystemSetup.txt")
        command.run_acmd("systemsetup -getwakeonmodem", "SysInfo/SystemSetup.txt")
        command.run_acmd("systemsetup -getwakeonnetworkaccess", "SysInfo/SystemSetup.txt")
        command.run_acmd("systemsetup -getrestartpowerfailure", "SysInfo/SystemSetup.txt")
        command.run_acmd("systemsetup -getrestartfreeze", "SysInfo/SystemSetup.txt")
        command.run_acmd("systemsetup -getallowpowerbuttontosleepcomputer", "SysInfo/SystemSetup.txt")
        command.run_acmd("systemsetup -getremotelogin", "SysInfo/SystemSetup.txt")
        command.run_acmd("systemsetup -getremoteappleevents ", "SysInfo/SystemSetup.txt")
        command.run_acmd("printf \"`echo StartUpDisk` `systemsetup -getstartupdisk`\n\"", "SysInfo/SystemSetup.txt")
        command.run_acmd("systemsetup -getwaitforstartupafterpowerfailure", "SysInfo/SystemSetup.txt")
        command.run_acmd("systemsetup -getdisablekeyboardwhenenclosurelockisengaged", "SysInfo/SystemSetup.txt")
        command.run_acmd("systemsetup -getkernelbootarchitecturesetting", "SysInfo/SystemSetup.txt")
        command.run_acmd("ifconfig -Lmavr", "Network/ipconfig.txt")
        command.run_acmd("netstat -AabisLmnvx", "Network/netstat.txt")
        command.run_acmd("netstat -rn", "Network/routing.txt")
        command.run_acmd("dscacheutil -q host", "Network/dnscache-host.txt")
        command.run_acmd("dscacheutil -q mount", "Network/dnscache-mount.txt")
        command.run_acmd("dscacheutil -q protocol", "Network/dnscache-protocol.txt")
        command.run_acmd("dscacheutil -q rpc", "Network/dnscache-rpc.txt")
        command.run_acmd("dscacheutil -q service", "Network/dnscache-service.txt") # Hanging
        command.run_acmd("dscacheutil -q user", "SysInfo/Users-Info.txt")
        command.run_acmd("dscacheutil -q group", "SysInfo/Groups-Info.txt")
        command.run_acmd("dscacheutil -q configuration", "Network/dnscache-configuration.txt")
        command.run_acmd("arp -a", "Network/arp.txt") # Hanging
        command.run_acmd("lsvfs", "SysInfo/virtualfs.txt")
        command.run_acmd("lsof", "Files/lsof-full.txt") # Hanging
        command.run_acmd("lsof|grep -i established", "Network/lsof-estab.txt")
        command.run_acmd("networksetup -getinfo Wi-Fi", "Network/WiFi-Info.txt") # Not supported
        command.run_acmd("networksetup -getinfo Ethernet", "Network/Ethernet-Info.txt") # Not supported
        command.run_acmd("networksetup -getinfo AirPort", "Network/Airport-Info.txt") # Not supported
        command.run_acmd("networksetup -listnetworkserviceorder", "Network/NetworkOrder.txt") # Not supported
        command.run_acmd("networksetup -listallnetworkservices", "Network/NetworkServices.txt") # Not supported
        command.run_acmd("networksetup -listallhardwareports", "Network/Network-Hardware.txt") # Not supported
        command.run_acmd("networksetup -getwebproxy Wi-Fi", "Network/WiFi-Proxy.txt") # Not supported
        command.run_acmd("networksetup -getsecurewebproxy Wi-Fi", "Network/WiFi-Proxy.txt") # Not supported
        command.run_acmd("networksetup -getwebproxy Ethernet", "Network/Ethernet-Proxy.txt") # Not supported
        command.run_acmd("networksetup -getsecurewebproxy Ethernet", "Network/Ethernet-Proxy.txt") # Not supported
        command.run_acmd("networksetup -getairportnetwork Wi-Fi", "Network/WiFi-Airport.txt") # Not supported
        command.run_acmd("networksetup -listpreferredwirelessnetworks en1", "Network/WiFi-PreferredNetworks.txt") # Not supported
        command.run_acmd("networksetup -getnetworkserviceenabled Ethernet", "Network/Enabled-Networks.txt") # Not supported
        command.run_acmd("networksetup -getnetworkserviceenabled Wi-Fi", "Network/Enabled-Networks.txt") # Not supported
        command.run_acmd("networksetup -getnetworkserviceenabled FireWire", "Network/Enabled-Networks.txt") # Not supported
        command.run_acmd("networksetup -getnetworkserviceenabled Ethernet", "Network/Network-MTU.txt") # Not supported
        command.run_acmd("networksetup -getnetworkserviceenabled Wi-Fi", "Network/Network-MTU.txt") # Not supported
        command.run_acmd("networksetup -getcurrentlocation Ethernet", "Network/Network-Locations.txt") # Not supported
        command.run_acmd("networksetup -getcurrentlocation Wi-Fi", "Network/Network-Locations.txt") # Not supported
        command.run_acmd("networksetup -listlocations Ethernet", "Network/Network-Locations.txt") # Not supported
        command.run_acmd("networksetup -listlocations Wi-Fi", "Network/Network-Locations.txt") # Not supported
        command.run_acmd("diskutil list", "SysInfo/DiskUtil.txt")
        command.run_acmd("ls /dev/disk*", "SysInfo/MountedDisks.txt")   
        command.run_acmd("dscl . list /users", "SysInfo/Users.txt")
        command.run_acmd("dscl . list /groups", "SysInfo/Groups.txt")
        command.run_acmd("dscl . readall /users", "SysInfo/Users-Readall.txt")
        command.run_acmd("dscl . readall /groups", "SysInfo/Groups-Readall.txt")
        command.run_acmd("mdutil -savp", "SysInfo/SpotLight-Info.txt")
        command.run_acmd("security list-keychains", "SysInfo/KeyChains.txt")
        command.run_acmd("security show-keychain-info", "SysInfo/KeyChainsInfo.txt") # Walk the list prior
        command.run_acmd("security find-generic-password", "SysInfo/Security-Generic-Passwords.txt")
        command.run_acmd("security find-internet-password", "SysInfo/Security-Internet-Passwords.txt")
        command.run_acmd("security find-certificate", "SysInfo/Security-Certificates.txt")
        command.run_acmd("security find-identity", "SysInfo/Security-Identity.txt")
        command.run_acmd("security dump-trust-settings", "SysInfo/Security-dump-trust-settings.txt")
        command.run_acmd("security user-trust-settings-enable", "SysInfo/Security-user-trust-settings-enable.txt")
        command.run_acmd("security leaks", "SysInfo/Security-leaks.txt")
        # command.run_acmd("security get-identity-preference", "SysInfo/Security-get-identity-preference.txt")
        # command.run_acmd("security verify-cert", "SysInfo/Security-verify-cert.txt")
        
        for r,d,f in os.walk("/dev"): # Find disks
            for files in f:
                if files.startswith("disk"):
                    _filename = os.path.join(r, files)
                    command.run_acmd("diskutil info " + _filename, "SysInfo/" + files + "-info.txt")
                    command.run_acmd("diskutil list " + _filename, "SysInfo/" + files + "-list.txt")
                    # command.run_acmd("pdisk " + _filename + " -dump", "SysInfo/" + files + "-Partition.txt")
                    command.run_acmd("hdiutil pmap " + _filename, "SysInfo/" + files + "-info2.txt")
                    
#       command.run_acmd("diskutil disk0", "SysInfo/Disk0-Info.txt")
#       command.run_acmd("pdisk /dev/disk0 -dump", "SysInfo/Disk0-Partition.txt")
#       command.run_acmd("hdiutil pmap /dev/disk0", "SysInfo/Disk0-Info2.txt")
        command.run_acmd("ls -lrth /System/Library/StartupItems/", "Procs/Startup2.txt")
        command.run_acmd("grep -r USBMC /var/log/system.log*", "SysInfo/USB-Info.txt") # OS X 10.8 --> /private/var/log/system.log + bziped -->bzgrep -- three values: 0x90c 0x1000 0x1100 are the Vendor ID, Product ID and the DeviceRelease number: http:/www.linux-usb.org/usb.ids
                
        if var.level == 2:
            command.run_acmd("ls -Rah / | grep ':$' | sed -e 's/:$//' -e 's/[^-][^\/]*\//--/g' -e 's/^/ /' -e 's/-/|/'", "Files/DirListing.txt")
            command.run_acmd("sysctl -a", "SysInfo/KernVars.txt") # Iterate through
            command.run_acmd("ls -liRhT /", "Files/file-listing.txt")
            command.run_acmd("find / -mtime -10 -ls", "Files/files-last10days.txt")
            command.run_acmd("ls -liRhT /|sort -n", "Files/file-listing-inode-sorted.txt")
            # command.run_acmd("qlmanage -", "Files/files.txt") # Text output???
            command.run_acmd("launchctl list", "Procs/Startup.txt")
            command.run_acmd("system_profiler -detaillevel full", "SysInfo/SystemInfo.txt")
            command.run_acmd("system_profiler -detaillevel full -xml", "SysInfo/SystemInfo.spx")
            # command.run_acmd("system_profiler -detaillevel full individual DataTypes", "SysInfo/DataTypes.txt")
            command.run_acmd("ioreg -c -i", "DeviceInfo.txt")
            command.run_acmd("ipfw list", "Network/IPFW.txt")
            command.run_acmd("plutil -p /Library/Preferences/com.apple.alf.plist", "Network/Firewall.txt")
            command.run_acmd("pmset -g everything", "SysInfo/PowerSettings.txt")  # pmset hanging for some
            for r,d,f in os.walk("/Users"): # Find certain types of file info - dmg, plist...
                for files in f:
                    if files.endswith(".dmg"):
                        _filename = os.path.join(r, files)
                        command.run_acmd("hdiutil imageinfo " + _filename, "Software/" + files + "-info.txt")
                    elif files.endswith(".plist"):
                        _filename = os.path.join(r, files)
                        command.run_acmd("plutil -p " + _filename, "Software/" + files + "-info.txt")
                    # elif: # Add runcmd to each if
                        # _filename = os.path.join(r, files)
                        # command.run_acmd("GetFileInfo" + _filename, "Software/DetailedFile-info.txt")
            # command.run_acmd("for f in $(find /Users -name '*.dmg' 2>/dev/null) ;do hdiutil imageinfo $f && echo && echo && echo; done", "Software/DMG-Info.txt")
            # command.run_acmd("for f in $(find /Users -name '*.plist' 2>/dev/null) ;do plutil -p $f && echo && echo && echo; done", "Software/Plist-Info.txt")     