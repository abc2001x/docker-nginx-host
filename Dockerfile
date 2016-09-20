FROM smebberson/alpine-nginx

ENV NGINX_VERSION 1.11.3

ENV WWW_PATH /www

RUN echo -e  "https://mirrors.tuna.tsinghua.edu.cn/alpine/v3.4/main\nhttps://mirrors.tuna.tsinghua.edu.cn/alpine/v3.4/community">/etc/apk/repositories \
	&& apk add --no-cache python \
	&& apk add --no-cache py-pip \
	&& apk add --no-cache dnsmasq \
	&& pip install -i https://pypi.tuna.tsinghua.edu.cn/simple docker-py \
	&& rm -f /var/cache/apk/*

COPY nginx.vh.default.conf /etc/nginx/conf.d/default.conf

COPY startup.sh /startup.sh
COPY hosts.py /hosts.py


EXPOSE 80 443

CMD ["/startup.sh"]