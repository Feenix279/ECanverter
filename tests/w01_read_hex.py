import src.w01mgr as mgr
def catch_data(data:bytes):
    print(data.hex())
mgr.return_data = catch_data
mgr.open_socket()
mgr.read_udp()