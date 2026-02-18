import asyncio
import logging

import grpc
import pb.post_pb2 as pb2
import pb.post_pb2_grpc as pb2_grpc

class Greeter(pb2_grpc.GreeterServicer):
    async def GetTitle(self, request, context):
        post_id=request.post_id
        names={1:"Ad", 2:"May", 3:"Bob"}
        name=names.get(post_id, f"Пользователь_#{post_id}")
        
        return pb2.UserNameReply(message=name)
    
async def serve()->None:
    server=grpc.aio.server()
    pb2_grpc.add_GreeterServicer_to_server(Greeter(),server)
    listen_addr="[::]:50051"
    server.add_insecure_port(listen_addr)
    await server.start()
    logging.info("Starting server in %s", listen_addr)
    await server.wait_for_termination()

def main():
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())