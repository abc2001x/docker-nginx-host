# docker-nginx-host
###a proxy of docker for mac

------

1. set up dnsmasq on your mac

2. set pan-domain in your dnsmasq ( like: address=/golf.com/127.0.0.1)


3. build docker file ,and run image:
		
		docker run -d -v /var/run/docker.sock:/var/run/docker.sock -p 80:80 yourImageName 

4. now , if you run a docker of http server on 80 port, you can visit the new container by container name,(like: YourContainerName.golf.com)


-----------

1.在宿主机mac上,安装并且dnsmasq  (https://blog.netsh.org/posts/mac-os-x-dnsmasq_1762.netsh.html)

2.设置泛解析域名 (如:address=/golf.com/127.0.0.1)

1. 在宿主机mac上,安装并且dnsmasq
2. 设置泛解析域名 (如:address=/golf.com/127.0.0.1)

3. build docker file,然后运行容器:
			
			docker run -d -v /var/run/docker.sock:/var/run/docker.sock -p 80:80 yourImageName 


4. 完毕,然后,当你新建了有80端口http服务的容器,你可以用名字在宿主机访问你的新容器,(like: YourContainerName.golf.com)
