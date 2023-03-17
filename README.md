# Web Site Temple with Nginx-VueJS (Vuetify)-Flask

## Instructions
Start all services:
```bash
docker compose up -d
```

Check they are running:
```bash
docker compose ps
```

## Creating Front End Prod Updates
As noted at vue/project/README.md the vue dev cli is running ```yarn dev```. We need to run ```yarn build``` to make an initial prod or a new prod version. Shell into vue service.

```bash
docker compose exec vue sh
```
This drops you here:
```bash
/project #
```
Then run the build command:
```bash
/project # yarn build
```


## Prod vs Dev
Nginx is serving a prod build of the UI at ./vue/project/dist. However docker compose is starting a dev vue server running at the same time.

### What is happening?
Port mappings at a glance (defined in docker-compose.yml):
* Nginx (listening on port 80):
  - matches "/" url patterns and sends to prod (./vue/project/dist)
  - matches "/api" url pattern and sends to flask:8080
* Dev Vuetify instance running on port 3000

Summary:
```bash
http://localhost or http://localhost:80 is production front end
http://localhost/api or http://localhost:80/api is flask backend api
http://localhost:3000 is dev front end
```

If running behind vpn or firewall you may need to port forward to your local machine in order to run.

[Port Forward Source](https://ljvmiranda921.github.io/notebook/2018/01/31/running-a-jupyter-notebook/)
```bash
local_port=XXXX
remote_port=YYYY
remote_ip=XX.XXX.XXX.XX
user=ubuntu
ssh -N -f -L localhost:$local_port:$remote_ip:$remote_port $user@$remote_ip
```
Find what's running on specific port so you can kill ssh tunnel when done:
```bash
port=XXXX
ss -tulpn | grep :$port

# kill it
kill <PID from ss command>
```

## Misc notes that helped me put this together
NGINX and FLASK Deploy:
This helped create a prod flask instance with nginx.
[source](https://dev.to/herbzhao/my-docker-learning-journey-edh)

Nginx Notes:
This helped me understand how to deploy both the flask and vue app through nginx
[nginx-notes in general](https://www.plesk.com/blog/various/nginx-configuration-guide/#:~:text=What%20is%20the%20Http%20Block,etc%2Fnginx%2Fnginx.conf)

Vue Notes:
[source](https://vuetifyjs.com/en/getting-started/installation/)
When first starting I had no .vue/project directory. I had to do the following:
```bash
docker run \
  -it \
  --rm \
  -v ./vue/project:/project \
  --entrypoint sh \
  node:lts-alpine3.17
```

Once in container:
```bash
/ # yarn create vuetify
/ # cp -r /vuetify-project/* /project/
/ # exit
```
