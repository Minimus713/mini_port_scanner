I would like to create a few different types of port scanners.

1. Vanilla
2. SYN Scan (Half-Open scan)
3. FIN
4. Xmas
5. Sweep Scan

Using a port scanner, I would like to get information about any defenses present like a firewall, any details about the targeted system, what machines are online, applications that might be running, and flagging vulnerabilities.

## The Process

- Been a minute since I worked on any side project. First had to get a new repo set up, that was a pain to do initially but I was able to get SSH auth for GitHub set up and got the repo going.
- Then I have to remember how to write python, it has been a little while since I have had to usee python at all.
- And I also have to figure out what the hell a port scanner is and how to build one.
  So, I figure starting with a simple scan of all ports makes sense. 0-65535, one by one. But, how do I actually ping/connect to a port, and what does that even mean to do that?
- Okay, so I wrote down a bunch of stuff in the README that helps me understand what the heck a port scanner is. Time to actually write some code.
- Was able to write most of the logic for creating a vanilla scan, but for some reason I am having some trouble creating the connection with the socket.
- Back at it today and this time with Chatty. Looks like that issue was not an issue but a misunderstanding. Looks like that means the port is filtered or unresponsive. Additionally, using setdefaulttimeout only works for sockets created after that, so that caused me to not auto-timeout properly.

## The Questions

1. _What is a port scanner?_

```
A port scanner is a tool used to probe different ports on a given machine. It attempts to connect to a given port or range or ports, which provides insights into whether or not the port(s) are open, closed, filtered (blocked by a firewall or something), or otherwise unclear.
```

2. _What are ports?_

```
A port is a virtual point where network connections start and end. Each port is assigned a number ranging from 0 to 65535. Ports allow computeres to easily differentiate between different kinds of traffic over the same internet connection.
In relation to IP addresses, the IP enables a request to find the right computer, but the port allows the request to find the right service on that device.
Ports are considered part of the transport layer, layer 4, of the OSI model because only TCP and UDP can indicate what port a packet should target.
```

3. _What is TCP?_

```
- Transmission Control Protocol
- TCP is connection-oriented
- It keeps track of the segments flowing in/out by assigning numbers to each segment.
- Allows configuration for the data transfer rate
- Has error control mechanisms
- Generally built for reliable data transmission at the cost of performance
- Used when you must get all the data intact and in order (web page, software download)
- Like a phone call: the call is made and a connection is estanlished, you communicate, then you say goodbye and kill the connection.
```

4. _What is UDP?_

```
- User Datagram Protocol
- Connectionless and less reliable, no way to know if a transfer was successful
- Used for less complex communication where the transfer size is smaller
- Commonly used for real-time applications where delays between messages aren't tolerated
- Used when you care more about speed and low latency than reliability (real-time voice, game updates, videos.)
    - Further example: In a game, your character movements are sent over UDP. As you move, sometimes you stutter or rubberband and that is often caused by a packet drop. It isn't worth the performance hit to use TCP for reliability, and the next packet with your most recent position will be delivered soon enough anyway.
- Like a postcard: you write it, send it, and hope it makes it to its destination.
```

5. _How does a port scanner differ when implementing for TCP and UDP?_

```
TCP is going to generally be more simple to implement and have more options for features. TCP gives more straightforward and reliable responses due to the connection dependent nature of the protocol. UDP is a bit more mysterious and is hard to extract reliable information from without further context.
```

6. _What does each response mean?_

```
Open: The port is open and accepting connections. TCP will give a clear acknowledgement whereas UDP generally won't respond (because no established connection is made).

Closed: Both TCP and UDP will generally give an acknowledgement if the port is closed and not filtered. This means the port is not listening.

Filtered: Filtered responses will typically show some kind of unauthorized response indicating that the port is actively listening, but being filtered by a firewall, router, or other filter is blocking your ping.

Unclear: While the above respones are common and clear, there are often other responses that are unclear and cannot be independently used to verify the state of the port.
```

7. _What is a Vanilla scan?_

```
The most basic type of scan, it attempts to scan all ports one at a time. It attempts a full connect scan, meaning it accomplishes the full TCP handshake (SYN --> SYN-ACK --> ACK).
While these are accurate and comprehensive scans, they are easily detected due to full connections being logged by firewalls.
```

8. _What is a SYN scan?_

```
Also referred to as a half-open scan, this type of scan does not send back an ACK flag is it receives a response to its SYN flag. This is important because the scan will indicate just as much information as a vanilla scan, but because the connection is never completed the interaction will not be logged.
```

9. _What is a FIN scan?_

```
A FIN scan will send a FIN flag (end session flag) to port and will sometimes reveal some additional information about a system or the specific port.
```

10. _What is a Xmas scan?_

```
Similar to a FIN scan, a Xmas scan will send random flags to a port to create a nonsensical interation. This can result in a more comprehensive set of responses to determine the systems ports and firewall.
```

11. _What is a Sweep scan?_

```
A sweep scan will ping the same port on a number of different computers on a network. This will reveal what systems on the network are active as part of a preliminary scan.
```
