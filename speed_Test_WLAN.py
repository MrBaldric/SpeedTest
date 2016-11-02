import time, subprocess

#carry out speedtest every 30mins and then pipe results with time stamp to a log file.as
#ensure speedtest-cli installed via pip
#sudo apt-get install python-pip
#sudo pip install speedtest-cli

#speedtest-cli --list will show available worldwide servers
#speedtest-cli --server 2604   will use the server ID for brisbane telstra the test.
#Server id are shown in the server list from above command

#speedtest-cli --help  will give more info on speedtest-cli

#/usr/local/bin/speedtest-cli  this maybe needed to make workin crontab -e

def speedTest():
    cmd = ['speedtest-cli','--server','2604']
    proc =  subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    speedTestResult = proc.communicate()[0]
    sTR = speedTestResult
    #print sTR
    return sTR

def writeLogfile(dataDict):
    timestamp = time.strftime("%b %d %Y %H:%M:%S hrs",time.localtime((time.time())))
    openfile = file("speedTest.log",'a')
    TestStartRef = dataDict.find('Testing')
    TestEndRef = dataDict.find(')...')
    Testing = dataDict[TestStartRef:TestEndRef + 2].rstrip("\n")

    HostStartRef = dataDict.find('Hosted')
    HostEndRef = dataDict.find('ms')
    Hosted = dataDict[HostStartRef:HostEndRef + 3].rstrip("\n")

    DownStartRef = dataDict.find('Download:')
    DownEndRef = dataDict.find('Mbit/s')
    DownSpeed = dataDict[DownStartRef:DownEndRef + 7].rstrip("\n")

    UpStartRef = dataDict.find('Upload:')
    UpSpeed = dataDict[UpStartRef:].rstrip("\n")
    print "{},{},{},{},{}\n".format(timestamp,Testing, Hosted, DownSpeed, UpSpeed)
    openfile.write("{},{},{},{},{}\n".format(timestamp,Testing, Hosted, DownSpeed, UpSpeed))
    openfile.close()

results = speedTest()
writeLogfile(results)