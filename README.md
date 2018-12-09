# About  
This is a script to translate chinese txt to audio, just say TTS. It's achieved from cloud.baidu.com for free. You need has a baidu Accound to create cloud-App which support audio concatenating.

# Dependencies  

```
system require:	          	linux  
linux program require:	       ffmpeg
python version:	          	3.5 or more later
python modules require:       	baidu_aip,  timeout_decorator

```


# Use  
```
python3 baidu_TTS.py --init	# to input you APP_ID
python3 baidu_TTS.py -i input.txt -o output.mp3
 ```   
~~ Note: No permit for baidu allow you for high request, So I can't trust you can input large txt. And you need log to request allow again when high request.~~

# Result  
[shadow.mp3](./Example.d/shadow.mp3)
[shadow.txt](./Example.d/shadow.txt)
