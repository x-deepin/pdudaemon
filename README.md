With this branch, you can change the power state of devices connected throught fpanel controller.

First, add a new PDU to `/etc/lavapdu/lavapdu.conf`
```
        [...]
        "127.0.0.1": {
            "driver": "fpanelctl"
        }
    }
}
```

Restart the PDU daemon
```
$ sudo systemctl restart lavapdu-listen.service lavapdu-runner.service
```

Then, you can change the power state of device 103 with the command below
```
# --daemon 127.0.0.1: where PDU daemon is running
# --hostname 127.0.0.1: where PDU (which is the actual conroller of power state) is running. Since fpanel controller has no
#                       network interface, the 127.0.0.1 is just a key to filter PDU from `/etc/lavapdu/lavapdu.conf`
$ pduclient --daemon 127.0.0.1 --hostname 127.0.0.1 --command [on|reboot|off] --port 3
```
