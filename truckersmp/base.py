from typing import Union
import urllib3
import json
from .baseExceptions import ConnectionError, NotFoundError, RateLimitError

http = urllib3.PoolManager()

class TruckersMP:
    def __init__(self):
        self._root_url = "https://api.truckersmp.com/v2"

    def __checkError(self, errorCode) -> Union[bool, Exception]:
        if errorCode in [400, 401, 403, 502, 503, 504]:
            raise ConnectionError()
        elif errorCode == 404:
            raise NotFoundError()
        elif errorCode == 429:
            raise RateLimitError()

    def __decode_data(self, req) -> dict:
        return json.loads(req.data.decode("utf-8"))

    # In Game
    def get_player(self, player_id: Union[int, str]) -> dict:
        """
        Fetches a player using the player ID given.
        """
        req = http.request("GET", f"{self._root_url}/player/{player_id}")
        self.__checkError(req.status)

        return self.__decode_data(req)
    
    
    def get_bans(self, player_id: Union[int, str]) -> dict:
        """
        Fetches bans for a given player using the player ID given.
        """
        
        req = http.request("GET", f"{self._root_url}/bans/{player_id}")
        self.__checkError(req.status)

        return self.__decode_data(req)


    def get_servers(self) -> dict:
        """
        Fetches server information for the mod.
        """
        req = http.request("GET", f"{self._root_url}/servers")
        self.__checkError(req.status)

        return self.__decode_data(req)


    def get_in_game_time(self) -> dict:
        """
        Fetches in-game time for all servers (Note that the time is synchronised across all servers).
        """
        req = http.request("GET", f"{self._root_url}/game_time")
        self.__checkError(req.status)

        return self.__decode_data(req)

    def get_version(self) -> dict :
        """
        Fetches the version that the mod is running on.
        """
        req = http.request("GET", f"{self._root_url}/version")
        self.__checkError(req.status)

        return self.__decode_data(req)

    # Events
    def get_events(self) -> dict:
        """
        Fetches all events happening from the events page.
        """
        req = http.request("GET", f"{self._root_url}/events")
        self.__checkError(req.status)

        return self.__decode_data(req)


    def get_event(self, event_id: Union[int, str]) -> dict:
        """
        Searches for a certain event using the given event ID.
        """
        req = http.request("GET", f"{self._root_url}/events/{event_id}")
        self.__checkError(req.status)

        return self.__decode_data(req)
        

    # VTC
    def get_vtc_index(self) -> dict:
        """
        Returns the index page for all VTCs in JSON format. Refer to https://truckersmp.com/vtc
        """
        req = http.request("GET", f"{self._root_url}/vtc/")
        self.__checkError(req.status)

        return self.__decode_data(req)

    def get_vtc(self, vtc_id: Union[int, str]):
        """
        Fetches all available information about a given VTC.
        """
        reqGeneral = http.request("GET", f"{self._root_url}/vtc/{vtc_id}")
        reqNews = http.request("GET", f"{self._root_url}/vtc/{vtc_id}/news/")
        reqRoles = http.request("GET", f"{self._root_url}/vtc/{vtc_id}/roles/")
        reqMembers = http.request("GET", f"{self._root_url}/vtc/{vtc_id}/members/")
        reqEvents = http.request("GET", f"{self._root_url}/vtc/{vtc_id}/events/")
        reqData = [reqGeneral, reqNews, reqRoles, reqMembers, reqEvents]
        
        for req in reqData:
            self.__checkError(req.status)
            
        reqData = list(map(lambda req: self.__decode_data(req), reqData))

        vtc_info = {"general": reqData[0].get("response"), "news": reqData[1].get("response"), "roles": reqData[2].get("response"), "members": reqData[3].get("response"), "events": reqData[4].get("response")}
        return vtc_info

    def get_vtc_member(self, vtc_id: Union[int, str] , member_id: Union[int, str]) -> dict:
        """
        Fetches a member from a given VTC.
        """
        req = http.request("GET", f"{self._root_url}/vtc/{vtc_id}/member/{member_id}")
        self.__checkError(req.status)

        return self.__decode_data(req)

    def get_vtc_event(self, vtc_id: Union[int, str] , event_id: Union[int, str]) -> dict:
        """
        Fetches a member from a given VTC.
        """
        req = http.request("GET", f"{self._root_url}/vtc/{vtc_id}/events/{event_id}")
        self.__checkError(req.status)

        return self.__decode_data(req)

    def get_rules(self):
        """
        Fetches the rules in JSON Format. Available at: https://truckersmp.com/rules
        """
        req = http.request("GET", f"{self._root_url}/rules/")
        self.__checkError(req.status)

        return self.__decode_data(req)