"""
Paul and Peter have made a long journey since they left Brazil to compete in the
ICPC World Finals, in Phuket, Thailand. They noticed that in each place where they
stopped, they had to adjust their watches because of the time zone.

This way, to plan for upcoming trips, they asked you to create a mobile application
that, given the departure time, travel time and the destination time zone with
respect to the origin, you have to inform the time of arrival of each
flight in the destination.

For example, if they left a place at 10 am for a 4 hour journey to a destination
that is on the east, in a time zone with an extra hour with respect to the time
zone of the starting point, the arrival time will be 10 hours + 4 hours + 1 hour
(due de time zone), i.e. they will arrive at 15 hours. Note that if the calculated
time is 24, its program should print 0 (zero).

Input:
The input contains 3 integers: S (0 ≤ S ≤ 23), T (1 ≤ T ≤ 12) y F (-5 ≤ F ≤ 5),
separated by a space, respectively indicating the time of departure, the travel
time and destination time zone with respect to the origin.

Output:
Print an integer that indicates the local time specified in destination,
as the examples below.
"""

S,T,F=list(map(int,input().split()))
d=S+T+F
if(d>=24):
    d=d-24
if(d<0):
    d=24+d
print(d)