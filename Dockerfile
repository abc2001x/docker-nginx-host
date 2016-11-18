FROM smebberson/alpine-nginx

ENV NGINX_VERSION 1.11.3

ENV WWW_PATH /www

RUN echo -e  "https://mirrors.tuna.tsinghua.edu.cn/alpine/v3.4/main\nhttps://mirrors.tuna.tsinghua.edu.cn/alpine/v3.4/community">/etc/apk/repositories && \
	apk add --no-cache python \
	&& apk add --no-cache py-pip \
	dnsmasq \
	supervisor \
	&& pip install --upgrade pip \
	&& pip install -i https://pypi.tuna.tsinghua.edu.cn/simple docker-py \
	&& rm -f /var/cache/apk/*

COPY nginx.vh.default.conf /etc/nginx/conf.d/default.conf
COPY supervisord.conf /root/supervisord.conf

COPY passport.abc.com.crt /nginx.crt
COPY passport.abc.com.key /nginx.key

COPY hosts.py /hosts.py


EXPOSE 80 443
CMD ["/usr/bin/supervisord","-c","/root/supervisord.conf"]
