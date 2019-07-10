import time, datetime, os, click

@click.command()
@click.option('--path','-p',help='path to git repository')
@click.option('--seconds','-s', default=300, help='seconds between each auto commit')
def main(path,seconds):
    #path = path.replace("\\", "/")
    if os.path.isdir(path):
        c = 0
        while True:
            print(datetime.datetime.now())
            os.system("cd "+path + " && git add -A && git commit -m 'auto"+ str(c) +"' && git push") 
            time.sleep(seconds)
        c = c + 1
    else:
        raise Exception('Invalid file path')

if __name__ == '__main__':
    main()