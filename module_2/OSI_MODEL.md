| Layer        | Function                  | Exists In         | Communication                     | Vanishes When                    |
| ------------ | ------------------------- | ----------------- | --------------------------------- | -------------------------------- |
| Physical     | Bits transmission         | NIC, cables, hubs | Passes raw bits                   | Bits passed up                   |
| Data Link    | Frames, MAC, errors       | NIC, switches     | Encapsulates/decapsulates frames  | Frames delivered to Network      |
| Network      | IP routing, addressing    | Routers, OS       | Encapsulates/decapsulates packets | Packet delivered to Transport    |
| Transport    | Reliable data, ports      | OS                | Segmentation/reassembly           | Segment delivered to Session     |
| Session      | Sessions, connections     | OS + APIs         | Manages session state             | Session ends                     |
| Presentation | Encoding, encryption      | OS + middleware   | Formats data for application      | Data ready for Application Layer |
| Application  | User interface, protocols | User applications | Sends/receives user data          | Data reaches user                |
