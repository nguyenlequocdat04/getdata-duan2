from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation
arguments = {"keywords": "banh xeo viet nam, banh cuon viet nam, bun dau mam tom","limit":1500,"print_urls":True, 'chromedriver':'./chromedriver'}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
