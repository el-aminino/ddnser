import dns.query
import dns.tsigkeyring
import dns.update
import dns.message
import dns.rdatatype


zone = "test.com"
server = "127.0.0.1"

def list_zone(zone,server) :
    query = dns.message.make_query(zone , dns.rdatatype.ANY)
    response  = dns.query.tcp(query,server)
    print(response)

list_zone(zone,server)
