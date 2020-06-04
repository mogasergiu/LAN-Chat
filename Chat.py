#!/usr/bin/python3

import ServerUtils as srv

server = srv.ChatServer(port = 2399)
server.server.listen(2)
thrd = srv.thr(target = server.accept_connection)
thrd.start()
thrd.join()
server.server.close()
