import dns.query
import dns.update
import dns.tsigkeyring



def add_record(server,keyname,algo,secret,zone,record_type,record_name,record_value):
    keyring = dns.tsigkeyring.from_text({keyname : secret})
    update = dns.update.Update(zone,keyring=keyring,keyalgorithm=algo)
    update.add(record_name,300,record_type,record_value)
    response = dns.query.tcp(update,server)
    print(response)

server = "127.0.0.1"
keyname = ""
algo = "hmac-5"
secret = "secret"
