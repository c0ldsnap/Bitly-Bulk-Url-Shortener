# Bitly-Bulk-Url-Shortener
This tool utilizes Bit.ly's Api to mass shorten up to 10k urls.

Requires an api key, you can get it by signing up here https://dev.bitly.com/
Bit.ly Api Documentation here https://dev.bitly.com/api.html

*Quick Notes*
The api limit is 10,000 per an Api Key.
You cannot  not make 1 url into 10,000 urls.(It will just give you the same shorten url 10,000 times and may also give you an exceeded limitation error.
You also cannot shorten urls which lead to dead 404 pages.
The urls must be in proper format such as http://cake.com , https://cake.com , http://www.cake.com , https://www.cake.com

Each url should be unique.

*Example*

#Both Bitly Links Unique

http://www.cake.com/page1 => bit.ly/fffef 
http://www.cake.com/page2 => bit.ly/eeefe

#Both Bitly Links Not Unique

http://www.cake.com/page3 => bit.ly/qwerty
http://www.cake.com/page3 => bit.ly/qwerty


