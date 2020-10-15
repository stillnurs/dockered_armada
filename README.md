# **Web project "ARMADA" on Django framework.** 
## Using Gunicorn, Nginx and PostgreSQL.



#### After cloning the project,



#### To run the project using Docker:

```
$ docker-compose up --build
$ docker-compose up -d
```



#### Some useful commands to check status of your images and containers:

```
$ docker images  #list of created images
```
Options:
  -a, --all             Show all images (default hides intermediate images)
      --digests         Show digests
  -f, --filter filter   Filter output based on conditions provided
      --format string   Pretty-print images using a Go template
      --no-trunc        Don't truncate output
  -q, --quiet           Only show numeric IDs
  
```
$ docker ps      #list of active containers
```

Options:
  -a, --all             Show all containers (default shows just running)
  -f, --filter filter   Filter output based on conditions provided
      --format string   Pretty-print containers using a Go template
  -n, --last int        Show n last created containers (includes all states) (default -1)
  -l, --latest          Show the latest created container (includes all states)
      --no-trunc        Don't truncate output
  -q, --quiet           Only display numeric IDs
  -s, --size            Display total file sizes



#### To drop Docker containers:

```
$ docker rm [OPTIONS] CONTAINER [CONTAINER...]
```

Options:
  -f, --force     Force the removal of a running container (uses SIGKILL)
  -l, --link      Remove the specified link
  -v, --volumes   Remove anonymous volumes associated with the container



#### To drop Docker images:

```
$ docker rmi [OPTIONS] IMAGE [IMAGE...]
```

Options:
  -f, --force      Force removal of the image
      --no-prune   Do not delete untagged parents
      


#### To stop and remove containers created by using `up` :

```
$ docker-compose down [options]
```

By default, the only things removed are:

- Containers for services defined in the Compose file
- Networks defined in the `networks` section of the Compose file
- The default network, if one is used

Options:
    --rmi type              Remove images. Type must be one of:
                              'all': Remove all images used by any service.
                              'local': Remove only images that don't have a
                              custom tag set by the `image` field.
    -v, --volumes           Remove named volumes declared in the `volumes`
                            section of the Compose file and anonymous volumes
                            attached to containers.
    --remove-orphans        Remove containers for services not defined in the
                            Compose file
    -t, --timeout TIMEOUT   Specify a shutdown timeout in seconds.
                            (default: 10)





#### To stop active container:

```
$ docker stop [OPTIONS] CONTAINER [CONTAINER...]
```

 Options:
  -t, --time int   Seconds to wait for stop before killing it (default 10)



#### To start container back:

```
$ docker start [OPTIONS] CONTAINER [CONTAINER...]
```

Options:
  -a, --attach                  Attach STDOUT/STDERR and forward signals
      --checkpoint string       Restore from this checkpoint
      --checkpoint-dir string   Use a custom checkpoint storage directory
      --detach-keys string      Override the key sequence for detaching a container
  -i, --interactive             Attach container's STDIN




#### To restart container:

```
$ docker restart [OPTIONS] CONTAINER [CONTAINER...]
```

Options:
  -t, --time int   Seconds to wait for stop before killing the container (default 10)




#### To enter the application interactively using `bash` console:

```
$ docker exec -it [CONTAINER ID] bash
```






     
##### For more useful commands check https://docs.docker.com/engine/reference/commandline/docker/
