from asyncio import Queue, Task

import pydantic
from easymcp.client.transports.generic import GenericTransport
from easymcp.vendored import types

async def reader(transport: GenericTransport, queue: Queue[types.JSONRPCMessage]):
    """Read data from the transport and put it in the queue"""

    async def _reader():
        while transport.state == "started":
            data = await transport.receive()
            
            try:
                parsed = types.JSONRPCMessage.model_validate_json(data)
                queue.put_nowait(parsed)
            except pydantic.ValidationError:
                continue

            queue.put_nowait(parsed)

    task = Task(_reader())
    return task

async def writer(transport: GenericTransport, queue: Queue[types.JSONRPCMessage]):
    """Write data from the queue to the transport"""

    async def _writer():
        while transport.state == "started":
            data = await queue.get()
            await transport.send(data.model_dump_json())

    task = Task(_writer())
    return task

