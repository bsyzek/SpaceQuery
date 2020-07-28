# SpaceQuery Script

**Usage:** 

space_query.py [-l --loc] [-p --pass PASSING_LOC] [-pp --people]

**Optional Arguments:**

-l, --loc             
Print the current location of the ISS.

-p, --pass (latitude,longitude)          
Print the passing details of the ISS for a given location. Takes argument of the form (latitude,longitude).

-pp, --people         
Print the details of those people that are currently in space.

**Examples:**

* python space_query.py --loc

    The ISS current location at 2020-07-28 18:01:24 (UTC) is (4.6708, -70.7546).

---
* python space_query.py --pass (38.534718,-105.998901)

    The ISS will be overhead (38.534718, -105.998901) at 2020-07-28 21:11:40 (UTC) for 541 seconds.

    The ISS will be overhead (38.534718, -105.998901) at 2020-07-28 22:47:07 (UTC) for 652 seconds.

    The ISS will be overhead (38.534718, -105.998901) at 2020-07-29 00:25:06 (UTC) for 570 seconds.

    The ISS will be overhead (38.534718, -105.998901) at 2020-07-29 02:03:36 (UTC) for 508 seconds.

    The ISS will be overhead (38.534718, -105.998901) at 2020-07-29 03:40:51 (UTC) for 588 seconds.

---
* python space_query.py --people

    Listed below are the personnel details for each space craft:

        Craft Name: ISS

        Num People: 5

            Chris Cassidy
        
            Anatoly Ivanishin
        
            Ivan Vagner
        
            Doug Hurley
        
            Bob Behnken

