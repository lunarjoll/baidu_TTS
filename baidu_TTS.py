#!/usr/bin/env python3
##this script is developed by lunarjoll and publish in git@github.com:lunarjoll/baidu_TTS.git
##sent Email to me :    lunarkindle@yahoo.com
#import requests, sys, getopt, configparser, timeit, argparse
import sys, os, configparser, timeit, argparse
import subprocess,  timeout_decorator
from aip import AipSpeech
start = timeit.default_timer()
#pip3 install baidu-aip aip?
input_file=None
output_file=None
tmp_dir='/tmp/baidu_tts'
# 定义参数变量
options = {
  'detect_direction': 'true',
  'per': '4',
}

def read_config():
    config = configparser.ConfigParser()
    config.read(".baidu_TTS.conf")
    client = AipSpeech(config["baidu"]["APP_ID"], config["baidu"]["API_KEY"], config["baidu"]["SECRET_KEY"])
    return client



def create_config():
    print("go to baidu and create APP_ID. \n\
            https://console.bce.baidu.com ")
    config = configparser.ConfigParser()
    config['baidu'] = {}
    config['baidu']['APP_ID'] = input("APP_ID=");
    config['baidu']['API_KEY'] = input("API_KEY=");
    config['baidu']['SECRET_KEY'] = input("SECRET_KEY=");
    with open('.baidu_TTS.conf', 'w') as configfile:
        config.write(configfile)
        configfile.close()




#def usage():
#    print("     when first use, go to baidu and create APP_ID. \n\
#            and pip3 install baidu-aip \n\
#            and use --init to create config file \n\
#            https://console.bce.baidu.com \n")
#    print (sys.argv[0], '--init')
#    print (sys.argv[0], '-i <inputfile> -o <outputfile>')
#    return 0



## 读取图片
#def get_file_content(input_file):
#    image_file = None
#    try:
#        if input_file.startswith('http://') or input_file.startswith('https://'):
#            return requests.get(input_file).content
#            #return image_file
#        else:
#            with open(input_file, 'rb') as fp:
#                return fp.read()
#    except Exception:
#        raise Exception('invalid input_file: %s' % input_file)
#
@timeout_decorator.timeout(10)
def baidu_action(client,byte_sent,iptions):
    result = client.synthesis(byte_sent, 'zh',1 ,options)
    return result

# 调用通用识别接口

def baidu_tts(input_file, output_file, client, options):
    if not os.path.exists(tmp_dir):
        os.path.join(os.path.split(tmp_dir)[0],os.path.split(tmp_dir)[1])
        os.mkdir(tmp_dir)
    with open(input_file,'r',encoding='utf-8') as f:
        i = 1
        while True :
            out_number_name=tmp_dir + '/' + str(i) + '.mp3'
            byte_sent=f.read(2048)
            if byte_sent  == "" :
                break
            try:
                result = baidu_action(client,byte_sent,options)
            except:
                print('time out,decode now')
                break
            if not isinstance(result, dict):
                with open( out_number_name, 'wb') as fw:
                    fw.write(result)
            else: 
                for wrong in result :
                    print(wrong)
                break
            i=i+ 1
    #if i >2 :
    with open(tmp_dir +'/mylist.txt','w') as mylist:
        iii =1
        while iii < i :
            mylist.write('file \'' + tmp_dir +'/' + str(iii) +'.mp3\'\n')
            #mylist.write(str(iii)+'.mp3\n')
            iii= 1+ iii
    subprocess.run(["ffmpeg","-f","concat", "-safe","0","-i",tmp_dir +'/mylist.txt',"-c","copy",output_file])
#    os.rmdir(tmp_dir)

#    words_result=result['words_result']
#    if output_file == None:
#        for i in range(len(words_result)):
#            print(words_result[i]['words'])
#        print("\n\n")
#    else:
#        fo = open(output_file,"a")
#        for i in range(len(words_result)):
#            fo.write(words_result[i]['words'] + "\n")
#        fo.write("\n\n")
#        fo.close()
#        end=timeit.default_timer()
#        print('Running time: %s Seconds'%(end-start))
#

def main ():
    parser = argparse.ArgumentParser(description='TTS program, use Baidu\'s cloud', prog='baidu_TTS')
    parser.add_argument('-i', '--ifile', help='-i input_file', dest='input_file')
    parser.add_argument('-o', dest='output_file', default=None)
    parser.add_argument('--init',action="store_true" ,help="first use it, you should brower cloud.baidu.com and create App id and then input there")
    args = parser.parse_args()
    
    if args.init :
       create_config() 
       return 0
    client = read_config()
    output_file = args.output_file
    input_file_name=args.input_file
    baidu_tts(input_file_name, output_file, read_config(), options)

''' #this is getopt
try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["verbose", "version", "ifile=", "init"])
except getopt.GetoptError:
    print (sys.argv[0], 'GetoptError' ),
    sys.exit(2)
for op, value in opts:
    if op in ("-i", "--ifile"):
        input_file = value
    elif op == "-o":
        output_file = value
    elif op == "-h":
        usage()
        sys.exit()
    elif op == "--init":
        create_config()
        sys.exit()
if input_file == None:
    usage()
    sys.exit(2)
'''        
        



if __name__ == "__main__":
        main()

##this script is developed by lunarjoll and publish in git@github.com:lunarjoll/baidu_OCR.git
##sent Email to me :    lunarkindle@yahoo.com
