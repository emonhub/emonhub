emonHub
=======

test-wunderground branch
------------------

## UNTESTED MERGE OF SOME OUTDATED CODE FOR ASSESMENT ONLY - NOT FOR USE !!!!!

The 2 conciderations at that time (as I recall) were having to use a "helper thread" so as not to reintroduce the blocking effect caused by a non-responding http request, overcome in the emoncms reporter using threading. And the uncertainty of whether the "weather node" data array should be defined in emonhub.conf nodes section rather than the runtimesettings or not.

Any in-depth development of this will be intended for the next gen of emonhub which uses threading for the interfacers, although it may not take much to "just get it working" with the current version

###the accompanying explanation at that time was

This is the initial draft of a weather api, needs some work still but it does work. requires testing for a while to check data consistency from provider see this forum thread [Weather data in emoncms](http://openenergymonitor.org/emon/node/5633)

the wunderground website has quite a bit of info on the api but not the actual values them selves so I'm currently unsure of their worth, but as a interfacer concept it works reasonably well, the provider can be possibly be changed there seem to be several out there.

This concept could extend to other website "queries" for other data maybe eg sunrise & sunset, tidal or moon phases. may also work for packetgen type applications.

I would like to consider doing something like creating a basic reporter type thread from the interfacers __init__() to prevent the main program being delayed by timeouts, no queue or buffer just a simple repeated request created from the interfacers settings (no reporter or addition settings sections) that stores the json to a holding variable each time it runs (interval set by interfacer) that the interfacer checks during each loop and if not blank, creates the data frame and clears the holding variable.

Currently available datafields are "temp_c", "feelslike_c", "dewpoint_c", "heat_index_c", "windchill_c", "wind_mph", "wind_gust_mph", "visibility_mi", "precip_1hr_metric", "precip_today_metric", "UV", "wind_degrees", "pressure_mb", "pressure_in", "pressure_trend", "relative_humidity", "temp_f", "feelslike_f", "dewpoint_f", "heat_index_f", "windchill_f", "wind_kph", "wind_gust_kph", "visibility_km", "precip_1hr_in", "precip_today_in"

Which any number can be strung together as csv, in any order to create a frame be passed to emoncms eg

    datafields = relative_humidity, feelslike_c, pressure_mb

[Registration for a wunderground account](http://www.wunderground.com/weather/api/d/login.html) is required and a [free apikey](http://www.wunderground.com/weather/api/d/pricing.html) will give 500 free calls a day (up to 10 a minute) 24hr divided by 500 is oen every 172.8 seconds so I've set a default of 180secs.

Location defaults to using the "autoIP" option but can be postcode zipcode country/city state/city lat,long airportcode or pwscode (personal weather station)

I think it may be more appropriate to have the "datafields" defined in the nodes section rather than the runtimesettings, this type of interfacer could also be used to report system data #65.

it is currently being developed on the "wunderground" branch 

![windspeed](https://cloud.githubusercontent.com/assets/5606042/4090807/a26a845a-2f81-11e4-9270-f73fa6dc7259.png)

*By pb66 on 2014-08-29 13:38:05 UTC*



