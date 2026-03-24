import asyncio
import logging

import grpc
from src.interfaces.grpc.pb import post_pb2 as pb2
from src.interfaces.grpc.pb import post_pb2_grpc as pb2_grpc

async def run()->None:

    async with grpc.aio.insecure_channel("localhost:50051") as ch:
        stub=pb2_grpc.GreeterStub(ch)
        try:
            response=await stub.GetUserName(
                pb2.PostRequest(post_id=1)
            )
            print(f"Получил от сервера {response.user_name}")
            # return(response.message)
        except grpc.RpcError as e:
            print(f"Ответ не получен {e.code()} - {e.details()}")
            # return f"Ответ не получен {e.code()} - {e.details()}"
    #     response=await async_stub.GetUserName(pb2.PostRequest(post_id=1))
    # print("Greeter client received: "+response.message)

def main():
    logging.basicConfig()
    asyncio.run(run())

if __name__=="__main__":
    main()