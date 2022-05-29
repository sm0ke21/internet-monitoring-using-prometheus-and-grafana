import re
import requests
import sys

def main():
    if len(sys.argv) != 3:
        sys.exit(-1)

    txt = open(sys.argv[1]).read()
    PROJECTNAME = sys.argv[2]
    PROMETHEUS_PUSHGATEWAY = 'http://prometheus-pushgateway.monitoring.svc.cluster.local:9091/metrics/job/%s' % PROJECTNAME

    regex_latency = "Latency: [\s\t]+([\d\.]+)\s{1}([^\s]+)"
    regex_download = "Download: [\s\t]+([\d\.]+)\s{1}([^\s]+)"
    regex_upload = "Upload: [\s\t]+([\d\.]+)\s{1}([^\s]+)"
    regex_packet_loss = "Packet Loss: [\s\t]+([\d\.]+)%"

    results = re.search(regex_latency, txt)
    latency_line = '%s_net_latency %s' % (PROJECTNAME, results.group(1))
    
    results = re.search(regex_download, txt)
    download_line = '%s_net_download %s' % (PROJECTNAME, results.group(1))
    
    results = re.search(regex_upload, txt)
    upload_line = '%s_net_upload %s' % (PROJECTNAME, results.group(1))
    
    results = re.search(regex_packet_loss, txt)
    packet_loss_line = '%s_net_loss %s' % (PROJECTNAME, results.group(1))

    final_line = """
{latency_line}
{download_line}
{upload_line}
{packet_loss_line}
""".format(latency_line=latency_line, download_line=download_line, upload_line=upload_line, packet_loss_line=packet_loss_line)
    result = requests.post(PROMETHEUS_PUSHGATEWAY, data=final_line)

if __name__ == "__main__":
    main()