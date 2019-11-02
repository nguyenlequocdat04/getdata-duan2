# getdata-duan2
**collect and make dataset**
- docker-compose up -d
- docker exec -it get-data bash
- pip install google_images_download
- googleimagesdownload --keywords "phở" --limit 1000 -cd ./chromedriver
- rename --> label imgs --> remove unused img --> (rewrite img) check width --> (remove unused) --> check --> train
