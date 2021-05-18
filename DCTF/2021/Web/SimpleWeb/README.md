## Description

<p align="center">
<img src="Image/image-20210518143008833.png">
</p>

## Solution

After open the URL given, we can see this on the webpage itself.

<p align="center">
<img src="Image/image-20210518143117445.png">
</p>

When we check the **I want flag** checkbox and click submit, we will get this output.

<p align="center">
<img src="Image/image-20210518143231860.png">
</p>

We are not authorized. Guess we need to somehow get it through.

By using DevTools (F12 on the web browser), we can see something like this.

<p align="center">
<img src="Image/image-20210518143352172.png">
</p>

We can see there is a hidden input where **auth** is set as 0 as default. We need to change it to 1 and check the checkbox again and click submit.

<p align="center">
<img src="Image/image-20210518143526421.png">
</p>
