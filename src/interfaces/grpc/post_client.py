import asyncio
import logging

import grpc
import pb.post_pb2 as pb2
import pb.post_pb2_grpc as pb2_grpc

async def run()->None:
    async with grpc.aio.insecure_channel("localhost:50051") as ch:
        async_stub=pb2_grpc.GreeterAsyncStub(ch)
        try:
            response=await async_stub.GetUserName(
                pb2.PostRequest(post_id=1)
            )
            print(f"Получил от сервера {response.message}")
        except grpc.RpcError as e:
            print(f"Ответ не получен {e.code()} - {e.details()}")
    #     response=await async_stub.GetUserName(pb2.PostRequest(post_id=1))
    # print("Greeter client received: "+response.message)

def main():
    logging.basicConfig()
    asyncio.run(run())