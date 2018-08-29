flow default tcp 192.168.60.63:50194 > 172.16.131.97:36482 (tcp.initialize;);
default > (content:"aaaaaaa";);
default < (content:"bbbbbbbbb";);
default > (tcp.close;);