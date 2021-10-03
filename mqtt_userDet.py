broker_address="192.168.0.58"
port=1882
username="pratyay"
password="26324926"

def connect_status(rc):
    if rc==0 : 
        return "CONNECTION_SUCCESSFULL"
    elif rc==1 :
        return "Connection refused - incorrect protocol version"
    elif rc==2 :
        return "Connection refused - invalid client identifier"
    elif rc==3 :
        return "Connection refused - server unavailable"
    elif rc==4 :
        return "Connection refused - bad username or password"
    elif rc==5 :
        return "Connection refused - not authorised"
    else:
        return "CONNECTION_UNSUCCESSFULL"
