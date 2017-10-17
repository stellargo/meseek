import platform
import webbrowser

def osname():
	if (platform.system()=='Darwin'):
		chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
	elif (platform.system()=='Windows'):
		chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
	else:
		chrome_path = '/usr/bin/google-chrome %s'
	return chrome_path

def openurl(url):
	chrome_path = osname()
	webbrowser.get(chrome_path).open(url)