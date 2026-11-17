import ssl
import socket

def check_cert_expiry(hostname):
    ctx = ssl.create_default_context()
    with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
        s.connect((hostname, 443))
        cert = s.getpeercert()
        exp_date_str = cert['notAfter']
        print(f'Host: {hostname} | Certificate Valid Until: {exp_date_str}')

if __name__ == '__main__':
    check_cert_expiry('google.com')
