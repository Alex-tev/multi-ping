#!/usr/bin/env python3

from sys import argv
from multiping import MultiPing
from multiping import multi_ping

if __name__ == "__main__":

    argvd = argv[1:]
    addrs = argvd
   #addrs = ["8.8.8.8", "youtube.com", "109.254.249.180"]

    print("sending one round of pings and checking twice for responses")
    mp = MultiPing(addrs)
    mp.send()
    # First attempt: We probably will only have received response from
    # localhost so far. Note: 0.01 seconds is usually a very unrealistic
    # timeout value. 1 second, or so, may be more useful in a real world
    # example
    # Здесь нужно указывать время, если ping  выше этого времени, то ip попадут в no_responses.
    responses, no_responses = mp.receive(0.1)


    respons = {}
    for i in responses:
        x = format(responses[i], '.3f')
        respons[i] = float(x)

    print("   received responses:  %s" % respons)
    print("   no responses so far: %s" % no_responses)
