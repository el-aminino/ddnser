import dns.query
import dns.tsigkeyring
import dns.update

def insert_dns_record(server,keyname,algo,secret,zone,record_type,record_name,record_value):
    keyring = dns.tsigkeyring.from_text({keyname : secret})
    update = dns.update.Update(zone , keyring=keyring , keyalgorithm=algo)
    update.add(record_name, 300 , record_type, record_value)
    response = dns.query.tcp(update,server)
    print(response)


server = "127.0.0.1"
keyname = "py-key"
secret = 'HF9G7cFMfjOq5U2GCU6KH6iwcjRfW2VnrFJByFO6N5g='
algo = 'hmac-sha256'
zone = "test.com"
record_type = 'A'
record_name = 'amz'
record_value = '192.168.1.228'

insert_dns_record(server=server,keyname=keyname,algo=algo,secret=secret,zone=zone,record_type=record_type,record_name=record_name,record_value=record_value)

