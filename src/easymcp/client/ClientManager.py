from typing import Awaitable
from easymcp.client.ClientSession import ClientSession


class ClientManager:
    """ClientManager class"""

    default_list_roots_callback: Awaitable | None = None
    default_list_sampling_callback: Awaitable | None = None

    sessions: list[ClientSession]

    def __init__(self):
        pass

    async def add_server(self):
        """add a server to the manager"""
        raise NotImplementedError
    
    async def remove_server(self):
        """remove a server from the manager"""
        raise NotImplementedError
    
    async def list_servers(self):
        """list available servers"""
        raise NotImplementedError
    
    async def list_tools(self):
        """list tools on all servers"""
        raise NotImplementedError
    
    async def call_tool(self, name: str, args: dict):
        """call a tool"""
        raise NotImplementedError
    
    async def list_resources(self):
        """list resources on all servers"""
        raise NotImplementedError
    
    async def read_resource(self, uri: str):
        """read a resource"""
        raise NotImplementedError
    
    async def list_prompts(self):
        """list prompts on all servers"""
        raise NotImplementedError
    
    async def read_prompt(self, name: str, args: dict):
        """read a prompt"""
        raise NotImplementedError
    
    # callbacks
    async def register_roots_callback(self, callback: Awaitable):
        """register a callback for roots"""
        self.default_list_roots_callback = callback
        for session in self.sessions:
            await session.register_roots_callback(callback)

    async def register_sampling_callback(self, callback: Awaitable):
        """register a callback for sampling"""
        self.default_list_sampling_callback = callback
        for session in self.sessions:
            await session.register_sampling_callback(callback)